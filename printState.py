

chars = ['0', '1', '2', '3','4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']

def convertStateToText(state):
    newState = [[],[],[],[]]
    for column in state:
        for i in range(4):
            newState[i].append(column[i])

    string = ''
    for row in newState:
        for i in range(4):
            index = int(row[i] / 16)
            string = string + chars[index]
            index = row[i] % 16
            string = string + chars[index]
            string = string + ' '
        string = string + '\n'
    string = string + '\n'
    return string


if __name__ == '__main__':
    state = [[57, 37, 132, 29], [2, 220, 9, 251], [220, 17, 133, 151], [25, 106, 11, 50]]
    print(convertStateToText(state))