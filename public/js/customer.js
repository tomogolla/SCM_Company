document.addEventListener('DOMContentLoaded', () => {
    fetchCustomers();

    function fetchCustomers() {
        // Use the correct backend server URL
        fetch('http://localhost:5000/customers/getAll') // Ensure the backend URL is correct
            .then(response => response.json())
            .then(data => {  
                console.log('Customer Data:', data); // Debug log
                loadCustomerTable(data); // Populate table with the fetched data
            })
            .catch(error => console.error('Error fetching customer data:', error));
    }

    function loadCustomerTable(data) {
        const customerTableBody = document.getElementById('customer-table-body');
        customerTableBody.innerHTML = ""; // Clear the table first

        if (data.length === 0) {
            customerTableBody.innerHTML = "<tr><td colspan='8' style='text-align: center;'>No customer data available</td></tr>";
            return;
        }

        // Populate table with customer data
        data.forEach(customer => {
            const row = document.createElement('tr');
            row.innerHTML = `
                <td>${customer.CustomerID}</td>
                <td>${customer.CustomerName}</td>
                <td>${customer.Gender}</td>
                <td>${customer.JobTitle}</td>
                <td>${customer.PhoneNumber}</td>
                <td>${customer.EmailAddress}</td>
                <td>${customer.City}</td>
                <td>${customer.State}</td>
            `;
            customerTableBody.appendChild(row);
        });
    }
});
