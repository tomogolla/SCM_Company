from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import json

app = Flask(__name__)

# Configure the database (replace with your own database credentials)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pyodbc://username:password@server/dbname?driver=ODBC+Driver+17+for+SQL+Server'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Define the Customer model (replace with actual schema if needed)
class Customer(db.Model):
    __tablename__ = 'Customers'
    CustomerID = db.Column(db.Integer, primary_key=True)
    CustomerName = db.Column(db.String)
    Gender = db.Column(db.String)
    JobTitle = db.Column(db.String)
    PhoneNumber = db.Column(db.String)
    EmailAddress = db.Column(db.String)
    City = db.Column(db.String)
    State = db.Column(db.String)

# Define the Orders model (replace with actual schema if needed)
class Order(db.Model):
    __tablename__ = 'Orders'
    OrderID = db.Column(db.Integer, primary_key=True)
    CustomerID = db.Column(db.Integer, db.ForeignKey('Customers.CustomerID'))
    OrderDate = db.Column(db.String)
    ShipDate = db.Column(db.String)
    ShipMode = db.Column(db.String)
    Shipping = db.Column(db.Float)
    Sales = db.Column(db.Float)
    Quantity = db.Column(db.Integer)
    Discount = db.Column(db.Float)

# Fetch all customers
@app.route('/getAllCustomers', methods=['GET'])
def get_customers():
    try:
        customers = Customer.query.all()  # Fetch all customers
        customer_list = [{"CustomerID": customer.CustomerID, "CustomerName": customer.CustomerName,
                          "Gender": customer.Gender, "JobTitle": customer.JobTitle,
                          "PhoneNumber": customer.PhoneNumber, "EmailAddress": customer.EmailAddress,
                          "City": customer.City, "State": customer.State} for customer in customers]
        return jsonify(customer_list), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Fetch all orders
@app.route('/getAllOrders', methods=['GET'])
def get_orders():
    try:
        orders = Order.query.all()  # Fetch all orders
        order_list = [{"OrderID": order.OrderID, "CustomerID": order.CustomerID, "OrderDate": order.OrderDate,
                       "ShipDate": order.ShipDate, "ShipMode": order.ShipMode, "Shipping": order.Shipping,
                       "Sales": order.Sales, "Quantity": order.Quantity, "Discount": order.Discount} 
                       for order in orders]
        return jsonify(order_list), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Insert a new customer
@app.route('/insert', methods=['POST'])
def insert_customer():
    try:
        customer_data = request.get_json()  # Get data from the POST request
        new_customer = Customer(CustomerName=customer_data['CustomerName'],
                                Gender=customer_data.get('Gender'),
                                JobTitle=customer_data.get('JobTitle'),
                                PhoneNumber=customer_data.get('PhoneNumber'),
                                EmailAddress=customer_data.get('EmailAddress'),
                                City=customer_data.get('City'),
                                State=customer_data.get('State'))

        db.session.add(new_customer)  # Add new customer to the database
        db.session.commit()  # Commit the transaction
        return jsonify({"message": "Customer added successfully"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
