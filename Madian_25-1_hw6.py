import re
from termcolor import colored

while True:
    print('\nМеню с опциями: '
          '\n1 - Считать имена и фамилии'
          '\n2 - Считать все емайлы'
          '\n3 - Считать названия файлов'
          '\n4 - Считать цвета'
          '\n5 - Для выхода нажмите 5'
          '\nВыберите цифру для активации опции')
    user_input = int(input())
    mock_data = open('MOCK_DATA.txt')
    if user_input == 5:
        text = colored('Вы вышли из меню)', 'green')
        print(text)
        break
    elif user_input == 1:
        with open('name.txt', 'w') as file:
            dt = mock_data.read()
            names = re.findall(r'\b[A-Z][a-zA-Z\'\-\.]+[\s]+[a-zA-Z\'\-\. ]+\b', dt)
            nm = '\n'.join(names)
            file.write(nm)
            text = colored('Все имена и фамилии сохранены в файле name.txt', 'yellow')
            print(text)
    elif user_input == 2:
        with open('emails.txt', 'w') as file:
            dt = mock_data.read()
            emails = re.findall(r'\s[a-z\d]+\W\w+\W[a-z\.\-]+', dt)
            em = '\n'.join(emails)
            file.write(em)
            text = colored('Все имейлы сохранены в файле emails.txt', 'yellow')
            print(text)
    elif user_input == 3:
        with open('files.txt', 'w') as file:
            dt = mock_data.read()
            files = re.findall(r'\s(?:[A]|[A-Z](?:[a-z]+|[A-Z][a-z]+|[a-z]+[A-Z][a-z]+|[a-z]+[A-Z][a-z]+[A-Z]*[a-z]*|'
                               r'[a-z]+[A-Z][A-Z][a-z]+|[a-z]+[A-Z]))\.[a-z]*(?:[a-z]+|[1-3])', dt)
            fl = '\n'.join(files)
            file.write(fl)
            text = colored('Все файлы сохранены в файле files.txt', 'yellow')
            print(text)
    elif user_input == 4:
        with open('colors.txt', 'w') as file:
            dt = mock_data.read()
            colors = re.findall(r'\s\W\w\w\w\w\w\w', dt)
            cl = '\n'.join(colors)
            file.write(cl)
            text = colored('Все цвета сохранены в файле colors.txt', 'yellow')
            print(text)
    else:
        text = colored('Неправильный ввод. Введите число только с 1 до 5', 'red')
        print(text)




