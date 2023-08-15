# Zadanie 1. Proszę napisać program wypisujący elementy ciągu Fibonacciego mniejsze od miliona

a = b = 1
print(b)
while a < 10 ** 6:
    print(a)
    tmp = b
    b = a
    a += tmp

# Zadanie 2. Proszę znaleźć wyrazy początkowe zamiast 1,1 o najmniejszej sumie, aby w ciągu analogicznym
# do ciągu Fibonacciego wystąpił wyraz równy numerowi bieżącego roku.

suma = 10000
best = (2022, 0)

for i in range(2023):
    x, y = best
    while x > 0 and y > x:
        x, y = y - x, x
    if x + y < suma:
        suma = x + y
        best = (x, y)


print(suma, best)


# Zadanie 3. Proszę napisać program sprawdzający czy istnieje spójny podciąg ciągu Fibonacciego o zadanej
# sumie.

def is_exist(sum):
    for i in range(1, sum):
        for j in range(sum):
            a = i
            b = j
            while a < sum:
                tmp = a
                a = a + b
                b = tmp
            if a == sum:
                return True
    return False


# Zadanie 4. Proszę napisać program obliczający pierwiastek całkowitoliczbowy z
# liczby naturalnej korzystając z zależności 1 + 3 + 5 + ... = n^2

# licz = 0
# k = 0
# a = 1
# n = 15
# while k + a <= n:
#     k += a
#     licz += 1
#     a += 2

liczba = int(input())

suma = 0
el = 1
i = 0
while suma < liczba:
    suma += el
    i += 1
    if liczba == suma:
        print(i)
    elif suma > liczba:
        print(i - 1)
        break
    el += 2

# print(licz)

# Zadanie 5. Proszę napisać program wyznaczający pierwiastek kwadratowy ze wzoru Newtona.
import math

s = math.sqrt(7)
a = 1
p = s ** 2
b = p
e = 10 ** (-100)

while abs(a - b) >= e:
    a = (a + b) / 2
    b = p / a


print(a)

def newton_raphson(num, ep=0.000001):
    a, b = 1, num
    while abs(a - b) > ep:
        a = (a + b) / 2
        b = num / a
    return a


print(newton_raphson(9))

# Zadanie 6. Proszę napisać program rozwiązujący równanie x^x = 2022 metodą bisekcji

def f(x):
    return x ** x - 2022


def solve(ep=0.0000001):
    a, b = 0, 100
    while abs(a - b) > ep:
        x = (a + b) / 2
        if f(x) == 0:
            return x
        if f(a) * f(x) < 0:
            b = x
        elif f(x) * f(b) < 0:
            a = x
    return (a + b) / 2


# Zadanie 7. Napisz program wczytujący liczbę naturalną z klawiatury i odpowiadający na pytanie, czy
# liczba ta jest iloczynem dowolnych dwóch kolejnych wyrazów ciągu Fibonacciego.

def isFibProduct(num):
    a, b = 1, 1
    while a * b < num:
        a, b = b, a + b
    if a * b == num:
        return True
    else:
        return False


print(isFibProduct(int(input())))

# Zadanie 8. Napisać program sprawdzający czy zadana liczba jest pierwsza.

def is_first(n):
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    if n <= 1:
        return False
    i = 5
    while i * i < n:
        if n % i == 0:
            return False
        i += 2
        if n % i == 0:
            return False
        i += 4
    return True


# Zadanie 9. Napisać program wypisujący podzielniki liczby.

def podzielniki(n):
    print(1)
    for i in range(2, n + 1):
        if n % i == 0:
            print(i)
            while n % i == 0:
                n //= i
        if n == 1:
            break


# podzielniki(18)


# Zadanie 10. Napisać program wyszukujący liczby doskonałe mniejsze od miliona

def sumOfDiv(num):
    s = 1
    i = 2
    while i ** 2 < num:
        if num % i == 0:
            s += i
            s += num // i
        i += 1
    if i ** 2 == num:
        s += i

    return s


for num in range(4, 1_000_000):
    if sumOfDiv(num) == num:
        print(num)


# Zadanie 11. Napisać program wyszukujący liczby zaprzyjaźnione mniejsze od miliona.

def sumOfDiv2(num):
    s = 1
    i = 2
    while i ** 2 < num:
        if num % i == 0:
            s += i
            s += num // i
        i += 1
    if i ** 2 == num:
        s += i

    return s


for num1 in range(2, 1_000_000):
    num2 = sumOfDiv2(num1)
    if num1 > num2 and sumOfDiv(num2) == num1:
        print(num1, num2)


