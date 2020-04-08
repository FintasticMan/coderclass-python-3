numbers = {"zero":10, "one":20}
print(numbers)

numbers["two"] = 30
print(numbers)

del numbers["one"]
print(numbers)

for i in numbers:
    print(i)
    print(numbers[i])
if input("What do you want to check? ") in numbers:
    print("Yeah, it's in there")
else:
    print("Nope, you're just a dunce")

dicOne = {"epic":"gamer"}
dicTwo = {"super":"EPICNESS"}
dicThree = {"wow":"now that's epic"}
dicFour = {}
for i in dicOne:
    dicFour[i] = dicOne[i]
for i in dicTwo:
    dicFour[i] = dicTwo[i]
for i in dicThree:
    dicFour[i] = dicThree[i]
print(dicFour)

dicFive = {}
for i in range(int(input("How many times do you want to do it"))):
    dicFive[i] = i ** 2
print(dicFive)
