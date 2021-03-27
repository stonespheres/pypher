import sys
import string

# Load a text file, remove whitespace
def loadText(file):
    with open(file) as fl:
        return fl.read().strip()
# Check punctuation mark position
def checkPosition(message, userInput):
    for i in range(1, userInput + 1):
        text = ''
        count = 0
        firstPM = 0
        for char in message:
            if char in string.punctuation:
                count = 0
                firstPM = True
            elif firstPM is True:
                count += 1
            if count == i:
                text += char
        print("Chosen offset = {} after punctuation = {}", format(i, text))
    print()
