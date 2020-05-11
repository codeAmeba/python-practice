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

# returns
