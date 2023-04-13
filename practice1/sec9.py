
name = input("이름을 입력하세요: ")
age = input("나이를 입력하세요: ")
student_id = input("학번을 입력하세요: ")

input_string = input("이름과 나이와 학번을 입력하세요.")
name_string, age_string, student_id_string = input_string.split(" ")

print("이름", name, "나이", age, "학번", student_id, "입니다")
print("이름", name_string, "나이", age_string, "학번", student_id_string, "입니다")