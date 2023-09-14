
def dict_1():
    list_1 = input('List 1: ').split()
    list_2 = input('List 2: ').split()
    if len(list_1) == len(list_2):
        dictionary = {k:v for k, v in zip(list_1, list_2) if list_1.count(k) == 1}
        return dictionary
    else:
        print('Ошибка')
    return False

def dict_2():
    dictionary = {i:i**3 for i in range(1, 11)}
    return dictionary