
import random
import logging
import time
import math

student = {}
now_time = time.localtime()
grade_count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

def main_process():
    return input('1=성적 입력 2=성적 조회 3=전체 성적 출력 4=랜덤 성적 생성 q=종료 >> ')

def input_grade():
    while True:
        name = input('학생 이름: ')
        if name == '.':
            print('성적이 입력되었습니다.')
            break
        grade = int(input('성적: '))
        if grade < 0 and grade > 100:
            logging.error('유효하지 않은 성적입니다.')
        student[name] = [grade, now_time]

def find_grade():
    find_name = input('조회할 학생 이름: ')
    for name in student.keys():
        if find_name == name:
            print(f'{find_name}의 성적은 {student[find_name][0]}입니다. (입력 시간: {student[find_name][1]})')

def view_all_grades():
    print('전체 성적 출력:')
    max_value = -1
    total_score = 0

    for name in student.keys():
        print(f'{name}: 성적 - {student[name][0]}, 입력 시간 - {student[name][1]}')

    for name in student.keys():
        total_score += student[name][0]
        if student[name][0] > max_value:
            max_value = student[name][0]
    print(f'평균 성적: {total_score / len(student)}, 최고 점수: {max_value}, 표준 편차: {calculate_std_dev(**student)}')
    plot_histogram()


def plot_histogram():
    for name in student.keys():
        if student[name][0] >= 0 and student[name][0] <= 9:
            grade_count[0] += 1
        if student[name][0] >= 10 and student[name][0] <= 19:
            grade_count[1] += 1
        if student[name][0] >= 20 and student[name][0] <= 29:
            grade_count[2] += 1
        if student[name][0] >= 30 and student[name][0] <= 39:
            grade_count[3] += 1
        if student[name][0] >= 40 and student[name][0] <= 49:
            grade_count[4] += 1
        if student[name][0] >= 50 and student[name][0] <= 59:
            grade_count[5] += 1
        if student[name][0] >= 60 and student[name][0] <= 69:
            grade_count[6] += 1
        if student[name][0] >= 70 and student[name][0] <= 79:
            grade_count[7] += 1
        if student[name][0] >= 80 and student[name][0] <= 89:
            grade_count[8] += 1
        if student[name][0] >= 90 and student[name][0] <= 100:
            grade_count[9] += 1
    first_number = 0
    last_number = 9

    print('성적 분포:')
    for grade in grade_count:
        if last_number == 99:
            last_number = 100
        print(f'{first_number}- {last_number}:', end='  ')
        for i in range(0, grade):
            print('*', end='')
        print()
        first_number += 10
        last_number += 10

def calculate_std_dev(**student):
    dev_total = 0
    total = 0
    for name in student.keys():
        total += student[name][0]
    average = total / len(student)
    for name in student.keys():
        dev_total += math.sqrt((student[name][0] - average)**2)
    return dev_total / len(student)

def generate_random_grade():
    for i in range(0, 10):
        student['학생' + str(i+1)] = [random.randint(0, 100), now_time]
    print('랜덤한 성적이 생성되었습니다.')


print('성적 관리 프로그램을 시작합니다.')
while True:
    cmd = main_process()
    if cmd == '1':
        input_grade()
    elif cmd == '2':
        find_grade()
    elif cmd == '3':
        view_all_grades()
    elif cmd == '4':
        generate_random_grade()
    elif cmd == 'q':
        print('프로그램을 종료합니다.')
        break
    else:
        print('올바른 명령을 입력해주세요.')