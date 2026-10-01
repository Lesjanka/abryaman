L = int(input("Введите длину окружности:"))
p = 3.14
if L <=0:
    print("Ошибка введеных данных")
else:
    R=L/(2*p)
    S=p*R*R
print(R)
print(S)