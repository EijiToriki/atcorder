bitFour = input()

bitFour = list(bitFour)

bitFour[3] = bitFour[2]
bitFour[2] = bitFour[1]
bitFour[1] = bitFour[0]
bitFour[0] = '0'

print("".join(bitFour))