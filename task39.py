A = float(input("Введите коэффицент a (A Не равен 0):"))
B = float(input("Введите коэффицент b:"))
C = float(input("Введите коэффицент c:"))
D = B*B-4*A*C
if D>0:
    x1=(-B+D*0.5)/(2*A)
    x2=(-B-D*0.5)/(2*A)
x_min = min(x1, x2)
x_max = max(x1, x2)
print("Меньший корень:", x_min)
print("Наибольший корень:", x_max)
