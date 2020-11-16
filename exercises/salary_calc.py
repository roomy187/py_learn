#  tax rate 18%

# input brutto salary

print("please input your brutto salary:")

brutto = input()

brutto = int(brutto)

# calc netto & tax

netto = brutto * 0.82
tax = brutto * 0.18

# output

print("Your brutto salary:", brutto)
print("Your netto income:", int(netto))
print("paid taxes:", int(tax))