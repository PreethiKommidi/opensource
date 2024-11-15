N, X, Y=map(int, input().split())
for i in range(0,N):
    totalscore=i*X+(N-i)*0
if totalscore==Y:
    print("YES")
else:
    print("NO")
