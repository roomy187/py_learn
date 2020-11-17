# import & init random module

import random
random.seed()

# random values & calculation

a = random.randint(1,100)
b = random.randint(1,100)
c = a + b

print("The task:", a, "+", b)

# for loop (set number of tries)

for t in range(10):

    # input

    print("your answer:")
    x = input()
    x = int(x)

    # win condition
    
    if x == c:
        
        print("That's correct, Matherfucker! That was attempt #:", t+1)
        break

    else:
        print(x, "is wrong! guess again, you dumbfuck! You have", 9-t, "tries left!")