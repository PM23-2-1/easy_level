def append_to_list():
    list_1 = input('List: ').split()
    a = input('a: ')
    list_1.append(a)
    print(list_1)

def list_extend():
    list_1 = input('List 1: ').split()
    list_2 = input('List 2: ').split()
    list_1.extend(list_2)
    print(list_1)

def list_reverse():
    list_1 = input('List: ').split()
    list_1.reverse()
    print(list_1)