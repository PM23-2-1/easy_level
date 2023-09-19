def check_any_sumb_in_str():
    string = input('Строка: ')
    if len(string) != 0:
        print('Симовлы есть')
    else:
        print('Символов нет')

def ch_nch_min_nch():
    n = int(input('n: '))
    ch = []
    nch = []
    for i in range(n):
        a = int(input(str(i) + ': '))
        if a % 2 == 0:
            ch.append(a)
        else:
            nch.append(a)
    print(ch, nch, min(nch), sep='\n')

def dictionary_month():
    month = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']
    dict_month = dict(zip(month, range(1, 13)))
    print(dict_month)