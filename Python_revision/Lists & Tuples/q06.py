# Q6. Split a list into chunks. Write chunk_list(items, size) that returns a list of smaller lists,
# each holding at most size items. Hint: slicing.
# Test: chunk_list([1, 2, 3, 4, 5, 6, 7], 3) → [[1, 2, 3], [4, 5, 6], [7]]

def chunk_list(items ,size):
    chunked_list=[]
    for i in range(0 ,len(items) ,size):
        chunked_list.append(items[i:i+size])
    return chunked_list

print(chunk_list([1, 2, 3, 4, 5, 6, 7], 3))

    