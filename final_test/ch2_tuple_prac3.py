
numbers = (0, 1, 2, 3, 4, 5)
animals = ('개','고양이','토끼','다람쥐')

print(numbers)
print(animals)

# numbers의 첫 번째 항목 출력
print(numbers[0])

# animals의 두 번째 항목 출력
print(animals[2])

# animals의 끝에서 두번째 항목 출력
print(animals[-2])

print()

#animals 뒤에 거북이 추가하여 zoo에 저장 출력
zoo = animals + ('거북이',)
print(zoo)
print(animals)
print()

animals = zoo

# animals 1~2번 항목 zoo에 저장 후 출력
zoo = animals[1:3]
print(zoo)

# 슬라이싱 이용해서 animals 전체 출력
print(animals)
print(animals[:])
print(animals[0:4])
print()

print()

# animals에서 '거북이'와 '토끼' 위치 출력(index)

print('토끼의 위치:', animals.index('토끼'))
print('거북이의 위치:', animals.index('거북이'))

# Sec 31 튜플 관련 내장함수
print(len(numbers))
print(len(animals))
print()

# numbers, animals 각 튜플 최대값 출력
print(max(numbers))
print(max(animals))
print()

# numbers, animals 각 튜플 최소값 출력
print(min(numbers))
print(min(animals))
print()

# numbers의 합 출력
print(sum(numbers))
print()

# numbers 오름차순으로 변경한 리스트 출력, numbers2 자체는 불변.(sorted)
numbers2 = (3, 4, -2, 1 ,5)
print(sorted(numbers2))
print(numbers)
print()

# 문자열 "Hello Python"을 튜플로 변경
## print(list("Hello Python"))
print(tuple("Hello Python"))