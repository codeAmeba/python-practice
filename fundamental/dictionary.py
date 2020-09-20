# dictionary: key:value로 이루어진 자료형

robot = {
    "name": "codroid",
    "serial_number": 1543,
    "maker": "Sooyoung Jeong"
}

# 요소 접근
print(robot["maker"])
print(robot.get("name"))
print("name" in robot)

# 요소 추가
robot["date"] = "2020-09-20"
print(robot["date"])

# 요소 변경
robot["name"] = "i-robo"
print(robot["name"])

# key 출력
print(robot.keys())

# value 출력
print(robot.values())

# key:value 쌍으로 출력
print(robot.items())

# 모든 요소 삭제
robot.clear()
print(robot)  # {}
