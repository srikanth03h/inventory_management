from inventory import add_product, update_stock, delete_product, view_products
from user_auth import register_user, authenticate
from reports import generate_report

def main():
    print("Welcome to the Inventory Management System")
    
    while True:
        print("\n1. Register User")
        print("2. Login")
        print("3. Add Product")
        print("4. View Products")
        print("5. Update Stock")
        print("6. Delete Product")
        print("7. Generate Report")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            username = input("Enter username: ")
            password = input("Enter password: ")
            role = input("Enter role (admin/employee): ")
            register_user(username, password, role)
        
        elif choice == "2":
            username = input("Enter username: ")
            password = input("Enter password: ")
            user = authenticate(username, password)
            if user:
                print(f"✅ Welcome, {username} ({user[0]})")
            else:
                print("❌ Invalid credentials")
        
        elif choice == "3":
            name = input("Enter product name: ")
            quantity = int(input("Enter quantity: "))
            price = float(input("Enter price: "))
            add_product(name, quantity, price)

        elif choice == "4":
            print(view_products())

        elif choice == "5":
            product_id = int(input("Enter product ID: "))
            new_quantity = int(input("Enter new quantity: "))
            update_stock(product_id, new_quantity)

        elif choice == "6":
            product_id = int(input("Enter product ID to delete: "))
            delete_product(product_id)

        elif choice == "7":
            generate_report()

        elif choice == "8":
            print("Goodbye!")
            break

        else:
            print("❌ Invalid choice! Try again.")

if __name__ == "__main__":
    main()
