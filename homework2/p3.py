# problem3 김승범 60181869

korean = ['정렬', '초보자', '내포', '사전']
english = ['sorting', 'novice', 'comprehension', 'dictionary']

word = input("찾을 단어 입력? ")

if word in korean:
    index = korean.index(word)
    print(english[index])
else:
    print("사전에 없는 단어입니다.")