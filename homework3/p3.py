printer_dict = {'잉크젯': [200, 100], '레이저젯': [200, 100], 'Epson': [200, 100]}
budget = 200000

def cmd_input():
    return input('명령을 입력하세요 (1=사용 2=상태 3=보충 4=등록 5=삭제 q=종료) >> ')

def printer_use(name, page):
    if name in printer_dict:
        if page <= printer_dict[name][0]:
            toner = page // 10
            printer_dict[name][0] -= page
            printer_dict[name][1] -= toner
    else:
        print('해당 프린터가 없습니다.')
        return
def printer_status():
    for name, counts in printer_dict.items():
        print(f'{name} 종이 {counts[0]} 토너 {counts[1]}')
    print(f'예산 {budget}원')

def printer_refill(name, page, toner):
    global budget # 함수 내에서 전역변수를 사용하기 위함
    if name in printer_dict:
        printer_dict[name][0] += page
        printer_dict[name][1] += toner
        budget -= (page * 100 + toner * 200)
def printer_add(name, page, toner):
    printer_dict[name] = [page, toner]

def printer_del(name):
    if name in printer_dict:
        del printer_dict[name]
    print(f'삭제 후 남아 있는 프린터들: {list(printer_dict.keys())}')

print('프린터 관리자입니다')
print('='*50)

while True:
    cmd = cmd_input()

    if cmd == '1':
        printer_name, usage = input('프린터와 장수를 입력하세요 ').split()
        usage = int(usage)
        printer_use(printer_name, usage)
    elif cmd == '2':
        printer_status()
    elif cmd == '3':
        printer_name, page, toner = input('프린터와 장수 및 토너를 입력하세요 (예: 잉크젯 100 50) >> ').split()
        page = int(page)
        toner = int(toner)
        printer_refill(printer_name, page, toner)
    elif cmd == '4':
        printer_name, page, toner = input('등록할 프린터와 장수 및 토너를 입력하세요 (예: 잉크젯 100 50) >> ').split()
        page = int(page)
        toner = int(toner)
        printer_add(printer_name, page, toner)
    elif cmd == '5':
        printer_name = input('삭제할 프린터를 입력하세요 (예: 잉크젯) >> ')
        printer_del(printer_name)
    elif cmd == 'q':
        print('프로그램을 종료합니다.')
        break
    else:
        print('잘못된 명령입니다.')

