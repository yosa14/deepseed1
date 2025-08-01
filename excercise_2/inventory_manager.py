inventory = {}

def add_item():
    name = input("Enter item name: ").strip()
    if name in inventory:
        print("Item already exists.")
        return
    try:
        price = float(input("Enter item price: "))
        stock = int(input("Enter item stock: "))
        category = input("Enter item category: ").strip()
        inventory[name] = {
            "price": price,
            "stock": stock,
            "category": category
        }
        print(f"{name} added to inventory.")
    except ValueError:
        print("Invalid price or stock.")

def update_stock():
    name = input("Enter item name to update: ").strip()
    if name in inventory:
        try:
            amount = int(input("Add/remove quantity (use - for remove): "))
            inventory[name]["stock"] += amount
            print(f"Stock updated. New stock: {inventory[name]['stock']}")
        except ValueError:
            print("Invalid input.")
    else:
        print("Item not found.")

def search_category():
    cat = input("Category to search: ").strip()
    found = []
    for item, details in inventory.items():
        if details["category"].lower() == cat.lower():
            found.append(item)
    if found:
        print(f"Found {len(found)} items in {cat}:")
        for item in found:
            info = inventory[item]
            print(f"• {item} - info['price']:.2f (info['stock'] in stock)")
    else:
        print("No items found.")

def check_low_stock():
    print("⚠ LOW STOCK ALERT:")
    for item, details in inventory.items():
        if details["stock"] <= 5:
            print(f"- item (details['stock'] units remaining)")

def total_value():
    total = 0
    for details in inventory.values():
        total += details["price"] * details["stock"]
    print(f"Current Inventory Value:{total:.2f}")

while True:
    print("\n=== SMART INVENTORY MANAGER ===")
    total_value()
    check_low_stock()
    print("\n1. Add New Item")
    print("2. Update Stock")
    print("3. Search Items by Category")
    print("4. Check Low Stock Items")
    print("5. Inventory Value")
    print("6. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        add_item()
    elif choice == "2":
        update_stock()
    elif choice == "3":
        search_category()
    elif choice == "4":
        check_low_stock()
    elif choice == "5":
        total_value()
    elif choice == "6":
        print("Goodbye!")
        break
    else:
        print("Invalid option.")

