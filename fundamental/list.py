# list []

fruits = ["apple", "grape", "melon"]
print(fruits)

# len은 리스트에서 사용 가능
print(len(fruits))

# melon은 몇 번째인가?
print(fruits.index('melon'))

# 요소 추가
fruits.append('kiwi')
print(fruits)

# 요소의 위치 설정하여 추가
fruits.insert(1, 'peach')
print(fruits)

# 요소 뒤에서 꺼내기
fruits.pop()
print(fruits)

# 동일한 요소 갯수 확인
nums = [1, 1, 2, 3, 4, 5, 5, 5, 7, 8]
print(nums.count(5))  # 3

# 정렬
randomNums = [5, 1, 16, 2, 25, 4]
randomNums.sort()
print(randomNums)  # [1, 2, 4, 5, 16, 25]

# 순서 역전
randomNums.reverse()
print(randomNums)  # [25, 16, 5, 4, 2, 1]

# 전체 삭제
randomNums.clear()
print(randomNums)

# 다양한 데이터타입 혼용 가능
mixList = ['apple', 30, True]

# 리스트 확장
mixList2 = ['peach', 15, False]
mixList.extend(mixList2)
print(mixList)  # ['apple', 30, True, 'peach', 15, False]

# https://docs.python.org/ko/3.7/tutorial/introduction.html#first-steps-towards-programming
# 피보나치
a, b = 0, 1
while a < 10:
    print(a)
    a, b = b, a+b

# 시퀀스(sequence) 자료형
# 파이썬에서 '시퀀스'는 연속형 자료형을 말한다.
# 대표적으로 튜플(tuple)과 리스트(list), 레인지(range), 문자열(string)이 있다.
# 튜플은 데이터 자체를 수정하지 못 하지만, 리스트는 데이터를 자유롭게 수정할 수 있다는 차이가 있다.
# 시퀀스 데이터는 인덱스를 갖고 있으며, 순회할 수 있다(iterable)
