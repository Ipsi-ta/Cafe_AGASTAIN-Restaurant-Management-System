import json

# -------------------- CONFIGURATION --------------------
MENU_PATH = "menu.json"
OWNER_PASSWORD = "Ipsita@cafe"

# -------------------- LOAD MENU --------------------
with open(MENU_PATH, "r", encoding="utf-8") as f:
    data = json.load(f)

items = data.get("items", [])
for item in items:
    if "reviews" not in item:
        item["reviews"] = []

cart = []  # Cart stores ordered items

# -------------------- FUNCTIONS --------------------
def show_menu():
    """Display menu with average reviews"""
    print("\n--- MENU ---")
    for item in items:
        avg = f"{sum(item['reviews'])/len(item['reviews']):.1f}" if item['reviews'] else "No reviews"
        print(f"{item['name']} - ₹{item['price']} | ⭐ {avg}")

def save_menu():
    """Save menu with any updates/reviews"""
    with open(MENU_PATH, "w", encoding="utf-8") as f:
        json.dump({"items": items}, f, indent=4, ensure_ascii=False)

# -------------------- MAIN LOOP --------------------
while True:
    print('_'*30)
    print("\n--- CAFE AGASTAIN ---")
    print('_'*30)
    print('Special Discount 10% for orders above Rs 1000/-')
    print('_'*30)
    print('a. Show Menu')
    print('b. Order Items')
    print('c. Update Menu')
    print('d. Show Cart') 
    print('e. Generate Bill & Add Review')
    print('f. Exit')
    print('_'*30)
    choice = input("Select option (a-f): ").strip().lower()

    # -------------------- a. Show Menu --------------------
    if choice == 'a':
        show_menu()

    # -------------------- b. Order Items --------------------
    elif choice == 'b':
        while True:
            print('_'*30)
            show_menu()
            print('_'*30)
            name = input("Enter item name to order (or 'done'): ").strip()
            if name.lower() == 'done':
                break
            item = next((i for i in items if i['name'].lower() == name.lower()), None)
            if not item:
                print("Item not found")
                continue
            while True:
                try:
                    qty = int(input(f"Enter quantity 1-10 for {item['name']}: "))
                    if 1 <= qty <= 10:
                        break
                    print("Quantity must be 1-10")
                except:
                    print("Enter a valid number 1-10")
            existing = next((c for c in cart if c['name'].lower() == name.lower()), None)
            if existing:
                existing['qty'] += qty
            else:
                cart.append({'name': item['name'], 'qty': qty, 'price': item['price']})
            print(f"Added {qty} x {item['name']}")

    # -------------------- c. Update Menu --------------------
    elif choice == 'c':
        attempts = 0
        auth = False
        while attempts < 5:
            pwd = input("Owner password or 'exit': ").strip()
            if pwd.lower() == 'exit': break
            if pwd == OWNER_PASSWORD:
                auth = True
                break
            attempts += 1
            print(f"Wrong! Attempts left: {5-attempts}")
        if not auth: continue
        name = input("Item name to add/update: ").strip()
        try:
            price = float(input("Price: "))
        except:
            print("Invalid price"); continue
        found = False
        for i in items:
            if i['name'].lower() == name.lower():
                i['price'] = price
                found = True
                print("Updated")
                break
        if not found:
            items.append({'name': name, 'price': price, 'reviews': []})
            print("Added")
        save_menu()

    # -------------------- d. Show Cart --------------------
    elif choice == 'd':
        if not cart:
            print("Cart empty")
        else:
            total = 0
            for c in cart:
                cost = c['qty']*c['price']; total+=cost
                print(f"{c['qty']} x {c['name']} = ₹{cost}")
            if total>1000:
                disc = total*0.1
                print(f"10% discount -₹{disc:.2f}"); total-=disc
            print(f"Total: ₹{total:.2f}")

        # -------------------- e. Generate Bill & Add Review --------------------
    elif choice == 'e':
        if not cart:
            print("Cart empty"); continue

        # Ask if user wants to give review
        while True:
            give_review = input("Do you want to give review? (y/n): ").strip().lower()
            if give_review in ['y','n']:
                break

        if give_review == 'y':
            for c in cart:
                while True:
                    try:
                        rating = int(input(f"Enter rating 1-5 for {c['name']}: "))
                        if 1 <= rating <= 5:
                            # Merge review with previous
                            for i in items:
                                if i['name'].lower() == c['name'].lower():
                                    i['reviews'].append(rating)
                            break
                        else:
                            print("Rating must be 1-5")
                    except:
                        print("Enter a number 1-5")
            save_menu()

        # Generate bill
        customer = input("Customer name: ").strip()
        print(f"\n--- BILL for {customer} ---")
        total = 0
        for c in cart:
            cost = c['qty']*c['price']; total+=cost
            print(f"{c['qty']} x {c['name']} = ₹{cost}")

        # First discount: 10% if total > 1000
        if total > 1000:
            disc1 = total * 0.10
            print(f"10% discount applied: -₹{disc1:.2f}")
            total -= disc1
        print(f"Total Bill: ₹{total:.2f}")
        cart.clear()

    # -------------------- f. Exit --------------------
    elif choice == 'f':
        print("Thanks for visiting!"); break

    # Invalid option
    else:
        print("Invalid option")








