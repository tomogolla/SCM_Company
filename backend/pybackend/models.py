from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Customer(db.Model):
    __tablename__ = 'customers'
    CustomerID = db.Column(db.String, primary_key=True)
    CustomerName = db.Column(db.String, nullable=False)
    Gender = db.Column(db.String)
    JobTitle = db.Column(db.String)
    PhoneNumber = db.Column(db.String)
    EmailAddress = db.Column(db.String)
    City = db.Column(db.String)
    Country = db.Column(db.String)
    State = db.Column(db.String)
    CustomerAddress = db.Column(db.String)

class Order(db.Model):
    __tablename__ = 'orders'
    OrderID = db.Column(db.String, primary_key=True)
    CustomerID = db.Column(db.String, db.ForeignKey('customers.CustomerID'))
    OrderDate = db.Column(db.DateTime)
    ShipDate = db.Column(db.DateTime)
    ShipMode = db.Column(db.String)
    Shipping = db.Column(db.Float)
    Sales = db.Column(db.Float)
    Quantity = db.Column(db.Integer)
    Discount = db.Column(db.Float)
