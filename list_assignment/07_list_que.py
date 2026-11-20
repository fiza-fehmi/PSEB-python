# Exercise 7: Copy or not?
# Make a = [1, 2, 3], then b = a and c = a.copy(). Append 4 to a, then print a, b and
# c. In a comment, explain why b changed but c did not.
a = [1, 2, 3]
b = a
c = a.copy()
a.append(4)
print(a)
print(a ,b ,c)

'''
Reason : Because b = a so b and a refres to the same list like a=b=[1,2,3]....in simple words it is shallow copy change in one variable would change the other variable too
on the other hand c=a.copy() forms deep copy where a points to the list at one location and c at the other one like a=[1 ,2 ,3] and c=[1 ,2 ,3] so a change in one variable will change that particular var only
'''