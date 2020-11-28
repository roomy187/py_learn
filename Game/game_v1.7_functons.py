#### rng

import random
random.seed()



#### define calcualtion task

def task():
    a = random.randint(1,100)
    b = random.randint(1,100)
    asw = a+b
    print("The task:", a, "+", b)
    return asw

### define comment function 

def comment(ipt, asw):
    if ipt == asw:
        print(ipt, "is correct, you Matherfucker!")
    else:
        print(ipt, "is the wrong answer, Fuckface!")

##### task

c = task()

#### init loop & counter

n = c+1
count = 0

###### while loop

while n !=  c:
    
    ### add to counter
    count = count+1

    ### input
    print("Your answer:")
    i = input()

    ### integer check

    try:
        n = int(i)
    except:
        print("Thats not a number, Fuckface!")
        continue

    ### comment 

    comment(n, c)

### final summary

print("Correct answer:", c)
print("You needed", count, "tries!")
