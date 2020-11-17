# safe exit if user provides incorrect input

# input

print("please input a number:")

z = input()

# try to convert into integer

try:
    z = int(z)
    print("your input", z, "is a integer!")
    
# exeption for wrong input 
   
except:
    print(z, "is not a number, Fuckface!")

print("exit")
