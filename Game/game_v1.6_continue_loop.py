# rng

import random
random.seed()

### values & calc

a = random.randint(1,100)
b = random.randint(1,100)
c = a + b
print("Question: What is the sum of", a, "and", b, "?")

# init loop & counter 

n = c + 1 
counter = 0 

# while loop

while n != c:
    # counter add
    counter = counter + 1

    # input 
    print("Please type your answer:")
    i = input()

    # try convert to integer 
    try:
        n = int(i)
    except:
        # if convert failed
        print("That was not a number, you Fuckface!")
        # start from top
        continue

    # win condition 

    if n == c:
        print(i, "is correct, you matherfucker!")

    else:
        print(i, "is not correct, you fuckface!")

# counter output 
print("Answer:", c)
print("tries:", counter)