// controllers/orders.js
const express = require('express');
const router = express.Router();
const db = require('../db'); // Import the database connection

// Get all orders
router.get('/getAll', async (req, res) => {
    try {
        const pool = await db.poolPromise;
        const result = await pool.request().query('SELECT * FROM Orders');
        res.json(result.recordset);
    } catch (err) {
        res.status(500).send('Error retrieving orders: ' + err);
    }
});

// Get a specific order by ID
router.get('/:id', async (req, res) => {
    try {
        const pool = await db.poolPromise;
        const result = await pool.request()
            .input('OrderID', db.sql.Int, req.params.id)
            .query('SELECT * FROM Orders WHERE OrderID = @OrderID');
        if (result.recordset.length === 0) {
            return res.status(404).send('Order not found');
        }
        res.json(result.recordset[0]);
    } catch (err) {
        res.status(500).send('Error retrieving order: ' + err);
    }
});
// controllers/orders.js

// Add new order (POST)
router.post('/create', async (req, res) => {
    try {
        const { orderID, customerID, orderDate, shipDate, shipMode, PostalCode, Shipping } = req.body;
        const pool = await db.poolPromise;
        await pool.request()
            .input('OrderID', db.sql.Int, orderID)
            .input('CustomerID', db.sql.Int, customerID)
            .input('OrderDate', db.sql.Date, orderDate)
            .input('ShipDate', db.sql.Date, shipDate)
            .input('ShipMode', db.sql.NVarChar, shipMode)
            .input('PostalCode', db.sql.NVarChar, PostalCode)
            .input('Shipping', db.sql.NVarChar, Shipping)
            .query(`INSERT INTO Orders (OrderID, CustomerID, OrderDate, ShipDate, ShipMode, PostalCode, Shipping) 
                    VALUES (@OrderID, @CustomerID, @OrderDate, @ShipDate, @ShipMode, @PostalCode, @Shipping)`);

        res.status(200).send("Order created successfully!");
    } catch (err) {
        console.error(err);
        res.status(500).send('Error creating order: ' + err.message);
    }
});



// Update an existing order
router.put('/update/:id', async (req, res) => {
    try {
        const { CustomerID, OrderDate, ShipDate, ShipMode, PostalCode, Shipping, Sales, Quantity, Discount } = req.body;
        const pool = await db.poolPromise;
        await pool.request()
            .input('OrderID', db.sql.Int, req.params.id)
            .input('CustomerID', db.sql.VarChar, CustomerID)
            .input('OrderDate', db.sql.DateTime, OrderDate)
            .input('ShipDate', db.sql.DateTime, ShipDate)
            .input('ShipMode', db.sql.VarChar, ShipMode)
            .input('PostalCode', db.sql.VarChar, PostalCode)
            .input('Shipping', db.sql.Decimal, Shipping)
            .input('Sales', db.sql.Decimal, Sales)
            .input('Quantity', db.sql.Int, Quantity)
            .input('Discount', db.sql.Decimal, Discount)
            .query(`
                UPDATE Orders
                SET CustomerID = @CustomerID,
                    OrderDate = @OrderDate,
                    ShipDate = @ShipDate,
                    ShipMode = @ShipMode,
                    PostalCode = @PostalCode,
                    Shipping = @Shipping,
                    Sales = @Sales,
                    Quantity = @Quantity,
                    Discount = @Discount
                WHERE OrderID = @OrderID
            `);
        res.send('Order updated successfully');
    } catch (err) {
        res.status(500).send('Error updating order: ' + err);
    }
});

// Delete an order
router.delete('/delete/:id', async (req, res) => {
    try {
        const pool = await db.poolPromise;
        await pool.request()
            .input('OrderID', db.sql.Int, req.params.id)
            .query('DELETE FROM Orders WHERE OrderID = @OrderID');
        res.send('Order deleted successfully');
    } catch (err) {
        res.status(500).send('Error deleting order: ' + err);
    }
});

module.exports = router;
