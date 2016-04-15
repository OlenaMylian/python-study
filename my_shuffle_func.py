##Solution 1.
##We make our own function.

import random

words = ["аня", "вася", "коля", "петя", "злата", "диана", "ира", \
         "нина", "поля", "веталь", "игорь", "назар"]

def my_shuffle(words):
    words_copy = words[:]
    new = []

    while len(words_copy) != 0:
        position = random.randint(0, len(words_copy) - 1)  
        new.append(words_copy[position])
        words_copy.remove(words_copy[position])
    return new
       
new = my_shuffle(words)
print(new)


##Solution 2.
##We can use function from random library.
words_new = words
random.shuffle(words_new)
print(words_new)
