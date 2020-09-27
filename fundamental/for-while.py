# for
for waiting_no in [0, 1, 2, 3, 4]:
    print("대기번호 : {0}".format(waiting_no))

for waiting_no2 in range(1, 6):
    print("대기번호 : {0}".format(waiting_no2))

starbucks_guest = ["ironman", "thor", "groot", "hulk"]

for guest in starbucks_guest:
    print("{0}'s drink is here".format(guest))

# while
customer = "Thor"
index = 5
while index >= 5:
    print("{0}'s drink is here. remain number is {1}".format(customer, index))
    index -= 1
    if index == 0:
        print("your drink is out")

customer = "Ironman"
person = "unknown"

while person != customer:
    print("{0}, coffee is here".format(customer))
    person = input("what is your name? ")
