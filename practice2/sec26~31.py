
# sec 26
numbers = [0,1,2,3,4,5]
animals = ['개','고양이','토끼','다람쥐']

print(numbers)
print(animals)

print(numbers[0])
print(animals[2])
print(animals[-2])

# sec 27
animals[2] = '거북이'
print(animals)

zoo = animals + ['토끼']
print(zoo)
print(animals)
print()

# sec 28
zoo = animals[1:3]
print(zoo)

print(animals)
print(animals[0:4])
print()

# sec 29
print("거북이의 위치: ", animals.index('거북이'))
print("다람쥐의 위치: ", animals.index('다람쥐'))

animals.append('원숭이')
print(animals)

animals.insert(3, '펭귄')
print(animals)

numbers.extend([6, 7, 8])
print(numbers)
print()

# sec 30

numbers.sort()
animals.sort()
print(numbers)
print(animals)

numbers.reverse()
print(numbers)

numbers2 = [4, 1, 3, 7, -2]
numbers2.reverse()
print(numbers)

my_animal = animals.pop()
print(my_animal)

numbers.remove(4)
print(numbers)

animals.insert(2, '펭귄')
animals.append('펭귄')
print(animals.count('펭귄'))
print(animals)
print(numbers)
print()

# sec 31

print(len(numbers))
print(len(animals))
print()

print(max(numbers))
print(max(animals))
print()

print(min(numbers))
print(min(animals))

print(sum(numbers))
print()

print(sorted(numbers))
print(numbers)
print()

print(list("Hello Python"))

