import pandas as pd
from models import db, Customer, Order

def load_data():
    customers = Customer.query.all()
    orders = Order.query.all()

    customer_df = pd.DataFrame([customer.as_dict() for customer in customers])
    order_df = pd.DataFrame([order.as_dict() for order in orders])

    return customer_df, order_df

def perform_analysis():
    customer_df, order_df = load_data()
    # Example analysis: Finding most frequent customer
    top_customers = order_df['CustomerID'].value_counts().head(5)
    return top_customers
