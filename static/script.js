// Fetch and display products from the backend
function fetchProducts() {
    fetch('/get_products')
        .then(response => response.json())
        .then(data => {
            let productList = document.getElementById("productList");
            productList.innerHTML = ""; // Clear previous list

            data.products.forEach(product => {
                let listItem = document.createElement("div");
                listItem.className = "list-group-item d-flex justify-content-between align-items-center";
                listItem.innerHTML = `
                    <span>${product.name} - ${product.quantity} available - $${product.price}</span>
                    <div>
                        <button class="btn btn-edit btn-sm" onclick="editProduct(${product.id})">
                            <i class="fas fa-edit"></i>
                        </button>
                        <button class="btn btn-delete btn-sm" onclick="deleteProduct(${product.id})">
                            <i class="fas fa-trash"></i>
                        </button>
                    </div>
                `;
                productList.appendChild(listItem);
            });
        })
        .catch(error => console.error("Error fetching products:", error));
}

// Add a new product
function addProduct() {
    let name = document.getElementById("productName").value;
    let quantity = document.getElementById("productQuantity").value;
    let price = document.getElementById("productPrice").value;

    fetch('/add_product', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ name: name, quantity: quantity, price: price })
    })
    .then(response => response.json())
    .then(data => {
        console.log(data.message); // Removed alert, now logs the message
        fetchProducts(); // Refresh product list
    })
    .catch(error => console.error("Error adding product:", error));
}

// Edit a product
function editProduct(productId) {
    let newName = prompt("Enter new product name:");
    let newQuantity = prompt("Enter new quantity:");
    let newPrice = prompt("Enter new price:");

    fetch(`/edit_product/${productId}`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ name: newName, quantity: newQuantity, price: newPrice })
    })
    .then(response => response.json())
    .then(data => {
        console.log(data.message); // Removed alert
        fetchProducts(); // Refresh product list
    })
    .catch(error => console.error("Error editing product:", error));
}

// Delete a product (without confirmation popup)
function deleteProduct(productId) {
    fetch(`/delete_product/${productId}`, {
        method: 'DELETE',
        headers: { 'Content-Type': 'application/json' }
    })
    .then(response => response.json())
    .then(data => {
        console.log(data.message); // Removed alert
        fetchProducts(); // Refresh product list
    })
    .catch(error => console.error("Error deleting product:", error));
}

// Fetch products when the page loads
document.addEventListener("DOMContentLoaded", fetchProducts);
