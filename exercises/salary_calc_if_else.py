#  tax rate 18%

# input brutto salary

print("please input your brutto salary:")

brutto = input()

brutto = int(brutto)

# calc netto & tax with high income statement for higher taxes

if brutto <= 2500:
    netto = brutto * 0.82
    tax = brutto * 0.18
else:
    netto = brutto * 0.78
    tax = brutto * 0.22


# output

print("Your brutto salary:", brutto)
print("Your netto income:", int(netto))
print("paid taxes:", int(tax))