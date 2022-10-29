import string
import random

adjectives = ['sleepy', 'slow', 'hot', 'cold', 'big', 'red', 'orange', 'yellow', 'green',
              'blue', 'good', 'old', 'white', 'free', 'brave']

nouns = ['apple', 'dinosaur', 'ball', 'cat', 'goat', 'dragon', 'car', 'duck', 'panda']


print('Hello there!')



def generate_password():
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    number = random.randrange(0, 100)
    special_char = random.choice(string.punctuation)
    return adjective + noun.capitalize() + str(number) + special_char


while True:
    password = generate_password()
    print('New password: %s' % password)

    password = generate_password()
    print('New password: %s' % password)

    password = generate_password()
    print('New password: %s' % password)

    response = input('Do you need other password? Please input y or n ')

    if response[-1] == 'n':
        break

