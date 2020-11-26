##### use of continue in a loop #####

for i in range (1,7):
    print("Number:", i)
    if 3 <= i <= 5:
        continue
    print("Quads:", i * i)