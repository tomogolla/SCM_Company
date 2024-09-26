from flask import Flask, render_template, request, jsonify
import pandas as pd
from dash_app import init_dashboard, create_dash_app

app = Flask(__name__)

# Create the Dash app and embed it in Flask
dash_app = create_dash_app(app)


# Load your CSV data
df = pd.read_csv('cleaned_sales_data.csv')

@app.route('/')
def index():
    # Serve the frontend (index.html)
    return render_template('index.html')
if __name__=='__main__':
    app.run(debug=True)

@app.route('/api/add_customer', methods=['POST'])
def add_customer():
    # Add new customer data from the form
    try:
        data = request.json
        # Append the new data to the dataframe
        global df
        new_data = pd.DataFrame([data])
        df = pd.concat([df, new_data], ignore_index=True)
    
        # Save the updated dataframe to CSV
        df.to_csv('cleaned_sales_data.csv', index=False)
        return jsonify({'status': 'Customer added successfully'})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/api/get_data', methods=['GET'])
def get_data():
    # Send the current data to the frontend or Dash
    return df.to_json(orient='records')

# Initialize Dash
init_dashboard(app)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
