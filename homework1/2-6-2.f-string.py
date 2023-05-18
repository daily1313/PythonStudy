weight = 68
height = 1.75

bmi = weight / (height * height)

print('체질량지수(BMI)를 계산해 보아요')
print(f'체중과 키를 입력하세요: {weight} {height}')
print(f'BMI는 {weight}/({height}*{height})이므로 {bmi:.2f}이다.')