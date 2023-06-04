def hap(a, b):
    result = a + b
    print('두 수의 합을 출력해주는 함수입니다.')
    print(a, b, '의 합은', result, '입니다')
def cha(a, b):
    result = a - b
    print('두 수의 차를 출력해주는 함수입니다.')
    print(a, b, '의 차는', result, '입니다')

def hapcha(a, b, op):
    if op == '+':
        result = a + b
        print('두 수의 합을 출력해주는 함수입니다.')
        print(a, b, '의 합은', result, '입니다')
    elif op == '-':
        result = a - b
        print('두 수의 차를 출력해주는 함수입니다.')
        print(a, b, '의 차는', result, '입니다')
    else:
        print('정의되지 않은 연산입니다')
print()
hapcha(10, 20, '+')
hapcha(10, 20, '-')
hapcha(-87, 172, '+')
hapcha(-87, 172, '-')
hapcha(-87, 172, '*')
