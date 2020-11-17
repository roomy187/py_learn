# import & init random module

import random
random.seed()

# random values & calculation

a = random.randint(1,100)
b = random.randint(1,100)
c = a + b

print("The task:", a, "+", b)

# while loop (run untill the correct answer is given)

# init loop

z = c + 1

# init loop counter

t = 0

# while loop 

while z != c:
    
    # adding to loop counter
    
    t = t + 1

    # input with conversion to integer

    print("please type your answer:")

    i = input()
    z = int(i)

    # status output 

    if z == c:
        print("That's correct, Matherfucker!")
    else:
        print("That's incorrect, Fuckface!")

# final output & summary

print("correct answer:", c)

if t == 1:
    print("WOW! First try, you Matherfucker!")
else:
    print("You needed", t, "tries! Go buy a calculator, Fuckface!")