#!/usr/bin/env python3

# import the necessary modules
import os
import json

# call the different functions depending on the user's choice
def main():
    global listPrimes
    listPrimes = [2]
    keepGoing = True
    print("Welcome to the Prime Mansion! Here you can do a bunch of things with primes! (If you haven't picked it up already, I like prime numbers)\n")
    while keepGoing: # when one function is finished, go back to the menu
        wotIWantToDo = menu()
        if wotIWantToDo == "t":
            if primeChecker(int(input("\nWhich positive integer would you like to test? "))):
                print("\nThat IS a prime!\n")
            else:
                print("\nNope, not a prime. Sorry.\n")
        elif wotIWantToDo == "c":
            infPrimeLister()
        elif wotIWantToDo == "r":
            rangePrimeLister(int(input("\nAt what point would you like the listed primes to start? ")), int(input("And at what point would you like them to end? ")))
        elif wotIWantToDo == "s":
            saveToFile()
        elif wotIWantToDo == "l":
            loadFromFile()
        elif wotIWantToDo == "q" or wotIWantToDo == "":
            print("\nBye bye!")
            keepGoing = False
        else:
            print("\nI think you messed up and typed something in wrong. Do better next time!\n")

# print the menu and return user's decision
def menu():
    print("""So, this place is called a 'menu' and this is where you choose what you want to do!
The things you can do are:
 Test whether a number is prime [t];
 Continuously list primes until you press Ctrl+C [c];
 List primes in a certain range [r];
 Save generated primes to file [s];
 Load previously generated primes from file [l];

 And, if you REALLY want to, you can also quit [q].\n""")
    wotIWantToDo = input(" What do you want to do? [t/c/r/s/l/Q] ")
    return wotIWantToDo

def primeChecker(intPotPrime):
    isPrime = True # assume true unless proven otherwise
    i = 2
    if intPotPrime == 1:
        isPrime = False # one is not a prime even though it is only divisible by itself and 1
    else:
        while isPrime and i <= intPotPrime / 2:
            if intPotPrime % i == 0: # checks if it's divisible by i
                isPrime = False
            else:
                i += 1
    return isPrime

def infPrimeLister():
    global listPrimes
    keepGoing = True
    intPotPrime = listPrimes[-1] + 1
    try:
        for i in listPrimes:
            print(i)
        while keepGoing:
            isPrime = True
            intIndex = 0
            i = listPrimes[intIndex]
            while isPrime and i <= intPotPrime / 2:
                if intPotPrime % i == 0:
                    isPrime = False
                else:
                    intIndex += 1
                    i = listPrimes[intIndex]
            if isPrime:
                listPrimes.append(intPotPrime)
                print(intPotPrime)
            intPotPrime += 1
    except:
        print("\n")

def rangePrimeLister(intStart, intEnd):
    global listPrimes
    for intPotPrime in range(listPrimes[-1] + 1, intEnd + 1):
        isPrime = True
        intIndex = 0
        i = listPrimes[intIndex]
        while isPrime and i <= intPotPrime / 2:
            if intPotPrime % i == 0:
                isPrime = False
            else:
                intIndex += 1
                i = listPrimes[intIndex]
        if isPrime:
            listPrimes.append(intPotPrime)
    for i in listPrimes:
        if intStart < i < intEnd:
            print(i)

def saveToFile():
    print("\nSaving to file...")
    jsonPrimes = json.dumps(listPrimes, indent=4)
    if os.path.exists("primes"):
        filePrimes = open("primes", "rt")
        if len(jsonPrimes) > len(filePrimes.read()):
            filePrimes.close()
            filePrimes = open("primes", "wt")
            filePrimes.write(jsonPrimes)
            print("Saved to file!\n")
        else:
            print("Not saved to file; more primes already in file.\n")
        filePrimes.close()
    else:
        filePrimes = open("primes", "wt")
        filePrimes.write(jsonPrimes)
        filePrimes.close()
        print("Saved to file!\n")

def loadFromFile():
    global listPrimes
    print("\nLoading from file...")
    filePrimes = open("primes", "rt")
    jsonPrimes = json.loads(filePrimes.read())
    if len(listPrimes) < len(jsonPrimes):
        listPrimes = jsonPrimes
        print("Loaded from file!\n")
    else:
        print("Not loaded from file; more primes already loaded.\n")
    filePrimes.close()

main()
