
chars = ['0', '1', '2', '3','4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']



def convertWordToText(word):
    string = ''
    for i in range(len(word)):

        index = int(word[i] / 16)
        string = string + chars[index]
        index = word[i] % 16
        string = string + chars[index]

    return string

if __name__ == '__main__':
    word = [0x2b, 0x7e, 0x15, 0x16]
    print(convertWordToText(word))


