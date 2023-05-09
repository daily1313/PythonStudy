coins = [['BTC', 50000], ['XRP', 20000], ['ADA', 30000]]

total_balance = 0
for i in range(len(coins)):
    total_balance += coins[i][1]


print('가상화폐 프로그램에 오신 것을 환영합니다')
print('='*60)

while True:
    command = input('명령을 입력하세요 (1=입력, 2=내역확인, 3=삭제, q=종료) >> ')

    if command == '1':
        while True:
            coin_info = input('코인 정보를 입력하세요 (입력종료는 마침표) >> ')
            if coin_info == ".":
                break
            coin_name, coin_price = coin_info.split()
            coin_price = int(coin_price)
            for i in range(len(coins)):
                if coins[i][0] == coin_name:
                    coins[i][1] += coin_price
                    total_balance += coin_price
                    break
            else:
                coins.append([coin_name, coin_price])
                total_balance += coin_price

    elif command == '2':
        print('현재 보유중인 가상화폐 내역입니다')
        for i in range(len(coins)):
            print('%s %d 원' %(coins[i][0], int(coins[i][1])), end="")
            if i != len(coins) - 1:
                print(", ", end="")
        print()
        print('총 보유액은 %d 원입니다' % total_balance)

    elif command == '3':
        coin_name = input('삭제할 코인을 입력하세요 >> ')
        for coin in coins:
            if coin[0] == coin_name:
                total_balance -= coin[1]
                coins.remove(coin)
                break
        else:
            print('해당 코인이 없습니다.')

    elif command == 'q':
        print('프로그램을 종료합니다.')
        break

    else:
        print('잘못된 입력입니다. 다시 입력해주세요.')