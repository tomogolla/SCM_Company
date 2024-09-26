// controllers/products.js
const express = require('express');
const router = express.Router();
const db = require('../db'); // Import the database connection

// Get all products
router.get('/getAll', async (req, res) => {
    try {
        const pool = await db.poolPromise;
        const result = await pool.request().query('SELECT * FROM Products'); // Adjust query to match your table structure
        res.json(result.recordset); // Send result as JSON
    } catch (err) {
        res.status(500).send('Error retrieving products: ' + err);
    }
});

// Get a specific product by ID
router.get('/:id', async (req, res) => {
    try {
        const pool = await db.poolPromise;
        const result = await pool.request()
            .input('ProductID', db.sql.Int, req.params.id)
            .query('SELECT * FROM Products WHERE ProductID = @ProductID');
        if (result.recordset.length === 0) {
            return res.status(404).send('Product not found');
        }
        res.json(result.recordset[0]);
    } catch (err) {
        res.status(500).send('Error retrieving product: ' + err);
    }
});

module.exports = router;
