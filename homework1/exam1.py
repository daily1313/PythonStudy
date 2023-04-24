
my_memo = ['운동하기', '영화 보기', '쇼핑하기']

print("파이썬 중간고사 제 이름은 김승범 학번은 60181869 입니다")

i = 0

while True :
    print('='*20)
    cmd = input('명령을 입력하세요>> ')
    c_list = cmd.split(' ')
    if cmd == '종료' :
        break
    elif cmd == '전체 출력' :
        for n in my_memo :
            print(n)
    elif c_list[0] == ['메모'] and c_list[1] == ['추가'] :
        my_memo.append(cmd[6:])
        print(my_memo)
    elif c_list[0] == '메모' and c_list[2] == '보여줘' :
        if c_list[1][-1] == '번' :
            if c_list[1][:-1].isdigit() :
                num = int(c_list[1][:-1])
                print(my_memo[num])
    elif c_list[0] == '메모' and c_list[2] == '삭제' :
        if c_list[1][-1] == '번' :
            if c_list[1][:-1].isdigit():
                num = int(c_list[1][:-1])
                my_memo.remove(my_memo[num])
                print(my_memo)
print('프로그램을 종료합니다')






