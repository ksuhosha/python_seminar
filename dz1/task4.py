# 4. Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных
# координат точек в этой четверти (x и y).

quarter = int(input('Ведите четверть (от 1 до 4х):'))

while 1 > quarter or 4 < quarter:
    X = int(input('Ведите четверть (от 1 до 4х):'))

if quarter == 1:
    print('x = (0; +∞) и y = (0; +∞)')
elif quarter == 2:
    print('x = (0; -∞) и y = (0; +∞)')
elif quarter == 3:
    print('x = (0; -∞) и y = (0; -∞)')
else:
    print('x = (0; +∞) и y = (0; -∞)')