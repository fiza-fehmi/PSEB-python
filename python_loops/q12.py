# Q12. Password checker (bonus)
# Keep asking for a password until it is strong:
# at least 8 characters
# at least one digit
# at least one capital letter
# Loop over the characters with .isdigit() and .isupper(), and use True/False flags.
# Expected: pakistan → weak · Pak2026 → weak (too short) · Pakistan2026 → Password
# accepted

length=8
while True:
    has_digit = False
    has_upper = False
    user_input =input("Enter a Strong Password of 8 characters: ")
    for i in user_input:
        if i.isdigit():
            has_digit=True
        if i.isupper():
            has_upper=True
    if len(user_input)<length:
            print("Too Shorter")
    elif has_digit and has_upper:
            print("password accepted")
            break
    else :
         print("not accepted, digit or capital letter is missing")
    
