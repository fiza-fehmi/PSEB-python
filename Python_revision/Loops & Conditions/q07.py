# Q7. Pak Zindabad. Write pak_zindabad(n) that returns a list for 1 to n: multiples of 3
# become "Pak", multiples of 5 become "Zindabad", multiples of both become
# "PakZindabad", and other numbers stay as they are. Hint: check “both” first.
# Test: pak_zindabad(15) → [1, 2, 'Pak', 4, 'Zindabad', 'Pak', 7, 8, 'Pak', 'Zindabad', 11, 'Pak', 13, 14,'PakZindabad']

def pak_zindabad(n):
    empty_list=[]
    for i in range(1,n+1):
        if (i%3==0 and i%5==0):
            empty_list.append("pakZindabad")
        elif i%5==0:
            empty_list.append("zindabad")
        elif i%3==0:
            empty_list.append("Pak")
        else:
            empty_list.append(i)
    return empty_list

print(pak_zindabad(15))
        