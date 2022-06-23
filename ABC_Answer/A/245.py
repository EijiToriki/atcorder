import datetime

A, B, C, D = map(int, input().split())

takahashi = datetime.datetime(1,1,1,A,B,0).time()
Aoki = datetime.datetime(1,1,1,C,D,1).time()

if takahashi < Aoki:
  print("Takahashi")
else:
  print("Aoki")
