document.addEventListener('DOMContentLoaded', () => {
    fetchOrders();

    function fetchOrders() {
        fetch('http://localhost:5000/orders/getAll') // Correct endpoint for orders
            .then(response => response.json())
            .then(data => {
                console.log('Order Data:', data);
                loadOrderTable(data);
            })
            .catch(error => console.error('Error fetching order data:', error));
    }

    function loadOrderTable(data) {
        const ordersTableBody = document.getElementById('orders-table-body');
        ordersTableBody.innerHTML = ""; // Clear table

        if (data.length === 0) {
            ordersTableBody.innerHTML = "<tr><td colspan='8' style='text-align: center;'>No order data available</td></tr>";
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
                <td>${order.PostalCode}</td>
                <td>${order.Shipping}</td>                
                <td>${order.ShippingCost}</td>
            `;
            ordersTableBody.appendChild(row);
        });
    }
});
