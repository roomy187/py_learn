# 1 inch = 2.54 cm

# input 

print("please input your inches:")
print("type \"0\" to quit")



# init loop & counter

i = 1
c = 0
fail = 1

# while loop (define exit argument)

while fail == 1:
   
    

        while i != 0:
            i = input()
            try:
                i = int(i)
                if i != 0:

                # loop counter
                    c = c + 1
                    print(i, "inches are", i * 2.54, "cm.")

                else:
                    print("BYE Fuckface!")
                    fail = 0
    
            except:
                print(i, "is not a valid input! Try again, Fuckface!")




# exit & counter output

print("you made", c, "calulations.")
print("see you next time, Fuckface!")