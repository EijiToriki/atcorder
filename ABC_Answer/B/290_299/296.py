S = []
for _ in range(8):
    S.append(input())

num_to_char = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h'}

ans = ''
for i in range(8):
    for j in range(8):
        if S[i][j] == '*':
            char2 = 8 - i
            ans = num_to_char[j] + str(char2)

print(ans)
