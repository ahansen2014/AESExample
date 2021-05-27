from galoisMult import *

def invMixColumns(state):

    newState = []
    for column in state:
        newColumn = []
        newColumn.append(galoisMult(column[0], 14) ^ galoisMult(column[1], 11) ^ galoisMult(column[2], 13) ^ galoisMult(column[3], 9))
        newColumn.append(galoisMult(column[0], 9) ^ galoisMult(column[1], 14) ^ galoisMult(column[2], 11) ^ galoisMult(column[3], 13))
        newColumn.append(galoisMult(column[0], 13) ^ galoisMult(column[1], 9) ^ galoisMult(column[2], 14) ^ galoisMult(column[3], 11))
        newColumn.append(galoisMult(column[0], 11) ^ galoisMult(column[1], 13) ^ galoisMult(column[2], 9) ^ galoisMult(column[3], 14))
        newState.append(newColumn)

    return newState


if __name__ == '__main__':
    state = [[4, 102, 129, 229], [224, 203, 25, 154], [72, 248, 211, 122], [40, 6, 38, 76]]
    state = invMixColumns(state)
    print(state) #[[212, 191, 93, 48], [224, 180, 82, 174], [184, 65, 17, 241], [30, 39, 152, 229]]



