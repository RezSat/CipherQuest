import string
import random

def caesar_cipher(message:str, shift: int):
    #encryption f(x) = f(x+n) mod 26
    cipher = ""
    #special char : cipher
    special = {}
    for i in message:
        #since lower case 97
        c = chr((ord(i) + shift -97 )%26 + 97)
        cipher += c
        if not i.isalpha():
            if i == ' ':
                i = "SPACE"
            elif i == ".":
                i = "COMMA(,)"
            elif i == "-":
                i = "MINUS/DASH ( - )"
            elif i == ".":
                i = "DOT(.)"
            special[i] = c
    
    s1 = random.choice(string.ascii_lowercase)
    s2 = random.choice(string.ascii_lowercase)
    special[s1] = chr((ord(s1) + shift -97 )%26 + 97)
    special[s2] = chr((ord(s2) + shift -97 )%26 + 97)

    return cipher, special, shift, message

def substitution_cipher(message, key):
    pass

def vigenere_cipher(message, keyword):
    pass