

def galoisMult(a, b):
    '''
    The parameter b will be either 1, 2 or 3.  Multiplication by 3 is defined as multiplication by 2 then adding the
    original value.  For example 3x6 is equivalent to 2x6+6.  The multiplication by 2 is done with a left shift
    (a <<= 1) and dropping the MSB.  If that bit had been a 1 then remainder after dividing by the irreducible
    polynomial 00011011 (1b). This polynomial is described in the literature as a 9 bit value 100011011, or in its
    Galois form x8 + x4 + x3 + x1 + 1
    :param a: the original value to be multiplied.
    :param b: the value to be multiplied by
    :return: the result
    '''
    result = 0
    for i in range(b): # This needs to run once for x1, twice for x2 and thrice for x3
        if b & 1 == 1: # If the LSB is 1.  This will happen with x1 and x3
            result ^= a # Add the original value to result.  This is the + part of x3 = x2 +1
        hiBitSet = a & 0x80 # Before doing x2 check to see if a is > 128
        a <<= 1 # Do x2
        a &= 0xff # reduce 9 bit numbers to 8 bit
        if hiBitSet == 0x80: # If the original value of a was > 128 then the result is > 256 so reduce.
            a ^= 0x1b # XOR with the irreducible polynomial
        b >>= 1 # Rotate b
    return result


if __name__ == '__main__':
    #print(hex(galoisMult(0xa0, 1))) # a0
    #print(hex(galoisMult(0xd4, 2))) # b3
    #print(hex(galoisMult(0xbf, 3))) # da
    print(hex(galoisMult(0x7f, 0)))
    print(hex(galoisMult(0x7f, 1)))
    print(hex(galoisMult(0x7f, 2)))
    print(hex(galoisMult(0x7f, 3)))


