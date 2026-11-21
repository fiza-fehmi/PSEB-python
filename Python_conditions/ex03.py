# Exercise 3: Pass or fail
# Take a student’s marks out of 100. 40 or above is Pass; below 40 is Fail.
# Test: 38 → Fail

obtained_marks = int(input("enter your marks to check result : "))
if obtained_marks>=40:
    print("Passed")
else:
    print("Fail")