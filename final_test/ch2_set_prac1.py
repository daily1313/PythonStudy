
days = {'월','화','수','목','금','토','일'}
weekend = {'토','일'}

weekday = set() # 빈 집합
weekday = days - weekend

for day in weekday:
    print(day, '요일이 weekday에 추가됩니다')

print('일주일은', days)
print('주말은', weekend)
print('평일은', weekday)