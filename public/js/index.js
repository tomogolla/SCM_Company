document.addEventListener('DOMContentLoaded', function () {
    // Initialize customer and order views on page load
    fetchCustomers();

    // Elements for navigation
    const customersDropdown = document.querySelector('.subnavbtn:nth-child(1)');
    const ordersDropdown = document.querySelector('.subnavbtn:nth-child(2)');
    const productsDropdown = document.querySelector('.subnavbtn:nth-child(3)');

    // Toggle dropdown visibility on click
    customersDropdown.addEventListener('click', () => {
        toggleDropdown(customersDropdown);
    });

    ordersDropdown.addEventListener('click', () => {
        toggleDropdown(ordersDropdown);
    });

    productsDropdown.addEventListener('click', () => {
        toggleDropdown(productsDropdown);
    });

    // Open modals for adding customer, order, and product
    const addCustomerBtn = document.getElementById('add-customer-btn');
    const addOrderBtn = document.querySelector('.dashboard-btn[data-target="#entryform1"]');
    const addProductBtn = document.getElementById('add-product-btn');

    const customerDialog = document.getElementById('add-customer-dialog');
    const orderDialog = document.getElementById('add-order-dialog');
    const productDialog = document.getElementById('add-product-dialog');

    const closeCustomerDialog = document.getElementById('close-customer-dialog');
    const closeOrderDialog = document.getElementById('close-order-dialog');
    const closeProductDialog = document.getElementById('close-product-dialog');

    // Open dialogs when the buttons are clicked
    addCustomerBtn.addEventListener('click', () => {
        customerDialog.style.display = 'block';
    });

    addOrderBtn.addEventListener('click', () => {
        orderDialog.style.display = 'block';
    });

    addProductBtn.addEventListener('click', () => {
        productDialog.style.display = 'block';
    });

    // Close dialogs when the close button is clicked
    closeCustomerDialog.addEventListener('click', () => {
        customerDialog.style.display = 'none';
    });

    closeOrderDialog.addEventListener('click', () => {
        orderDialog.style.display = 'none';
    });

    closeProductDialog.addEventListener('click', () => {
        productDialog.style.display = 'none';
    });

    // Close dialogs when clicking outside of the dialog box
    window.addEventListener('click', (event) => {
        if (event.target === customerDialog) {
            customerDialog.style.display = 'none';
        } else if (event.target === orderDialog) {
            orderDialog.style.display = 'none';
        } else if (event.target === productDialog) {
            productDialog.style.display = 'none';
        }
    });

    // Handle form submissions for adding customer, order, and product
    const customerForm = document.getElementById('add-customer-form');
    const orderForm = document.getElementById('add-order-form');
    const productForm = document.getElementById('add-product-form');

    handleFormSubmission(customerForm, '/customers/add', customerDialog);
    handleFormSubmission(orderForm, '/orders/add', orderDialog);
    handleFormSubmission(productForm, '/products/add', productDialog);

    // Fetch customers and orders when links are clicked
    document.getElementById('view-customers').addEventListener('click', function () {
        setActive(this); // Highlight the active tab
        showCustomers(); // Display the customer table
        fetchCustomers(); // Fetch customer data
    });

    document.getElementById('view-orders').addEventListener('click', function () {
        setActive(this); // Highlight the active tab
        showOrders();    // Display the orders table
        fetchOrders();   // Fetch orders data
    });
});

// Toggle dropdown visibility
function toggleDropdown(dropdown) {
    const subnavContent = dropdown.nextElementSibling;
    subnavContent.classList.toggle('show');
}

// Handle form submission for customer, order, and product forms
function handleFormSubmission(form, url, dialog) {
    form.addEventListener('submit', function (event) {
        event.preventDefault();
        const formData = new FormData(form);
        const data = Object.fromEntries(formData.entries());

        fetch(url, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data),
        })
            .then(response => response.json())
            .then(result => {
                alert(`${result.message}`);
                dialog.style.display = 'none';
            })
            .catch(error => console.error('Error:', error));
    });
}

// Fetch and display customers
function fetchCustomers() {
    fetch('http://127.0.0.1:5000/getAllCustomers')
        .then(response => response.json())
        .then(data => loadCustomerTable(data))
        .catch(error => console.error('Error fetching customer data:', error));
}

// Load customers into table
function loadCustomerTable(data) {
    const customerTableBody = document.getElementById('customer-table-body');
    customerTableBody.innerHTML = ''; // Clear existing content

    if (data.length === 0) {
        customerTableBody.innerHTML = "<tr><td colspan='8' class='no-data'>No Data available</td></tr>";
        return;
    }

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

// Fetch and display orders
function fetchOrders() {
    fetch('http://127.0.0.1:5000/getAllOrders')
        .then(response => response.json())
        .then(data => loadOrdersTable(data))
        .catch(error => console.error('Error fetching orders data:', error));
}

// Load orders into table
function loadOrdersTable(data) {
    const ordersTableBody = document.getElementById('orders-table-body');
    ordersTableBody.innerHTML = ''; // Clear existing content

    if (data.length === 0) {
        ordersTableBody.innerHTML = "<tr><td colspan='9' class='no-data'>No orders data available</td></tr>";
        return;
    }

    data.forEach(order => {
        const row = document.createElement('tr');
        row.innerHTML = `
            <td>${order.OrderID}</td>
            <td>${order.CustomerID}</td>
            <td>${order.OrderDate}</td>
            <td>${order.ShipDate}</td>
            <td>${order.ShipMode}</td>
            <td>${order.Shipping}</td>
            <td>${order.Sales}</td>
            <td>${order.Quantity}</td>
            <td>${order.Discount}</td>
        `;
        ordersTableBody.appendChild(row);
    });
}

// Show customers table and hide orders table
function showCustomers() {
    document.getElementById('customers-table').style.display = 'table';
    document.getElementById('orders-table').style.display = 'none';
    document.getElementById('page-title').textContent = 'Customers';
}

// Show orders table and hide customers table
function showOrders() {
    document.getElementById('customers-table').style.display = 'none';
    document.getElementById('orders-table').style.display = 'table';
    document.getElementById('page-title').textContent = 'Orders';
}

// Highlight the active tab
function setActive(button) {
    const links = document.querySelectorAll('.navbar a');
    links.forEach(link => link.classList.remove('active'));
    button.classList.add('active');
}
document.getElementById("add-order-form").addEventListener("submit", function (e) {
    e.preventDefault();

    const orderData = {
        orderID: document.getElementById("orderID").value,
        customerID: document.getElementById("customerID").value,
        orderDate: document.getElementById("orderDate").value,
        shipDate: document.getElementById("shipDate").value,
        shipMode: document.getElementById("shipMode").value,
        postalCode: document.getElementById("postalCode").value,
        Shipping: document.getElementById("Shipping").value
    };

    fetch('/orders/create', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(orderData)
    })
    .then(response => {
        if (response.ok) {
            alert("Order added successfully!");
            location.reload();  // Reload the page to reflect new data
        } else {
            throw new Error('Failed to add order');
        }
    })
    .catch(error => {
        alert("Error: " + error.message);
    });
});
