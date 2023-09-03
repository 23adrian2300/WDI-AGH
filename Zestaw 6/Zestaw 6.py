# Zestaw 6: Rekurencja
# Zadanie 1. Proszę napisać funkcję, która jako argument przyjmuje liczbę całkowitą i wypisuje wszystkie
# co najmniej dwucyfrowe liczby pierwsze, powstałe poprzez wykreślenie z liczby pierwotnej co najmniej jednej
# cyfry.
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


def rek(n, result=0, pos=0, b=False):
    if n == 0:
        if result > 9 and b and is_first(result):
            print(result)
        return
    rek(n // 10, result, pos, True)
    rek(n // 10, result + ((n % 10) * 10 ** pos), pos + 1, b)


# Zadanie 2. ”Waga” liczby jest określona jako ilość różnych czynników pierwszych liczby. Na przykład
# waga(1)=0, waga(2)=1, waga(6)=2, waga(30)=3, waga(64)=1. Dana jest tablica T[N] zawierająca liczby
# naturalne. Proszę napisać funkcję, która sprawdza czy można elementy tablicy podzielić na 3 podzbiory o
# równych wagach. Do funkcji należy przekazać wyłącznie tablicę, funkcja powinna zwrócić wartość typu Bool.
import math


def waga(n):
    suma = 0
    k = 2
    while n > 1 and k < n // 2:
        if n % k == 0:
            suma += 1
            while n % k == 0:
                n //= k
        k += 1
    return suma


def podzial(t, n1=0, n2=0, n3=0, i=0):
    if i == len(t):
        return n1 == n2 and n2 == n3
    return (t, n1 + t[i], n2, n3, i + 1) or (t, n1, n2 + t[i], n3, i + 1) or (t, n1, n2, n3 + t[i], i + 1)


def spr(t):
    suma = 0
    odw = [0] * len(t)
    for i in range(len(t)):
        odw[i] = waga(t[i])
        suma += odw[i]
    if suma % 3 == 0:
        if podzial(odw):
            return True
    else:
        return False


# Zadanie 3. Szachownica jest reprezentowana przez tablicę T[8][8] wypełnioną liczbami naturalnymi zawierającymi
# koszt przebywania na danym polu szachownicy. Król szachowy znajduje się w wierszu 0 i kolumnie
# k. Król musi w dokładnie 7 ruchach dotrzeć do wiersza 7. Proszę napisać funkcję, która wyznaczy minimalny
# koszt przejścia króla. Do funkcji należy przekazać tablicę t oraz startową kolumnę k. Koszt przebywania na
# polu startowym i ostatnim także wliczamy do kosztu przejścia.
def koszt_przejscia(t, k, w=0, koszt=0):
    koszt += t[w][k]
    if w == 7:
        return koszt
    min_koszt = koszt_przejscia(t, k, w + 1, koszt)
    if k - 1 >= 0:
        min_koszt = min(min_koszt, koszt_przejscia(t, k - 1, w + 1, koszt))
    if k + 1 < len(t):
        min_koszt = min(min_koszt, koszt_przejscia(t, k + 1, w + 1, koszt))
    return min_koszt


# Zadanie 4. Problem skoczka szachowego. Proszę napisać funkcję, która wypełnia pola szachownicy o
# wymiarach NxN ruchem skoczka szachowego.
moves = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]


def szkoczek(tab, x=0, y=0, i=1):
    if tab[x][y] == 0:
        tab[x][y] = i

    else:
        return False

    if i == len(tab) ** 2:
        return True

    for w, k in moves:
        if (x + w >= 0 and x + w < len(tab)) and (y + k >= 0 and y + k < len(tab)):
            new = szkoczek(tab, x + w, y + k, i + 1)
            if new == True:
                return True
    tab[x][y] = 0
    return False


# Zadanie 5. Dany jest ciąg zer i jedynek zapisany w tablicy T[N]. Proszę napisać funkcję, która odpowiada
# na pytanie czy jest możliwe pocięcie ciągu na kawałki z których każdy reprezentuje liczbę pierwszą. Długość
# każdego z kawałków nie może przekraczać 30. Na przykład dla ciągu 111011 jest to możliwe, a dla ciągu
# 110100 nie jest możliwe.

def tnij(t, od=0):
    n = len(t)
    i = od + 2
    while i <= n and i <= 30:
        liczba = 0
        for a in range(od, i):
            liczba = liczba * 2 + t[a]
        if is_first(liczba):
            if (od != 0 and i == n) or tnij(t, i):
                return True
        i += 1
    return False


# Zadanie 6. Dana jest tablica T[N]. Proszę napisać funkcję, która znajdzie niepusty, najmniejszy (w sensie
# liczebności) podzbiór elementów tablicy, dla którego suma elementów jest równa sumie indeksów tych elementów.
# Do funkcji należy przekazać tablicę, funkcja powinna zwrócić sumę elementów znalezionego podzbioru.
# Na przykład dla tablicy: [ 1,7,3,5,11,2 ] rozwiązaniem jest liczba 10.

def podzbior(t, s_ind=0, s_elem=0, dl=0, i=0):
    if i == len(t):
        if s_ind == s_elem:
            return dl, s_elem

        else:
            return 0, 0

    a = podzbior(t, s_ind + i, s_elem + t[i], dl + 1, i + 1)
    b = podzbior(t, s_ind, s_elem, dl, i + 1)

    if (a[0] > 0 and b[0] > 0 and a[0] < b[0]) or b[0] == 0:
        return a
    return b


t = [3, 2, 1, 5, 5, 2]

# print(rek(t, 0))

# print(podzbior(t))


# Zadanie 7. Dany jest zestaw odważników T[N]. Napisać funkcję, która sprawdza czy jest
# możliwe odważenie określonej masy. Odważniki można umieszczać tylko na jednej szalce.
def odwaga(T, m, i=0):
    if i == len(T) - 1:
        if m == 0:
            return True
        else:
            return False
    return odwaga(T, m - T[i], i + 1) or odwaga(T, m, i + 1)


T = [2, 3, 2, 1, 6]
# print(odwaga(T, 10))


# Zadanie 8. Poprzednie zadanie, ale odważniki można umieszczać na obu szalkach.
def odwagapro(T, m, i):
    if i == len(T) - 1:
        if m == 0:
            return True
        else:
            return False
    return odwagapro(T, m - T[i], i + 1) or odwagapro(T, m, i + 1) or odwagapro(T, m + t[i], i + 1)


# Zadanie 9. Poprzednie zadanie. Program powinien wypisywać wybrane odważniki.
def odwagapro2(li, n, p, t):
    if n == 0:
        print(t)
        return True
    if p == len(li):
        return False

    return odwagapro2(li, n - li[p], p + 1, [*t, li[p]]) or odwagapro2(li, n, p + 1, [*t]) or odwagapro2(li, n + li[p],
                                                                                                         p + 1,
                                                                                                         [*t, -li[p]])


# Zadanie 10. Rekurencyjne obliczanie wyznacznika z macierzy (treść oczywista)
def wyznacznik(T):
    n = len(T)
    if n == 1:
        return T[0][0]
    suma = 0
    for i in range(n):
        suma += T[0][i] * (-1) ** (1 + i + 1) * wyznacznik(minor(T, 0, i))
    return suma


def minor(T, i, j):
    n = len(T)
    M = [[0 for _ in range(n - 1)] for _ in range(n - 1)]
    for a in range(n):
        if a < i:
            for b in range(n):
                if b < j:
                    M[a][b] = T[a][b]
                elif b > j:
                    M[a][b - 1] = T[a][b]
        elif a > i:
            for b in range(n):
                if b < j:
                    M[a - 1][b] = T[a][b]
                elif b > j:
                    M[a - 1][b - 1] = T[a][b]
    return M


# Zadanie 11. Dana jest tablica T[N]. Proszę napisać program zliczający liczbę “enek” o określonym iloczynie.
def count_pairs_with_product(arr, target_product):
    n = len(arr)
    count = 0

    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] * arr[j] == target_product:
                count += 1

    return count

