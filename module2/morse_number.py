import re


def morse_number(num):
    res = ''
    for i in num:
        if i == '1':
            res = res + '.----' + ' '
        elif i == '2':
            res = res + '..---' + ' '
        elif i == '3':
            res = res + '...--' + ' '
        elif i == '4':
            res = res + '....-' + ' '
        elif i == '5':
            res = res + '.....' + ' '
        elif i == '6':
            res = res + '-....' + ' '
        elif i == '7':
            res = res + '--...' + ' '
        elif i == '8':
            res = res + '---..' + ' '
        elif i == '9':
            res = res + '----.' + ' '
        elif i == '0':
            res = res + '-----' + ' '
        else:
            print('Unknown value')
    return res


print(morse_number("295"))
print(morse_number("005"))
print(morse_number("513"))
print(morse_number("784"))
