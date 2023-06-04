# 가계부를 집합 속의 튜플 형태로 작성

my_book = {('점심', 10000), ('커피', 3000)}

while True:
    cmd = input('명령을 입력하세요 (1=입력 2=상태 3=삭제 4=종료) >> ')

    if cmd == '1':
        cmd_list = input('항목과 가격을 입력하세요 (예: 점심 10000) >> ').split()
        # '점심 10000' -> ['점심', 10000]
        name = cmd_list[0]
        price = int(cmd_list[1])
        item = (name, price)
        my_book.add(item)
    elif cmd == '2':
        total = 0
        for item in my_book:
            print('항목', item[0], '금액', item[1])
            total += item[1]
        print('총액', total, '원')
    elif cmd == '3':
        name = input('삭제 항목을 입력하세요 (예: 점심) >> ')
        for item in my_book:
            if name == item[0]:
                my_book.remove(item)
                break
    elif cmd == '4':
        break
    else:
        print('잘못된 명령입니다.')
    print()

print('프로그램을 종료합니다.')