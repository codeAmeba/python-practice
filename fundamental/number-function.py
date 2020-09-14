from math import *
from random import *

print(abs(-5))
print(pow(4, 2))
print(max(5, 12))
print(min(4, 14))
print(round(3.14))
print(round(3.98))

print(floor(4.56))
print(ceil(3.14))
print(sqrt(9))

print(random())
print(floor(random() * 100))
print(int(random() * 10) + 1)  # 1 ~ 10
print(int(random() * 45) + 1)  # 1 ~ 45
print(randrange(1, 46))  # 1 ~ 45
print(randint(1, 45))  # 1 ~ 45


# QUIZ: 월 4회 스터디 중 3회는 온라인 1회는 오프라인
# 조건1. 랜덤으로 날짜 뽑기
# 조건2. 월별 날짜가 다르므로 최소 일수인 28일 이내로 한정
# 조건3. 매월 1~3일은 준비기간이므로 제외
# 출력문: 오프라인 스터디 모임 날짜는 매월 X 일로 선정되었습니다.

off_study_day = randint(4, 28)

print('오프라인 스터디 모임 날짜는 매월 ' + str(off_study_day) + ' 일로 선정되었습니다.')
