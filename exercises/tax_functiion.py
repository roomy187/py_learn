#### define funtion for tax rate based on income

def tax(x):
    if x > 2500:
        netto = x * 0.78
        tax = x * 0.22
        print("Brutto:", x)
        print("Netto:", netto)
        print("Taxes:", tax)
    else:
        netto = x * 0.82
        tax = x * 0.18
        print("Brutto:", x)
        print("Netto:", netto)
        print("Taxes:", tax)

# main prog

for i in [1800, 2200, 2500, 2900]:
    tax(i)