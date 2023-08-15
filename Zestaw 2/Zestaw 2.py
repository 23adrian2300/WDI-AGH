"""
Ćwiczenia 2: Proste programy z pętlami cz. 2
"""

"""
# Zadanie 1. Napisz program wczytujący liczbę naturalną z klawiatury i odpowiadający na pytanie, czy
# liczba ta jest iloczynem dowolnych dwóch wyrazów ciągu Fibonacciego.
"""

n = int(input())

a = b = 1
flag = False
while a <= n:
    a1, b1 = 1, 1
    while a1 <= n:
        if a * a1 == n:
            print("true")
            flag = True
            break
        tmp = a1
        a1 = a1 + b1
        b1 = tmp
    tmp = a
    a = a + b
    b = tmp
    if flag:
        break
if not flag:
    print("false")

"""
Zadanie 2. Napisać program wczytujący trzy liczby naturalne a,b,n i wypisujący rozwinięcie dziesiętne
ułamka a/b z dokładnością do n miejsc po kropce dziesiętnej. (n jest rzędu 100)
"""
a = int(input())
b = int(input())
n = int(input())

print(a // b, "." if a % b != 0 else "", sep="", end="")
a %= b
while a > 0 and n > 0:
    a *= 10
    print(a // b, end="")
    a %= b
    n -= 1

"""
Zadanie 3. Napisz program wczytujący liczbę naturalną z klawiatury i odpowiadający na pytanie, czy
liczba naturalna jest palindromem, a następnie czy jest palindromem w systemie dwójkowym
"""
num = int(input())

rev_num = 0
num_copy = num
while num_copy > 0:
    rev_num = rev_num*10 + num_copy%10
    num_copy //= 10

print(rev_num == num,rev_num)

#binary
rev_num = 0
num_copy = num
while num_copy > 0:
    rev_num = rev_num*2 + num_copy%2
    num_copy //= 2

print(rev_num == num)

# Zadanie 4. Liczba dwu-trzy-piątkowa w rozkładzie na czynniki pierwsze nie posiada innych czynników niż
# 2,3,5. Jedynka też jest taką liczbą. Napisz program, który wylicza ile takich liczb znajduje się w przedziale
# od 1 do N włącznie.

n = int(input())
counter = 0
for num in range(1, n + 1):
    copy = num
    if num % 2 == 0:
        while num % 2 == 0:
            num //= 2
    if num % 3 == 0:
        while num % 3 == 0:
            num //= 3
    if num % 5 == 0:
        while num % 5 == 0:
            num //= 5
    if num == 1:
        counter += 1
print(counter)

# Zadanie 5. Dana jest liczba naturalna o niepowtarzających się cyfrach pośród których nie ma zera. Ile
# różnych liczb podzielnych np. przez 7 można otrzymać poprzez wykreślenie dowolnych cyfr w tej liczbie. Np.
# dla 2315 będą to 21, 35, 231, 315.
import math
def get_leng(num):
    return math.floor(math.log10(num)) + 1


def create_number(org_num, mask):
    new_rev_num = 0
    while org_num > 0:
        if mask % 2 == 1:
            new_rev_num *= 10
            new_rev_num += org_num % 10
        mask //= 2
        org_num //= 10

    new_num = 0
    while new_rev_num > 0:
        new_num *= 10
        new_num += new_rev_num % 10
        new_rev_num //= 10

    return new_num



# n = int(input())

counter = 0
for i in range(1, 2**get_leng(n)):
    if create_number(n, i) % 7 == 0:
        print(create_number(n,i))
        counter += 1

print(counter)

# Zadanie 6. Napisać program wczytujący liczbę naturalną z klawiatury i rozkładający ją na iloczyn 2 liczb
# o najmniejszej różnicy. Np. 30 = 5 ∗ 6, 120 = 10 ∗ 12

# n = int(input())
copy = n
i = 1
sub = n
best = (0, 0)
if n > 1:
    while i * i <= n:
        if copy % i == 0:
            new = n // i
            if new <= sub:
                best = (i, n // i)
        i += 1

print(n, " = ", best[0], " * ", best[1])


# Zadanie 7. Napisz program wczytujący liczbę naturalną z klawiatury i odpowiadający na pytanie, czy
# liczba ta jest wielokrotnością dowolnego wyrazu ciągu danego wzorem An = n ∗ n + n + 1.

# num = int(input())

an = 0
n = 0
flag = False
while an < num:
    an = n * n + n + 1
    if num%an == 0:
        print("True")
        flag = True
        break
    n += 1
if not flag:
    print("False")
"""
# Zadanie 8. Pewnych liczb nie można przedstawić jako sumy elementów spójnych
# fragmentów ciągu Fibonacciego, np. 9,14,15,17,22. Proszę napisać program,
# który wczytuje liczbę naturalną n, wylicza i wypisuje
# następną taką liczbę większą od n. Można założyć, że 0 < n < 1000.
"""


def find_the_smallest_unsumable(num):  # probably it is possible to do this faster
    num += 1
    while True:
        f1, f2 = 1, 1
        fib_suma = 0
        while fib_suma < num:
            fib_suma += f1
            f1, f2 = f2, f1 + f2

        f1, f2 = 1, 1
        while fib_suma > num:
            fib_suma -= f1
            f1, f2 = f2, f1 + f2

        if fib_suma != num:
            return num
        num += 1


# num = int(input())

print(find_the_smallest_unsumable(num))

# Zadanie 9. Napisać program, który oblicza pole figury pod wykresem funkcji y = 1/x w przedziale od 1
# do k, metodą prostokątów.

k = int(input())
step = 0.00001
area = 0
x = 1
while x < k:
    height = 1 / x
    area += (step * height)
    x += step
print(area)

# Zadanie 10. Napisz program wczytujący liczbę naturalną z klawiatury i odpowiadający na pytanie, czy
# liczba ta jest wielokrotnością dowolnego wyrazu ciągu danego wzorem An = 3 ∗ An−1 + 1, a pierwszy wyraz
# jest równy 2.

# num = int(input())
a0 = 2
n = 0
an = 0
flag = False
while an < num:
    an = n * a0 + n + 1
    if num % an == 0:
        print("True")
        flag = True
        break
    n += 1
    a0 = an
if not flag:
    print("False")

# Zadanie 11. Napisz program wczytujący liczbę naturalną z klawiatury i odpowiadający na pytanie, czy
# jej cyfry stanowią ciąg rosnący.

# num = int(input())
last = 10
flag = True
while num > 0:
    current = num % 10
    if last <= current:
        print("false")
        flag = False
        break
    num //= 10
    last = current
if flag:
    print("True")


# Zadanie 12. Napisz program wczytujący liczbę naturalną z klawiatury i odpowiadający na pytanie, czy
# liczba ta zawiera cyfrę równą liczbie swoich cyfr.

# num = int(input())
copy = num
length = 0
flag = False
while copy > 0:
    length += 1
    copy //= 10

while num > 0:
    if num % 10 == length:
        print("True")
        flag = True
        break
    num //= 10
if not flag:
    print("False")

# Zadanie 13. Napisz program wczytujący liczbę naturalną z klawiatury i odpowiadający na pytanie, czy
# liczba zakończona jest unikalną cyfrą.

# n = int(input())
last = n % 10
spr = n // 10
flag = True
while spr > 0:
    if spr % 10 == last:
        print("False")
        flag = False
    if not flag:
        break
    spr //= 10
if flag:
    print("True")


# Zadanie 14. Dane są dwie liczby naturalne z których budujemy trzecią liczbę. W budowanej liczbie
# muszą wystąpić wszystkie cyfry występujące w liczbach wejściowych. Wzajemna kolejność cyfr każdej z liczb
# wejściowych musi być zachowana. Na przykład mając liczby 123 i 75 możemy zbudować liczby 12375, 17523,
# 75123, 17253, itd. Proszę napisać funkcję która wyznaczy ile liczb pierwszych można zbudować z dwóch
# zadanych liczb.
import math


def is_prime(num):
    if num <= 1:
        return False
    if num == 2 or num == 3 or num == 5:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False

    for i in range(6, int(math.sqrt(num)) + 1, 6):
        if num % (i - 1) == 0 or num % (i + 1) == 0:
            return False
        i += 2

    return True


def get_leng(num):
    return math.floor(math.log10(num)) + 1


def validate_mask(leng1, leng2, mask):
    while mask > 0:
        if mask % 2 == 0:
            leng1 -= 1
        else:
            leng2 -= 1
        mask //= 2
    return leng1 >= 0 and leng2 == 0


def mix_numbers(a, b, mask):
    new_num = 0
    mult = 1
    while mask > 0 or a > 0:
        if mask % 2 == 0:
            d = a % 10
            a //= 10
        else:
            d = b % 10
            b //= 10

        mask //= 2

        new_num = d * mult + new_num
        mult *= 10

    return new_num


# counter = 0
# a, b = map(int, input().split())
# leng_a, leng_b = get_leng(a), get_leng(b)
#
# for mask in range(2 ** (leng_a + leng_b)):
#     if validate_mask(leng_a, leng_b, mask) and is_prime(mix_numbers(a, b, mask)):
#         counter += 1


# Zadanie 15. Napisać program znajdujący wszystkie liczby N-cyfrowe dla których suma N-tych potęg cyfr
# liczby jest równa tej liczbie, np. 153 = 1^3 + 5^3 + 3^3


def get_leng(num):
    return math.floor(math.log10(num)) + 1


def check_condition(num, leng):
    sum = 0
    num_copy = num
    while num_copy > 0:
        sum += (num_copy % 10) ** leng
        num_copy //= 10
    return sum == num


# i = 1
# leng = 1
# while leng * (9 ** leng) >= 10 ** (leng - 1):
#     if check_condition(i, leng):
#         print(i)
#     i += 1
#     leng = get_leng(i)


# Zadanie 16. Liczba Smitha to taka, której suma cyfr jest równa sumie cyfr wszystkich liczb występujących
# w jej rozkładzie na czynniki pierwsze. Na przykład: 85 = 5∗17, 8+5 = 5+1+7. Napisać program wypisujący
# liczby Smitha mniejsze od 1000000.

def smith(n):
    def digitsum(n):
        k = str(n)
        sum = 0
        for i in range(len(k)):
            sum += int(k[i])
        return sum

    i = 2
    copy = n
    suma = 0
    while n > 0 and i * i < n:
        if n % i == 0:
            suma += digitsum(i)
            suma += digitsum((n // i))
            while n % i == 0:
                n //= i
        i += 1
    if digitsum(copy) == suma:
        return True
    return False


# n = 0
# while n < 1e3:
#     if smith(n):
#         print(n)
#     n+=1


# Zadanie 17. Napisać program wyliczający pierwiastek równania x
# x = 2020 metodą stycznych.


import math


def solve(f, df):
    x = 1
    eps = 0.0001
    prev_x = x + eps * 10
    while abs(prev_x - x) > eps:
        # for i in range(1000):
        prev_x = x
        x = x - f(x) / df(x)

    print(x)


def function(x):
    return x ** x - 2020


def derivative(x):
    return (x ** x) * (math.log(x) + 1)


# Zadanie 18. Mamy dane dwa ciągi A,B o następujących zależnościach:
# A: a0 = 0, a1 = 1, an = an−1 − bn−1 ∗ an−2
# B: b0 = 2, bn = bn−1 + 2 ∗ an−1
# Proszę napisać program, który czyta liczby typu int ze standardowego wejścia i tak długo jak liczby te są
# kolejnymi wyrazami ciągu An (tj. a0, a1, a2, ...) wypisuje na standardowe wyjście wyrazy drugiego ciągu Bn
# (tj. b0, b1, b2, ...).

a0, a1 = 0, 1
b0 = 2
b1 = b0 + 2 * a0

if int(input()) == a0:
    print("b", b0)
else:
    exit()

while int(input()) == a1:
    print("b", b1)
    a0, a1 = a1, a1 - b1 * a0
    b0, b1 = b1, b1 + 2 * a0

# Zadanie 19. Napisać program wczytujący dwie liczby naturalne a,b i wypisujący rozwinięcie dziesiętne
# ułamka a/b w postaci ułamka okresowego. Na przykład 1/3 = 0.(3), 1/6 = 0.1(6), 1/7 = 0.(142857)
def fraction_to_recurring_decimal(a, b):
    int_part = a // b
    decimal_part = []
    remainder = a % b
    cycle_start = -1

    while remainder != 0:
        a = remainder * 10
        digit = a // b
        remainder = a % b

        if remainder == 0:
            decimal_part.append(str(digit))
        elif cycle_start == -1:
            cycle_start = a

        if cycle_start != -1 and cycle_start == a:
            decimal_part.insert(0, '(')
            decimal_part.append(')')
            break

        decimal_part.append(str(digit))

    if len(decimal_part) == 0:
        return str(int_part)
    else:
        return f"{int_part}." + ''.join(decimal_part)

# Wczytaj dwie liczby naturalne a i b
a = int(input("Podaj licznik (a): "))
b = int(input("Podaj mianownik (b): "))

recurring_decimal = fraction_to_recurring_decimal(a, b)
print(f"{a}/{b} = {recurring_decimal}")

# Zadanie 20. Dwie liczby naturalne są różno-cyfrowe jeżeli nie posiadają żadnej wspólnej cyfry.
# Proszę napisać program, który wczytuje dwie liczby naturalne i poszukuje najmniejszej podstawy systemu (w zakresie
# 2-16) w którym liczby są różno-cyfrowe. Program powinien wypisać znalezioną podstawę, jeżeli podstawa
# taka nie istnieje należy wypisać komunikat o jej braku. Na przykład: dla liczb 123 i 522 o    dpowiedzią jest
# podstawa 11 bo 123(10) = 102(11) i 522(10) = 435(11).

def different_num(a, b, k):
    t1 = [False for _ in range(k)]
    t2 = [False for _ in range(k)]

    while a > 0:
        t1[a % k] = True
        a //= k

    while b > 0:
        t2[b % k] = True
        b //= k

    for i in range(k):
        if t1[i] == True and t2[i] == True:
            return False
    return True


a = int(input())
b = int(input())

for i in range(2, 16 + 1):
    if different_num(a, b, i) == True:
        print(i)
        break
    elif i == 16:
        print('brak systemu')
