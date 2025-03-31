# Inventory Management System

## Overview
This is a simple **Inventory Management System** built using **Flask, JavaScript, HTML, CSS, and MySQL (or SQLite)**. It helps businesses efficiently manage their stock by allowing users to **add, edit, and delete products** dynamically.

## Features
- 📌 **View products** with name, quantity, and price
- ➕ **Add new products** to inventory
- ✏ **Edit existing products**
- ❌ **Delete products** from the list
- 🔄 **Real-time updates** without page refresh

## Technologies Used
- **Frontend:** HTML, CSS, JavaScript (Fetch API)
- **Backend:** Flask (Python)
- **Database:** MySQL / SQLite
- **Version Control:** Git & GitHub

## Installation & Setup
### 1️⃣ Clone the repository
```sh
git clone https://github.com/your-username/inventory-management.git
cd inventory-management
```

### 2️⃣ Install dependencies
```sh
pip install -r requirements.txt
```

### 3️⃣ Set up the database
- If using **SQLite**, create a database file:
```sh
python init_db.py  # Initializes the database
```
- If using **MySQL**, update `config.py` with your credentials.

### 4️⃣ Run the application
```sh
python app.py
```
Then open **http://127.0.0.1:5000/** in your browser.

## API Endpoints
| Method | Endpoint          | Description           |
|--------|------------------|----------------------|
| GET    | /get_products    | Fetch all products  |
| POST   | /add_product     | Add a new product   |
| PUT    | /edit_product/id | Edit product by ID  |
| DELETE | /delete_product/id | Delete product by ID |

## Future Improvements
✅ Add **User Authentication**
✅ Implement **Low Stock Alerts**
✅ Integrate **Barcode Scanner**

## Contributing
Feel free to fork this project, submit issues, or contribute with pull requests! 🚀

## License
This project is licensed under the **MIT License**.

---



