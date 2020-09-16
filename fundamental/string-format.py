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

# escape
print("Hello\nWorld")  # 줄바꿈
print("Hello \"world\"")  # 따옴표 출력
print("usr\\local\\mysql")  # path 출력
print("Red Apple\rPine")  # 커서를 맨 앞으로 이동
print("Redd\bApple")  # 한 글자 삭제
print("Red\tApple")  # tab

# Quiz: 사이트별로 비밀번호를 만들어주는 프로그램 작성
# 예) http://naver.com
# 규칙1. http:// 부분은 제외 -> naver.com
# 규칙2. 처음 만나는 점(.) 이후 부분은 제외 -> naver
# 규칙3. 남은 글자 중 첫 세자리 + 글자 갯수 + 글자 내 e 갯수 + ! -> nav51!

url = "http://codeameba.netlify.app"
# removeHttp = url[7:]
removeHttp = url.replace("http://", "")
removeAfterFirstDot = removeHttp[:removeHttp.find('.')]
makePassword = f"{removeAfterFirstDot[:3]}{len(removeAfterFirstDot)}{removeAfterFirstDot.count('e')}!"
print(makePassword)  # cod92!
