#!/usr/bin/env python3

def menu():
    print("So, this place is called a 'menu' and this is where you choose what you want to do!\nThe things you can do are:\n Kill a unicorn (k);\n Spare the unicorn (s);\n Be an amazing person (a).\n\n And, if you REALLY want to, you can also quit (q).\n")
    wotIWantToDo = input(" What do you want to do? (k/s/a/Q) ")
    print("")
    return wotIWantToDo

def main():
    keepGoing = True
    print("Welcome to the most awesome-est program ever! (It's so awesome, I don't even know what it does yet!)\n")
    while keepGoing:
        wotIWantToDo = menu()
        if wotIWantToDo == "k":
            killUnicorn()
        elif wotIWantToDo == "s":
            spareUnicorn()
        elif wotIWantToDo == "a":
            beAmazing()
        elif wotIWantToDo == "q" or wotIWantToDo == "":
            print("Bye bye!")
            keepGoing = False
        else:
            print("I think you messed up and typed something in wrong. Do better next time!\n")

def killUnicorn():
    print("Killed the unicorn\n")

def spareUnicorn():
    print("Spared the unicorn\n")

def beAmazing():
    print("You're already amazing!\n")

main()

# plans for this project: have 3 functions, a prime checker, a prime lister (that just writes the primes to stdout continuously), and a prime lister (that prints primes between given integers). have 2 files, one that records primes so that on subsequent runs it doesn't have to recalculate, and another one that lists the prime number, how long it took to calculate it (in seconds), and how long is took to calculate all of the primes preceding it
