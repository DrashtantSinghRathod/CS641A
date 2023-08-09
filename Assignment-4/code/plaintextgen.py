import numpy as np
import random

hex2char = {
 '0000': 'f',
 '0001': 'g',
 '0010': 'h',
 '0011': 'i',
 '0100': 'j',
 '0101': 'k',
 '0110': 'l',
 '0111': 'm',
 '1000': 'n',
 '1001': 'o',
 '1010': 'p',
 '1011': 'q',
 '1100': 'r',
 '1101': 's',
 '1110': 't',
 '1111': 'u'
}

char2hex = {x:y for y,x in hex2char.items()}

# XOR value between pairs of plaintexts is 00 00 80 10 00 00 40 00
XOR_value = list((bin(0x0000801000004000))[2:].zfill(64))
XOR_value = [int(x) for x in XOR_value]
binplaintexts = []
for i in range(2500):
    tmp = np.random.choice(['f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u'],size=(1,16),replace = True)[0]
    bininput=[]
    for i in tmp:
        bininput.extend([int(a) for a in char2hex[i]])

    binplaintexts.append(bininput)
    binplaintexts.append(list(np.bitwise_xor(bininput,XOR_value)))

plaintexts = []

for i in range(len(binplaintexts)):
    s = ""
    for j in range(0,64,4):

        s+=hex2char[''.join([str(a) for a in binplaintexts[i][j:j+4]])]

    plaintexts+=[s]

file = open("plaintexts1.txt","w")
for plaintext in plaintexts:
    file.write(plaintext+"\n")
file.close()

# XOR value between pairs of plaintexts is  00 00 08 01 00 10 00 00
XOR_value = list((bin(0x0000080100100000))[2:].zfill(64))
XOR_value = [int(x) for x in XOR_value]
binplaintexts = []
for i in range(2500):
    tmp = np.random.choice(['f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u'],size=(1,16),replace = True)[0]
    bininput=[]
    for i in tmp:
        bininput.extend([int(a) for a in char2hex[i]])

    binplaintexts.append(bininput)
    binplaintexts.append(list(np.bitwise_xor(bininput,XOR_value)))

plaintexts = []

for i in range(len(binplaintexts)):
    s = ""
    for j in range(0,64,4):

        s+=hex2char[''.join([str(a) for a in binplaintexts[i][j:j+4]])]
    plaintexts+=[s]

file = open("plaintexts2.txt","w")
for plaintext in plaintexts:
    file.write(plaintext+"\n")
file.close()