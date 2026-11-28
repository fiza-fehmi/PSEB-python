# Q8. Number triangle. Write print_triangle(n) that prints this pattern with nested loops
# (this one prints instead of returning).
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# Test: print_triangle(4) → the pattern above

def print_triangle(n):
    for i in range(1 ,n+1):
        for j in range(1 ,i+1):
            print(j ,end=" ")
        print()
print_triangle(4)