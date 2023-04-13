
import math

print("ax^2 + bx + c = 0 (a!=0)의 근은")
print("x = (-b+/-sqrt(b^2-4ac))/2a (단, b^2-4ac >=0)")
print()

a, b, c = 3, -6, -2

# a, b, c = 3, 1, 2

tested_condition = b**2 - 4*a*c

if tested_condition >= 0 :
    x1 = (-b + math.sqrt(tested_condition)) / (2*a)
    x2 = (-b - math.sqrt(tested_condition)) / (2*a)

    print("x의 값은", x1, "와", x2, "이다")

    x = 2.290994448735806

    print("x 가 2.290994448735806 일때, 방정식의 값을 계산하면", a*x**2+b*x+c, "이다")
    print("그러므로", x, "는 올바른 근이다")

else :
    print("근의 공식을 적용할 수 없음")