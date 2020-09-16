# 방법 1
print("I am %d years old" % 33)  # 정수
print("I like %s" % "cats")  # 문자열
print("Apple is start with %c" % "A")  # 한 문자
print("My favorite color is %s and %s" % ("blue", "red"))

# 방법 2
print("I am {} tears old".format(33))
print("My favorite color is {} and {}".format("blue", "red"))
print("My favorite color is {1} and {0}".format("blue", "red"))  # 순서

# 방법 3
print("I am {age} years old and my favorite color is {color}".format(
    age=33, color="blue"))

# 방법 4 (v3.6 이상)
age = 33
color = "blue"
print(f"I am {age} years old and my favorite color is {color}")
