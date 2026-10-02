import json
import os

inventory = []
FILENAME = "inventory.json"

def load_inventory():
    """Subroutine to load persistence data from inventory.json or initialize defaults."""
    global inventory
    if os.path.exists(FILENAME):
        try:
            with open(FILENAME, "r") as f:
                inventory = json.load(f)
            print("inventory.json found.")
            print("Inventory loaded successfully.\n")
        except Exception:
            print("Corrupted data-stack detected. Starting with empty inventory.\n")
            inventory = []
    else:
        # default products so inventory not empty
        inventory = [
            {"id": "P001", "name": "Laptop", "price": 1200.00, "stock": 15},
            {"id": "P002", "name": "Mouse", "price": 25.50, "stock": 40},
            {"id": "P003", "name": "Keyboard", "price": 45.00, "stock": 25},
        ]

def display_all():
    print("\nDisplay all")

def add_product():
    print("\nAdd product")

def update_stock():
    print("\nUpdate stock")

def search_product():
    print("\nSearchi product")

def save_inventory():
    print("\nSaved")

def main():
    print("=" * 45)
    print("INVENTORY MANAGEMENT SYSTEM")
    print("=" * 45 + "\n")

    load_inventory()

    while True:
        print("---------- MENU ----------")
        print("1.Display All Products")
        print("2.Add Product")
        print("3.Update Stock")
        print("4.Search Product")
        print("5.Save Inventory")
        print("6.Exit")
        print("--------------------------")

        option = input("\nEnter option: ").strip()

        if option == "1":
            display_all()
        elif option == "2":
            add_product()
        elif option == "3":
            update_stock()
        elif option == "4":
            search_product()
        elif option == "5":
            save_inventory()
        elif option == "6":
            print("\nSaving inventory before exit...")
            save_inventory()
            print("Thank you for using Inventory Management System.")
            print("Program terminated.")
            break
        else:
            print("Invalid input. Please enter an option from 1 to 6.\n")

if __name__ == "__main__":
    main()