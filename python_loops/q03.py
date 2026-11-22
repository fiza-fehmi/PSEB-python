# Q3. Highest and lowest price
# prices = [450, 1200, 300, 980, 75]
# Find the highest and lowest price with a loop. Don’t use max() or min().
# Expected: Highest: 1200, Lowest: 75

prices = [450, 1200, 300, 980, 75]
highest=prices[0]
lowest=prices[0]
for i in prices :
    if i>highest:
        highest=i
    if i<lowest:
        lowest=i
print(f"Highest :{highest}, Lowest={lowest}")


    
