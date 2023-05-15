# section_043.py

# 사전에서 값 가져오기
# 사전에 해당 키가 없으면 오류 발생 ex) my_idol['name']
# get() 메서드를 이용 ex) my_idol.get('name'), 오류 발생 x
# 가변객체 : 사전은 가변객체이기 때문에 새로운 항목을 언제든 추가할 수 있다.
# 키에 연결된 값 수정도 가능

my_idol = {"name" : "쯔위", "age" : 18, "job" : "singer"}
print(my_idol['name'])
print(my_idol.get('age'))
print(my_idol.get('birth'))
print()

my_idol['name'] = '수지'
print(my_idol)
print()

my_idol['birth'] = '1994-10-10'
my_idol['manager'] = 'JYP'
print(my_idol)