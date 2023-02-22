N = int(input())

div3 = N // 3
div5 = N // 5
div7 = N // 7
div15 = N // 15
div21 = N // 21
div35 = N // 35
div105 = N // 105

ans = (div3 + div5 + div7) - (div15 + div21 + div35) + div105
print(ans)