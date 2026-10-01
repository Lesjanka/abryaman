V = float(input("Скорость первого автомобиля:"))
V2 = float(input("Скорость второго автомобиля:"))
S = float(input("Начальное расстояние:"))
T = float(input("Время:"))
all_v = V + V2
path = T * all_v
S_new = S + path
print("Расстояние автомобилей через введенное время", S_new)