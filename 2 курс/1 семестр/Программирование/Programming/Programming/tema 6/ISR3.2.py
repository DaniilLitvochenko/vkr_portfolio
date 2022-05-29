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

input_str = input("Введите строку для поиска: ")
searchable_str = input("Введите строку, по которой мы ищем: ")
print("Первое вхождение :", search_str(input_str, searchable_str))
