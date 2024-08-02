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
mode = input("Do you want to decrypt or encrypt?\n")

if mode == "encrypt":
  key = input("What is the key? Choose a number from 0 to "+str(len(possChar)-1)+"\n")

  for character in initMsg:
    if character in possChar:
      initPos = possChar.find(character)
      shiftPos = initPos + int(key)
      wrap()
      shiftMsg += possChar[shiftPos]
    else:
      shiftMsg+= character

  # Print the shifted message
  print("Your message is\n"+shiftMsg)

elif mode=="decrypt":
  print("\n")
  key = 0
  for character in possChar:
    for character in initMsg:
      if character in possChar:
        initPos = possChar.find(character)
        shiftPos = initPos - int(key)
        wrap()
        shiftMsg += possChar[shiftPos]
      else:
        shiftMsg+= character
    print(shiftMsg + " | Key: "+ str(key))
    key = key + 1

    # Print the shifted message
    shiftMsg = ""

# I also did this whole program without using any of the videos :P