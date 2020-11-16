# set marriage state

print("are you married? y/n:")

m = input(str())

if m == "y" or "yes":
    m = True
elif  input == "n" or "no":
    m = False
else:
    print("Wrong input, please answer with \"y\" or \"n\"!")

# input brutto salary

print("please input your brutto salary:")

brutto = input()

brutto = int(brutto)

# calc individual netto & tax with high income statements for higher tax classes, with marriage status

if brutto <= 4000 and m == True:
    netto = brutto * 0.82
    tax = brutto * 0.18

elif brutto <= 4000 and m == False:
    netto = brutto * 0.78
    tax = brutto * 0.22

elif brutto > 4000 and m == True:
    netto = brutto * 0.78
    tax = brutto * 0.22
else:
    netto = brutto * 0.74
    tax = brutto * 0.26


# output

print("Your brutto salary:", brutto)
print("Your netto income:", int(netto))
print("paid taxes:", int(tax))