# Przykład użycia
T = [2, 3, 4, 5, 6]
target_product = 12

result = count_pairs_with_product(T, target_product)
# print(f"Liczba par o iloczynie {target_product}: {result}")

# Zadanie 12. Proszę zmodyfikować poprzedni program aby wypisywał znalezione n-ki.
def find_pairs_with_product(arr, target_product):
    n = len(arr)
    pairs = []

    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] * arr[j] == target_product:
                pairs.append((arr[i], arr[j]))

    return pairs

# Przykład użycia
T = [2, 3, 4, 5, 6]
target_product = 12

result_pairs = find_pairs_with_product(T, target_product)
# print(f"Pary o iloczynie {target_product}:")
# for pair in result_pairs:
#     print(pair)
# Zadanie 13. Napisać program wypisujący wszystkie możliwe podziały liczby naturalnej na sumę składników.
# Na przykład dla liczby 4 są to: 1+3, 1+1+2, 1+1+1+1, 2+2.

def rozklad(liczba, result='', i=1):
    if liczba == 0:
        result = result[1:]
        if '+' in result:
            print(result)

    for i in range(i, liczba + 1):
        rozklad(liczba - i, result + '+' + str(i), i)


# Zadanie 14. Problem wież w Hanoi (treść oczywista)

def hanoi(number, a, b, c):
    if number == 0:
        pass
    else:
        hanoi(number - 1, a, c, b)
        print('move from', a, 'to', c)
        hanoi(number - 1, b, a, c)


