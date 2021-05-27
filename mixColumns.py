from galoisMult import galoisMult as gMult
from printState import convertStateToText as printState

def mixColumns(state):

    newState = []
    for column in state:
        newColumn = []
        newColumn.append(gMult(column[0], 2) ^ gMult(column[1], 3) ^ gMult(column[2], 1) ^ gMult(column[3], 1))
        newColumn.append(gMult(column[0], 1) ^ gMult(column[1], 2) ^ gMult(column[2], 3) ^ gMult(column[3], 1))
        newColumn.append(gMult(column[0], 1) ^ gMult(column[1], 1) ^ gMult(column[2], 2) ^ gMult(column[3], 3))
        newColumn.append(gMult(column[0], 3) ^ gMult(column[1], 1) ^ gMult(column[2], 1) ^ gMult(column[3], 2))
        newState.append(newColumn)

    return newState


if __name__ == '__main__':
    state = [[212, 191, 93, 48], [224, 180, 82, 174], [184, 65, 17, 241], [30, 39, 152, 229]]
    print(printState(state))
    state = mixColumns(state)
    print(printState(state))


