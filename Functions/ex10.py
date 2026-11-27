# Exercise 10: Who passed? (dictionary + default)
# Write filter_passed(students, pass_mark=50) that returns a list of the names whose
# marks are at or above pass_mark.
# students = {"Ali": 45, "Sara": 78, "Ahmed": 52, "Hina": 90}
# Test: filter_passed(students) → ['Sara', 'Ahmed', 'Hina'] · filter_passed(students, 60) →
# ['Sara', 'Hina']

def filter_passed(students ,pass_marks=50):
    passed_students=[]
    for key,value in students.items():
        if value>pass_marks:
            passed_students.append(key)
    return passed_students
students = {"Ali": 45, "Sara": 78, "Ahmed": 52, "Hina": 90}
print(filter_passed(students ,60))