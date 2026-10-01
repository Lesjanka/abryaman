a = float(input("Введите угол:"))
p = 3.14
if 0>a:
    print("Ошибка")
elif a>360:
   print("Ошибка")
else:
    r=a*180//p
print(r)