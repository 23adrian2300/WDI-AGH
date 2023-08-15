# Zestaw 4: Tablice dwuwymiarowe
# Zadanie 1. Dana jest tablica T[N][N]. Proszę napisać funkcję wypełniającą tablicę kolejnymi liczbami
# naturalnymi po spirali.

T = [[0 for _ in range(8)] for _ in range(8)]


def spirala(T):
    n = len(T)
    a = 0
    b = n
    count = 1
    while a <= b:
        for i in range(a, b - 1):
            T[a][i] = count
            count += 1
        for i in range(a, b - 1):
            T[i][b - 1] = count
            count += 1
        for i in range(b - 1, a, -1):
            T[b - 1][i] = count
            count += 1
        for i in range(b - 1, a, -1):
            T[i][a] = count
            count += 1
        a += 1
        b -= 1
    if n % 2 == 1:
        sr = n // 2
        T[sr][sr] = count
    return T


def pt(T):
    for line in T:
        print(line)


# pt(spirala(T))

# Zadanie 2. Dana jest tablica T[N][N] wypełniona liczbami naturalnymi. Proszę napisać funkcję, która
# odpowiada na pytanie, czy w każdym wierszu tablicy występuje co najmniej jedna liczba złożona wyłącznie
# z nieparzystych cyfr.
def allodd(T):
    def oddy(a):
        while a > 0:
            if a % 2 == 0:
                return False
            a //= 10
        return True

    n = len(T)

    for i in range(n):
        flag = False
        for j in range(n):
            if oddy(T[i][j]):
                flag = True
        if not flag:
            return False
    return True


# Zadanie 3. Dana jest tablica T[N][N] wypełniona liczbami naturalnymi. Proszę napisać funkcję, która
# odpowiada na pytanie, czy istnieje wiersz w tablicy w którym każda z liczb zawiera przynajmniej jedna cyfrę
# parzystą.
def ally(T):
    def non(a):
        while a > 0:
            if a % 2 == 0:
                return True
            a //= 10
        return False

    n = len(T)

    for i in range(n):
        flag = True
        for j in range(n):
            if not non(T[i][j]):
                flag = False
        if not flag:
            return False
    return True


# Zadanie 4. Dana jest tablica T[N][N] wypełniona liczbami naturalnymi. Proszę napisać funkcję, która
# zwraca wiersz i kolumnę dowolnego elementu, dla którego iloraz sumy elementów w kolumnie w którym leży
# element do sumy elementów wiersza w którym leży element jest największa + Poprzednie zadanie z tablicą
# wypełnioną liczbami całkowitymi.

t = [[-1, -2, 3]
    , [4, -5, 6],
     [7, 8, 9]]


def bestsum(T):
    n = len(T)
    col = [0] * n
    row = [0] * n
    for i in range(n):
        for j in range(n):
            row[i] += T[i][j]
            col[i] += T[j][i]
    best = 0
    best_row = 0
    best_col = 0
    for i in range(n):
        for j in range(n):
            if row[j] != 0:
                k = col[i] / row[j]
                if k > best:
                    best = k
                    best_row = j
                    best_col = i
    print(row, col)
    return best, best_row, best_col


# print(bestsum(t))


# Zadanie 6. Dane są dwie tablice mogące pomieścić taką samą liczbę elementów: T1[N][N] i T2[M], gdzie
# M=N*N. W każdym wierszu tablicy T1 znajdują się uporządkowane rosnąco (w obrębie wiersza) liczby
# naturalne. Proszę napisać funkcję przepisującą wszystkie singletony (liczby występujące dokładnie raz) z
# tablicy T1 do T2, tak aby liczby w tablicy T2 były uporządkowane rosnąco. Pozostałe elementy tablicy T2
# powinny zawierać zera.

def findmax(l):
    maks = 0
    for i in range(len(l)):
        for j in range(len(l)):
            maks = max(maks, l[i][j])

    return maks


def single(t1):
    n = len(t1)
    maks_el = findmax(t1)
    count_sing = [0 for _ in range(maks_el + 1)]
    t2 = [0 for _ in range(n * n)]
    for i in range(n):
        for j in range(n):
            count_sing[t1[i][j]] += 1
    ind = 0
    for i in range(maks_el + 1):
        if count_sing[i] == 1:
            t2[ind] += i
            ind += 1
    return t2


