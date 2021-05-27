
def invShiftRows(state):
    newCol0 = [state[0][0], state[3][1], state[2][2], state[1][3]]
    newCol1 = [state[1][0], state[0][1], state[3][2], state[2][3]]
    newCol2 = [state[2][0], state[1][1], state[0][2], state[3][3]]
    newCol3 = [state[3][0], state[2][1], state[1][2], state[0][3]]
    newState = []
    newState.append(newCol0)
    newState.append(newCol1)
    newState.append(newCol2)
    newState.append(newCol3)
    return newState



if __name__ == '__main__':
    state = [[212, 191, 93, 48], [224, 180, 82, 174], [184, 65, 17, 241], [30, 39, 152, 229]]
    state = invShiftRows(state)
    print(state) # [[212, 39, 17, 174], [224, 191, 152, 241], [184, 180, 93, 229], [30, 65, 82, 48]]