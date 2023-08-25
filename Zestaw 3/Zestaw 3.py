# Zadanie 1. Napisać funkcję zamieniającą i wypisującą liczbę naturalną na system o podstawie 2-16.

def to_system(num, base, chars):
    base_num = []
    while num > 0:
        base_num.append(chars[num % base])
        num //= base
    return "".join(base_num[::-1])


# n = int(input())
chars = [str(i) for i in range(10)] + [chr(i) for i in range(ord("A"), ord("F") + 1)]


# for i in range(2, 16 + 1):
#     print("base", i, ":", to_system(n, i, chars))

# Zadanie 2. Napisać program wczytujący dwie liczby naturalne i odpowiadający na pytanie czy są one
# zbudowane z takich samych cyfr, np. 123 i 321, 1255 i 5125, 11000 i 10001.

def thesame(a, b):
    num = [0] * 10
    while a != 0:
        num[a % 10] += 1
        a //= 10
    while b != 0:
        num[b % 10] -= 1
        b //= 10
    for i in range(10):
        if num[i] != 0:
            return False
    return True


# Zadanie 3. Napisać program generujący i wypisujący liczby pierwsze mniejsze od N metodą Sita Eratostenesa.

def sieve(n):
    sieve = [i for i in range(n)]
    sieve[0] = False
    sieve[1] = False

    for i in range(2, n):
        if sieve[i] > 0:
            for j in range(2 * sieve[i], n, sieve[i]):
                sieve[j] = 0

    for el in sieve:
        if el > 0:
            print(el, end=" ")


# Zadanie 4. Napisać program obliczający i wypisujący stałą e z rozwinięcia w szereg e = 1/0! + 1/1! +
# 1/2! + 1/3! + ... z dokładnością N cyfr dziesiętnych (N jest rzędu 1000).

def factorial(n):
    silnia = 1
    for x in range(1, n + 1):
        silnia *= x
    return silnia


"""
# def count(x):
#     mianownik = factorial(x)
#     for m in range(0, o + 2):
#         d = x // mianownik
#         T[m] += d
#         r = x % mianownik
#         r = r * 10
#         x = r


# o = int(input(""))
# T = [0 for i in range(0, o + 2)]
# for x in range(1, 10):
#     count(x)
# 
# for x in range(o + 1, 0, -1):
#     if T[x] // 10 > 0:
#         T[x - 1] += T[x] // 10
#         T[x] = T[x] % 10


# print(T[0], ",", end="", sep="")
# for x in range(1,z+2):
#     print(T[x], end="", sep="")
"""


# Zadanie 5. Napisać program, który wczytuje wprowadzany z klawiatury ciąg liczb naturalnych zakończonych zerem stanowiącym wyłącznie znacznik końca danych. Program powinien wypisać 10 co do wielkości
# wartość, jaka wystąpiła w ciągu. Można założyć, że w ciągu znajduje się wystarczająca liczba elementów.

def find_10th_largest_value():
    numbers = []

    while True:
        try:
            num = int(input("Enter a natural number (0 to finish): "))
            if num == 0:
                break
            numbers.append(num)
        except ValueError:
            print("Invalid number format. Please try again.")

    numbers.sort(reverse=True)

    if len(numbers) >= 10:
        tenth_largest = numbers[9]
        print(f"10th largest value: {tenth_largest}")
    else:
        print("Not enough data to find the 10th largest value.")


# Zadanie 6. Napisać program wypełniający N-elementową tablicę t liczbami naturalnymi 1-1000 i sprawdzający czy każdy element tablicy zawiera co najmniej jedną cyfrę nieparzystą.
from random import randint


def odd(n):
    t = [randint(1, 1001) for _ in range(n)]
    print(t)
    for i in range(n):
        while t[i] % 2 != 1:
            t[i] //= 10
            if t[i] == 0:
                return False
    return True


# Zadanie 7. Napisać program wypełniający N-elementową tablicę t liczbami naturalnymi 1-1000 i sprawdzający czy istnieje element tablicy zawierający wyłącznie cyfry nieparzyste.
def odds(n):
    t = [randint(1, 1001) for _ in range(n)]
    print(t)
    for i in range(n):
        while t[i] != 0:
            if t[i] % 2 == 0:
                return False
            t[i] //= 10
    return True


