# init while loop

fail = 1

# loop at worng input

while fail == 1:

    # input

    print("please input a number:")
    z = input()

    # try convert to integer

    try:
        z = int(z)
        print(z, "is a number, that's correct!")
        fail = 0
    
    # exeption message

    except:
        print(z, "is not a number! Try again, Fuckface!")

print("exit")