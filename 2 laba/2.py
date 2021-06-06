import math

#33
print("33------------")
print("а)")
x = int(input("x = "))
y = int(input("y = "))
if x > y:
    print("max = x = ", x)
elif y > x:
    print("max = y = ", y)
print("б)")
if x < y:
    print("min = x = ", x)
else:
    print("min = y = ", y)
print("в)")
if x > y:
    print("max = x = ", x)
    print("min = y = ", y)
elif y > x:
    print("max = y = ", y)
    print("min = x = ", x)

#43
print("43------------")
const1 = int(input("Число 1 = "))
const2 = int(input("Число 2 = "))
const3 = int(input("Число 3 = "))
if const1 > 0:
    print("Число 1 в квадрате = ", pow(const1, 2))
if const2 > 0:
    print("Число 2 в квадрате = ", pow(const2, 2))
if const3 > 0:
    print("Число 3 в квадрате = ", pow(const3, 2))

#53
print("53------------")
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
d = int(input("d = "))
e = int(input("e = "))
f = int(input("f = "))
g = int(input("g = "))
h = int(input("h = "))

f=(x-e)*(h-f)-(y-f)*(g-e)

f1 = (a-e)*(h-f)-(b-f)*(g-e)

f2=(c-e)*(h-f)-(d-f)*(g-e)

if ((f1>0) and (f2>0)) or ((f1<0) and (f2<0)):
    print("Да, приналежат")
else:
    print("Нет, не пренадлежат")


#34
print("34------------")

x = int(input("x = "))
y = int(input("y = "))
z = int(input("z = "))
if (x >= y) and (x >= z):
    max = x
elif (y >= x) and (y >= z):
    max = y
elif (z >= y) and (z >= x):
    max = z
print("max = ", max)
if (x <= y) and (x <= z):
    min = x
elif (y <= x) and (y <= z):
    min = y
elif (z <= y) and (z <= x):
    min = z
print("min = ", min)

#44
print("44------------")
x = int(input("x = "))
y = int(input("y = "))
z = int(input("z = "))

if (x + y + z <100):

    if((x < y) and (x < z)):
        x = (y+z)/2
    elif (y < z):
        y = (x+z)/2
    else:
        z = (x+y)/2
else:    
    if(x<y):
       x = (y+z)/2
    else:
       y = (x+z)/2


#54
print("54------------")

#35
print("35------------")
x = int(input("x = "))
y = int(input("y = "))
z = int(input("z = "))
print("a)") 

if (x + y + z > x * y * z):
    print("Максимальное x + y + z: ", x + y + z)
else:
    print("максимальное x * y * z: ", x * y * z)
print("b)")
if (x + y + z / 2 > x * y * z):
    min = x * y * z
else:
    min = x + y + z / 2
print("Минимальное: ", pow(min, 2) + 1)


#45
print("45------------")
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
d = int(input("d = "))
array = [a, b, c, d]
if (a <= b) and (b <= c) and (c <= d):
    max = array[0]
    #max foundation
    for i in array:
        if i > max:
            max = i
    #adding for every number
    a = array[0]
    b = array[1]
    c = array[2]
    d = array[3]
    print("Добавили к каждой переменной")
elif (a > b) and (b > c) and (c > d):
    print("Оставили как есть")




#55
print("55------------")
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

if ((a < c) and (b < d)) or ((a < d) and (b < c)):
    print("Да, можно уместить внутри прямоугольника")
else:
    print("Нельзя")

#36
print("36------------")
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

if (a < b) and (b < c):
    print("Неравенства выполняются")
else:
    print("неравенство не выполняется")


#----------------------------------------------------------Part 2. FIGHT!!!!

#61
print("61------------")
x = float(input("x = "))
print("Число Х", x, "Целая часть числа: ", int(x), "Округлене: ", round(x))
#71
print("71------------")

#62
print("62------------")
a = int(input("a = "))
if a % 2 == 0:
    print("парное")
else:
    print("не парное")
#72
print("72------------")


#63
print("63------------")
a = int(input("Введите неотрицательное число: "))
b = int(input("Введите положительное число: "))
r = int(input("r = "))
s = int(input("s = "))

if (a % b) == r or (a % b) == s:
    print("Остаток деления равен числу r или s")
else:
    print("остаток не равен")



#73
print("73------------")
m = int(input("m = "))
n = int(input("n = "))
if m > n :
    n = m
elif n > m:
    m = n
else:
    m = 0
    n = 0
print("m = ", m, " n = ", n)


#64
print("64------------")
print("а > 99")
a = int(input("a = "))
print("Колличество сотен:", a // 100)

#74
print("74------------")
n = int(input("Введите возраст до 100 лет"))

while n <= 100:
    if ((n % 10) == 1) or (n == 11):
        print(n, "год")
    elif ((n % 10) == 2) or ((n % 10) == 3) or ((n % 10) == 4):
        print(n, "года")
    elif ((n % 10) == 5) or ((n % 10) == 6) or ((n % 10) == 7) or ((n % 10) == 8) or ((n % 10) == 9) or ((n % 10) == 0):
        print(n, "лет")
#65
print("65------------")
num = int(input("Введите целое: "))
sqr = pow(n, 2)
sum = 0
while (num != 0):
    sum = sum + num % 10
    num = num // 10
if sqr == sum :
    print("равно")
else:
    print("не равно")

#75
print("75------------")
n = int(input("n > 7 = "))
if n <= 7:
    a = 1
    b = 1
    while a < n:
        while b < n:
            if (3 * a + 5 * b) == n:
                print("3 * ", a , " + 5 * ", b, " = ", n)