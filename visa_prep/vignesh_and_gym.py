X, Y, Z=map(int, input().split())
if X+Y<=Z:
    print(2)
elif X+Y>=Z:
    if X>Z:
        print(0)
    else:
        print(1)