# Zadanie 7. Dane są dwie tablice mogące pomieścić taką samą liczbę elementów: T1[N][N] i T2[M], gdzie
# M=N*N. W każdym wierszu tablicy T1 znajdują się uporządkowane niemalejąco (w obrębie wiersza) liczby
# naturalne. Proszę napisać funkcję przepisującą wszystkie liczby z tablicy T1 do T2, tak aby liczby w tablicy
# T2 były uporządkowane niemalejąco.

def findmax2(t):
    maks = 0
    for i in range(len(t)):
        for j in range(len(t)):
            if t[i][j] > maks:
                maks = t[i][j]
    return maks


def porzadkowanie(t1):
    index = 0
    n = len(t1)
    maks = findmax2(t1)
    t2 = [0 for _ in range(n * n)]
    current_num = [0 for _ in range(maks + 1)]

    for i in range(n):
        for j in range(n):
            current_num[t1[i][j]] += 1

    for i in range(maks + 1):  # counting sort
        if current_num[i] == 1:
            t2[index] = i
            index += 1
        elif current_num[i] > 1:
            while current_num[i] != 0:
                t2[index] = i
                index += 1
                current_num[i] -= 1

    return t2


# Zadanie 8. Dana jest tablica T[N][N] wypełniona liczbami naturalnymi. Proszę napisać funkcję, która w
# poszukuje w tablicy najdłuższego ciągu geometrycznego leżącego ukośnie w kierunku prawo-dół, liczącego
# co najmniej 3 elementy. Do funkcji należy przekazać tablicę. Funkcja powinna zwrócić informacje czy udało
# się znaleźć taki ciąg oraz długość tego ciągu.

def ciag(t):
    n = len(t)
    q = t[1][1] / t[0][0]

    for i in range(n):
        for j in range(n):
            x = i
            y = j
            l = 1
            while x + 1 < n and y + 1 < n:
                if t[x][y] * q == t[x + 1][y + 1]:
                    l += 1
                else:
                    if l >= 3:
                        return True, l
                    else:
                        l = 1
                        q = t[x + 1][y + 1] / t[x][y]
                        if t[x][y] * q == t[x + 1][y + 1]:
                            l += 1

                x += 1
                y += 1
            if l >= 3:
                return True, l

    return False


# Zadanie 9. Dana jest tablica T[N][N] wypełniona liczbami naturalnymi. Proszę napisać funkcję, która w
# poszukuje w tablicy kwadratu o liczbie pól będącej liczbą nieparzystą większą od 1, którego iloczyn 4 pól
# narożnych wynosi k. Do funkcji należy przekazać tablicę i wartość k. Funkcja powinna zwrócić informacje
# czy udało się znaleźć kwadrat oraz współrzędne (wiersz, kolumna) środka kwadratu.

def square(t, k):
    n = len(t)
    for i in range(n):
        for j in range(n):
            x = 2
            y = 2
            while i + x < n and j + y < n:
                if ((x + 1) * (y + 1)) % 2 == 1:
                    print(i + x, y + j)
                    if (t[i][j] * t[i + x][j] * t[i][j + y] * t[x + i][y + j]) == k:
                        return x // 2 + i, y // 2 + j

                x += 2
                y += 2

    return False


tab = [
    [1, 2, 4, 2, 1, 3],
    [3, 2, 56, 7, 7, 4],
    [1, 2, 7, 2, 1, 3],
    [2, 3, 5, 1, 3, 0],
    [3, 2, 56, 7, 7, 4],
    [4, 6, 2, 3, 45, 6]
]

# Zadanie 10. Napisać funkcję która dla tablicy T[N][N], wypełnionej liczbami całkowitymi, zwraca wartość
# True w przypadku, gdy w każdym wierszu i każdej kolumnie występuje co najmniej jedno 0 oraz wartość
# False w przeciwnym przypadku.
T = [[2, 1, 1],
     [2, 0, 3],
     [0, 9, 0]]


