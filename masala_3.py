# 3-masala. FILE MANAGER
# s = "Salom bolalar ishlar qaley"
# s = "O'rdak."
# s = "Assalomu aleykum. Bugun imtihon va men undan o'taman!"
s = input(">>> ")
for i in s.split():
    lampochka = 1
    c = ""
    for j in i:
        if j in c:
            lampochka = 0
            break
        if j.isalpha():
            c += j
    if lampochka:
        n = len(c) // 2
        c = c[-n:] + c[:-n]
        print(c)