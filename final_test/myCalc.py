def mySum(*args):
    return sum(args)

def myAve(*args):
    return mySum(*args) / len(args)

if __name__ == "__main__":
    print('myCalc 모듈을 직접 실행함')
    result_sum = mySum(1, 2, 3, 4)
    result_avg = myAve(3, 4, 5, 6, 7, 8)
    print(f'합 : {result_sum}')
    print(f'평균 : {result_avg:.2f}')