# Q12. Reverse a string with recursion. Write reverse_text(text) without slicing [::-1] and
# without a loop. Hint: the reverse of "Lahore" is the reverse of "ahore" plus "L".
# Test: reverse_text("Lahore") → 'erohaL'

def reverse_text(text):
    if len(text)<=1:
        return text
    return reverse_text(text[1:])+text[0]

print(reverse_text("Peshawar"))