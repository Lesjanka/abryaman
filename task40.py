a1 = float(input("Введите a1:"))
b1 = float(input("Введите b1:"))
c1 = float(input("Введите c1:"))
a2 = float(input("Введите a2:"))
b2 = float(input("Введите b2:"))
c2 = float(input("Введите c2:"))
D= a1 * b2 - a2 * b1
if D != 0:
    x = (c1 * b2 - c2 * b1) / D
    y =(a1 * c2 - a2 * c1) / D
    print(f"x={x:.4f}")
    print(f"y={y:.4f}")
else:
    print("У системы нет решения (D = 0)")