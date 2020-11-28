#### define funtion for tax rate based on income

def tax(x):
    if x > 2500:
        netto = x * 0.78
        t = x * 0.22
        return (netto,t)
        
    else:
        netto = x * 0.82
        t = x * 0.18
        return (netto,t)    ###  return values
        

# main prog

for i in [1800, 2200, 2500, 2900]:
    netto, t =  tax(i)     #### define vars from function befor function call!!! 
    
## outputs

    print("Brutto:", i)
    print("Netto:", netto)
    print("Taxes:", t)