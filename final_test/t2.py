def select_even_odd(msg, *arg):
    result = [msg]
    for num in arg:
        if msg == 'even':
            if num%2==0:
                result.append(num)
        else:
            if num%2==1:
                result.append(num)
    return result

print(select_even_odd('odd', 1, 2, 3, 4))
print(select_even_odd('even', 2, 4, 81, 99, 58, 20))
# *args 가변 인자를 위한 변수(인자의 개수가 변할 수 있음, 유동적으로 임의의 개수의 인자를 전달 할 수 있음)
# **kwargs 임의의 개수의 키워드 인수(keyword argements), 유동적으로 임의의 개수의 키워드 인수를 받아 "딕셔너리" 형태로 저장
def my_book_report(**kwargs):
    total = 0
    print('가계부 내역 출력:')
    for key in kwargs.keys():
        print(f'항목 {key}: 금액 {kwargs[key]}원')
        total += kwargs[key]
    else:
        print(f'총액은 {total}원 입니다.')

my_book_report(점심=10000, 커피=3000, 저녁=12000)
my_dict = {'점심':10000, '커피': 3000, '저녁': 12000}
my_book_report(**my_dict)