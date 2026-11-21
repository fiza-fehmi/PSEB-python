# Exercise 8: Character type
# Take one character and print whether it is a Vowel, Consonant, Digit or Special character.
# Hint: .isdigit(), .isalpha(), and .lower() in "aeiou".
# Test: e → Vowel · 7 → Digit · K → Consonant · @ → Special character

user_input =(input("Enter a char : "))
if user_input.isdigit() :
    print(f"{user_input} -> Digit")
elif (user_input.lower()=="a" or user_input.lower()=="e" or user_input.lower()=="i" or user_input.lower()=="o" or user_input.lower()=="u"):
    print(f"{user_input.lower()} -> Vowel")
elif user_input.isalpha() :
    print(f"{user_input} -> Consonant")
else:
    print(f"{user_input} -> Special Charcter")
