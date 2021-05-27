from printState import convertStateToText as printState

def addRoundKey(state, roundKey):
    newState = []
    for column in range(4):
        newCol = []
        for row in range(4):
            newCol.append(state[column][row] ^ roundKey[column][row])
        newState.append(newCol)
    return newState




if __name__ == '__main__':
    state = [[50, 67, 246, 168], [136, 90, 48, 141], [49, 49, 152, 162], [224, 55, 7, 52]]
    roundKey = [[43, 126, 21, 22], [40, 174, 210, 166], [171, 247, 21, 136], [9, 207, 79, 60]]

    state = addRoundKey(state, roundKey)
    print(printState(state))