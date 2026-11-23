# Q9. Student report card
# students = [
# {"name": "Ali", "marks": [80, 75, 90]},
# {"name": "Sara", "marks": [95, 88, 92]},
# {"name": "Ahmed", "marks": [55, 62, 48]},
# ]
# For each student, print the average (2 decimals) and Pass (60+) or Fail. At the end, print
# the topper.
# Expected: Ali 81.67 Pass · Sara 91.67 Pass · Ahmed 55.0 Fail · Topper: Sara

students = [
{"name": "Ali", "marks": [80, 75, 90]},
{"name": "Sara", "marks": [95, 88, 92]},
{"name": "Ahmed", "marks": [55, 62, 48]},
]
highest_average = 0
topper = ""
for student in students:
    total =round(sum(student["marks"])/len(student["marks"]) ,2)
    if total>60:
        print(f"{student["name"]} {total} Pass")
    else :
        print(f"{student["name"]} {total} Fail")
    if total > highest_average:
        highest_average = total
        topper = student["name"]
print(f"Topper: {topper}")



