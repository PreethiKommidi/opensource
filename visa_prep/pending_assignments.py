x, y, z=map(int, input().split())
total_min=z*1440
assign_time=x*y
if assign_time<=total_min:
    print("YES")
else:
    print("NO")
