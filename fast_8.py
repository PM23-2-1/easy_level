def str_work():
    string_1 = input('Str 1:')
    string_2 = input('Str 2:')
    ind = input('Ind: ')
    if (ind.isdigit() or (ind[1:].isdigit and ind[0] == '-')) and int(ind) < len(string_1):
        len_1 = len(string_1)
        len_2 = len(string_2)
        ind = int(ind)
        pod_str = string_1.find(string_2)
        print(len_1, len_2, pod_str, string_1[ind], string_1[:8], string_1.lower(), string_1.upper(), sep='\n')
    else:
        print(ind, '- не число')
    return