# Exercise 12: Palindrome checker
# Write is_palindrome(word) that returns True if the word reads the same backwards.
# Ignore capital letters.
# Test: is_palindrome("Madam") → True · is_palindrome("level") → True ·
# is_palindrome("python") → False
def is_palindrome(word):
    word=word.lower()
    if word[::-1]==word:
        return True
    else:
        return False
print(is_palindrome("python"))
