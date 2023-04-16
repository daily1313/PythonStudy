# section_023.py

# 슬라이싱 [시작위치 : 끝위치] -> 주의 사항 끝 위치의 문자는 포함 x
# 끝위치, 시작위치 생략하면 마지막 문자, 첫 문자 부터 추출

string = "NATURE"
print("-" * 5 + "정방향" + "-" * 5)
print(string[0:5])
print(string[2:4])
print(string[2:])
print(string[:3])

print("-" * 5 + "역방향" + "-" * 5)
print(string[-4:-2])
print(string[-6:])
print(string[:-3])


