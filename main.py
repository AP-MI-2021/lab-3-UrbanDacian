def get_longest_div_k(lst, k):
    """
    Determina secventa cu cele mai multe numere divizibile cu k dintr-o lista
    :param lst: lista de nr. intrego
    :param k: numarul intreg
    :return: o lista continand cea mai lunga secventa de elementele divizibile cu k din lst
    """
    secv_act = []
    secv_max = []
    cnt_act = 0
    cnt_max = 0
    for x in lst:
        if x % k == 0:
            secv_act.append(x)
            cnt_act = cnt_act + 1
        else:
            if cnt_act > cnt_max:
                secv_max = secv_act
            cnt_act = 0
            secv_act = []
    return secv_max


def test_get_longest_div_k():
    assert get_longest_div_k([12, 85, 77, 15], 5) == [85]
    assert get_longest_div_k([11, 77, 111, 89, 78, 121], 11) == [11, 77]


def is_desc(x):
    """
    Determina daca cifrele unui numar se afla in ordine decrecatoare
    :param x: un numar intreg
    :return: True, daca cifrele se alfa in ordine descrescatoare, False in caz contrar
    """
    while x > 9:
        if x % 10 >= x // 10 % 10:
            return False
        x = x // 10
    return True


def get_longest_digit_count_desc(lst):
    """
    Determina cea mai lunga secventa de numerele care au cifrele in ordine descrescatoare
    :param lst: lista de nr. intregi
    :return: o lista continand secventa cea mai lunga de numerele ce au cifrele in ordine descrecatoare
    """
    secv_act = []
    secv_max = []
    cnt_act = 0
    cnt_max = 0
    for i in lst:
        if is_desc(i):
            secv_act.append(i)
            cnt_act = cnt_act + 1
        else:
            if cnt_max < cnt_act:
                secv_max = secv_act
            cnt_act = 0
            secv_act = []
    return secv_max


def test_get_longest_digit_count_desc():
    assert get_longest_digit_count_desc([]) == []
    assert get_longest_digit_count_desc([111, 39, 982, 471, 5321]) == [982]
    assert get_longest_digit_count_desc([45, 932, 173, 92, 84, 359, 4421]) == [92, 84]


def palindrom(n):
    copie = n
    numar = 0
    if n <= 9 and n >= -9:
        return True
    else:
        n = str(n)
        if n == n[::-1]:
            return True
    return False


def  get_longest_all_palindrome(lst):
    '''
    Determina secventa maxima de valori care sunt palindroame din lista
    :param lst: lista initiala
    :return: secventa maxima de palindroame ca lista
    '''
    secv_act = []
    secv_max = []
    cnt_act = 0
    cnt_max = 0
    for n in lst:
        if palindrom(n) is True:
            cnt_act += 1
            secv_act.append(n)
        else:
            if cnt_act > cnt_max:
                cnt_max = cnt_act
                secv_max = secv_act.copy()
                secv_act = []
                cnt_act = 0
    if (cnt_act > cnt_max):
        secv_max = secv_act.copy()
    return secv_max

def test_get_longest_all_palindrome():
    assert get_longest_all_palindrome([22, 33, 45]) == [22, 33]
    assert get_longest_all_palindrome([2, 2, 2]) == [2, 2, 2]
    assert get_longest_all_palindrome([14, 33, 11]) == [33]



def print_menu():
    print("1.Citire lista")
    print("2.Afiseaza cea mai lunga secventa de numere divizibile cu k")
    print("3.Afiseaza cea mai lunga secventa de numere care au cifrele in ordine descrescatoare")
    print("4.Afiseaza cea mai lunga secventa de palindroame")
    print("a.Afisare lista")
    print("x.Iesire\n")


def citire_lista():
    lst = []
    n = int(input("Dati numarul de valori din lista "))
    for i in range(n):
        lst.append(int(input("lst[" + str(i) + "]=")))
    return lst


def main():
    test_get_longest_div_k()
    test_get_longest_digit_count_desc()
    lst = []
    while True:
        print_menu()
        optiune = input("Alegeti optiunea ")
        if optiune == "1":
            lst = citire_lista()
        elif optiune == "2":
            k = int(input("k="))
            print(get_longest_div_k(lst, k))
        elif optiune == "3":
            print(get_longest_digit_count_desc(lst))
        elif optiune == "4":
            print (get_longest_all_palindrome(lst))
        elif optiune == "a":
            print(lst)
        elif optiune == "x":
            break
        else:
            print("Optiune gresita. Reincercati!")


main()