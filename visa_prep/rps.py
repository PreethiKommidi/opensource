v, c=map(str ,input().split())
if v=="R" and c=="P":
    print("Charan")
elif v=="P" and c=="R":
    print("Vignesh")
elif v=="P" and c=="S":
    print("Charan")
elif v=="S" and c=="P":
    print("Vignesh")
elif v=="S" and c=="R":
    print("Charan")
elif v=="R" and c=="S":
    print("Vignesh")
else:
    print("NULL")
