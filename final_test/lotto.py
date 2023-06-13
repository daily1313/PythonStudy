import random


alpha_index = ['A', 'B', 'C', 'D', 'E']

def getWinningLottoNumbersList() :
    winningNumber = set()
    while len(winningNumber) < 6:
        winningNumber.add(random.randint(1, 45))
    winningNumber = list(winningNumber)
    winningNumber.sort()
    return winningNumber
def getUserLottoNumbersList():
    number = set()
    while len(number) < 6:
        number.add(random.randint(1, 45))
    number = list(number)
    number.sort()
    return number
def getBonusNumber() :
    return random.randint(1, 45)
def compare_lotto_numbers(user_lotto_numbers, winning_numbers, bonus_number):
    count = 0
    bonus_count = 0

    for number in user_lotto_numbers:
        if number in winning_numbers:
            count += 1

    if bonus_number in user_lotto_numbers:
        bonus_count += 1

    return [count, bonus_count]

def getMatchNumbers(user_lotto_numbers, winning_numbers, bonus_number):
    matchedNumbers = []
    for number in user_lotto_numbers:
        if number in winning_numbers:
            matchedNumbers.append(number)

    if bonus_number in user_lotto_numbers:
        matchedNumbers.append(number)
    return matchedNumbers
def getRank(count_list):
    if count_list[0] == 6:
        print(f'일치하는 개수: {count_list[0]}, 1등')
    elif count_list[0] == 5:
        if count_list[1]:
            print(f'일치하는 개수: {count_list[0]} + 보너스 넘버, 2등')
        else:
            print(f'일치하는 개수: {count_list[0]}, 3등')
    elif count_list[0] == 4:
        print(f'일치하는 개수: {count_list[0]}, 4등')
    elif count_list[0] == 3:
        print(f'일치하는 개수: {count_list[0]}, 5등')
    else:
        print(f'일치하는 개수 3개 이하 꽝 !')


# 로또 당첨 번호
winningNumbers = getWinningLottoNumbersList()
bonusNumber = getBonusNumber()
print(f'로또 당첨 번호: {winningNumbers}')
print(f'보너스 번호: {bonusNumber}')

# 사용자가 구매한 번호

for i in range(0, 5):
    print(f'{alpha_index[i]}  자 동 ', end=' ')
    userNumbers = getUserLottoNumbersList()
    for number in userNumbers:
        print(number, end='  ')
    getRank(compare_lotto_numbers(userNumbers, winningNumbers, bonusNumber))
    matchedNumbersList = getMatchNumbers(userNumbers, winningNumbers, bonusNumber)
    if not matchedNumbersList:
        print('당첨 번호가 하나도 없습니다.')
    else:
        print(f'당첨 번호 : ', end=' ')
        for number in matchedNumbersList:
            if number == bonusNumber:
                print(f', 보너스 넘버 {number}', end=' ')
            else:
                print(f'{number}', end=' ')
    print()






