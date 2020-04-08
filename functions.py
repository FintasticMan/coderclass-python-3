def helloWorld(times):
    for i in range(times):
        print("Hello World!")
helloWorld(10)

def fiveTimesTable(times):
    for i in range(1, times + 1):
        print(5 * i)
fiveTimesTable(10)

def printStr(str, times):
    for i in range(times):
        print(str)
printStr("Hi, silly", 15)

listKerstboomThing = []
def halveKerstboom(str):
    listKerstboomThing = list(str)
    for i in range(len(listKerstboomThing)):
        print(listKerstboomThing[i] * (i + 1))
halveKerstboom("hello")

def maxOfThree(intOne, intTwo, intThree):
    if intOne > intTwo and intOne > intThree:
        return intOne
    elif intTwo > intOne and intTwo > intThree:
        return intTwo
    else:
        return intThree
print(maxOfThree(1, 2, 3))

def reverseString(str):
    listReverse = list(str)
    strReverse = listReverse[0]
    for i in range(1, len(listReverse)):
        strReverse = listReverse[i] + strReverse
    return strReverse
print(reverseString("olleH"))

def isPrime(int):
    partialPrime = "True"
    i = 2
    while partialPrime == "True" and i <= int / 2:
        if int % i == 0:
            partialPrime = "False"
        else:
            i = i + 1
    if partialPrime == "False":
        return "False"
    else:
        return "True"
number = 97
if isPrime(number) == "True":
    print(str(number) + " is prime!")
else:
    print(str(number) + " is not prime!")

def isPalindrome(str):
    if str == reverseString(str):
        return "True"
    else:
        return "False"
string = "yeey"
if isPalindrome(string) == "True":
    print(string + " is a palindrome!")
else:
    print(string + " is not a palindrome!")

def reverseList(list):
    listReverse = []
    for i in range(len(list)):
        listReverse.append(list[len(list) - (i + 1)])
    return listReverse
print(reverseList(["silly", "billy"]))

def myLen(list):
    length = 0
    while True:
        try:
            a = list[length]
        except:
            return length
        length += 1
print(myLen(["hello", "there"]))

def appenderer(list, value):
    list.append(value)
    return list
print(appenderer(["super"], "gamer"))

def secondPlace(list, value):
    if len(list) == 1:
        list.append(value)
        return list
    else:
        listSecondPlace = []
        listSecondPlace.append(list[0])
        listSecondPlace.append(value)
        for i in range(1, len(list)):
            listSecondPlace.append(list[i])
        list[1] = value
        return listSecondPlace
print(secondPlace(["yeet", "all", "of", "them"], "not"))

def removeLast(list):
    del list[len(list) - 1]
    return list
print(removeLast(["super", "gamerness"]))

def removeItem(list, value):
    for i in range(len(list)):
        if list[i] == value:
            del list[i]
    return list
print(removeItem(["hi", "people"], "people"))

def dictionaryMakerSquare(int):
    dicSquare = {}
    for i in range(1, int + 1):
        dicSquare[i] = i ** 2
    return dicSquare
print(dictionaryMakerSquare(7))

# def appearenceChecker(list, value):
