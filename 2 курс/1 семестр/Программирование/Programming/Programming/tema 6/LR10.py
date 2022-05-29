def main():
    input_str = input("Введите строку для поиска: ")

    searchable_str = input("Введите строку, по которой мы ищем: ")
    
    choice = None
    while choice != '4':

        print('1 - поиск первого вхождения подстроки')
        print('2 - замена первой подстроки')

        print('3 - найти все вхождения подстроки' )

        print('4 - для выхода')
        choice = input("Сделайте  выбор (1..4) ")
        
        if choice == '1':
            print("Первое вхождение :", search_str(input_str, searchable_str))

        if choice == '2':
            rep_str = input('Строка для замены: ')
            searchable_str = search_n_replace_str(input_str, rep_str, searchable_str)
            print("Результат: ", searchable_str)

        if choice == '3':
            print("Все вхождения: ", search_all(input_str, searchable_str))
            

def search_str(what="", where=""):
    lenin=len(what)
    lense=len(where)
    res = []
    for i in range (lense):
        if where[i:i+lenin:]==what:
            res.append((i, i + lenin))
    if len(res)==0:
        return "ничего не найдено"
    else:
        return res[0]


def search_all(what="", where=""):
    lenin=len(what)
    lense=len(where)
    res = []
    for i in range (lense):
        if where[i:i+lenin:]==what:
            res.append((i, i + lenin))
    if len(res)==0:
        return "ничего не найдено"
    else:
        return res


def search_n_replace_str(what="",  to_what="", where=""):
    index = search_str(what, where)[0]
    print(index)
    resstr = where[0:index:] + to_what + where[index+len(what):len(where):]
    return resstr

main()
