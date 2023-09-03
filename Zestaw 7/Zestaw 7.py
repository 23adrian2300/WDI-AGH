# Definicja Node
class Node:
    def __init__(self, value=None):
        self.val = value
        self.next = None


# 1. Zaimplementuj zbiór mnogościowy liczb naturalnych korzystając ze
# struktury listy odsyłaczowej.
# - czy element należy do zbioru
# - wstawienie elementu do zbioru
# - usunięcie elementu ze zbioru

class setts:
    def __init__(self):
        self.first = Node()

    def find(self, val):
        current = self.first
        while current.val != val and current.next is not None:
            current = current.next
        return current.val == val

    def add(self, val):
        if not setts.find(self, val):
            current = self.first
            while current.next is not None:
                current = current.next
            current.next = Node(val)

    def delete(self, val):
        current = self.first
        previous = self.first
        while current.val != val and current.next is not None:
            previous = current
            current = current.next
        if current.val != val:
            return False
        else:
            current.val = None
            previous.next = current.next


# 2. Zastosowanie listy odsyłaczowej do implementacji
# tablicy rzadkiej. Proszę napisać trzy funkcje:
# – inicjalizującą tablicę,
# – zwracającą wartość elementu o indeksie n,
# – podstawiającą wartość value pod indeks n.

def make_linked_list(tab):
    first = Node()
    current = first
    zeros = 0
    for i in tab:
        if i != 0:
            temp = Node(i, zeros)
            current.next = temp
            current = temp
            zeros = 0
        else:
            zeros += 1
    if zeros > 0:
        temp = Node(0, zeros - 1)
        current.next = temp
        current = temp
    return first


def print_el(first, index):
    current = first.next
    licznik = 0
    while current.next is not None:
        if current.zeros > 0:
            licznik = licznik + current.zeros
        if licznik > index:
            return 0
        if licznik == index:
            return current.val
        else:
            licznik += 1
        current = current.next


def base(first, index, value):
    curr = first.next
    count = 0
    while curr.next is not None:
        if curr.zeros > 0:
            count = count + curr.zeros
        if count > index:
            print(curr.zeros, index, count - index, curr.zeros - index)
            temp = Node(value)
            curr.next.zeros = curr.zeros - index
            temp.next = curr.next
            curr.next = temp
            break
        if count == index:
            curr.val = value
            break
        else:
            count += 1
        curr = curr.next


# 3. Proszę napisać funkcję scalającą dwie posortowane listy w jedną
# posortowaną listę. Do funkcji należy przekazać wskazania na pierwsze
# elementy obu list, funkcja powinna zwrócić wskazanie do scalonej listy.
# - funkcja iteracyjna,
# - funkcja rekurencyjna.


def scal(p1, p2):
    node = Node()
    curr = node
    while p1 is not None and p2 is not None:
        if p1.val < p2.val:
            curr.next = p1
            curr = p1
            p1 = p1.next
        else:
            curr.next = p1
            curr = p2
            p2 = p2.next
    if p1 != None:
        curr.next = p1
    else:
        curr.next = p2
    return node.next


def rek_scal(p1, p2):
    if p1 == None:
        return p2
    if p2 == None:
        return p1

    if p1.val < p2.val:
        curr = p1
        curr.next = rek_scal(p1.next, p2)
    else:
        curr = p2
        curr.next = rek_scal(p1, p2.next)

    return curr


# 4. Proszę napisać funkcję, która dla podanej listy odsyłaczowej odwraca
# kolejność jej elementów.


def reverse(first):
    if first is None:
        return first
    p = None
    r = first
    while r is not None:
        next = r.next
        r.next = p
        p = r
        r = next
    return p


# 5. Proszę napisać funkcję, która rozdziela elementy listy odsyłaczowej do
# 10 list, według ostatniej cyfry pola val. W drugim kroku powstałe listy
# należy połączyć w jedną listę odsyłaczową, która jest posortowana
# niemalejąco według ostatniej cyfry pola val.

def changer(first):
    flist = [None for _ in range(10)]
    llist = [None for _ in range(10)]
    p = first
    while p != None:
        last = p.val % 10
        if flist[last] == None:
            flist[last] = llist[last] = p
        else:
            llist[last].next = p
            llist[last] = p
        p = p.next
    result = None
    for i in range(9, -1, -1):
        if flist[i] != None:
            llist[i].next = result
            result = flist[i]
    return result


# 6. Proszę napisać funkcję wstawiającą na koniec listy nowy element. Do
# funkcji należy przekazać wskazanie na pierwszy element listy oraz wstawianą
# wartość.

def add_end(first, val):
    p = first
    while p.next != None:
        p = p.next
    p.next = Node(val)


# 7. Proszę napisać funkcję usuwającą ostatni element listy. Do funkcji
# należy przekazać wskazanie na pierwszy element listy.

def delete_last(first):
    p = first
    while p.next.next != None:
        p = p.next
    p.next = None


# 8. Dana jest niepusta lista, proszę napisać funkcję usuwającą co drugi
# element listy. Do funkcji należy przekazać wskazanie na pierwszy element
# listy.

def remove_every_second_element(head):
    if head is None or head.next is None:
        return
    current = head
    prev = None
    remove = False

    while current is not None:
        if remove:
            prev.next = current.next
            remove = False
        else:
            prev = current
            remove = True
        current = current.next


