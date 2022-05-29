# Написать программу, позволяющую выполнять подсчет слов 
# в тексте, а также вычислять размер (в символах) каждого слова. 
# Используйте для возвращения результатов подсчета механизм генераторов.


def count(a):

    words = a.split()
    yield len(words)
    for el in words:
        yield len(el)

text = str(input("Введите текст: "))
temp = count(text)

Arr = []
for i in temp:
    Arr.append(i)
    
print("Количество слов: ", Arr[0])
print("Количество букв в каждом слове: ", Arr[1:])


