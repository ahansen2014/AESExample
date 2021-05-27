
def rConsts(rounds):

    rcon = [[1, 0, 0, 0]]


    for _ in range(1, rounds):
        rcon.append([rcon[-1][0]*2, 0, 0, 0])
        if rcon[-1][0] > 0x80:
            rcon[-1][0] ^= 0x11b

    return rcon

print(rConsts(10))
