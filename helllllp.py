#Coding Problem 3
products = ["Laptop", "Mouse", "Keyboard", "Monitor", "Headset"]
quantities = [12, 45, 30, 8, 22]

print("=== Inventory ===")
for i in range(len(products)):
    print(f"{products[i]}:\t{quantities[i]}")
print("=================")

max_index = None
min_index = None
max_quantity = 0
min_quantity = 1000
for index in range(len(quantities)):
    print(index, quantities[index], products[index])
    if quantities[index] > max_quantity:
        max_quantity = quantities[index]
        max_index = index
    
    if quantities[index] < min_quantity:
        min_quantity = quantities[index]
        min_index = index
        
print(f"Highest: {products[max_index]} {quantities[max_index]}")
print(f"Lowest: {products[min_index]} {quantities[min_index]}")
print(f"Total quantity: {sum(quantities)}")
print(f"Average quantity: {sum(quantities) / len(quantities):.2f}")

products.append("Webcam")
quantities.append(15)
products.insert(2, "USB Hub")
quantities.insert(2, 50)
products.remove("Headset")
quantities.remove(22)
removed_product = products.pop(5)
removed_quantity = quantities.pop(5)
print(removed_product, removed_quantity)
print("Updated Inventory")
for i in range(len(products)):
    print(f"{products[i]}:\t{quantities[i]}")
print("=================")