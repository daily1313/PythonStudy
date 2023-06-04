def report(message, job, who='Everyone', message2='Good bye!'):
    print(f'{message} {job} {who} {message2}')

report('Good Morning', 'worker', 'Have a good day')
report('Good Morning', 'student','Mr. Park', 'Have a good day')
report('Good Morning', 'worker', message2='Have a good day')
report('Good Morning', 'student', message2='Have a good day', who='Mr. Park')

def select_even_odd(msg, *args):
    result = []
    if msg == 'odd':
        for x in args:
            if x % 2 != 0:
             result.append(x)
    elif msg == 'even':
        for x in args:
            if x % 2 == 0:
                result.append(x)
    return [msg] + result
print(select_even_odd('odd', 1, 2, 3, 4))
print(select_even_odd('even', -12, 2, 81, 99, 48, 20))

def my_book_report(**kwargs):
    total = 0
    print('가계부 내역 출력: ')
    for key, value in kwargs.items():
        print(f'항목 {key}: 금액 {value}원')
        total += value
    print(f'총액은 {total}원입니다.')

my_book_report(점심=10000, 커피=3000, 저녁=12000)
my_dict = {'점심' : 10000, '커피' : 3000, '저녁' : 12000}
my_book_report(**my_dict)
