# Exercise 15: Countdown (generator with yield)
# Write a generator countdown(n) that yields n, n-1 … 1. Print each value with a for loop,
# then print Go!
# Test: countdown(5) → 5 4 3 2 1 Go!

def countdown(n):
    while(n>=1):
        yield n
        n-=1
for i in countdown(10):
    print(i ,end=" ")
print("Go!")

