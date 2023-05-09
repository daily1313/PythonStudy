
subjects_and_scores_list = [['부동산학개론', 55],['민법', 35],['공법', 40], ['공시법', 70],['세법', 65],['중개사법', 30]]
falling_count = 0
total_score = 0

for i in range(len(subjects_and_scores_list)):
    total_score += subjects_and_scores_list[i][1]
    if subjects_and_scores_list[i][1] < 40:
        falling_count += 1


average_score = total_score / len(subjects_and_scores_list)

if falling_count >= 1 :
    print('40점 미만 과목 수 :',falling_count)
    print('평균 점수 :',average_score)
    print('아쉽습니다. 불합격하셨습니다.')
else:
    print('평균 점수 :', average_score)
    print('축하드립니다. 합격하였습니다.')