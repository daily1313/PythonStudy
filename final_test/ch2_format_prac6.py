# format 실습

print('햄버거를 만들어보자.')

basemat = ('빵', '토마토', '야채', '소스')
coremat = ('새우', '불고기', '한우', '치즈')

food = '햄버거'

for item in coremat:
    print(f'핵심재료가 {item}이면 {item}버거')
print()

print('체질량지수(BMI)를 계산해 보아요')

weight, height = input('체중과 키를 입력하세요: ').split()
weight = int(weight)
height = float(height)

bmi = weight/(height*height)

print(f"BMI는 {bmi:.2f}이다.")