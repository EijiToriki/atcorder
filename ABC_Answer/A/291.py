S = input()

ans = 0
for i in range(len(S)):
    if S[i] != str(S[i].lower()):
        ans = i + 1
        break

print(ans)


