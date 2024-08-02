#This program is the starter code for the Programming Caesar's Cipher Project. 
# This code is inspired by Cracking Codes with Python: An Introduction to Building and Breaking Ciphers by Al Sweigart https://www.nostarch.com/crackingcodes (BSD Licensed)

import string

# Global variables
letLow = string.ascii_lowercase
letUp = string.ascii_uppercase
nums = string.digits
symbols = string.punctuation

possChar = letLow + letUp + nums + symbols
initPos = 0
shiftPos = 0
shiftMsg = ""

# Define the function called encryptOrDecrypt
def encOrDec():
  global shiftPos
  if mode == "decrypt":
    shiftPos = initPos - int(key)
  elif mode == "encrypt":
    shiftPos = initPos + int(key)

# Define the function called wraparound
def wrap():
  global shiftPos
  if (shiftPos >= len(possChar)):
    shiftPos-=len(possChar)
  elif (shiftPos<0):
    shiftPos+=len(possChar)

# Run code

# Introduction
print("Welcome! This program will encrypt or decrypt your secret message using the Caesar cipher. \n\nWhen creating your message, you may only choose from the following characters: \n" + possChar + "\n\nLet's get started!\n")

# Receive user input
initMsg = input("What is your message?\n")
key = input("What is the key? Choose a number from 0 to "+str(len(possChar)-1)+"\n")
mode = input("Do you want to decrypt or encrypt?\n")

# Encrypt or decrypt the message

for character in initMsg:
  if character in possChar:
    initPos = possChar.find(character)
    encOrDec()
    wrap()
    shiftMsg += possChar[shiftPos]
  else:
    shiftMsg+= character

# Print the shifted message
print("Your message is\n"+shiftMsg)