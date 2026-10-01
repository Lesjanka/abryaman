R = int(input("Введите радиус:"))
r = int(input("Введите радиус:"))
p = 3.14
if R < r:
    print("Ошибка")
else:
  S1=p*(R**2)
  S2=p*(r**2)
  S3=S1-S2
print(S1)
print(S2)
print(S3)