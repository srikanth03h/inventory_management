from tabulate import tabulate
from inventory import view_products

# Function to generate a stock report
def generate_report():
    products = view_products()
    print("\n📊 Inventory Report:")
    print(tabulate(products, headers=["ID", "Name", "Quantity", "Price"], tablefmt="grid"))

# Generate and display report
generate_report()