# print(hanoi(3, "A", 'C', 'B'))


# Zadanie 15. Problem 8 Hetmanów (treść oczywista)
def is_safe(board, row, col):
    # Sprawdza czy hetman może być umieszczony na danej pozycji
    for prev_row, prev_col in board:
        if prev_row == row or prev_col == col or abs(prev_row - row) == abs(prev_col - col):
            return False
    return True

def solve_n_queens(n):
    solutions = []

    def backtrack(board, row):
        if row == n:
            solutions.append(board[:])
            return

        for col in range(n):
            if is_safe(board, row, col):
                board.append((row, col))
                backtrack(board, row + 1)
                board.pop()

    backtrack([], 0)
    return solutions

# Rozwiązania dla problemu 8 hetmanów
solutions = solve_n_queens(8)

# for solution in solutions:
#     print(solution)


# Zadanie 17. Dane są dwie liczby naturalne z których budujemy trzecią liczbę. W budowanej liczbie muszą wystąpić
# wszystkie cyfry występujące w liczbach wejściowych. Wzajemna kolejność cyfr każdej z liczb
# wejściowych musi być zachowana. Na przykład mając liczby 123 i 75 możemy zbudować liczby 12375, 17523,
# 75123, 17253, itd. Proszę napisać funkcję która wyznaczy ile liczb pierwszych można zbudować z dwóch
# zadanych liczb.
primes = 0


def build(a, b, i=0, j=0, new=''):
    a = str(a)
    b = str(b)
    if i == len(a) and j == len(b):
        if is_first(int(new)):
            global primes
            primes += 1
        return
    if i < len(a):
        build(a, b, i + 1, j, new + a[i])
    if j < len(b):
        build(a, b, i, j + 1, new + b[j])


build(13, 1)
# print(primes)


# Zadanie 21. Tablica T[8][8] zawiera liczby naturalne. Proszę napisać funkcję, która sprawdza czy można
# wybrać z tablicy niepusty podzbiór o zadanej sumie. Warunkiem dodatkowym jest aby żadne dwa wybrane
# elementy nie leżały w tej samej kolumnie ani wierszu. Do funkcji należy przekazać wyłącznie tablicę oraz
# wartość sumy, funkcja powinna zwrócić wartość typu bool.

