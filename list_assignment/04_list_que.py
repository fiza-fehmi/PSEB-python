# Exercise 4: Remove duplicates
# nums = [3, 1, 3, 2, 1, 5]
# Make a new list without duplicates, keeping the original order. Use a loop and not in, not
# set().
# Expected: [3, 1, 2, 5]
nums = [3, 1, 3, 2, 1, 5]
empty_list = []
for i in nums:
    if i not in empty_list:
        empty_list.append(i)
print(empty_list)