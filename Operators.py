# Compare two numbers and check whether the first is greater than the second.
print(12 > 133)

# Check whether two variables contain equal values.
var1 = 20
var2 = 20
print(var1 == var2)

# Check whether a number is NOT equal to 10 using the NOT operator.
num = 15
print(num != 10)

# Take a number and check whether it is positive or negative.
num = 12
if num%2 == 0:
    print("even")
else :
    print("odd")

# Check whether a number is divisible by both 3 and 5.
numbers = 15
if((numbers%3==0) & (numbers%5==0)):
    print("yes divisible")

# Check whether a person is eligible for admission if their age is 18 or their marks are above 80 using or.
age = 18
marks = 60
if((age == 18) | (marks >80) ):
    print("eligible for admission")
