# Exercise 14: Fibonacci(recursion)
# The series goes 0, 1, 1, 2, 3, 5, 8, 13 … where each number is the sum of the two before it.
# Write fibonacci(n) that returns the nth number (starting at fibonacci(0) = 0).
# Test: fibonacci(7) → 13 · fibonacci(10) → 55
def fibonacci(n):
    if n<=1:
        return n
    else:
        result = fibonacci(n-1)+fibonacci(n-2)
        return result
print(fibonacci(40))