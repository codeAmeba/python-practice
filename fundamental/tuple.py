# tuple: 리스트와 달리 데이터 변경이나 추가가 불가능하며 속도가 더 빠르다
fruits = ("apple", "peach", "grape")
print(fruits[0])

# fruits.add("melon") # error

# 한번에 할당하기
name, age, job = "Sooyoung", 33, "Development"
print(name, age, job)
