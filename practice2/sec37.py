# section_037.py
# 집합
# 중괄호 {}를 이용해서 항목을 묶는다
# 파이썬에서 set이라는 이름을 가짐
# 다양한 종류의 자료형을 담을 수 있지만, 가변 객체(리스트)는 담지 못한다
# 중복이 없다
# 순서가 없기 때문에, 인덱싱, 슬라이싱이 안된다
# 빈 집합 내장 함수인 set() 함수를 이용해서 만든다.

my_set = {1,2,3}
print(my_set)
print(type(my_set))

my_set = {"hello",1.0, (1,2,3)}
print(my_set)

my_set = {}
print(type(my_set))
my_set = set()
print(type(my_set))