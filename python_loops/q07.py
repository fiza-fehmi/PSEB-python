# Q7. Stock check with tuples
# products = [("Laptop", 150000, 3), ("Mouse", 2500, 0),
# ("Keyboard", 5000, 12), ("Monitor", 45000, 2)]
# Each tuple is (name, price, quantity). Unpack each tuple in the loop, then:
# print the items that are out of stock (quantity 0)
# print the items with low stock (1 to 4)
# print the total stock value (price × quantity, added up)
# Expected: out of stock Mouse · low stock Laptop, Monitor · total 600000
products = [("Laptop", 150000, 3), ("Mouse", 2500, 0),("Keyboard", 5000, 12), ("Monitor", 45000, 2)]
total_stock_value =0
for name ,price ,quantity in products:
    if quantity==0 :
        print(f"Out of Stock: {name}")
    if quantity>=1 and quantity<=4 :
        print(f"Low Stock: {name}")
    total_stock_value += price*quantity
print(total_stock_value)
    
    
    
    # print(name ,price ,quantity)

    