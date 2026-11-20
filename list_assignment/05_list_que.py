# Exercise 5: Even and odd
# Using list comprehension, make two lists from the numbers 1 to 15: one with the even numbers
# None
# and one with the odd numbers.
nums = list(range(1 ,15))
even_list = []
odd_list = []
for i in nums:
    if(i%2 == 0):
        even_list.append(i)
    else:
        odd_list.append(i)
print("even numbers " ,even_list)
print("odd numbers " ,odd_list)