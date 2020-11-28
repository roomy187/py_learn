#!/usr/bin/python3
#### init rng

import random
random.seed()


### select how much tasks user want to do

tasks = -1 

while tasks<0 or tasks>10:
    try:
        print("How many task do you want to perform? (1-10)")
        tasks = int(input())
    except:
        continue

### counter for correct answers

correct = 0

### while loop with "tasks" # 

for counter in range(1,tasks+1):

    #### randomize calulation operator
    operator = random.randint(1,4)

    #### define caluation operators

    if operator == 1:
        a = random.randint(1,30)
        b = random.randint(1,30)
        op = "+"
        c = a+b
    elif operator == 2:
        a = random.randint(1,30)
        b = random.randint(1,30)
        op = "-"
        c = a-b
    elif operator == 3:
        a = random.randint(1,30)
        b = random.randint(1,30)
        op = "*"
        c = a*b
    ### special case for division 
    elif operator == 4:
        c = random.randint(1,30)
        b = random.randint(1,30)
        op = "/"
        a = c*b

    ### print task
    print("Task", counter, "of", tasks, ":", a, op, b)

    ### loop with 3 tries per task max

    for tri in range(1,4):

        # input answer
        try:
            print("Your answer:")
            asw = int(input())
        except:
            print("Thats not a number, Fuckface!")
            continue
    

    ### comment 

        if asw == c:
            print(asw, "is correct, you Matherfucker!")
            correct = correct+1
            break
        else:
            print(asw, "is not correct, Fuckface!")

    ### if 3 tries failed, print correct answer

    print("The correct answer was:", c, "Fuckface!")

### final summary

print("Correct answers:", correct, "of", tasks)