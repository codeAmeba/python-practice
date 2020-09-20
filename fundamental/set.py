# set(집합): 중복이 없고, 순서가 없음
my_set = {1, 2, 3, 3, 3}
print(my_set)  # {1, 2, 3} -> 중복값 자동 제거

# 교집합 출력
fruits_box_1 = {"apple", "peach"}
fruits_box_2 = set(["grape", "melon", "apple"])

print(fruits_box_1 & fruits_box_2)  # {'apple'}
print(fruits_box_1.intersection(fruits_box_2))  # {'apple'}

# 합집합 출력
print(fruits_box_1 | fruits_box_2)  # {'apple', 'grape', 'melon', 'peach'}
print(fruits_box_1.union(fruits_box_2))  # {'apple', 'grape', 'melon', 'peach'}

# 차집합
print(fruits_box_1 - fruits_box_2)  # {'peach'}
print(fruits_box_1.difference(fruits_box_2))  # {'peach'}

fruits_box_2.add("blueberry")
print(fruits_box_2)

fruits_box_2.remove("melon")
print(fruits_box_2)
