scores = []
students = {}
def compute_score(**kwargs):
    if not kwargs:
        print('성적 정보가 없습니다.')
        return

    for name, score in kwargs.items():
        print(f'{name}: {score}')
        scores.append(score)
    total_score = sum(scores)
    average_score = total_score / len(scores)
    max_score = max(scores)
    min_score = min(scores)

    print(f'총점: {total_score}')
    print(f'평균: {average_score}')

    for name, score in kwargs.items():
        if score == max_score:
            print(f'최고점자: {name} ({score}점)')
        if score == min_score:
            print(f'최하점자: {name} ({score}점)')

while True:
    opt = input('메뉴: 1=입력 2=성적산출 q=종료 >> ')

    if opt == '1':
        while True:
            data = input('성적을 입력하세요 (이름=점수): ')
            if data == '.':
                print('성적이 입력되었습니다.')
                break
            name, score = data.split('=')
            students[name] = int(score)
    elif opt == '2':
        compute_score(**students)
    elif opt == 'q':
        print('프로그램을 종료합니다')
        break
    else:
        print('올바른 메뉴를 선택해주세요')