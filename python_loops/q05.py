# Q5. Grade report from a dictionary
# students = {"Ali": 85, "Sara": 92, "Ahmed": 76, "Hina": 58, "Bilal": 64}
# Loop through it with .items() and print each name with a grade: A (80+), B (70–79), C (60–
# 69), F (below 60). Then print the class average.
# Expected: Ali A, Sara A, Ahmed B, Hina F, Bilal C and Average: 75.0

students = {"Ali": 85, "Sara": 92, "Ahmed": 76, "Hina": 58, "Bilal": 64}
for name ,marks in students.items():
    average = sum(students.values())/len(students)
    if marks>80:
        print(f"{name} :A")
    elif marks>70:
        print(f"{name} :B")
    elif marks>60:
        print(f"{name} :C")
    else:
        print(f"{name} :F")
    print(f"Average :{average}")
        
