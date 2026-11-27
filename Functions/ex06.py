# Exercise 6: Smallest and largest(return two values)
# Write min_max(numbers) that returns the smallest and largest number as two values. Use
# a loop, not min() or max().
# Test: low, high = min_max([45, 12, 89, 33]) → low = 12, high = 89

def min_max(numbers):
    high=numbers[0]
    low=numbers[0]
    for i in numbers:
        if i<low:
            low=i
        if i>high:
            high=i
    print(f"Low={low}, High={high}")

min_max([5 ,6 ,7 ,0 ,12])