def zerointab(T):
    n = len(T)
    row = [False] * n
    col = [False] * n
    for i in range(n):
        for j in range(n):
            if T[j][i] == 0:
                col[j] = True
            if T[i][j] == 0:
                row[i] = True
    for i in range(n):
        if not row[i] or not col[i]:
            return False
    return True


# print(zerointab(T))

# Zadanie 11. Dwie liczby naturalne są „przyjaciółkami jeżeli zbiory cyfr z których zbudowane są liczby
# są identyczne. Na przykład: 123 i 321, 211 i 122, 35 3553. Dana jest tablica T[N][N] wypełniona liczbami
# naturalnymi. Proszę napisać funkcję, która dla tablicy T zwraca ile elementów tablicy sąsiaduje wyłącznie z
# przyjaciółkami
from math import log


def friends(a, b):
    if a == b == -1:
        return True
    t_a = [False for _ in range(10)]
    t_b = [False for _ in range(10)]

    while a > 0:
        t_a[a % 10] = True
        a //= 10

    while b > 0:
        t_b[b % 10] = True
        b //= 10

    for i in range(10):
        if t_a[i] != t_b[i]:
            return False
    return False


def extend_tab(t):
    n = len(t)
    result = [[-1 for _ in range(n + 2)] for _ in range(n + 2)]
    for i in range(n):
        for j in range(n):
            result[i + 1][j + 1] = t[i][j]
    return result


def neig(t):
    n = len(t)
    counter = 0
    tab = extend_tab(t)
    for i in range(1, n + 2 - 1):
        for j in range(1, n + 2 - 1):
            if friends(tab[i][j], tab[i + 1][j]) and friends(tab[i][j], tab[i - 1][j]) and friends(tab[i][j], tab[i][
                j + 1]) and friends(tab[i][j], tab[i][j - 1]):
                counter += 1

    return counter


# Zadanie 12. Dana jest tablica T[N][N][N]. Proszę napisać funkcję, do której przekazujemy tablicę wypełnioną liczbami
# większymi od zera. Funkcja powinna zwracać wartość True, jeżeli na wszystkich poziomach 1
# tablicy liczba elementów sąsiadujących (w obrębia poziomu) z co najmniej 6 liczbami złożonymi
# jest jednakowa albo wartość False w przeciwnym przypadku.

def extend_tab3d(t):
    n = len(t)
    result = [[[-1 for _ in range(n + 2)] for _ in range(n + 2)] for _ in range(n + 1)]
    for i in range(n):
        for j in range(n):
            for z in range(n):
                result[i + 1][j + 1][z + 1] = t[i][j][z]

    return result


def is_not_prime(n):
    if n == -1:
        return False
    if n == 2 or n == 1:
        return False
    elif n % 2 == 0:
        return True
    k = 3
    while k * k <= n:
        if n % k == 0:
            return True

    return False


def poziom(t):
    n = len(t)
    counter = 0
    temp_tab = extend_tab3d(t)

    for i in range(1, n + 1):
        for j in range(n + 1):
            print(temp_tab[2][i][j])
            if is_not_prime(temp_tab[2][i + 1][j]):
                counter += 1
            if is_not_prime(temp_tab[2][i + 1][j + 1]):
                counter += 1
            if is_not_prime(temp_tab[2][i + 1][j - 1]):
                counter += 1
            if is_not_prime(temp_tab[2][i - 1][j]):
                counter += 1
            if is_not_prime(temp_tab[2][i - 1][j - 1]):
                counter += 1
            if is_not_prime(temp_tab[2][i - 1][j + 1]):
                counter += 1
            if is_not_prime(temp_tab[2][i][j + 1]):
                counter += 1
            if is_not_prime(temp_tab[2][i][j - 1]):
                counter += 1

    if counter < 6:
        return False
    return counter


# Zadanie 13. Liczby naturalne a,b są komplementarne jeżeli ich suma jest liczbą pierwszą. Dana jest tablica
# T[N][N] wypełniona liczbami naturalnymi. Proszę napisać funkcję, która zeruje elementy nie posiadające
# liczby komplementarnej.
def extend_tab2d(t):
    n = len(t)
    result = [[-1 for _ in range(n + 2)] for _ in range(n + 2)]
    for i in range(0, n):
        for j in range(0, n):
            result[i + 1][j + 1] = t[i][j]

    return result


