# 자료구조의 변경
from random import *
menu = {"coffee", "milk", "juice"}
print(menu, type(menu))  # {'coffee', 'milk', 'juice'} <class 'set'>

menu = list(menu)
print(menu, type(menu))  # ['coffee', 'milk', 'juice'] <class 'list'>

menu = tuple(menu)
print(menu, type(menu))  # ('coffee', 'milk', 'juice') <class 'tuple'>

menu = set(menu)
print(menu, type(menu))  # {'coffee', 'milk', 'juice'} <class 'set'>

# Quiz: 랜덤으로 1명은 치킨, 3명은 커피를 받는 추첨 프로그램을 작성하시오
# 조건1. 편의상 댓글은 20명이 작성하였고 아이디는 1~20으로 가정
# 조건2. 댓글 내용과 상관 없이 무작위로 추첨하되 중복 불가
# 조건3. random 모듈의 shuffle과 sample을 활용
# 출력 예시
# 치킨 당첨자: 1
# 커피 당첨자: [2, 3, 4]

users = range(1, 21)
# print(type(users))
users = list(users)
# print(type(users))
print(users)

shuffle(users)
print(users)

winners = sample(users, 4)
print("치킨 당첨자: {0}".format(winners[0]))
print("커피 당첨자: {0}".format(winners[1:]))
