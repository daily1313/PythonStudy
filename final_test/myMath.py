def calculate_sum(start, end):
    return sum(range(start, end+1))

def calculate_product(start, end):
    result = 1
    for i in range(start, end+1):
        result *= i
    return result

if __name__ == "__main__":
    print('myMath 모듈의 간단한 테스트를 모듈 내에서 실행합니다.')
    result_sum = calculate_sum(1, 5)
    result_product = calculate_product(1, 5)
    print(f'1부터 5까지의 합: {result_sum}')
    print(f'1부터 5까지의 곱: {result_product}')