# print(odds(1))
# Zadanie 8. Dana jest N-elementowa tablica t zawierająca liczby naturalne. W tablicy możemy przeskoczyć
# z pola o indeksie k o n pól w prawo jeżeli wartość n jest czynnikiem pierwszym liczby t[k]. Napisać funkcję
# sprawdzającą czy jest możliwe przejście z pierwszego pola tablicy na ostatnie pole.

def skoczek(T):
    n = len(T)
    moves = [False] * n
    moves[0] = True
    for i in range(n):
        if moves[i]:
            d = 2
            while T[i] > 1:
                if T[i] % d == 0:
                    if i + d < n:
                        moves[i + d] = True
                    while T[i] % d == 0:
                        T[i] //= d
                d += 1
    return moves


# Zadanie 9. Napisać funkcję, która dla N-elementowej tablicy t wypełnionej liczbami naturalnym wyznacza
# długość najdłuższego, spójnego podciągu rosnącego.

def incsub(T):
    n = len(T)
    best = 0
    curr = 1
    for i in range(2, n):
        if T[i - 1] < T[i]:
            curr += 1
        else:
            best = max(best, curr)
            curr = 1
    return max(curr, best)


# Zadanie 10. Napisać funkcję, która dla N-elementowej tablicy t wypełnionej liczbami naturalnym wyznacza długość najdłuższego,
# spójnego podciągu arytmetycznego.

def leng_of_longest_arythmetic_subsequence(T):
    if len(T) <= 2:
        return len(T)
    n = len(T)
    r = T[1] - T[0]
    max_leng = 1
    leng = 2
    for i in range(2, n):
        if T[i] == T[i - 1] + r:
            leng += 1
        else:
            max_leng = max(max_leng, leng)
            leng = 2
            r = T[i] - T[i - 1]

    return max(max_leng, leng)


# Zadanie 11. Napisać funkcję, która dla N-elementowej tablicy t wypełnionej liczbami naturalnym wyznacza
# długość najdłuższego, spójnego podciągu geometrycznego.

def leng_of_longest_geometric_subsequence(sequence):
    if len(sequence) <= 2:
        return len(sequence)

    q = sequence[1] / sequence[0]
    max_leng = 1
    leng = 2
    for i in range(2, len(sequence)):
        if sequence[i] == sequence[i - 1] * q:
            leng += 1
        else:
            max_leng = max(max_leng, leng)
            leng = 2
            q = sequence[i] / sequence[i - 1]

    return max(max_leng, leng)


# Zadanie 12. Proszę napisać program, który wypełnia N-elementową tablicę t pseudolosowymi liczbami
# nieparzystymi z zakresu [1..99], a następnie wyznacza i wypisuje różnicę pomiędzy długością najdłuższego
# znajdującego się w niej ciągu arytmetycznego o dodatniej różnicy, a długością najdłuższego ciągu arytmetycznego
# o ujemnej różnicy, przy założeniu, że kolejnymi wyrazami ciągu są elementy tablicy o kolejnych
# indeksach.
def leng_of_longestarythmetic_subsequence(sequence):
    if len(sequence) <= 2:
        return len(sequence)

    r = sequence[1] - sequence[0]
    max_leng_incr = 1
    max_leng_decr = 1
    leng = 2
    for i in range(2, len(sequence)):
        if sequence[i] == sequence[i - 1] + r:
            leng += 1
        else:
            if r > 0:
                max_leng_incr = max(max_leng_incr, leng)
            else:
                max_leng_decr = max(max_leng_decr, leng)
            leng = 2
            r = sequence[i] - sequence[i - 1]

        if r > 0:
            max_leng_incr = max(max_leng_incr, leng)
        else:
            max_leng_decr = max(max_leng_decr, leng)

    return max_leng_incr, max_leng_decr


