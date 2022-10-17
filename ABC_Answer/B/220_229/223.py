S = input()

S_dict = []

for i in range(len(S)):
  S_dict.append(S[i:] + S[:i])

S_dict = sorted(S_dict)
print(S_dict[0])
print(S_dict[len(S)-1])