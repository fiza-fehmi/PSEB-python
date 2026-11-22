# Exercise 11: University admission   A student is eligible if (Matric 60% or above and Inter 50% or above), or Entry test 70 or above. Take all three and print Eligible or Not eligible.  
matric = int(input("Enter your Matric marks : "))
inter = int(input("Enter your Inter marks : "))
entry_test_marks = int(input("Enter entry test marks : "))
if(matric>=60 and inter>=50) or (entry_test_marks>=70):
    print("Eligible")
else :
    print("Not eligible")