# Zadanie 13. Proszę napisać program, który wypełnia N-elementową tablicę t trzycyfrowymi liczbami
# pseudolosowymi, a następnie wyznacza i wypisuje długość najdłuższego podciągu spójnego znajdującego
# się w tablicy dla którego w tablicy występuje również rewers tego ciągu. Na przykład dla tablicy: t=
# [2,9,3,1,7,11,9,6,7,7,1,3,9,12,15] odpowiedzią jest liczba 4.
import random


def find_longest_reverse_subsequence_length(N):
    def generate_random_array(n):
        return [random.randint(100, 999) for _ in range(n)]

    def longest_reverse_subsequence_length(arr):
        longest_length = 0

        for i in range(len(arr)):
            for j in range(i + 1, len(arr) + 1):
                subseq = arr[i:j]
                if subseq == subseq[::-1] and len(subseq) > longest_length:
                    longest_length = len(subseq)

        return longest_length

    t = generate_random_array(N)
    print("Generated array:", t)

    longest_length = longest_reverse_subsequence_length(t)
    return longest_length


# N = int(input("Enter the size of the array: "))
# result = find_longest_reverse_subsequence_length(N)
# print("Length of the longest reverse subsequence:", result)

# Zadanie 14. Napisać program wyznaczający na drodze eksperymentu prawdopodobieństwo tego, że w
# grupie N przypadkowo spotkanych osób, co najmniej dwie urodziły się tego samego dnia roku. Wyznaczyć
# wartości prawdopodobieństwa dla N z zakresu 20-40.
import random


def has_shared_birthday(people):
    birthdays = set()
    for _ in range(people):
        birthday = random.randint(1, 365)
        if birthday in birthdays:
            return True
        birthdays.add(birthday)
    return False


def calculate_birthday_probability(N, trials):
    shared_birthday_count = 0
    for _ in range(trials):
        if has_shared_birthday(N):
            shared_birthday_count += 1
    probability = shared_birthday_count / trials
    return probability


min_N = 20
max_N = 40
trials = 100000


# print("N\tProbability")
# print("-" * 20)
#
# for N in range(min_N, max_N + 1):
#     probability = calculate_birthday_probability(N, trials)
#     print(f"{N}\t{probability:.4f}")

# Zadanie 15. Dana jest duża tablica t. Proszę napisać funkcję, która zwraca informację czy w tablicy
# zachodzi następujący warunek: „wszystkie elementy, których indeks jest elementem ciągu Fibonacciego są
# liczbami złożonymi, a wśród pozostałych przynajmniej jedna jest liczbą pierwszą”

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def is_composite(n):
    return n > 1 and not is_prime(n)


def fibonacci_numbers_up_to_n(n):
    fib = [0, 1]
    while fib[-1] <= n:
        fib.append(fib[-1] + fib[-2])
    fib.pop()
    return fib


def check_condition(t):
    max_index = len(t) - 1
    fib_numbers = fibonacci_numbers_up_to_n(max_index)

    has_prime = False
    for i, num in enumerate(t):
        if i in fib_numbers:
            if not is_composite(num):
                return False
        else:
            if is_prime(num):
                has_prime = True

    return has_prime


# Przykładowe użycie
tablica = [4, 9, 6, 8, 3, 5, 10, 15]
print(check_condition(tablica))


# Zadanie 16. Mamy zdefiniowaną n-elementową tablicę liczb całkowitych. Proszę napisać funkcję zwracającą
# wartość typu bool oznaczającą, czy w tablicy istnieje dokładnie jeden element najmniejszy i dokładnie
# jeden element największy (liczba elementów najmniejszych oznacza liczbę takich elementów o tej samej
# wartości).

def has_one_smallest_and_one_largest(t):
    min_count = 0
    max_count = 0
    min = t[0]
    max = t[0]
    for num in t:
        if num < min:
            min = num
            min_count = 1
        elif num == min:
            min_count += 1
        if num > max:
            max = num
            max_count = 1
        elif num == max:
            max_count += 1

    return min_count == 1 and max_count == 1


