from CAESARCIPHER_ART import *
print(logo)

def caesar(direction1,text1,shift1):
    shift1%=26
    new=''
    
    if direction1.lower()=='encode':
        for i in range(len(text1)):
            if text1[i] in alphabet:
                if (alphabet.index(text1[i])+shift1)<26:
                    new+=alphabet[alphabet.index(text1[i])+shift1]
                else:
                    new+=alphabet[alphabet.index(text1[i])+shift1-len(alphabet)]
            else:
                new+=text1[i]
        print(f"The encoded text is {new}")
    
    elif direction1.lower()=='decode':
        for j in range(len(text1)):
            if text1[j] in alphabet:
                new+=alphabet[alphabet.index(text1[j])-shift1]
            else:
                new+=text1[j]
        print(f"The decoded text is {new}")

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',\
                'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(direction,text,shift)
    more=input('Do you want to go back(yes/no):').lower()
    if more=='no':
        print('GOODBYE')
        break