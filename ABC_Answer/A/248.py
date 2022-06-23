inNumStr = input()

inNum = list(inNumStr)
numList = [str(i) for i in range(10)]

result = list(set(numList)-set(inNum))

print(result[0])
