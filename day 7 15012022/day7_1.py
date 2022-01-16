
from numpy import random


import random
word_list = ['ardvark','baboon','camel']

chosen_word = random.choice(word_list)

guess = input("guess a letter: ").lower()

for char in chosen_word:
    if guess==char:
        print('right')
    else:
        print('wrong')