def is_prime(n):
    if n == 2:
        return True
    if n <= 1 or n % 2 == 0:
        return False
    k = 3
    while k * k <= n:
        if n % k == 0:
            return False
        k += 2
    return True


moves = [(0, 1), (0, -1), (-1, 0), (1, 0)]


def komplementarne(t):
    t1 = extend_tab2d(t)
    n = len(t)
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            for x, y in moves:
                if t1[i + x][j + y] == -1:
                    continue
                elif is_prime(t1[i][j] + t1[i + x][j + y]) == False:
                    t[i - 1][j - 1] = 0

    return t


# Zadanie 14. Dwie liczby naturalne są zgodne jeżeli w zapisie dwójkowym zawierają tę samą liczbę jedynek,
# np. 22 = 101102 i 14 = 11102. Dane są tablice T1[N1][N1] T2[N2][N2], gdzie N2¿N1. Proszę napisać funkcję,
# która sprawdza czy istnieje takie położenie tablicy T1 wewnątrz tablicy T2, przy którym liczba zgodnych
# elementów jest większa od 33%. Do funkcji należy przekazać tablicę T1 i T2. Obie oryginalne tablice powinny
# pozostać nie zmieniane.

def count_binary_ones(num):
    ones = 0
    while num > 0:
        ones += num % 2
        num //= 2

    return ones


def create_binary_ones_array(tab, n):
    bin_tab = [[0] * n for _ in range(n)]
    for y in range(n):
        for x in range(n):
            bin_tab[y][x] = count_binary_ones(tab[y][x])

    return bin_tab


def compare_arrays(arr1, arr2, x2, y2):
    if y2 + len(arr1) < len(arr2):
        return 0

    same_cells = 0
    for y in range(len(arr1)):
        if x2 + len(arr1[y]) < len(arr2[y]):
            return 0
        for x in range(len(arr1[y])):
            if arr1[y][x] == arr2[y + y2][x + x2]:
                same_cells += 1
    return same_cells


def find_t1_pos_inside_t2(t1, t2):
    n1 = len(t1)
    n2 = len(t2)
    bin_t1 = create_binary_ones_array(t1, n1)
    bin_t2 = create_binary_ones_array(t2, n2)
    for x in range(n2 - n1 + 1):
        for y in range(n2 - n1 + 1):
            if 100 * compare_arrays(bin_t1, bin_t2, x, y) > 33 * (n1 ** 2):
                return True, x, y

    return False


# Zadanie 15. Dana jest tablica T[N][N], wypełniona liczbami naturalnymi. Proszę napisać funkcję, która
# odpowiada na pytanie, czy w tablicy istnieje wiersz, w którym każda liczba zawiera co najmniej jedną cyfrę
# będącą liczbą pierwszą?


def firstinrow(T):
    def firstdigit(a):
        first = [2, 3, 5, 7]
        while a > 0:
            if a % 10 in first:
                return True
            a //= 10
        return False

    n = len(T)
    for i in range(n):
        flag = True
        for j in range(n):
            if not firstdigit(T[i][j]):
                flag = False
        if flag:
            return True
    return False



# Zadanie 16. Dana jest tablica T[N][N], wypełniona liczbami naturalnymi. Proszę napisać funkcję która
# odpowiada na pytanie, czy w tablicy każdy wiersz zawiera co najmniej jedną liczbą złożoną wyłącznie z cyfr
# będących liczbami pierwszymi?


def allrowswithfn(T):
    def firstnumbers(a):
        first = [2, 3, 5, 7]
        while a > 0:
            if a % 10 not in first:
                return False
            a //= 10
        return True

    n = len(T)
    for i in range(n):
        flag = False
        for j in range(n):
            if firstnumbers(T[i][j]):
                flag = True
        if not flag:
            return False
    return True


# Zadanie 17. Dana jest tablica T[N][N] wypełniona liczbami naturalnymi. Proszę napisać funkcję która
# zwraca wiersz i kolumnę dowolnego elementu, dla którego suma otaczających go elementów jest największa.