# 9. Dana jest niepusta lista reprezentująca liczbę naturalną. Kolejne
# elementy listy przechowują kolejne cyfry. Proszę napisać funkcję
# zwiększającą taką liczbę o 1.

def increase(first, rek=0, ahead=None):
    if rek == 0:
        curr1 = None
        curr2 = first
        while curr2 is not None:
            curr1 = curr2
            curr2 = curr2.next
        curr1.val += 1
        if curr1.val == 10:
            curr1.val = 0
            return increase(first, 1, curr1)
        return first
    if rek == 1:
        curr1 = None
        curr2 = first
        while curr2 is not ahead:
            curr1 = curr2
            curr2 = curr2.next
        if not curr1:
            b = Node(1)
            b.next = first
            first = b
            return first
        curr1.val += 1
        if curr1.val == 10:
            curr1.val = 0
            return increase(first, 1, curr1)
        return first


# 10. Liczby naturalne reprezentowane jak poprzednim zadaniu. Proszę napisać
# funkcję dodającą dwie takie liczby. W wyniku dodawania dwóch liczb powinna
# powstać nowa lista.
def add_two(f_1, f_2, first=None, el=0, b1=0, b2=0):
    p1 = None
    p2 = None
    r1 = f_1
    r2 = f_2
    while r1 is not None and r1 and r1 != b1 and b1 is not None:
        p1 = r1
        r1 = r1.next
    while r2 is not None and r2 and r2 != b2 and b2 is not None:
        p2 = r2
        r2 = r2.next
    if p1 is not None:
        el += p1.val
    if p2 is not None:
        el += p2.val
    if el == 0:
        return first
    new_el = Node(el % 10)
    new_el.next = first
    first = new_el
    return add_two(f_1, f_2, first, el // 10, p1, p2)


# 11. Lista zawiera niepowtarzające się elementy. Proszę napisać funkcję do
# której przekazujemy wskaźnik na początek oraz wartość klucza. Jeżeli
# element o takim kluczu występuje w liście należy go usunąć z listy. Jeżeli
# elementu o zadanym kluczu brak w liście należy element o takim kluczu
# wstawić do listy.

def lookforkey(first, key):
    p = first
    while p is not None:
        if p.val == key:
            return True
        p = p.next
    return False


def keys(first, key):
    if lookforkey(first, key):
        if first.val == key:
            first = first.next
            return first
        curr1 = None
        curr2 = first
        while curr2.val != key:
            curr1 = curr2
            curr2 = curr2.next
        curr1.next = curr2.next
        return first
    else:
        b = Node(key)
        b.next = first
        first = b
        return first


# 22. Dana jestlista, który być może zakończona jest cyklem.
# Napisać funkcję, która sprawdza ten fakt.

def is_cycle(node):
    if not node:
        return False
    if not node.next:
        return False
    curr1 = node
    curr2 = node
    while curr1 and curr2 and curr2.next:
        curr1 = curr1.next
        curr2 = curr2.next.next
        if curr1 == curr2:
            return True
    return False


# 25. Dana jest lista, który zakończona jest cyklem. Napisać funkcję, która
# zwraca wskaźnik do ostatniego elementu przed cyklem.
def last_one(node):
    if not node:
        return node
    curr1 = node
    curr2 = node
    while curr1 and curr2 and curr2.next:
        curr1 = curr1.next
        curr2 = curr2.next.next
        if curr1 == curr2:
            k = curr2
            break
    n1 = None
    n2 = node
    while n2 != k:
        n1 = n2
        n2 = n2.next
        k = k.next
    return n1


# 30. Dane są dwie niepuste listy, z których każda zawiera niepowtarzające
# się elementy. Elementy w pierwszej liście są uporządkowane rosnąco, w
# drugiej elementy występują w przypadkowej kolejności. Proszę napisać
# funkcję, która z dwóch takich list stworzy jedną, w której uporządkowane
# elementy będą stanowić sumę mnogościową elementów z list wejściowych.
# Do funkcji należy przekazać wskazania na obie listy, funkcja powinna
# zwrócić wskazanie na listę wynikową. Na przykład dla list:
# 2 -> 3 -> 5 ->7-> 11
# 8 -> 2 -> 7 -> 4
# powinna pozostać lista:
# 2 -> 3 -> 4 -> 5 ->7-> 8 -> 11

def append(f, val):
    new_el = Node(val)
    if not f:
        return new_el
    curr1 = None
    curr2 = f
    while curr2:
        curr1 = curr2
        curr2 = curr2.next
    curr1.next = new_el
    return f


def adding(first, second):
    first = None
    v = first

    while v:
        first = append(first, v.val)
        v = v.next
    curr1 = second
    while curr1:
        if curr1.val < first.val:
            temp = Node(curr1.val)
            temp.next = first
            first = temp
        curr1 = curr1.next
    curr = second

    while curr:
        curr1 = first
        curr2 = first.next
        if curr1.val == curr.val:
            curr = curr.next
            continue

        while curr2:
            if curr1.val < curr.val < curr2.val:
                temp = Node(curr.val)
                curr1.next = temp
                temp.next = curr2
                break

            curr1 = curr2
            curr2 = curr2.next

        if not curr2:
            if curr1.val < curr.val:
                temp = Node(curr.val)
                curr1.next = temp
        curr = curr.next

    return first
