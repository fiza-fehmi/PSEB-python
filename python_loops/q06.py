# Q6. Even and odd counter
# numbers = [12, 7, 9, 20, 33, 48, 51]
# result = {"even": 0, "odd": 0}
# Loop through the numbers and add 1 to the right key.
# Expected: {'even': 3, 'odd': 4}

numbers = [12, 7, 9, 20, 33, 48, 51]
even_count =0
odd_count =0
for i in numbers :
    if(i%2==0) :
        even_count+=1
    else:
        odd_count+=1
result ={'even' :even_count ,'odd' :odd_count}
print(result)
