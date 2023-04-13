# problem1 김승범 60181869

spring = [4, 5]
summer = [6, 7, 8]
autumn = [9, 10]
winter = [11, 12, 1, 2, 3]

month = int(input("월 입력? "))

if month in spring :
    print("%d월 봄" % month)
elif month in summer :
    print("%d월 여름" % month)
elif month in autumn :
    print("%d월 가을" % month)
else:
    print("%d월 겨울" % month)