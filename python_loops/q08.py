# Q8. Unique values and the most frequent
# nums = [3, 5, 3, 8, 5, 3, 9]
# Use a dictionary to count how many times each number appears. Then print the unique
# numbers and the one that appears most.
# Expected: unique [3, 5, 8, 9] · most frequent 3 (3 times)

nums = [3, 5, 3, 8, 5, 3, 9]
dictionary={}
for num in nums :
    if num not in dictionary :
        dictionary[num] =1
    else:
        dictionary[num] +=1
print(f"Unique: {list(dictionary.keys())}")
most_frequent=max(dictionary.values())
for key ,value in dictionary.items():
    if value==most_frequent:
        print(f"Most frequent {key} ({value} times)")


