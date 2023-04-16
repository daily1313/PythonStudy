# section_029.py

colors = ['red', 'orange', 'yellow']
print(colors)

print('red의 위치:', colors.index('red'))
print('orange의 위치:',colors.index('orange'))
print()

colors.append('purple')
print(colors)

colors.insert(3, 'green')
print(colors)
colors.extend(['black', 'white'])
print(colors)