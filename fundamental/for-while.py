# for
from random import *
for waiting_no in [0, 1, 2, 3, 4]:
    print("대기번호 : {0}".format(waiting_no))

for waiting_no2 in range(1, 6):
    print("대기번호 : {0}".format(waiting_no2))

starbucks_guest = ["ironman", "thor", "groot", "hulk"]

for guest in starbucks_guest:
    print("{0}'s drink is here".format(guest))

# while
customer = "Thor"
index = 5
while index >= 5:
    print("{0}'s drink is here. remain number is {1}".format(customer, index))
    index -= 1
    if index == 0:
        print("your drink is out")

customer = "Ironman"
person = "unknown"

while person != customer:
    print("{0}, coffee is here".format(customer))
    person = input("what is your name? ")


# 한줄 for문
# students = [1, 2, 3, 4, 5]
# students = [i + 100 for i in students]
# print(students)

# students = ["Ironman", "Hulk", "Thor", "Doctor Strange"]
# students = [len(i) for i in students]
# print(students)

students = ["Ironman", "Hulk", "Thor", "Doctor Strange"]
students = [i.upper() for i in students]
print(students)


# QUIZ: 50명의 승객과 매칭 기회가 있을 때, 총 탑승 승객 수를 구하시오
# 조건1. 승객별 운행 소요 시간은 5분 ~ 50분 사이의 난수로 정해짐
# 조건2. 당신은 소요 시간 5분 ~ 15분 사이의 승객만 매칭해야 함
# 출력 예시: [0] 1번째 손님 (소요시간 : 15분)
# ...
# 총 탐승 승객 : 2명

cnt = 0  # 총 탐승 승객 수
for i in range(1, 51):  # 1 ~ 50 승객
    time = randrange(5, 51)  # 5 ~ 50 소요 시간
    if 5 <= time <= 15:
        print("[O] {0} 번째 손님 (소요 시간 : {1} 분)".format(i, time))
        cnt += 1
    else:
        print("[ ] {0} 번째 손님 (소요 시간 : {1} 분)".format(i, time))

print("총 탐승 승객 : {0} 명".format(cnt))
