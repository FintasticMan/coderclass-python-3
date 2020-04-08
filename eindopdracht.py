#!/usr/bin/env python3

def main():
    global keepGoing
    keepGoing = True
    print("Welcome to the most awesome-est program ever! (It's so awesome, I don't even know what it does yet!)\n")
    while keepGoing:
        menu()

def menu():
    global keepGoing
    print("So, this place is called a 'menu' and this is where you choose what you want to do!\nSo, the things you can do are:\n\tKill a unicorn (k);\n Spare the unicorn (s);\n Be an amazing person (a).\n\n And, if you REALLY want to, you can also quit (q).\n")
    wotIWantToDo = input(" What do you want to do? (k/s/a/Q) ")
    print("")
    if wotIWantToDo == "k":
        killUnicorn()
    elif wotIWantToDo == "s":
        spareUnicorn()
    elif wotIWantToDo == "a":
        beAmazing()
    elif wotIWantToDo == "q" or wotIWantToDo == "":
        keepGoing = False
        print("Bye bye!")
    else:
        print("I think you messed up and typed something in wrong. Do better next time!\n")

def killUnicorn():
    print("Killed the unicorn\n")

def spareUnicorn():
    print("Spared the unicorn\n")

def beAmazing():
    print("You're already amazing!\n")

main()
