# Exercise 7: Average of any number of marks (*args)
# Write average(*marks) that returns the average of all marks given. If no marks are given,
# return 0.
# Test: average(80, 90, 70) → 80.0 · average(55, 65) → 60.0 · average() → 0

def average(*marks):
    if len(marks)==0:
        return 0
    else:
     average = sum(marks)/len(marks)
     return average

print(average())