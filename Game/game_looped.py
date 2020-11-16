# import & init random module

import random
random.seed()

# random values & calculation

a = random.randint(1,100)
b = random.randint(1,100)
c = a + b

print("The task:", a, "+", b)

# for loop (set number of tries)

for i in range(5):

    # input

    print("your answer:")
    x = input()
    x = int(x)

    # win condition
    
    if x == c:
        
        print("That's correct, Matherfucker!")
        break

    else:
        print(x, "is wrong! guess again, you dumbfuck!")