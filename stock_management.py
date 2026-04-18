inventory = {}

n = int(input("Enter number of products: "))

for i in range(n):
    name = input(f"Enter product name {i+1}: ")
    qty = int(input("Enter quantity: "))
    inventory[name] = qty

print("\n--- Inventory Status ---")

for item, qty in inventory.items():
    print(f"{item}: {qty}")

print("\nLow Stock Items (less than 10):")
for item, qty in inventory.items():
    if qty < 10:
        print(f"{item} is low on stock!")