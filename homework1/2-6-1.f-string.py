ingredients = ('빵', '토마토', '야채', '소스')
coremat = ('새우', '불고기', '한우', '치즈')


print('햄버거를 만들어보자.')
print(f'''햄버거의 기본재료는 {ingredients}이고, 
핵심재료에 따라 이름이 달라져.''')
print()
for item in coremat :
    print(f'핵심재료가 {item}면 {item}버거')