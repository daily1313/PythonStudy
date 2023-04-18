

spending_list = []

print("가계부 프로그램에 오신 것을 환영합니다.")
print("=" * 50)

while True:
    cmd = input("명령을 입력하세요 (1=내역입력, 2=결과출력, 3=종료)")

    if cmd == "1":
        item = str(input("지출 항목을 입력하세요: "))
        price = int(input("지출 금액을 입력하세요: "))
        spending_list.append((item, price))
    elif cmd == "2":
        total = 0
        print("지출항목 리스트입니다")
        for item, price in spending_list :
            print("%s %d 원" % (item, price))
            total += price
        print("지출 총액은 %d 원입니다" % total)
    elif cmd == "3":
        print("프로그램을 종료합니다.")
        break
    else:
        # 잘못된 명령어 입력시 경고 메세지 출력 후 다시 명령어 입력 받음
        print("잘못된 명령입니다.")
