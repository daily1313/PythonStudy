# Python's Naming Rule(네이밍 규칙)(변수, 상수, 함수, 클래스 등의 이름에 권장되는 규칙)
# 메서드명(소문자 + 밑줄(의미 단위로 밑줄 나누기))
# 변수명(소문자 + 밑줄(의미 단위로 밑줄 나누기))
# 전역 변수명(g + 밑줄 + 변수명)
# 상수명(모두 대문자로 사용)

import random

LOTTO_FIRST_NUMBER = 1
LOTTO_LAST_NUMBER = 45
ONE_LOTTO_LENGTH = 6
ALPHA_INDEX = ['A', 'B', 'C', 'D', 'E']
GAME_START_MESSAGE = '로또 게임을 시작합니다.'
INVALID_COMMAND_MESSAGE = '잘못된 명령을 입력하였습니다.'
GAME_OVER_MESSAGE = '게임을 종료합니다.'
MESSAGE_ASKING_IF_YOU_WANT_TO_START_THE_GAME = '로또 게임을 시작하시겠습니까 ? (y/n)'
MESSAGE_ASKING_IF_YOU_WANT_TO_RESTART_THE_GAME = '로또 게임을 다시 진행하실건가요 ? (c/q)'
NUMBER_OF_LOTTO_TICKETS_TO_BUY = '구매할 로또 장 수: '


def get_winning_lotto_numbers_list():
    winning_numbers_list = set()
    while len(winning_numbers_list) < ONE_LOTTO_LENGTH:
        winning_numbers_list.add(random.randint(LOTTO_FIRST_NUMBER, LOTTO_LAST_NUMBER))
    return sorted(winning_numbers_list)


def get_user_lotto_numbers_list():
    user_lotto_numbers_list = set()
    while len(user_lotto_numbers_list) < ONE_LOTTO_LENGTH:
        user_lotto_numbers_list.add(random.randint(1, 45))
    return sorted(user_lotto_numbers_list)


def print_user_lotto_numbers_list(user_lotto_numbers_list):
    for number in user_lotto_numbers_list:
        print(number, end='  ')


def get_bonus_number():
    return random.randint(LOTTO_FIRST_NUMBER, LOTTO_LAST_NUMBER)


def compare_lotto_numbers(user_lotto_numbers, winning_numbers, bonus_number):
    count = 0
    bonus_count = 0

    for number in user_lotto_numbers:
        if number in winning_numbers:
            count += 1

    if bonus_number in user_lotto_numbers:
        bonus_count += 1

    return [count, bonus_count]


def get_matching_numbers(user_lotto_numbers, winning_numbers, bonus_number):
    matching_numbers_list = []
    for number in user_lotto_numbers:
        if number in winning_numbers:
            matching_numbers_list.append(number)

    if bonus_number in user_lotto_numbers:
        matching_numbers_list.append(bonus_number)
    return matching_numbers_list


def print_matching_numbers(match_numbers_list):
    if not match_numbers_list:
        print('당첨 번호가 하나도 없습니다.', end=' ')
    else:
        print(f'당첨 번호 : ', end=' ')
        for number in match_numbers_list:
            if number == bonus_number:
                print(f', 보너스 넘버 {number}', end=' ')
            else:
                print(f'{number}', end=' ')


def print_rank(count_list):
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


def ask_whether_to_play_a_game():
    return input(f'{MESSAGE_ASKING_IF_YOU_WANT_TO_START_THE_GAME}')


def ask_whether_to_continue_playing_a_game():
    return input(f'{MESSAGE_ASKING_IF_YOU_WANT_TO_RESTART_THE_GAME}')


def ask_how_many_lotto_tickets_to_buy():
    return int(input(f'{NUMBER_OF_LOTTO_TICKETS_TO_BUY}'))


print(f'{GAME_START_MESSAGE}')
while True:
    command = ask_whether_to_play_a_game()
    if command == 'y':
        user_buying_lotto_ticket_count = ask_how_many_lotto_tickets_to_buy()
        # 로또 당첨 번호
        winning_lotto_numbers_list = get_winning_lotto_numbers_list()
        bonus_number = get_bonus_number()

        for j in range(0, user_buying_lotto_ticket_count):
            # 사용자가 구매한 번호
            for i in range(0, 5):
                print(f'{ALPHA_INDEX[i]}  자 동 ', end=' ')
                user_lotto_numbers_list = get_user_lotto_numbers_list()
                print_user_lotto_numbers_list(user_lotto_numbers_list)
                print_rank(compare_lotto_numbers(user_lotto_numbers_list, winning_lotto_numbers_list, bonus_number))
                match_numbers_list = get_matching_numbers(user_lotto_numbers_list, winning_lotto_numbers_list, bonus_number)
                print_matching_numbers(match_numbers_list)
                print()

        print(f'로또 당첨 번호: {winning_lotto_numbers_list}')
        print(f'보너스 번호: {bonus_number}')

        restart_game_option = ask_whether_to_continue_playing_a_game()
        if restart_game_option == 'c':
            continue
        elif restart_game_option == 'q':
            break
        else:
            print(f'{INVALID_COMMAND_MESSAGE}')
    elif command == 'n':
        break
    else:
        print(f'{INVALID_COMMAND_MESSAGE}')

print(f'{GAME_OVER_MESSAGE}')


