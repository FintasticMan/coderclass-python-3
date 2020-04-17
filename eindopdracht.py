#!/usr/bin/env python3

# import the necessary modules
import os
import json
import time

# call the different functions depending on the user's choice
def main():
    global listPrimes
    global dicPrimes
    listPrimes = [2]
    dicPrimes = {}
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
    global dicPrimes
    keepGoing = True
    intPotPrime = listPrimes[-1] + 1
    try:
        startTime = time.time()
        for i in listPrimes:
            print(i)
        while keepGoing:
            thisPrimeTime = time.time()
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
                dicPrimes[intPotPrime] = [len(dicPrimes) + 1, time.time() - thisPrimeTime, time.time() - startTime]
                print(intPotPrime)
            intPotPrime += 1
    except:
        print("\n")

def rangePrimeLister(intStart, intEnd):
    global listPrimes
    global dicPrimes
    startTime = time.time()
    for intPotPrime in range(listPrimes[-1] + 1, intEnd + 1):
        thisPrimeTime = time.time()
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
            dicPrimes[intPotPrime] = [len(dicPrimes) + 1, time.time() - thisPrimeTime, time.time() - startTime]
    for i in listPrimes:
        if intStart < i < intEnd:
            print(i)

def saveToFile():
    print("\nSaving to file...")
    jsonListPrimes = json.dumps(listPrimes, indent=4)
    jsonDicPrimes = json.dumps(dicPrimes, indent=4)
    if os.path.exists("primes"):
        fileListPrimes = open("primes", "rt")
        if len(jsonListPrimes) > len(fileListPrimes.read()):
            fileListPrimes.close()
            fileListPrimes = open("primes", "wt")
            fileListPrimes.write(jsonListPrimes)
            print("Saved to file!\n")
        else:
            print("Not saved to file; more primes already in file.\n")
        fileListPrimes.close()
    else:
        fileListPrimes = open("primes", "wt")
        fileListPrimes.write(jsonListPrimes)
        fileListPrimes.close()
        print("Saved to file!\n")
    if os.path.exists("primesData"):
        fileDicPrimes = open("primesData", "rt")
        if len(jsonDicPrimes) > len(fileDicPrimes.read()):
            fileDicPrimes.close()
            fileDicPrimes = open("primesData", "wt")
            fileDicPrimes.write(jsonDicPrimes)
            print("Saved to file!\n")
        else:
            print("Not saved to file; more primes already in file.\n")
        fileDicPrimes.close()
    else:
        fileDicPrimes = open("primesData", "wt")
        fileDicPrimes.write(jsonDicPrimes)
        fileDicPrimes.close()
        print("Saved to file!\n")

def loadFromFile():
    global listPrimes
    global dicPrimes
    print("\nLoading from file...")
    fileListPrimes = open("primes", "rt")
    jsonListPrimes = json.loads(fileListPrimes.read())
    fileDicPrimes = open("primesData", "rt")
    jsonDicPrimes = json.loads(fileDicPrimes.read())
    if len(listPrimes) < len(jsonListPrimes):
        listPrimes = jsonListPrimes
        print("Loaded from file!\n")
    else:
        print("Not loaded from file; more primes already loaded.\n")
    if len(dicPrimes) < len(jsonDicPrimes):
        dicPrimes = jsonDicPrimes
        print("Loaded from file!\n")
    else:
        print("Not loaded from file; more primes already loaded.\n")
    fileListPrimes.close()
    fileDicPrimes.close()

main()
