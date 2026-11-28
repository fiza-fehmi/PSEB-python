# Q13. Guessing game checker. Write check_guesses(secret, guesses, max_tries=5). Loop
# through the guesses list; if a guess matches within max_tries, return "Won in N tries".
# Otherwise return "Lost, the number was " plus the secret.
# Test: check_guesses(7, [3, 9, 7]) → 'Won in 3 tries' · check_guesses(7, [1, 2, 3, 4, 5, 7]) →
# 'Lost, the number was 7'

def check_guesses(secret, guesses ,max_tries=5):
    tries =0
    for guess in guesses[:max_tries]:
        tries+=1
        if guess == secret:
            return f"won in {tries} tries"
    return f"lost ,the number was {secret}"

print(check_guesses(7, [3, 9, 7]))

    