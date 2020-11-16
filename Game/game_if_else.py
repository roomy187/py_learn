# import & init random module

import random

random.seed()

# random values & calculation

a = random.randint(1,100)
b = random.randint(1,100)
c = a + b

print("The task:", a, "+", b)

# input answer & convert to integer

print("your answer:")
x = input()
x = int(x)

# output with if / else statement

if x == c:
    print("That's correct, you matherfucker!")
else:
    print("Nope! The correct answer was:", c, "not", x, "you fuckface!")