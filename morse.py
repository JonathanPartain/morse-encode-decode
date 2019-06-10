#!/usr/bin/env python3
import os  # to clear terminal
alphabet = {
    "a" : ".-",
    "b" : "-...",
    "c" : "-.-.",
    "d" : "-..",
    "e" : ".",
    "f" : "..-.",
    "g" : "--.",
    "h" : "....",
    "i" : "..",
    "j" : ".---",
    "k" : "-.-",
    "l" : ".-..",
    "m" : "--",
    "n" : "-.",
    "o" : "---",
    "p" : ".--.",
    "q" : "--.-",
    "r" : ".-.",
    "s" : "...",
    "t" : "-",
    "u" : "..-",
    "v" : "...-",
    "w" : ".--",
    "x" : "-..-",
    "y" : "-.--",
    "z" : "--.."
}
numbers = {
    1 : ".----",
    2 : "..---",
    3 : "...--",
    4 : "....-",
    5 : ".....",
    6 : "-....",
    7 : "--...",
    8 : "---..",
    9 : "----.",
    0 : "-----"
}
morse_a = {
    ".-" : "a",
    "-..." : "b",
    "-.-." : "c",
    "-.." : "d",
    "." : "e",
    "..-." : "f",
    "--." : "g",
    "...." : "h",
    ".." : "i",
    ".---" : "j",
    "-.-" : "k",
    ".-.." : "l",
    "--" : "m",
    "-." : "n",
    "---" : "o",
    ".--." : "p",
    "--.-" : "q",
    ".-." : "r",
    "..." : "s",
    "-" : "t",
    "..-" : "u",
    "...-" : "v",
    ".--" : "w",
    "-..-" : "x",
    "-.--" : "y",
    "--.." : "z",
    ".----" : "1",
    "..---" : "2",
    "...--" : "3",
    "....-" : "4",
    "....." : "5",
    "-...." : "6",
    "--..." : "7",
    "---.." : "8",
    "----." : "9",
    "-----" : "0"
}
def encode(str):
    out = ""
    for s in str:
        if s.isalpha():  # alphabet
            out += alphabet[s.lower()] + " "
        elif s.isdigit():
            out += numbers[s] + " "
        else:  # space
            out += " / "
    return out

def decode(str):
    out = ""
    split = str.strip().split()
    for m in split:
        if m == '/':
            out += " "
        else:
            out += morse_a[m]

    return out

while True:
    print("Options: ")
    print("1: Encode")
    print("2: Decode")
    print("3: Learn")
    print("q: Quit")
    ans = input("What would you like to do? ")
    if ans == "1":
        os.system('clear')
        e = input("Enter the string you would like to encode: ")
        print("The result of the encoding is: ")
        print(encode(e))
    elif ans == "2":
        os.system('clear')
        d = input("Enter the string you would like to decode: ")
        print("The result of the decoding is: ")
        print(decode(d))
    elif ans == "3":
        os.system('clear')
        print("Learning is not available at the moment!")
    elif ans == "q":
        print("Goodbye!")
        break
    else:
        os.system('clear')
        print(ans + " is not one of the options above, try again!")
