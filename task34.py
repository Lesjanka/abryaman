X = float(input("Введите кол-во конфет в кг X:"))
A = float(input("Введите стоимость A:"))
Y = float(input("Введите кол-во конфет в кг Y:"))
B = float(input("Введите стоимость B:"))
price = A/X
price_y = price * Y
price2 = B/Y
price_x = price2 * X
raznitsa = price_x/price_y
print(price)
print(price_y)
print("Разница в", raznitsa)