def rekurs(T, suma, pom, i=0, new=0):
    if new == suma:
        return True
    if suma < new or i == len(T):
        return False
    found = False
    for j in range(len(T)):
        if pom[i]:
            continue
        pc = pom[:]
        pc[i] = True
        found = found or rekurs(T, suma, pc, i + 1, new + T[i][j])
    return found


T = [1, 2, 3, 4]
# print(T[1:])
# print(T[0:])
# print(T[:2])
# print(T[1:2])


# Zadanie 25. Tablica t[N] jest wypełniona liczbami naturalnymi. Skok z pola i-tego można wykonać na pola
# o indeksach i+k, gdzie k jest czynnikiem pierwszym liczby t[i] (mniejszym od niej samej). Napisz funkcję,
# która sprawdza, czy da się przejść z pola 0 do N-1 – jeśli się da, zwraca ilość skoków, jeśli się nie da, zwraca
# -1.
def div(num):
    i = 2
    c_num = num
    arr = []
    while num > 1 and i < c_num:
        if num % i == 0:
            arr.append(i)
            while num % i == 0:
                num //= i
        i += 1

    return arr


# Zadanie 26. Do budowy liczby naturalnej reprezentowanej w systemie dwójkowym możemy użyć A cyfr
# 1 oraz B cyfr 0, gdzie A, B > 0. Proszę napisać funkcję, która dla zadanych parametrów A i B zwraca ilość
# wszystkich możliwych do zbudowania liczb, takich że pierwsza cyfra w systemie dwójkowym (najstarszy
# bit) jest równa 1, a zbudowana liczba jest złożona. Na przykład dla A=2, B=3 ilość liczb wynosi 3, są to
# 10010(2), 10100(2), 11000(2)
def czy_zlozona(n):
    if n < 4:
        return False
    if n % 2 == 0:
        return True
    i = 3
    while i ** 2 <= n:
        if n % i == 0:
            return True
        i += 2
    return False


def build(A, B, liczba=0):
    if liczba == 0:
        A -= 1
        liczba = 1
    if A == 0 == B:
        return czy_zlozona(liczba)

    if A > 0 and B > 0:
        return build(A - 1, B, liczba * 2 + 1) + build(A, B - 1, liczba * 2)
    elif A>0:
        return build(A - 1, B, liczba * 2 + 1)
    elif B>0:
        return build(A, B-1, liczba * 2)


# Zadanie 31. Proszę napisać funkcję, która jako parametr otrzymuje liczbę naturalną i zwraca sumę iloczynów
# elementów wszystkich niepustych podzbiorów zbioru podzielników pierwszych tej liczby. Można założyć,
# że liczba podzielników pierwszych nie przekracza 20, zatem w pierwszym etapie funkcja powinna wpisać
# podzielniki do tablicy pomocniczej. Przykład: 60 → [2, 3, 5] → 2 + 3 + 5 + 2 ∗ 3 + 2 ∗ 5 + 3 ∗ 5 + 2 ∗ 3 ∗ 5 = 71
def sumi(a):
    def podz(a):
        t = [0] * 20
        i = 2
        c = 0
        while a > 0:
            if a % i == 0:
                t[c] = i
                c += 1
                while a % i == 0:
                    a //= i
        counter = 0
        for i in range(20):
            if t[i] != 0:
                counter += 1
        sol = [0] * counter
        a = 0
        for i in range(20):
            if t[i] != 0:
                sol[a] = t[i]
                a += 1
        return sol

    t = podz(a)

    def rek(t, il=1, i=0):
        if i == len(t):
            if il == 1:
                return
            nonlocal s
            s += il
            return
        rek(t, il, i + 1)
        rek(t, il * t[i], i + 1)

    s = 0

    rek(podz(a))
    return s
