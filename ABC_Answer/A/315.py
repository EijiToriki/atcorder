S = input()

ans = []
zyogai = set({"a", "i", "u", "e", "o"})
for s in S:
  if s not in zyogai:
    ans.append(s)

print("".join(ans))