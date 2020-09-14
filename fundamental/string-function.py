sentence3 = """
I am a boy,
Hello World!
"""
print(sentence3)

phone_number = '010-2684-0242'
print(phone_number[-1])
print(phone_number[9:])
print(phone_number[:3])
print(phone_number[4:8])
print(phone_number[-9:])

python = 'Python is Amazing'
print(python.lower())
print(python.upper())
print(python[0].isupper())
print(len(python))
print(python.replace('Python', 'JavaScript'))

index = python.index('n')
print(index)

index = python.index('n', index + 1)
print(index)

print(python.find('n'))  # find에서는 원하는 값이 없으면 -1을 출력하지만, index에서는 에러

print(python.count('n'))
