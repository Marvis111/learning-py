from random import *
import sys

for i in range(4):
    print(randint(1,10))


"""while True:
    print('Type exit to exit.')
    response = input()
    if response == 'exit':
        sys.exit()
    print('You typed ' + response + '.')
"""

eggs = 42

def spam():
    global eggs
    print(eggs)

eggs= 454

spam()

