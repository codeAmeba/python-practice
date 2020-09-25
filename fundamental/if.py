weather = input("What's the weather like today?")

if weather == "rainy" or weather == "snowy":
    print("take a umbrella")
elif weather == "dust":
    print("take a mask")
else:
    print("nice weather!")


temp = int(input("What's the temperature today?"))

if 30 <= temp:
    print("so hot")
elif 10 <= temp and temp < 30:
    print("not bad")
elif 0 <= temp and temp < 10:
    print("It's a little cold")
else:
    print("so cold. Don't go anywhere")
