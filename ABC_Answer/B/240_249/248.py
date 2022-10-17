A, B, K = map(int, input().split())

slimeSum = A
shoutCnt = 0

while 1:
  if slimeSum >= B:
    break
  shoutCnt = shoutCnt + 1
  slimeSum = slimeSum * K

print(shoutCnt)