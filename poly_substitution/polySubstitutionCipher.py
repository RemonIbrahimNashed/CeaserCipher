from collections import Counter
import numpy as np
import matplotlib.pyplot as plt
import string
import operator

def encrypt_decrypt(line, key , mode ):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    key = key.upper()
    line = line.upper()
    
    index = 0 
    result = ""
    for letter in line :
        
        if letter in alpha :
            num = alpha.find(letter)
            if mode == "encryption":
                num += alpha.find(key[index])
            elif mode == "decryption":
                num -= alpha.find(key[index])
            num = num % 26
            
            result += alpha[num]
            index += 1 
            if index == len(key):
                index = 0 
        else :
            result = result + letter
            
    return result 





print("\n\t\tWelcom to PolySubstitution Algorthim")
filePath = input('Enter the path of the file to decrypt or "test.txt" to try on the test file: ')
file = open(filePath,"r")
outFile = open("out.txt","w")
lines = file.readlines()
cipherLines = [] 
plainText = ""
cipherText = ""
decryptedText = ""

key =input("Enter the key : ") 

letters = string.ascii_lowercase
englishLetterFreq = {'e': 12.70, 't': 9.06, 'a': 8.17, 'o': 7.51, 'i': 6.97, 'n': 6.75, 's': 6.33, 'h': 6.09, 'r': 5.99, 'd': 4.25, 'l': 4.03, 'c': 2.78, 'u': 2.76, 'm': 2.41, 'w': 2.36, 'f': 2.23, 'g': 2.02, 'y': 1.97, 'p': 1.93, 'b': 1.29, 'v': 0.98, 'k': 0.77, 'j': 0.15, 'x': 0.15, 'q': 0.10, 'z': 0.07}


# encrypt line by line 
for line in lines :
	plainText += line
	cipherLine = encrypt_decrypt(line,key,"encryption")
	cipherText += cipherLine
	cipherLines.append(cipherLine )

# get freq of each letter in the plain text 
plainText = plainText.lower()
plainTextCounter = Counter(plainText)
plainDict = dict()

# get freq of each letter in the chipher text
cipherText = cipherText.lower()
cipherTextCounter = Counter(cipherText)
cipherDict = dict()

# set the dic for plain and chiper text hold letters and thier freq 
for letter in letters :
    cipherDict[letter] = cipherTextCounter[letter]/len(cipherText)
    plainDict[letter] = plainTextCounter[letter]/len(plainText)

# plot the graph of plain , chipher and english letters 
plt.figure("Plain Text Letters Frequency")
plt.bar(list(plainDict.keys()), plainDict.values(), color='b')
plt.figure("English Letters Frequency")
plt.bar(list(englishLetterFreq.keys()), englishLetterFreq.values(), color='r')
plt.figure("Cipher Text Letters Frequency ")
plt.bar(list(cipherDict.keys()), cipherDict.values(), color='g')



outFile.write(cipherText)

#close the two opened files 
file.close()
outFile.close()
plt.show()