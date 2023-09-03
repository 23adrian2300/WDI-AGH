# Zadanie 1. Liczby wymierne są reprezentowane przez krotkę (l,m). Gdzie: l - liczba całkowita oznaczająca
# licznik, m - liczba naturalna oznaczająca mianownik. Proszę napisać podstawowe operacje na ułamkach,
# m.in. dodawanie, odejmowanie, mnożenie, dzielenie, potęgowanie, skracanie, wypisywanie i wczytywanie.
import math

def gcd(a, b):
    # Największy wspólny dzielnik (GCD) dwóch liczb
    while b:
        a, b = b, a % b
    return a

def reduce_fraction(l, m):
    # Skracanie ułamka do postaci nieskracalnej
    common_divisor = gcd(l, m)
    return l // common_divisor, m // common_divisor

def add_fractions(frac1, frac2):
    l1, m1 = frac1
    l2, m2 = frac2
    common_denominator = m1 * m2
    new_numerator = l1 * m2 + l2 * m1
    return reduce_fraction(new_numerator, common_denominator)

def subtract_fractions(frac1, frac2):
    l1, m1 = frac1
    l2, m2 = frac2
    common_denominator = m1 * m2
    new_numerator = l1 * m2 - l2 * m1
    return reduce_fraction(new_numerator, common_denominator)

def multiply_fractions(frac1, frac2):
    l1, m1 = frac1
    l2, m2 = frac2
    new_numerator = l1 * l2
    new_denominator = m1 * m2
    return reduce_fraction(new_numerator, new_denominator)

def divide_fractions(frac1, frac2):
    l1, m1 = frac1
    l2, m2 = frac2
    new_numerator = l1 * m2
    new_denominator = m1 * l2
    return reduce_fraction(new_numerator, new_denominator)

def power_fraction(frac, exponent):
    l, m = frac
    new_numerator = l ** exponent
    new_denominator = m ** exponent
    return reduce_fraction(new_numerator, new_denominator)

def print_fraction(frac):
    l, m = frac
    print(f"{l}/{m}")

def input_fraction():
    l = int(input("Podaj licznik: "))
    m = int(input("Podaj mianownik: "))
    return l, m

# frac1 = (3, 4)
# frac2 = (2, 5)
#
# sum_result = add_fractions(frac1, frac2)
# print_fraction(sum_result)
#
# difference_result = subtract_fractions(frac1, frac2)
# print_fraction(difference_result)
#
# product_result = multiply_fractions(frac1, frac2)
# print_fraction(product_result)
#
# quotient_result = divide_fractions(frac1, frac2)
# print_fraction(quotient_result)
#
# power_result = power_fraction(frac1, 2)
# print_fraction(power_result)

# Zadanie 2. Używając funkcji z poprzedniego zadania proszę napisać funkcję rozwiązującą układ 2 równań
# o 2 niewiadomych.
def solve_2x2_system(eq1, eq2):
    # eq1 i eq2 to równania w postaci krotek (l, m) reprezentujących lewą stronę równania jako ułamek

    a1, b1 = eq1
    a2, b2 = eq2

    determinant = a1 * b2 - a2 * b1

    if determinant == 0:
        return None

    l1 = b2 * a1
    l2 = b1 * a2

    m1 = m2 = b1 * b2

    x = reduce_fraction(l1 - l2, m1)
    y = reduce_fraction(a1 * b2 - a2 * b1, m2)

    return x, y

eq1 = (3, 4), (2, 3)
eq2 = (5, 6), (4, 5)

solution = solve_2x2_system(eq1, eq2)

if solution:
    print("Rozwiązanie układu:")
    print(f"x = {solution[0][0]}/{solution[0][1]}")
    print(f"y = {solution[1][0]}/{solution[1][1]}")
else:
    print("Układ równań jest sprzeczny lub nieoznaczony.")

# Zadanie 3. Na szachownicy o wymiarach 100 na 100 umieszczamy N hetmanów (N < 100). Położenie
# hetmanów jest opisywane przez tablicę dane = [(w1, k1),(w2, k2),(w3, k3), ...(wN , kN )]
# Proszę napisać funkcję, która odpowiada na pytanie: czy żadne z dwa hetmany się nie szachują? Do funkcji należy przekazać
# położenie hetmanów.

# Zadanie 4. Dana jest tablica zawierająca liczby wymierne. Proszę napisać funkcję, która policzy występujące w tablicy ciągi arytmetyczne (LA) i geometryczne (LG) o długości większej niż 2. Funkcja powinna
# zwrócić wartość 1 gdy LA > LG, wartość -1 gdy LA < LG oraz 0 gdy LA = LG.

# Zadanie 5. Dany jest zbiór punktów leżących na płaszczyźnie opisany przy pomocy struktury dane =
# [(x1, y1),(x2, y2),(x3, y3), ...(xN , yN )] Proszę napisać funkcję, która zwraca wartość True
# jeżeli zbiorze istnieją 4 punkty wyznaczające kwadrat o bokach równoległych do osi układu współrzędnych, a wewnątrz
# tego kwadratu nie ma żadnych innych punktów. Do funkcji należy przekazać strukturę opisującą położenie
# punktów.

# Zadanie 6. Liczby zespolone są reprezentowane przez krotkę (re, im). Gdzie: re - część rzeczywista liczby,
# im - część urojona liczby. Proszę napisać podstawowe operacje na liczbach zespolonych, m.in. dodawanie,
# odejmowanie, mnożenie, dzielenie, potęgowanie, wypisywanie i wczytywanie.

# Zadanie 7. Używając funkcji z poprzedniego zadania proszę napisać funkcję rozwiązującą równanie kwadratowe
# o współczynnikach zespolonych.

# Zadanie 8. Napis nazywamy wielokrotnym, jeżeli powstał przez n-krotne (n > 1) powtórzenie innego napisu
# o długości co najmniej 1. Przykłady napisów wielokrotnych: ABCABCABC, AAAA, ABAABA. Dana
# jest tablica T[N] zawierająca napisy. Proszę napisać funkcję multi(T), która zwraca długość najdłuższego
# napisu wielokrotnego występującego w tablicy T lub wartość 0, jeżeli takiego napisu nie ma w tablicy.


# Zadanie 9. Dana jest tablica T[N][N] wypełniona wartościami 0, 1. Każdy wiersz tablicy traktujemy jako
# liczbę zapisaną w systemie dwójkowym o długości N bitów. Stała N jest rzędu 1000.
# Proszę zaimplementować funkcję distance(T), która dla takiej tablicy wyznaczy dwa wiersze, dla których różnica zawartych
# w wierszach liczb jest największa. Do funkcji należy przekazać tablicę, funkcja powinna zwrócić odległość
# pomiędzy znalezionymi wierszami. Można założyć, że żadne dwa wiersze nie zawierają identycznego ciągu
# cyfr.

# Zadanie 10. Proszę napisać funkcję która zamienia liczby wymierne reprezentowane jako
# rozwinięcia dziesiętne w postaci napisów na liczbę w postaci pary licznik mianownik. Na przykład: ”0.25” na (1,4), ”0.1(6)”
# na (2,3), ”0.(142857)” na (1,7)
