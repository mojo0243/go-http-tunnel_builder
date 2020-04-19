#!/usr/bin/python

import os
from colorama import Fore

os.system('clear')

def menu1():
    global btype
    print(Fore.CYAN+"Welcome to the go-http-tunnel builder") 
    print("")
    print(Fore.YELLOW+"1) Client")
    print(Fore.YELLOW+"2) Server")
    choice = input(Fore.CYAN+"Please choose to build a client or server tunnel binary: ")
    if choice == '1':
        btype = 'tunnel'
    elif choice == '2':
        btype = 'tunneld'
    else:
        print(Fore.RED+"Please enter a valid choice 1 or 2")
        menu1()
    menu2()

def menu2():
    print("")
    print("")
    global goos
    print(Fore.CYAN+"Architecture")
    print("")
    print(Fore.YELLOW+"1) linux")
    print(Fore.YELLOW+"2) MacOs")
    print(Fore.YELLOW+"3) Windows")
    choice = input(Fore.CYAN+"Please choose an Architecture to build for: ")
    if choice == '1':
        goos = 'linux'
    elif choice == '2':
        goos = 'darwin'
    elif choice == '3':
        goos = 'windows'
    else:
        print(Fore.RED+"Please enter a valid choice 1, 2, or 3")
        menu2()
    menu3()

def menu3():
    global arch
    global bit
    print(Fore.CYAN+"Bitness")
    print("")
    print(Fore.YELLOW+"1) arm 32")
    print(Fore.YELLOW+"2) arm 64")
    print(Fore.YELLOW+"3) 32 Bit")
    print(Fore.YELLOW+"4) 64 Bit")
    choice = input(Fore.CYAN+"Please select a bitness: ")
    if choice == '1':
        arch = 'arm'
    elif choice == '2':
        arch = 'arm64'
    elif choice == '3':
        arch = '386'
    elif choice == '4':
        arch = 'amd64'
    else:
        print(Fore.RED+"Please enter a valid choice 1, 2, 3, or 4")
        menu3()
    build()

def build():
    os.system('clear')
    print(Fore.YELLOW+"Building your tunnel now")
    os.system("cd cmd/{btype}; GOOS={goos} GOARCH={arch} go build -o ../../{btype}_builds/{btype}_{goos}{arch} -v -ldflags '-s -w'; cd ../..".format(goos=goos, arch=arch, btype=btype))
    print(Fore.GREEN+"Tunnel binary built")

def main():
    menu1()

if __name__ == "__main__":
    main()
