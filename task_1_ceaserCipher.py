from collections import Counter
import numpy as np
import matplotlib.pyplot as plt
import string
import operator

#encryption function 
def encrypt(line , key ):
	line = line.upper()
	alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	result = ""
	for letter in line:
		if letter in alpha:
			letter_index = (alpha.find(letter) - key) % len(alpha)
			result = result + alpha[letter_index]
		else:
			result = result + letter
	return result.lower()
#decryption function 
def decrypt(line,key):
	line = line.upper()
	alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	result = ""
	for letter in line:
		if letter in alpha:
			letter_index = (alpha.find(letter) - key) % len(alpha)
			result = result + alpha[letter_index]
		else:
			result = result + letter
	return result.lower()




print("\n\t\tWelcom to ceaser cipher algorthim\n")
print("Note in order for the program to work good you must enter large text file ")	
filePath = input('Enter the path of the file to decrypt or "test.txt" to try on the test file: ')
file = open(filePath,"r")
outFile = open("out.txt","w")
lines = file.readlines()
cipherLines = []
plainText = ""
cipherText = ""
decryptedText = ""

key =int( input("Enter the key : ") )

letters = string.ascii_lowercase
englishLetterFreq = {'e': 12.70, 't': 9.06, 'a': 8.17, 'o': 7.51, 'i': 6.97, 'n': 6.75, 's': 6.33, 'h': 6.09, 'r': 5.99, 'd': 4.25, 'l': 4.03, 'c': 2.78, 'u': 2.76, 'm': 2.41, 'w': 2.36, 'f': 2.23, 'g': 2.02, 'y': 1.97, 'p': 1.93, 'b': 1.29, 'v': 0.98, 'k': 0.77, 'j': 0.15, 'x': 0.15, 'q': 0.10, 'z': 0.07}
# encrypt line by line  
for line in lines :
	plainText += line
	cipherLine = encrypt(line,key)
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


# get max freq in chipher text compare it with max freq in english language then find the key 
maxFreqInCipher = max(cipherDict.items(), key=operator.itemgetter(1))[0]
maxFreqInEnglish = max(englishLetterFreq.items(), key=operator.itemgetter(1))[0]

dedectedKey =   (ord(maxFreqInCipher) - ord(maxFreqInEnglish))%26

# decrypt the cipher text using the dedected key  
decryptedText += decrypt(cipherText,dedectedKey)

# get freq of each letter in the decrypted text 
decryptedText.lower()
decryptedCounter = Counter(decryptedText)
decryptDict = dict()

#set the dic for decrypted text hold letters and their freq 
for letter in letters :
	decryptDict[letter] = decryptedCounter[letter]/len(decryptedText)

#plot the graph of decrypted text letters 
plt.figure("dedected Text Letters Frequency ")
plt.bar(list(decryptDict.keys()), decryptDict.values(), color='y')

#out the decrypted file to text file 
outFile.write(decryptedText)

#close the two opened files 
file.close()
outFile.close()

plt.show()
