
money_list = []
price_list = []
total = 0
print("가계부 프로그램에 오신 것을 환영합니다.")
print("=" * 50)
cmd = "0"
while cmd != "3" :
    cmd = input("명령을 입력하세요 (1=내역입력, 2=결과출력, 3=종료)")

    if cmd == "1" :
        item = input("지출 항목을 입력하세요: ")
        price = int(input("지출 금액을 입력하세요: "))
        money_list.append(item)
        price_list.append(price)
        total += price
    elif cmd == "2" :
        print(money_list)
        print(price_list)
        print(total)
    elif cmd == "3" :
        print("프로그램을 종료합니다.")


