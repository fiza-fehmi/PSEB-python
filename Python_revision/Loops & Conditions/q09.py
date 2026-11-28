# Q9. Mobile number check. Write is_valid_mobile(number) that returns True only if the
# number is 12 characters, starts with 03, has a dash at index 4, and every other character is
# a digit.
# Test: "0300-1234567" → True · "0300 1234567" → False · "1300-1234567" → False · "0300-
# 12345" → False

def is_valid_mobile(number):
        if len(number)==12 and number[:2]=="03" and number[4]=="-" and number[:4].isdigit() and number[:5]: 
            return True
        else:
              return False

print(is_valid_mobile("0300-12345"))
