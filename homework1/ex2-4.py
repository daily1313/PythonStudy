
menu_list = ("아메리카노", "카페라떼", "당근케익")
price_list = (2000, 3000, 4000)
order_list = [0, 0, 0]


cmd = '0'

while True :
    print("=" * 60)
    cmd = input('커피숍 명령을 입력하세요(1=메뉴보기 2=주문입력 3=주문출력 q=종료) >> ')
    if cmd == '1':
        for i in range(len(menu_list)):
            print('%s 가격 %d원' % (menu_list[i], price_list[i]))
    elif cmd == '2':
        menu, quantity = input("메뉴와 갯수를 입력하세요 >> ").split()
        index = menu_list.index(menu)
        order_list[index] += int(quantity)
    elif cmd == '3':
        total_price = 0
        for i in range(len(menu_list)):
            if order_list[i]:
                print('%s 가격 %s 주문 %d 개' %(menu_list[i], price_list[i], order_list[i]))
                total_price += price_list[i] * order_list[i]
        print('주문 총액은 %d 원입니다' % total_price)
    elif cmd == 'q':
        print("프로그램을 종료합니다.")
        break
    else:
        print("잘못된 명령입니다.")