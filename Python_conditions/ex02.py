# Exercise 2: Voting eligibility
# Take a person’s age. At 18 or above, print “Eligible to vote”. Otherwise, print how many
# years are left.
# Test: 15 → Not eligible, wait 3 more years

user_age = int(input("Enter your age : "))
if user_age>=18 :
    print("Eligible to vote")
else:
    waiting_years = 18-user_age
    print(f"not eligible ,you have to wait for {waiting_years} more years")