def ex_t(T):
    n = len(T)
    ex = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            ex[i][j] = T[i - 1][j - 1]
    return ex


def max_sum(arr):
    best_sum = float("-inf")
    best_arr = []

    for leng in range(min(11, len(arr)) - 1, 0, -1):
        start = 0
        end = leng - 1
        curr_sum = sum(arr[:leng])
        if best_sum < curr_sum:
            best_sum = curr_sum
            start = 0
            end = leng - 1
            best_arr = arr[start:end + 1]
        print(leng, len(arr))
        print(arr)

        for i in range(leng, len(arr)):
            curr_sum += arr[i]
            curr_sum -= arr[i - leng]
            if best_sum < curr_sum:
                best_sum = curr_sum
                start = i - leng + 1
                end = i
                best_arr = arr[start:end + 1]

        arr = arr[start:end + 1]

    return best_sum, best_arr


# print(max_sum([3, 6, 2, -4, 67, 34, -100, 46, -345, 7, 4, 23, -43, 6, 2]))


def calc(tab):
    best_sum = float("-inf")

    for line in tab:
        best_sum = max(best_sum, max_sum(line))

    for x in range(len(tab)):
        column = [tab[i][x] for i in range(len(tab))]
        best_sum = max(best_sum, max_sum(column))

    return best_sum


# Zadanie 18. Dana jest tablica T[N][N] wypełniona liczbami całkowitymi. Proszę napisać funkcję, która
# wyszuka spójny podciąg elementów leżący poziomo lub pionowo o największej sumie. Maksymalna długość
# podciągu może wynosić 10 elementów. Do funkcji należy przekazać tablicę T, funkcja powinna zwrócić sumę
# maksymalnego podciągu.
def podciag(t):
    n = len(t)
    s_max = 0
    for i in range(n):
        for j in range(n):
            suma_w = suma_k = t[i][j]
            for k in range(1, 10):
                s_max = max(suma_w, suma_k, s_max)
                if k + i >= n and k + j >= n:
                    break
                elif k + j >= n:
                    suma_k += t[i + k][j]
                elif k + i >= n:
                    suma_w += t[i][j + k]
                else:
                    suma_w += t[i][j + k]
                    suma_k += t[i + k][j]

    return s_max


# Zadanie 19. Dana jest tablica T[N][N] wypełniona liczbami naturalnymi. Proszę napisać funkcję, która
# zwraca liczbę par elementów, o określonym iloczynie, takich że elementy są odległe o jeden ruch skoczka
# szachowego.
def pary_iloczyn(t, il):
    n = len(t)
    ruchy = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]
    counter = 0
    for i in range(n):
        for j in range(n):
            for w, k in ruchy:
                if i + w < n and i + w >= 0 and j + k >= 0 and j + k < n:
                    if t[i][j] * t[i + w][j + k] == il:
                        counter += 1

    return counter // 2


# Zadanie 20. Dana jest tablica T[N][N] (reprezentująca szachownicę) wypełniona liczbami naturalnymi.
# Proszę napisać funkcję która ustawia na szachownicy dwie wieże, tak aby suma liczb na „szachowanych”
# przez wieże polach była największa. Do funkcji należy przekazać tablicę, funkcja powinna zwrócić położenie
# wież. Uwaga- zakładamy, że wieża szachuje cały wiersz i kolumnę z wyłączeniem pola na którym stoi
def wieze(t):
    n = len(t)
    suma_k = [0 for _ in range(n)]
    suma_w = [0 for _ in range(n)]

    for w in range(n):
        for k in range(n):
            suma_k[k] += t[w][k]
            suma_w[w] += t[w][k]

    maks = 0
    max_i, max_j = 0, 0
    for i in range(n):
        for j in range(n):
            sum_w1 = suma_w[i] + suma_k[j] - 2 * t[i][j]
            if (sum_w1) > maks:
                maks = sum_w1
                max_i, max_j = i, j

    return maks, max_i, max_j


def convert_array_2D_to_1D(array_2D, rows, columns):
    array_1D = [0 for i in range(rows * columns)]
    for row in range(rows):
        for column in range(columns):
            array_1D[row * columns + column] = array_2D[row][column]

    return array_1D
