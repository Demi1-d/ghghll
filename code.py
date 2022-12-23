from random import choice
def main(size_pass: int, *list1):
    password = []
    code = []
    num_code = ['1','2','3','4','5','6','7','8','9','0']
    for i in range(size_pass):
        password.append(choice(list1))
    for j in range(6):
        if len(code) >= 6:
            break
        code.append(choice(num_code))
    return password, code
    
size_password = int(input('pass size: '))
end_pass = main(size_password, '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm')
passs = ''.join(end_pass[0])
code = ''.join(end_pass[1])
print(passs, code)