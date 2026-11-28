# Q5. Class report from tuples. Each record is a tuple (name, marks). Write
# class_report(records) that returns a tuple of (average rounded to 2, topper’s name, list of
# names below 60).
# records = [("Ali", 85), ("Sara", 92), ("Ahmed", 58)]
# Test: class_report(records) → (78.33, 'Sara', ['Ahmed'])

def class_report(records):
    total_marks=0
    highest_marks=0
    topper=""
    below_60=[]
    for name ,marks in records:
        if marks>highest_marks:
            highest_marks=marks
            topper=name
        if marks<60:
            below_60.append(name)
        total_marks+=marks
    average=round(total_marks/len(records) ,2)
    return (average,topper,below_60)
        

records=[("Ali", 85), ("Sara", 92), ("Ahmed", 58)]
print(class_report(records))
