import json
products = [
    {"name": "Laptop", "price": 50000, "category": "Electronics", "quantity": 3},
    {"name": "Mouse", "price": 500, "category": "Electronics", "quantity": 10},
    {"name": "Phone", "price": 25000, "category": "Electronics", "quantity": 2},
    {"name": "Table", "price": 3000, "category": "Furniture", "quantity": 0},
    {"name": "Chair", "price": 1500, "category": "Furniture", "quantity": 4},
    {"name": "Bottle", "price": 200, "category": "Kitchen", "quantity": 8}
]
def low_stock(products, threshold=5):
    for p in products:
        if p["quantity"] < threshold:
            yield p
def expensive_items(products, min_price=1000):
    for p in products:
        if p["price"] > min_price:
            yield p
category = input("Enter category: ")
upper_names = [p["name"].upper() for p in products if p["category"] == category]
print(upper_names)


updated_products = list(map(lambda p: {
    "name": p["name"],
    "price": p["price"] * 1.10,
    "category": p["category"],
    "quantity": p["quantity"]
}, products))


for p in updated_products:
    print(p)

s = list(filter(lambda p: p["quantity"] > 0, updated_products))

print("\nIn Stock Products:")
for p in s:
    print(p)

with open("inventory.json", "w") as f:
    json.dump(updated_products, f, indent=4)

# Read JSON
with open("inventory.json", "r") as f:
    data = f.read()
    print("\nInventory File:")
    print(data)
    print("Total Characters:", len(data))
