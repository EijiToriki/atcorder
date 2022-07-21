import bisect

N = int(input())
S = input()
MOD = 10**9 + 7

a = at = atc = atco = atcod = atcode = atcoder = 0

for s in S:
  if s == 'a':
    a += 1
  if s == 't':
    at += a
  if s == 'c':
    atc += at
  if s == 'o':
    atco += atc
  if s == 'd':
    atcod += atco
  if s == 'e':
    atcode += atcod
  if s == 'r':
    atcoder += atcode

print(atcoder%MOD)