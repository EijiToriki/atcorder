s = input()
ans = []

for s01 in s:
    if s01 == '0':
        ans.append('1')
    else:
        ans.append('0')

print(''.join(ans))