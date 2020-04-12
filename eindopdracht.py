#!/usr/bin/env python3

def menu():
    print("So, this place is called a 'menu' and this is where you choose what you want to do!\nThe things you can do are:\n Test whether a number is prime [t];\n Continuously list primes until you press q or esc [c];\n List primes in a certain range [l];\n Load previously generated primes from file [f]\n\n And, if you REALLY want to, you can also quit [q].\n")
    wotIWantToDo = input(" What do you want to do? [t/c/l/f/Q] ")
    return wotIWantToDo

def main():
    keepGoing = True
    print("Welcome to the Prime Mansion! Here you can do a bunch of things with primes! (If you haven't picked it up already, I like prime numbers)\n")
    while keepGoing:
        wotIWantToDo = menu()
        if wotIWantToDo == "t":
            if primeChecker(int(input("\nWhich positive integer would you like to test? "))):
                print("\nThat IS a prime!\n")
            else:
                print("\nNope, not a prime. Sorry.\n")
        elif wotIWantToDo == "c":
            infPrimeLister()
        elif wotIWantToDo == "l":
            rangePrimeLister(int(input("\nAt what point would you like the listed primes to start? ")), int(input("And at what point would you like them to end? ")))
        elif wotIWantToDo == "f":
            loadFromFile
        elif wotIWantToDo == "q" or wotIWantToDo == "":
            print("\nBye bye!")
            keepGoing = False
        else:
            print("\nI think you messed up and typed something in wrong. Do better next time!\n")

def primeChecker(intPotPrime):
    isPrime = True
    i = 2
    if intPotPrime == 1:
        isPrime = False
    else:
        while isPrime and i <= intPotPrime / 2:
            if intPotPrime % i == 0:
                isPrime = False
            else:
                i += 1
    return isPrime
def infPrimeLister():
    keepGoing = True
    listPrimes = []
    intPotPrime = 2
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
    wantToSave = input("\nDo you want to save these primes to a file for future convenience? [Y/n] ")
    print("\nUnder construction\n")

def rangePrimeLister(intStart, intEnd):
    listPrimes = [2]
    for intPotPrime in range(3, intEnd + 1):
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
    startPrint = 0
    while listPrimes[startPrint] < intStart:
        startPrint += 1
    for i in range(startPrint, len(listPrimes)):
        print(listPrimes[i])
    wantToSave = input("\nDo you want to save these primes to a file for future convenience? [Y/n] ")
    print("\nUnder construction\n")

def loadFromFile:
    print("\nUnder construction\n")

main()
