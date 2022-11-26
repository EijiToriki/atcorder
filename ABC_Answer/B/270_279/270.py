import sys
x, y, z = map(int, input().split())

if x > 0:
    if y < 0 or y > x:
        print(x)
        sys.exit()
    else:
        if z > 0:
            if z < y:
                print(x)
                sys.exit()
            else:
                print(-1)
                sys.exit()
        else:
            print(abs(z) * 2 + x)
            sys.exit()
else:
    if y > 0 or y < x:
        print(abs(x))
        sys.exit()
    else:
        if z < 0:
            if z > y:
                print(abs(x))
                sys.exit()
            else:
                print(-1)
                sys.exit()
        else:
            print(2*z + abs(x))
            sys.exit()

