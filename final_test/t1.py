
my_book = {'점심': 10000, '커피': 3000}

def book_input(name, price):
    my_book[name] = int(price)

def book_report():
    total = 0
    for key, value in my_book.items():
        print(f'항목 {key}: 금액 {value}원')
        total += value
    return total

def book_del(name):
    del my_book[name]
    return list(my_book.keys())

while True:
    cmd = input('명령을 입력하세요 (1=입력 2=상태 3=삭제 4=종료) >> ')

    if cmd == '1':
        name, price = input('항목과 가격을 입력하세요 (예: 점심 10000) >> ').split()
        book_input(name, price)
    elif cmd == '2':
        price = book_report()
        print(f'총액 {price}원')
    elif cmd == '3':
        name = input('삭제 항목을 입력하세요 (예: 점심) >> ')
        my_list = book_del(name)
        print(f'삭제 후 키워드 리스트: {my_list}')
    elif cmd == '4':
        print('프로그램을 종료합니다')
        break
    else:
        print('잘못된 명령입니다.')