# Exercise 10: Mobile package
# Take the balance and the package price. If the balance is enough, print “Package
# activated” and the remaining balance. Otherwise, print how much more is needed.
# Test: balance 300, price 450 → Insufficient balance, need Rs 150 more

balance = int(input("Enter your balance : "))
package_price = int(input("Enter package price : "))
if balance>=package_price :
    print("Package Acitavted!")
else :
    needed_amount =package_price-balance
    print(f"Insuficient balance, need Rs {needed_amount} more")

