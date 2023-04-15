
print("*"*50)

str1 = "Hello, my princess. Are you hungry?"
print(str1.upper())
print(str1.lower())
print(str1.title())
print()

print(str1.count('r'))
print(str1.endswith('?'))
print(str1.startswith('h'))
print(str1.lower().startswith('h'))
print()

str2 = str1.split()
print(str2)

str2 = str1.split(',')
print(str2)

str2 = str1.split('.')
print(str2)
print()

print(len(str1))
print(str1.zfill(50))
print()