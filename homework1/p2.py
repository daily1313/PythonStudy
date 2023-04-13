# problem2 김승범 60181869

n = int(input("소수(prime number)인지를 판별하는 2이상의 정수 입력 >> "))

if n < 2 :
    print("2 이상의 정수를 입력해주세요.")
elif n == 2 :
    print("2는 소수입니다.")
else :
    for i in range(2, n) :
        if n % i == 0 :
            print("정수 %d는 소수가 아닙니다." % n)
            break
    else:
        print("정수 %d는 소수입니다." % n)

