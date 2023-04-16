# section_025.py

myStr = 'Hello, My little baby'
print(myStr.upper()) # 소 -> 대
print(myStr.lower()) # 대 -> 소
print(myStr.title()) # 각 단어에서 첫 문자만 대문자로 변환
print()

print(myStr.count('b'))
print(myStr.endswith('y'))
print(myStr.startswith('h'))
print(myStr.lower().startswith('h'))
print()

myStrlist1 = myStr.split()
print(myStrlist1)
myStrlist2 = myStr.split(',')
print(myStrlist2)
print()

myStrfill = myStr.zfill(30)
print(myStrfill)