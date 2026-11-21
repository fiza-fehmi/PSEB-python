# Exercise 6: Day name
# Take a number from 1 to 7 and print the day (1 = Monday … 7 = Sunday). Any other number
# prints “Invalid day”.
# Test: 5 → Friday

day_num = int(input("Enter a number to see current day : "))
if day_num==1:
    print(f"{day_num} = Monday")
elif day_num==2:
    print(f"{day_num} = Tuesday")
elif day_num==3:
    print(f"{day_num} = Wednesday")
elif day_num==4:
    print(f"{day_num} = Thursday")
elif day_num==5:
    print(f"{day_num} = Friday")
elif day_num==6:
    print(f"{day_num} = Saturday")
elif day_num==7:
    print(f"{day_num} = Sunday")
else:
    print("Invalid day")
