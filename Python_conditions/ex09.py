# Exercise 9: Triangle checker
# Take three sides. If any two sides add up to no more than the third, print “Not a valid
# triangle”. Otherwise print its type: Equilateral (all equal), Isosceles (two equal) or Scalene
# (none equal).
# Test: 3, 4, 5 → Scalene · 5, 5, 8 → Isosceles · 1, 2, 10 → Not a valid triangle

side1 =int(input("Enter first side length : "))
side2 =int(input("Enter second side length : "))
side3 =int(input("Enter third side length : "))
if (side1+side2)>side3 and (side1+side3)>side2 and (side2+side3)>side1:
    if (side1==side2==side3) :
       print("Equilateral")
    elif (side1==side2) or (side2==side3) or (side3==side1):
       print("Isosceles")
    else :
       print("Scalene")
else :
    print("Not a valid triangle")
