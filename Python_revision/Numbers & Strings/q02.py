# Q2. Name formatter. Write format_name(name) that removes extra spaces, capitalises
# every word and returns a tuple of (full name, initials).
# Test: format_name(" muhammad ali khan ") → ('Muhammad Ali Khan', 'M.A.K.'

def format_name(name):
    words=name.title().split()
    full_name=" ".join(words)
    initials=""
    for i in words:
        initials += i[0]+"."
    return full_name ,initials
    
print(format_name(" muhammad ali khan "))
