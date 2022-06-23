def calc_edge_LED(length):
    if length % 2 == 0:
        return length // 2
    else:
        return length // 2 + 1

H, W = int(input())
led_H = calc_edge_LED(H)
led_W = calc_edge_LED(W)

print(H*W)

