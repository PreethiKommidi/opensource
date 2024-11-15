n=input()
new=""
t=1
for i in range(1,len(n)):
    if n[i]==n[i-1]:
        t+=1
    else:
        new+=n[i-1]+str(t)
        t=1
new+=n[-1]+str(t)
print(new)
            
        