# Zadanie 17. Dane są dwie N-elementowe tablice t1 i t2 zawierające liczby naturalne. Z wartości w obu
# tablicach możemy tworzyć sumy. „Poprawna” suma to taka, która zawiera co najmniej jeden element (z
# tablicy t1 lub t2) o każdym indeksie. Na przykład dla tablic: t1 = [1,3,2,4] i t2 = [9,7,4,8] poprawnymi
# sumami są na przykład 1+3+2+4, 9+7+4+8, 1+7+3+8, 1+9+7+2+4+8. Proszę napisać funkcje generującą
# i wypisująca wszystkie poprawne sumy, które są liczbami pierwszymi. Do funkcji należy przekazać dwie
# tablice, funkcja powinna zwrócić liczbę znalezionych i wypisanych sum.


def is_prime2(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def solution(t1, t2):
    def rek(t1, t2, i, sum):
        if i == len(t1):
            if is_prime2(sum):
                print(sum)
            return
        rek(t1, t2, i + 1, sum + t1[i]) or rek(t1, t2, i + 1, sum + t2[i]) or rek(t1, t2, i + 1, sum + t1[i] + t2[i])

    rek(t1, t2, 0, 0)


# solution([1,2],[3,4])

# Zadanie 18. Dana jest N-elementowa tablica t jest wypełniona liczbami naturalnymi. Proszę napisać
# funkcję, która zwraca długość najdłuższego spójnego podciągu będącego palindromem złożonym wyłącznie
# z liczb nieparzystych. Do funkcji należy przekazać tablicę, funkcja powinna zwrócić długość znalezionego
# podciągu lub wartość 0 jeżeli taki podciąg nie istnieje.

def lops(t):
    n = len(t)
    for i in range(n):
        k = len(str(t[i]))
        for j in range(k):
            num = str(t[i])[j]
            if int(num) % 2 == 0:
                t[i] = False
                break
    maxi = 0
    for i in range(n):
        if t[i] != False:
            t[i] = str(t[i])
    for i in range(n):
        if t[i] != False:
            st = t[i]
            for j in range(i + 1, n):
                if t[j] == False:
                    break
                st += t[j]
                if st == st[::-1]:
                    lll = j - i + 1
                    print(st)
                    if lll > maxi:
                        maxi = lll
    return maxi


# print(lops([303, 333, 131, 2, 331, 333, 2,133,3,3,4,3,22,5]))


# Zadanie 19. Dana jest N-elementowa tablica t wypełniona liczbami naturalnymi. Proszę napisać funkcję,
# która zwraca długość najdłuższego, spójnego podciągu rosnącego dla którego suma jego elementów jest
# równa sumie indeksów tych elementów. Do funkcji należy przekazać tablicę, funkcja powinna zwrócić długość
# znalezionego podciągu lub wartość 0 jeżeli taki podciąg nie istnieje.
def longest_increasing_subsequence_with_equal_sum(t):
    n = len(t)
    max_length = 0

    for start in range(n):
        current_sum = t[start]
        current_length = 1

        for end in range(start + 1, n):
            if t[end] > t[end - 1]:
                current_length += 1
                current_sum += t[end]

                if current_length == current_sum:
                    max_length = max(max_length, current_length)
            else:
                break

    return max_length


# Zadanie 20. Dana jest N-elementowa tablica t zawierająca liczby naturalne mniejsze od 1000.
# Proszę napisać funkcję, która zwraca długość najdłuższego, spójnego fragmentu tablicy,
# dla którego w iloczynie jego elementów każdy czynniki pierwszy występuje co najwyżej raz.
# Na przykład dla tablicy t=[2,23,33,35,7,4,6,7,5,11,13,22] wynikiem jest wartość 5.
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def max_unique_prime_factors_subarray(t):
    n = len(t)
    max_length = 0
    for start in range(n):
        factors = set()
        for end in range(start, n):
            if t[end] != 1:
                prime_factors = [f for f in range(2, t[end] + 1) if is_prime(f) and t[end] % f == 0]
                if all(factor not in factors for factor in prime_factors):
                    factors.update(prime_factors)
                else:
                    break
                max_length = max(max_length, end - start + 1)
    return max_length
