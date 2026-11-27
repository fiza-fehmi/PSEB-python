# Exercise 13: Sum of digits (recursion)
# Write sum_digits(n) recursively. Hint: the last digit is n % 10 and the rest is n // 10. Stop
# when n is a single digit.
# Test: sum_digits(1234) → 10 · sum_digits(9875) → 29
def sum_digits(n):
    if n<10:
        return n
    else:
        last_digit=n%10
        return last_digit+sum_digits(n//10)

print(sum_digits(1234))

