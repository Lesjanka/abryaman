x1 = float(input("Введите точку"))
y1 = float(input("Введите точку"))
x2 = float(input("Введите точку"))
y2 = float(input("Введите точку"))
a = abs(x2-x1)
b = abs(y2-y1)
if a==0 or b == 0:
    print("Ошибка")
else:
    P = 2*(a+b)
    S = a*b
print(a)
print(b)
print(P)
print(S)