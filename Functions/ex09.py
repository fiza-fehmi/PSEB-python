# Exercise 9: Word counter (return a dictionary)
# Write count_words(sentence) that returns a dictionary of how many times each word
# appears. Treat The and the as the same word.
# Test: count_words("The cat and the dog and the bird") → {'the': 3, 'cat': 1, 'and': 2, 'dog': 1,
# 'bird': 1}

def count_word(sentence):
    sentence = sentence.lower()
    words = sentence.split()
    dictionary={}
    for word in words:
        if word in dictionary:
            dictionary[word]+=1
        else:
            dictionary[word]=1
    return dictionary

print(count_word("The cat and the dog and the bird"))




