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

# multiple conditions and output

if x == c:
    print("That's correct, you matherfucker!")

elif x < 0 or x > 300:
    print("holy fuck thats so wrong, you dumbfuck! The correct answer was:", c)

elif c-1 <= x <= c+1:
    print("almost, but still incorrect! The right answer was", c, "not", x, "you retard!")

else:
    print("Nope! The correct answer was:", c, "not", x, "you fuckface!")