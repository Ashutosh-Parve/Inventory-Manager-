from database import init_db, add_item, get_all_items, update_quantity, delete_item
from backup import upload_backup

# Initialize database
init_db()

def menu():
    print("\n===== Inventory Manager =====")
    print("1. Add Item")
    print("2. View All Items")
    print("3. Update Quantity")
    print("4. Delete Item")
    print("5. Backup Database to S3")
    print("6. Exit")
    choice = input("Enter choice: ")
    return choice

while True:
    choice = menu()
    
    if choice == "1":
        name = input("Enter item name: ")
        try:
            quantity = int(input("Enter quantity: "))
            price = float(input("Enter price: "))
            add_item(name, quantity, price)
            print(f"Item '{name}' added successfully!")
        except ValueError:
            print("Invalid input. Quantity must be integer and price must be a number.")

    elif choice == "2":
        items = get_all_items()
        if not items:
            print("No items in inventory.")
        else:
            print("\n--- Inventory Items ---")
            for item in items:
                print(f"ID: {item[0]}, Name: {item[1]}, Quantity: {item[2]}, Price: {item[3]}")

    elif choice == "3":
        try:
            item_id = int(input("Enter item ID to update: "))
            new_quantity = int(input("Enter new quantity: "))
            if update_quantity(item_id, new_quantity):
                print(f"Item ID {item_id} quantity updated to {new_quantity}.")
            else:
                print("Item not found.")
        except ValueError:
            print("Invalid input. Please enter numbers only.")

    elif choice == "4":
        try:
            item_id = int(input("Enter item ID to delete: "))
            if delete_item(item_id):
                print(f"Item ID {item_id} deleted successfully.")
            else:
                print("Item not found.")
        except ValueError:
            print("Invalid input. Please enter numbers only.")

    elif choice == "5":
        upload_backup()

    elif choice == "6":
        print("Exiting Inventory Manager. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
