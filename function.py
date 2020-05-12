# function -> 내장 함수가 많음, 문서 읽어볼 것
print("Hello world!")
print(len("abcdefg"))

# custom function
def say_hello(who):
    print("hello", who)
    print("bye", who)

say_hello("Sooyoung")


def plus(a, b):
    print(a + b)

# default value
def minus(a, b=3):
    print(a - b)

plus(3, 5)
minus(5)

# return
# return하면 함수는 값을 내놓고 종료되며 return 아래의 코드는 실행되지 않음 -> JS와 동일
def p_plus(a, b):
  print(a + b)

def r_plus(a, b):
  return a + b

# p_result = p_plus(3, 6)
r_result = r_plus(3, 6)

# print(p_result) # 9 None -> return이 없으므로 print를 두 번 실행, 그래서 두 번째 print는 None
print(r_result) # 9

# keyworded arguments
# 순서에 상관없이 인수를 지정해줌
def introduce_yourself(name, age):
  return f"Hello my name is {name}, I'm {age} years old"

introduce = introduce_yourself(name="Sooyoung", age="32")
print(introduce)

