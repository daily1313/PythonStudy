# 튜플 종합문제 커피숍
menu_list = ("아메리카노", "카페라떼", "당근케익")
price_list = (2000, 3000, 4000)
order_list = [0, 0, 0]

while True:
    print("="*60)
    cmd = input('커피숍 명령을 입력하세요 (1=메뉴보기 2=주문입력 3=주문출력 q=종료) >> ')

    if cmd == 'q':
        print('프로그램을 종료합니다.')
        break
    elif cmd == '1':
        for menu in menu_list:
            print(menu, '가격', str(price_list[menu_list.index(menu)])+'원')
    elif cmd == '2':
        menu, num = input('메뉴와 갯수를 입력하세요 >> ').split()
        order_list[menu_list.index(menu)] = int(num)
    elif cmd == '3':
        total = 0
        for n in range(len(menu_list)):
            if order_list[n]:
                print(menu_list[n], "가격", price_list[n], "주문", order_list[n], "개")
                total += price_list[n] * order_list[n]
        print('주문 총액은', total, '원입니다')
    else:
        print('해당 명령이 없습니다.')
