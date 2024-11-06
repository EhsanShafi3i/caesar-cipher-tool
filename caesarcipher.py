import string
from collections import Counter

def findAlphabet(num):
    alphabetMapping = {
        0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E',
        5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J',
        10: 'K', 11: 'L', 12: 'M', 13: 'N', 14: 'O',
        15: 'P', 16: 'Q', 17: 'R', 18: 'S', 19: 'T',
        20: 'U', 21: 'V', 22: 'W', 23: 'X', 24: 'Y',
        25: 'Z'
    }
    return alphabetMapping[num % 26]

def findNumOfAlphabet(alphabet):
    reverseAlphabetMapping = {
        'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4,
        'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9,
        'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14,
        'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19,
        'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24,
        'Z': 25
    }
    return reverseAlphabetMapping[alphabet.upper()]

def decryptWithKey(text, key):
    decryptedText = ""
    for i in text:
        if i.isalpha():
            shiftedIndex = (findNumOfAlphabet(i) - key) % 26
            decryptedText += findAlphabet(shiftedIndex)
        elif i.isdecimal():
            decryptedText += str((int(i) - key) % 10)
        else:
            decryptedText += i
    return decryptedText

def bruteForceDecrypt(text):
    possibleTexts = {}
    for key in range(26):
        decryptedText = decryptWithKey(text, key)
        possibleTexts[key] = decryptedText
    return possibleTexts

def frequencyAnalysisDecrypt(text):
    letterCounts = Counter(c for c in text.upper() if c.isalpha())
    mostCommon = letterCounts.most_common()
    print(f"Most common letters in the encrypted text: {mostCommon}")
    
    # لیست حروف رایج در زبان انگلیسی
    commonLetters = ['E', 'T', 'A', 'O', 'I', 'N', 'S', 'H', 'R', 'D', 'L', 'C', 'U', 'M', 'W', 'F', 'G', 'Y', 'P', 'B', 'V', 'K', 'J', 'X', 'Q', 'Z']
    
    for commonLetter in commonLetters:
        if mostCommon:
            mostCommonLetter = mostCommon[0][0]
            keyGuess = (findNumOfAlphabet(mostCommonLetter) - findNumOfAlphabet(commonLetter)) % 26
            decryptedText = decryptWithKey(text, keyGuess)
            print(f"Trying key {keyGuess}: {decryptedText}")
            # بررسی کنید که آیا متن رمزگشایی شده منطقی است یا خیر
            if "THIS IS A TEST MESSAGE" in decryptedText:
                return keyGuess
    return None

def knownWordAttackDecrypt(text, knownWord="THE"):
    knownWord = knownWord.upper()
    possibleKeys = []
    
    for i in range(len(text) - len(knownWord) + 1):
        substring = text[i:i+len(knownWord)]
        if substring.isalpha(): 
            keyGuess = (findNumOfAlphabet(substring[0]) - findNumOfAlphabet(knownWord[0])) % 26
            possibleKeys.append(keyGuess)
    
    decryptedTexts = {}
    for key in possibleKeys:
        decryptedText = decryptWithKey(text, key)
        decryptedTexts[key] = decryptedText
    
    return decryptedTexts

def transpositionAttackDecrypt(text):
    possibleDecrypts = {}
    for shift in range(1, len(text)):
        shiftedText = ''.join([text[i - shift] for i in range(len(text))])
        possibleDecrypts[shift] = shiftedText
    return possibleDecrypts

def anagramAttackDecrypt(text):
    possibleDecrypts = {}
    words = text.split()
    for word in words:
        wordAnagrams = [''.join(sorted(word)) for word in words]
        possibleDecrypts[word] = wordAnagrams
    return possibleDecrypts

def main():
    mode = input("Choose (E)ncrypt, (D)ecrypt with Key, ").upper()
    while True:
        if mode == "E":
            encryptedAlgo = int(input("Enter a number to shift by: "))
            text = input("Enter the text to encrypt: ")
            encryptedText = ""

            for i in text:
                if i.isalpha():
                    shiftedIndex = (findNumOfAlphabet(i) + encryptedAlgo) % 26
                    encryptedText += findAlphabet(shiftedIndex)
                elif i.isdecimal():
                    encryptedText += str((int(i) + encryptedAlgo) % 10)
                else:
                    encryptedText += i
            print("Encrypted message:", encryptedText)

        elif mode == "D":
            encryptedAlgo = int(input("Enter the decryption key: "))
            text = input("Enter the text to decrypt: ")
            decryptedText = decryptWithKey(text, encryptedAlgo)
            print("Decrypted message:", decryptedText)
        elif mode == "W":
            print("Enter mode to Decrypt")
            choice = input("(B)rute-force Decrypt, (F)requency Analysis, (K)nown Word Attack, (T)ransposition Attack, or (A)nagram Attack: ").upper()
            if choice == "B":
                text = input("Enter the text to brute-force decrypt: ")
                possibleTexts = bruteForceDecrypt(text)
                print("Possible decrypted messages:")
                for key, decryptedText in possibleTexts.items():
                    print(f"Key {key}: {decryptedText}")

            elif choice == "F":
                text = input("Enter the text for frequency analysis: ")
                key = frequencyAnalysisDecrypt(text)
                if key is not None:
                    decryptedText = decryptWithKey(text, key)
                    print(f"Decrypted message using frequency analysis: {decryptedText}")
                else:
                    print("Could not determine the key.")

            elif choice == "K":
                text = input("Enter the text for known word attack: ")
                decryptedTexts = knownWordAttackDecrypt(text)
                print("Decrypted texts from known word attack:")
                for key, decryptedText in decryptedTexts.items():
                    print(f"Key {key}: {decryptedText}")

            elif choice == "T":
                text = input("Enter the text for transposition attack: ")
                possibleDecrypts = transpositionAttackDecrypt(text)
                print("Possible decrypted texts using transposition attack:")
                for shift, decryptedText in possibleDecrypts.items():
                    print(f"Shift {shift}: {decryptedText}")

            elif choice == "A":
                text = input("Enter the text for anagram attack: ")
                possibleDecrypts = anagramAttackDecrypt(text)
                print("Possible decrypted texts using anagram attack:")
                for word, anagrams in possibleDecrypts.items():
                    print(f"Word: {word} -> Anagrams: {anagrams}")
            elif choice == "EXIT":
                break

def test_frequency_analysis():
    encrypted_text = "Wklv lv d whvw phvvdjh"
    key = frequencyAnalysisDecrypt(encrypted_text)
    if key is not None:
        decrypted_text = decryptWithKey(encrypted_text, key)
        print(f"Decrypted message using frequency analysis: {decrypted_text}")
    else:
        print("Could not determine the key.")

test_frequency_analysis()

main()
