# Exercise 6: Rotate a list
# r = [1, 2, 3, 4, 5]
# Use slicing only to move the first two items to the end.
# Expected: [3, 4, 5, 1, 2]
r = [1, 2, 3, 4, 5]
new = r[2:5] + r[0:2]
print(new)