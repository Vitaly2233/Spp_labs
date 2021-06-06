import math
# 1
a = 6
b = 3
print("сума ", a + b)
print("Разность", a - b)
print("произведение", a * b)

# 2
y = 10
x = 5
c = (abs(x) - abs(y)) / (1 + abs(x) * abs(y))
print("2 задание", c)
# 3

rebro = 5
print("Объем", pow(rebro, 3))
print("Площадь боковой поверхности", rebro * rebro)

# 4
d = (a + b) / 2
print("Среднее арифметическое: ", d)
e = math.sqrt(a * b)
print("среднее геометрическое", e)

# 5

print("Среднее арифметическое модулей", (abs(x) + abs(y)) / 2)
print("Среднее геометрическое модулей", math.sqrt(abs(x) * abs(y)))
# 6

print("Гипотенуза", math.sqrt(math.pow(x, 2) + math.pow(y, 2)))
print("площадь", x * y / 2)

# 7
v1 = 27
t1 = 13
v2 = 30
t2 = 18
print("Обем", v1 + v2)
print("температура", (t1 + t2) / 2)

# 8
r = 7
a = 2 * pow(3, 1 / 3) * r
print("периметр", a * 3)

# 9

r1 = 14
r2 = 10
r3 = 5

print("сопротивление соедениния", 1 / (1 / r1 + 1 / r2 + 1 / 3))

# 10

g = 10
h = 20
print("время падения", math.sqrt(2 * h / g))

# import math
#
# x = int(input())
# y = int(input())
#
# # 11
# # A
# z = 19
# a = (math.sqrt(x - 1) - math.pow(abs(y), 1 / 3)) / (1 + pow(x, 2) / 2 + pow(y, 2) / 4)
# b = x * (math.atan(z) + math.exp(-1 * (x + 3)))
# print(b)
# # Б
# a = (3 + math.exp(y - 1)) / (1 + pow(x, 2) * abs(y - math.tan(z)))
# b = 1 + abs(y - z) + pow((y - x), 2) / 2 + pow(abs(y - x), 3) / 3
# # B
# a = (a + y) * (x + y) / (pow(x, 2) + 4) / (math.exp(-1 * x - 2) + 1 / (pow(x, 2) + 4))
# b = (1 + math.cos(y - 2)) / (pow(x, 4) / 2 + (pow(math.sin(z), 2)))
# # Д
# a = y + x / (pow(y, 2) + abs(pow(x, 3) / (y + pow(x, 3) / 3)))
# b = 1 + pow(math.tan(z / 2), 2)
# # Г
# a = 2 * math.cos(x - math.pi / 6) / (1 / 2 + pow(math.sin(y), 2))
# b = 1 + pow(z, 2) / (3 + pow(z, 2) / 5)
# # E
# a = (1 + pow(math.sin(x + y), 3)) / (2 + abs(x - 2 * x)) / (1 + pow(x, 2) * pow(y, 2))
# b = pow(math.cos(math.atan(1 / z)), 2)
# # Ж
# a = math.log(abs((y - math.sqrt(abs(x))) * (x - y / (z + pow(x, 3) / 4))))
# b = x - pow(x, 2) / 3 * 2 * 1 + pow(x, 5) / 5 * 4 * 3 * 2 * 1
#
# # 21
# c = 10
# d = 5
#
# check1 = (3 - math.sqrt((9 - 4) * 1 * c * d)) / 2
# check2 = (3 + math.sqrt((9 - 4) * 1 * c * d)) / 2
# if check1 > check2:
#     x1 = check1
#     x2 = check2
# else:
#     x1 = check2
#     x2 = check1
#
# abs(pow(math.sin(abs(c * pow(x1, 3) + d * pow(x2, 2) - c * d)), 3) / (
#             pow(math.sqrt(c * pow(x1, 3) + d * pow(x2, 2) - x1), 2) + 3.14)) + math.tan(
#     c * pow(x1, 3) + d * pow(x2, 2) - x1)
# # 31
#
#
# # 41
# nun = [1, 2, 2]
# for x in nun:
#     if nun[x] > 1 and nun[x] < 3:
#         print(nun[x])
#
# # 51
# a = 5
# b = 6
# c = 6.4
# d = math.sqrt(b * b) - (4 * a * c)
# if d > 0:
#     t1 = (-b - math.sqrt(d)) / (2 * a)
#     t2 = (-b + math.sqrt(d)) / (2 * a)
#     if t1 >= 0:
#         x1 = math.sqrt(t1)
#         x2 = - math.sqrt(t1)
#     elif t2 >= 0:
#         x3 = math.sqrt(t2)
#         x4 = - math.sqrt(t2)
#         print("Корені: ", x1, x2, x3, x4)
#     if d == 0:
#         x1 = math.sqrt(-b / 2 * a)
#         x2 = - math.sqrt(-b / 2 * a)
#         print("Корені: ", x1, x2)
#     if d < 0:
#         print("немає коренів")
#
# # 61
# x = 3.123213
# print("Число Х", x, "Целая часть числа: ", int(x), "Округлене: ", round(x))
#
# # 71
# min = 0
# max = 1.5
#
# # 81
# x = 5
# a = 1
# n = 10
# p = 0
# i = 0
# while i < n:
#     p = math.sqrt(p + a)
#     print("P= ", p)
#     i += 1
#
# # 91
