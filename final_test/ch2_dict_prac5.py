# 가계부를 사전 데이터 구조로 작성

my_book = {'점심' : 10000, '커피' : 3000}

while True:
    cmd = input('명령을 입력하세요 (1=입력 2=상태 3=삭제 4=종료) >> ')

    if cmd == '1':
        name, price = input('항목과 가격을 입력하세요 (예: 점심 10000) >> ').split()
        my_book[name] = int(price)
    elif cmd == '2':
        total = 0
        for key in my_book:
            print('항목', key, '금액', my_book[key])
            total += my_book[key]
        print('총액', total, '원')
    elif cmd == '3':
        name = input('삭제 항목을 입력하세요 (예: 점심) >> ')
        del my_book[name]
    elif cmd == '4':
        break
    else:
        print('잘못된 명령입니다')
    print()
print('프로그램을 종료합니다')