# Zadanie 12. Napisać program wyznaczający największy wspólny dzielnik 3 zadanych liczb.
def nwd(a, b):
    while b != 0:
        b, a = a % b, b
    return a


def nwd3(a, b, c):
    return nwd(nwd(a, b), c)


print(nwd3(60, 30, 105))


# Zadanie 13. Napisać program wyznaczający najmniejszą wspólną wielokrotność 3 zadanych liczb.


def nwd(a, b):
    while b != 0:
        b, a = a % b, b
    return a


def nww(a, b):
    return a * b // nwd(a, b)


def nww3(a, b, c):
    return nww(nww(a, b), c)


print(nww3(60, 30, 105))

# Zadanie 14. Napisać program obliczający wartości cos(x) z rozwinięcia w szereg Maclaurina

from math import factorial


def szereg_Maclaurina(x, dok=5):
    s = 0
    for i in range(dok):
        s += ((-1) ** i) * (x ** (2 * i)) / factorial(2 * i)
    return s


szereg_Maclaurina(0)

# Zadanie 15. Nieskończony iloczyn sqrt(0.5) ∗ sqrt(0.5 + 0.5 ∗ sqrt(0.5)) ∗ sqrt(0.5 + 0.5 ∗ sqrt(0.5 + 0.5 ∗
# sqrt(0.5))) ∗ ... ma wartość 2/π. Napisz program korzystający z tej zależności i wyznaczający wartość π.

# wyrazy tego nieskończonego iloczynu można przedstawić jako ciąg rekurencyjny
# a(1) = sqrt(0.5)
# a(n) = sqrt(0.5 + 0.5*a(n-1))


from math import sqrt


def calc_pi(prec=10):
    pi = 2
    a = sqrt(0.5)
    for _ in range(prec):
        pi /= a
        a = sqrt(0.5 + 0.5 * a)
    return pi


print(calc_pi())


# Zadanie 16. Dany jest ciąg określony wzorem: An+1 = (An mod 2) ∗ (3 ∗ An + 1) + (1 − An mod 2) ∗ An/2
# Startując z dowolnej liczby naturalnej > 1 ciąg ten osiąga wartość 1. Napisać program, który znajdzie wyraz
# początkowy z przedziału 2-10000 dla którego wartość 1 jest osiągalna po największej liczbie kroków.

def find():
    best_num = 0
    best_counter = 0
    for start_a in range(2, 10_001):
        a = start_a
        counter = 0
        while abs(a - 1) > 0.00000001:
            a = (a % 2) * (3 * a + 1) + (1 - a % 2) * (a / 2)
            counter += 1
        if counter > best_counter:
            best_counter = counter
            best_num = start_a
    return best_num


print(find())


# Zadanie 17. Napisać program wyznaczający wartość do której zmierza iloraz dwóch kolejnych wyrazów
# ciągu Fibonacciego. Wyznaczyć ten iloraz dla różnych wartości początkowych wyrazów ciągu.

def golden_ratio(prec=50):
    a, b = 1, 1
    old_ratio, ratio = 1, 0
    # for _ in range(prec):
    while abs(old_ratio - ratio) > 0.00000000001:
        a, b = b, a + b
        old_ratio, ratio = ratio, b / a
    return b / a


print(golden_ratio())


# Zadanie 18. Zmodyfikować wzór Newtona aby program z zadania 5 obliczał pierwiastek stopnia 3.

def newton_cube(num):
    b, c = 1, num
    while abs(c - b) > 0.0000000001:
        b = (b * 2 + c) / 3
        c = num / b / b
    return b


print(newton_cube(int(input())))


# Zadanie 19. Napisać program wyznaczający wartość liczby e korzystając z zależności: e = 1/0! + 1/1! +
# 1/2! + 1/3! + .....

def calc(prec=50):
    fac = 1
    c = 0
    for i in range(1, prec):
        c += 1 / fac
        fac *= i
    return c


# print(calc())

# Zadanie 20. Dane są ciągi: An+1 = sqrt( An ∗ Bn) oraz Bn+1 = (An + Bn)/2.0. Ciągi te są zbieżne do
# wspólnej granicy nazywanej średnią arytmetyczno-geometryczną. Napisać program wyznaczający średnią
# arytmetyczno-geometryczną dwóch liczb.
from math import sqrt


def average(a, b):
    while abs(a - b) > 0.000001:
        a, b = sqrt(a * b), (a + b) / 2
    return a


# print(average(4, 7))
