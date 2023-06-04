my_book = {'점심': 10000, '커피' : 3000}

def book_input(name, price):
    my_book[name] = price

def book_report():
    total = 0
    for item, price in my_book.items():
        print(f'항목 {item}: 금액 {price}원')
        total += price
    return total

def book_del(name):
    del my_book[name]
    keys = list(my_book.keys())
    return keys

while True:
    cmd = input('명령을 입력하세요 (1=입력 2=상태 3=삭제 4=종료) >> ')

    if cmd == '1':
        name, price = input('항목과 가격을 입력하세요 (예: 저녁 12000) >> ').split()
        book_input(name, int(price))
    elif cmd == '2':
        total = book_report()
        print(f'총액 {total}원')
    elif cmd == '3':
        delete_item = input('삭제 항목을 입력하세요 (예: 점심) >> ')
        keysAfterDeleteItem = book_del(delete_item)
        print(f'삭제 후 키워드 리스트 {keysAfterDeleteItem}')
    elif cmd == '4':
        print('프로그램을 종료합니다.')
        break
    else:
        print('올바른 명령을 입력해주세요')