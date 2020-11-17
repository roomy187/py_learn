# simple while loop

# rng 

import random
random.seed()

# initialize

sum = 0

# while loop

while sum < 50:
    x = random.randint(1,8)
    sum = sum + x
    print("added:", x, "Sumary:", sum)

# exit

print("exit!")