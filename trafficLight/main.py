print('Время первого светофора: ')
t1 = float(input())

print('Время второго светофора: ')
t2 = float(input())

print('Колличество дорог на первой дороге: ')
n1 = int(input())

print('Колличество дорог на второй дороге: ')
n2 = int(input())

print('Колличество машин которое может пропустить перекресток за один цикл: ')
print(t1*40*n2/100+t2*40*n1/100)