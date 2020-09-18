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

# 피보나치
a, b = 0, 1
while a < 10:
    print(a)
    a, b = b, a+b
