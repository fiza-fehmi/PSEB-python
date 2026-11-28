# Q10. Number analyzer (functions calling functions). Write small helpers is_even(n),
# is_prime(n) and digit_sum(n), then analyze(n) that uses them and returns a tuple of (is
# even, is prime, number of digits, digit sum, is palindrome).
# Test: analyze(121) → (False, False, 3, 4, True) · analyze(13) → (False, True, 2, 4, False)

def is_even(n):
    if n%2==0:
        return True
    else:
        return False

def is_prime(n):
    if n<=1:
        return False
    for i in range(2 ,n):
        if n%i==0:
            return False
    return True

def digit_sum(n):
    total=0
    while n>0:
        last_digit=n%10
        total+=last_digit
        n=n//10
    return total

def is_palindrome(n):
    if str(n)[::-1]==str(n):
        return True 
    
    
def analyze(n):
    number_of_digits= len(str(n))
    return (is_even(n) ,is_prime(n) ,number_of_digits ,digit_sum(n) ,is_palindrome(n))
    
print(analyze(121))