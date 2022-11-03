S1 = input()
S2 = input()
S3 = input()
S = {S1, S2, S3}
contest = {'ABC', 'ARC', 'AGC', 'AHC'}
ans = list(contest - S)
print(ans[0])