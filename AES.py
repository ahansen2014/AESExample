'''
Author: Andrew Hansen, Jan 2021
This is my own implementation of the AES encryption system for the purposes of understanding the algorithm and its
implementation.  It goes without saying that this is not for use in production and is for academic purposes only.


'''

from keyExpansion import *
from addRoundKey import *
from subBytes import *
from shiftRows import *
from mixColumns import *
from invSubBytes import *
from invShiftRows import *
from invMixColumns import *
from printState import *

def createState(plain):
    state = []
    for col in [0,4,8,12]:
        column=[]
        for row in range(4):
            column.append(plain[col + row])
        state.append(column)
    return state


def doAESEncryption(message, key):
    state = createState(message)
    print('Initial message in plain ascii.  Note, read down, not across')
    print(convertStateToText(state))
    roundKeys = expandKey(key)

    for round in range(11):
        if round == 0: # First round only has addRoundKey
            state = addRoundKey(state, roundKeys[round])
            #print(convertStateToText(state))
        elif round == 10: # Last round does not have mixColumns
            state = subBytes(state)
            state = shiftRows(state)
            state = addRoundKey(state, roundKeys[round])
            #print(convertStateToText(state))
        else:
            state = subBytes(state)
            state = shiftRows(state)
            state = mixColumns(state)
            state = addRoundKey(state, roundKeys[round])
            #print(convertStateToText(state))

    output = []
    for column in state:
        for i in range(4):
            output.append(column[i])
    return output

def doAESDecryption(data, key):
    state = createState(data)
    #print(convertStateToText(state))
    roundKeys = expandKey(key)

    for round in range(10,-1,-1):
        if round == 10:
            state = addRoundKey(state, roundKeys[round])
            state = invShiftRows(state)
            state = invSubBytes(state)
            #print(convertStateToText(state))
        elif round == 0:
            state = addRoundKey(state, roundKeys[round])
            #print(convertStateToText(state))
        else:
            state = addRoundKey(state, roundKeys[round])
            state = invMixColumns(state)
            state = invShiftRows(state)
            state = invSubBytes(state)
            #print(convertStateToText(state))

    print('Decrypted state:')
    print(convertStateToText(state))
    output = ''
    for column in state:
        for i in range(4):
            output = output + chr(column[i])
    return output


def convertStrToData(inStr):
    data = []
    for letter in inStr:
        data.append(ord(letter))
    return data

if __name__ == '__main__':
    #input = [0x32, 0x43, 0xf6, 0xa8, 0x88, 0x5a, 0x30, 0x8d, 0x31, 0x31, 0x98, 0xa2, 0xe0, 0x37, 0x07, 0x34]
    input = convertStrToData('attack the tower')
    #key = [0x2b, 0x7e, 0x15, 0x16, 0x28, 0xae, 0xd2, 0xa6, 0xab, 0xf7, 0x15, 0x88, 0x09, 0xcf, 0x4f, 0x3c]
    key = convertStrToData('yellow submarine')
    cipher = doAESEncryption(input, key)
    print('Encrypted message as decimal values:',cipher)
    for char in cipher:
        print(chr(char))
    plain = doAESDecryption(cipher, key)
    print('Decrypted message:',plain)