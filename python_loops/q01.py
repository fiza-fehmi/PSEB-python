# Q1. Pass or fail list
# marks = [78, 45, 92, 33, 67, 88]
# Loop through the list and print each mark with Pass (40 or above) or Fail. At the end, print
# how many students passed.
# Expected: 78 Pass … 33 Fail … and Passed: 5

marks = [78, 45, 92, 33, 67, 88]
total = 0
for i in marks:
    if(i>=40):
        print(f"{i} :Passed")
        total+=1
    else :
        print(f"{i} :Failed")
print(f"total passed students are : {total}")



