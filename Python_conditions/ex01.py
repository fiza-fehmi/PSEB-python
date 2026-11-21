# Exercise 1: Positive, negative or zero
# Take a number and print whether it is Positive, Negative or Zero.
# Test: -7 → Negative

user_num = int(input("enter a number : "))
if user_num>0:
    print(f"{user_num} is Positive")
elif user_num<0:
    print(f"{user_num} is negative")
else:
    print(f"{user_num} is zero")