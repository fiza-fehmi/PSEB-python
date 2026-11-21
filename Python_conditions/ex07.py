# Exercise 7: Shop discount
# Take the bill amount and print the discount and the final amount.
# Bill (Rs),Discount
# 5000 or more,10%
# 2000 to 4999,5%
# Below 2000,None
# Test: 3000 → Discount: 150.0, Pay: 2850.0

bill_amount = float(input("Enter the amount : "))
if bill_amount>=5000:
    '''Formula found via Google.'''
    discount =(10/100)*bill_amount
    print(f"original bill: {bill_amount}")
    pay = bill_amount-discount
    print(f"Discount :{discount} ,Pay :{pay}")
elif bill_amount>=2000:
    discount =(5/100)*bill_amount
    print(f"original bill: {bill_amount}")
    pay = bill_amount-discount
    print(f"Discount :{discount} ,Pay :{pay}")
else:
    print(f"Discount= 0.00 Pay :{bill_amount}")




