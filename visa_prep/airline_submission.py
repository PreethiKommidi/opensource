x, n=map(int, input().split())
rem_passengers=n-(x*100)
planes=rem_passengers/100
r=planes-int(planes)
if r>0:
    print(int(planes)+1)
else:
    print(int(planes))
