a = float(input("Введите число:"))
b = float(input("Введите число:"))
if a==0 or b==0:
    print("Ошибка")
else:
    a_abs = abs(a)
    b_abs = abs(b)
s = a_abs + b_abs
r = a_abs - b_abs
p = a_abs * b_abs
c = a_abs / b_abs
print(s)
print(r)
print(p)
print(c)