
inkjet = [100, 20]
laserjet = [200, 50]
my_money = 200000
print('파이썬 중간고사 제 이름은 김승범 학번은 60181869 입니다.')
print('=' * 50)

while True :
    cmd = int(input('명령을 입력하세요(1=사용 2=상태 3=보충 4=종료>>'))

    if cmd == 1 :
        opt = int(input('프린터를 선택하세요(1=잉크젯 2=레이저젯)>>'))
        quantity = int(input('몇 장 프린트 하시겠습니까?>>'))
        if opt == 1 :
            inkjet[0] -= quantity
            inkjet[1] -= int(quantity/10)
        elif opt == 2 :
            laserjet[0] -= quantity
            laserjet[1] -= int(quantity/10)
    elif cmd == 2 :
        print('잉크젯 상태 종이 %d 토너 %d' %(inkjet[0],inkjet[1]))
        print('레이저젯 상태 종이 %d 토너 %d' %(laserjet[0],laserjet[1]))
        print('잔액 %d' % my_money)
    elif cmd == 3 :
        opt = int(input('보충하실 프린터를 선택하세요(1=잉크젯 2=레이저젯)>>'))

        if opt == 1 :
            paper = int(input('종이 수를 입력하세요 >>'))
            toner = int(input('토너 수를 입력하세요 >>'))
            inkjet[0] += paper
            inkjet[1] += toner
            my_money -= (paper * 100 + toner * 200)
        elif opt == 2 :
            paper = int(input('종이 수를 입력하세요 >>'))
            toner = int(input('토너 수를 입력하세요 >>'))
            laserjet[0] += paper
            laserjet[1] += toner
            my_money -= (paper * 100 + toner * 200)
    elif cmd == 4 :
        print('프로그램을 종료합니다')
        break
    else :
        print('잘못된 명령입니다')
