// backend/controllers/customers.js
const express = require('express');
const router = express.Router();
const db = require('../db'); // Adjust the path if necessary

// Define your routes here

// Example route to get all customers
router.get('/getAll', async (req, res) => {
    try {
        const pool = await db.poolPromise;
        const result = await pool.request().query('SELECT TOP (30) * FROM Customers');
        res.json(result.recordset);
    } catch (err) {
        console.error('Error fetching customers:', err);
        res.status(500).send('Server Error');
    }
});
// Add a new customer
router.post('/add', async (req, res) => {
    const { CustomerID, CustomerName, Gender, JobTitle, PhoneNumber, EmailAddress, City, State } = req.body;
    //validate request
    if (!CustomerName || !EmailAddress) { 
        return res.status(400).json({message: 'Name and email required'});
    }
    try {
        const pool = await db.poolPromise;
        const request = pool.request();

        //add parameter to prevent SQL injection
        request.input('CustomerID', CustomerID)
        .input('CustomerName', CustomerName)        
        .input('Gender', Gender)
        .input('JobTitle', JobTitle)
        .input('EmailAddress', EmailAddress)
        .input('City', City)
        .input('State', State);
    // Execute the query
    await request.query(
        `INSERT INTO Customers (CustomerID, CustomerName, Gender, JobTitle, PhoneNumber, EmailAddress, City, State) 
        VALUES (@CustomerID, @CustomerName, @Gender, @JobTitle, @PhoneNumber, @EmailAddress, @City, @State)`
    );  
    
    res.status(201).json({ message: 'Customer added successfully' });
} catch (err) {
    console.error('Error adding customer:', err);
    res.status(500).json({ error: 'Internal Server Error' });
}
});  

// Update a customer's information
router.put('/update/:id', async (req, res) => {
    const { CustomerName, Gender, JobTitle, PhoneNumber, EmailAddress, City, State } = req.body;
    const { id } = req.params; // Get the customer ID from the URL params

    try {
        // Find the customer by ID
        const customer = await Customer.findByPk(id);

        if (!customer) {
            return res.status(404).json({ message: 'Customer not found' });
        }

        // Update the customer record
        customer.CustomerName = CustomerName || customer.CustomerName;
        customer.Gender = Gender || customer.Gender;
        customer.JobTitle = JobTitle || customer.JobTitle;
        customer.PhoneNumber = PhoneNumber || customer.PhoneNumber;
        customer.EmailAddress = EmailAddress || customer.EmailAddress;
        customer.City = City || customer.City;
        customer.State = State || customer.State;

        // Save the updated customer
        await customer.save();

        res.status(200).json(customer);
    } catch (err) {
        console.error('Error updating customer:', err);
        res.status(500).json({ message: 'Internal Server Error' });
    }
});

// Delete a customer
router.delete('/delete/:id', async (req, res) => {
    const { id } = req.params; // Get the customer ID from the URL params

    try {
        // Find the customer by ID
        const customer = await Customer.findByPk(id);

        if (!customer) {
            return res.status(404).json({ message: 'Customer not found' });
        }

        // Delete the customer
        await customer.destroy();

        res.status(200).json({ message: 'Customer deleted successfully' });
    } catch (err) {
        console.error('Error deleting customer:', err);
        res.status(500).json({ message: 'Internal Server Error' });
    }
});



module.exports = router;
