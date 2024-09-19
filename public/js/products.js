
document.addEventListener('DOMContentLoaded', () => {
    // Initialize or fetch product data if needed
    console.log('Products page loaded')
    fetchProducts();

    function fetchProducts() {
        fetch('http://localhost:5000/products/getAll') //endpoint for products
            .then(response => response.json())
            .then(data => {
                console.log('Products Data:', data);
                loadProductTable(data);
            })
            .catch(console.error('Error fetching Products data:', error));
    }
    function loadProductTable(data) {
        const loadProductTableBody = document.getElementById('products-table-body');
        loadProductTableBody.innerHTML = ""; //clear data

        if (data.length === 0) {
            loadProductTableBody.innerHTML = "<tr><td colspan='8' style='text-align: center;'>No data available</td></tr>";
            return;
        }

            data.forEach(product => {
                const row = document.createElement('tr');
                row.innerHTML = `
                    <td>${product.ProductID}</td>
                    <td>${product.SupplierID}</td>
                    <td>${product.CarMaker}</td>
                    <td>${product.CarModel}</td>
                    <td>${product.CarColor}</td>
                    <td>${product.CarModelYear}</td>
                    <td>${product.CarPrice}</td>
                    <td>${product.PostalCode}</td>
                `;
                loadProductTableBody.appendChild(row);
            });
    }
});
