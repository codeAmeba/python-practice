# data types
a_string = "Hi there"
a_number = 3
a_float = 3.14
a_boolean = True
a_none = None

# python에서는 기본적으로 snake case를 사용함 ex) snake_case_variable
# type -> JS에서 type of와 같은 메서드
print(type(a_float))

# list -> mutable
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
print(type(days))
print(days[3])
print("Mon" in days)
print(len(days))

days.reverse()
print(days)

# tuple -> immutable
new_days = ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun")
print(type(new_days))

# dict -> JS에서의 object와 유사
robot = {
    "name": "coderoid",
    "serial_number": 1543,
    "fuel": ["electric", "gas", "disel"]
}

robot["author"] = "Sooyoung"
print(robot)

# function -> 내장 함수가 많음, 문서 읽어볼 것
print("Hello world!")
print(len("abcdefg"))

# custom function
def say_hello():
	print("hello")
	print("bye")

say_hello()

# fuction arguments
