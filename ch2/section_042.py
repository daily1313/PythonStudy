# section_042.py

# 파이썬의 사전은 독특하고 재밌는 자료형, 간단하게 국어사전, 영어사전과 같은 개념
# Key-Value 형식
# 중괄호 {} 를 사용, 항목들이 키:값 형태로 되어있고, 인덱싱, 슬라이싱은 불가능하다(순서가 없기 때문에)
# 키는 중복될 수 없고, 불변객체만 사용할 수 있다.
# dict()함수 : 괄호 안의 자료를 사전형으로 변경해준다. dict([(1,'서울'),(2,'부산')])
# 직접적으로 key값에 접근하여 value값을 불러올 수 있다.

my_dict = {}
my_dict = {1 : "수소", 2: "헬륨", 2: "리튬", 3: "리튬"}
print(my_dict)

my_dict = {"name" : "mr.Kang", 14003 : [3,2,0,1]}
my_dict = dict([(1, '서울'), (2, '부산')])
print(my_dict)

my_exo = {"name" : "찬열", "age" : 25, "manager" : "SM", "job" : "singer"}
print(my_exo)
print(type(my_exo))