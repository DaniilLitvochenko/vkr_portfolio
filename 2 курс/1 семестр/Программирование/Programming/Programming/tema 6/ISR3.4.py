def rot13(letter):
    if ord('a') + 13 > ord(letter) >= ord('a'):
        return chr(ord(letter) + 13)
    elif ord('z') >= ord(letter) >= ord('a') + 13:
        return chr(ord(letter) - 13)
    elif ord('A') + 13 > ord(letter) >= ord('A'):
        return chr(ord(letter) + 13)
    elif ord('Z') >= ord(letter) >= ord('A') + 13:
        return chr(ord(letter) - 13)
    else:
        return letter

inpstr = input('Введите строку для шифрования: ')
resstr = ''.join(list((map(rot13, inpstr))))
print('Результат:', resstr)
resstr = ''.join(list((map(rot13, resstr))))
print('Проверка:', resstr)
