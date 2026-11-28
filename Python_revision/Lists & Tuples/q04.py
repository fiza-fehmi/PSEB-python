# B. Lists and tuples
# Q4. Merge without duplicates. Write merge_unique(list1, list2) that joins two lists, keeps
# each value once (use a loop and not in, not set()) and returns them sorted.
# Test: merge_unique([3, 1, 5], [5, 2, 3]) → [1, 2, 3, 5]

def merge_unique(list1 ,list2):
    merged_list =list1+list2
    unique_list=[]
    for i in merged_list:
        if i not in unique_list:
            unique_list.append(i)
        unique_list.sort()
    return unique_list
print(merge_unique([3, 1, 5], [5, 2, 3]))