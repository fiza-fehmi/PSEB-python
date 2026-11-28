# Q3. Character counter. Write count_types(text) that loops over the text and returns a
# tuple of (letters, digits, spaces, others).
# Test: count_types("Pakistan 2026!") → (8, 4, 1, 1)

def count_types(text):
    letters=0
    digits=0
    spaces=0
    others=0
    for i in text:
        if i.isalpha():
            letters+=1
        elif i.isdigit():
            digits+=1
        elif i.isspace():
            spaces+=1
        else:
            others+=1
    return (letters ,digits,spaces,others)

print(count_types("Pakistan 2026!"))