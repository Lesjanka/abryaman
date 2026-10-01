a = int(input("Введите a:"))
b = int(input("Введите b:"))
c = int(input("Введите c:"))
a, b = b, a
b, c = c, b
c, a = a, c
print(a, b, c)
