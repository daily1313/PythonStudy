def c_to_f(c):
    f = (c * 9/5) + 32
    return round(f, 2)

def f_to_c(f):
    c = (f - 32) * 5/9
    return round(c, 2)

while True:
    opt = input('메뉴: 1=섭씨->화씨, 2=화씨->섭씨, q=종료 >> ')

    if opt == '1':
        c = float(input('섭씨 온도를 입력하세요: '))
        f = c_to_f(c)
        print(f'{c:.2f}도는 화씨로 {f:.2f}도입니다.')
    elif opt == '2':
        f = float(input('화씨 온도를 입력하세요: '))
        c = f_to_c(f)
        print(f'{f:.2f}도는 섭씨로 {c:.2f}도입니다.')
    elif opt == 'q':
        print('프로그램을 종료합니다.')
        break
    else:
        print('올바른 메뉴를 선택하세요.')
