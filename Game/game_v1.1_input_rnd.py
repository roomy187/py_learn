# import module

import random

# init random

random.seed()

# random values & calculation

a = random.randint(1,10)
b = random.randint(1,10)
c = a + b

print("The task:", a, "+", b)

# input answer

print("your answer:")
x = input()

# convert to integer 

x = int(x)

# output
print("your answer:", x)
print("correct answer:", c)