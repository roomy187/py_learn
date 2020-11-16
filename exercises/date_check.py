# input values

print("input day:")

d = input()
d = int(d)

print("input month:")

m = input()
m = int(m)

print("input year:")

y = input()
y = int(y)

# leap year check

if y % 4 == 0 and y % 100 != 0:
    
    ly = True
else:
    
    ly = False

# validate month

if m < 1 or m > 12:

    print("incorrect month, fuckface!")
    exit

elif m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
    
    me = 31

elif m == 2:
    
    if ly == True:
        
        me = 29
    else:

        me = 28

else:
    me = 30

# validate day

if d < 1 or d > me:
    print("wrong day,motherfucker!")


# output

print("last day of month is:", me)