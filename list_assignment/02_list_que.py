# Exercise 2: Marks report
# marks = [78, 92, 65, 88, 54]
# Print the total, the average, the highest, the lowest, and how many marks are above 70 (use a
# loop).
marks = [78, 92, 65, 88, 54]
print("sum is" ,sum(marks))
average =sum(marks)/len(marks)
print("average is" ,average)
print("highest number is " ,max(marks))
print("lowest number is " ,min(marks))
total = 0
for number in marks :
    if(number>70) :
        total += 1
print("total numbers are " ,total)