#  tax rate 18%

# input brutto salary

print("please input your brutto salary:")

brutto = input()

brutto = int(brutto)

# calc individual netto & tax with high income statements for higher tax classes

if brutto <= 2500:
    netto = brutto * 0.82
    tax = brutto * 0.18

elif brutto <= 4000:
    netto = brutto * 0.78
    tax = brutto * 0.22
else:
    netto = brutto * 0.74
    tax = brutto * 0.26


# output

print("Your brutto salary:", brutto)
print("Your netto income:", int(netto))
print("paid taxes:", int(tax))