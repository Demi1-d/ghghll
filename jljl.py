baza = {}
import os 
os.system('clear')
import random
def genric_password(nr_letters=4, nr_numbers=3, nr_sysmbool=6):
    alph = 'qweertyuiopasdfghjklzxcvbnm'
    num = '1234567890'
    symbol = '!@#$%^&*()|?'
    
    #  = int(input('how many letters do want?: '))
    #  = int(input('how many numbers do want?: '))
    #  = int(input('how many sysmbols do want?: '))
    passwrod = []
    for i in range(1, nr_letters + 1):
        passwrod += random.choice(alph)
    for i in range(1, nr_numbers + 1):
        passwrod += random.choice(num)
    for i in range(1, nr_sysmbool + 1):
        passwrod += random.choice(symbol)

    random.shuffle(passwrod)
    
    password_string = ""
    for i in passwrod:
        password_string += i
    return password_string

# genric_password()

def code_chek():
    num = ['1','2','3','4','5','6','7','8','9','0']
    code = ''
    
    for i in range(1,7):
        code += random.choice(num)
    return int(code)

# print(code_chek())

while True:
    table = int(input('''
    register        1
    autorization    2
    >>> '''))
    if table == 1:
        login = input('login: ')
        password2 = genric_password()
        code = code_chek()
        print(code)
        try:
            inpcode = int(input('code: '))
        except ValueError:
            print('пиши код в циврах')
        else:
            while inpcode != code:
                print('повторите ввод кода')
                inpcode = int(input('code: '))
            else:
                print('ты зарегитрирован')
                baza.update({
                    'login': login,
                    'password': password2
                })
                print(baza)
    elif table == 2:
        login = input('login; ')
        password2 = input('pass: ')
        if login in baza.values():
            if password2 in baza.values():
                print('вы авторизованы')
            else:
                print('не верный пароль')
        else:
            print('у нас нет такого пользователя')
    else:
        print('убедитесь что вы ввели правильно')