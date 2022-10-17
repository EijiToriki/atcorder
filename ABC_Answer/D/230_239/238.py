## Qiita 参照
def main():
    A, S = map(int, input().split())
    T = S - 2 * A
    if T < 0:
        return False
    return T & A == 0
 
if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        print("Yes" if main() else "No")