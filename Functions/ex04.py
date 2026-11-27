# Exercise 4: Grade from marks
# Write grade(marks) that returns A (80+), B (70–79), C (60–69) or F (below 60).
# Test: grade(85) → A · grade(72) → B · grade(64) → C · grade(40) → F

def grade(marks):
    if marks>80:
        return("A")
    elif marks>70:
        return("B")
    elif marks>60:
        return("C")
    else:
        return("F")
print(grade(72))

