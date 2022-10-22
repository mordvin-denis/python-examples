import string
import random

adjectives = ['sleepy', 'slow', 'hot', 'cold', 'big', 'red', 'orange', 'yellow', 'green',
              'blue', 'good', 'old', 'white', 'free', 'brave']

nouns = ['apple', 'dinosaur', 'ball', 'cat', 'goat', 'dragon', 'car', 'duck', 'panda']

print('Hello there!')

while True:
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    number = random.randrange(0, 100)
    special_char = random.choice(string.punctuation)

    password = adjective + noun + str(number) + special_char
    print('New password: %s' % password)

    response = input('Do you need other password? Please input y or no')

    if response == 'n':
        break

