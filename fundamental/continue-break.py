absent = [2, 5]
no_book = [7]
for student in range(1, 11):
    if student in absent:
        continue  # absent를 만나면 다음으로 넘어감
    elif student in no_book:
        print("{0}, out".format(student))
        break  # no_book을 만나면 끝
    print("{0}, pick".format(student))
