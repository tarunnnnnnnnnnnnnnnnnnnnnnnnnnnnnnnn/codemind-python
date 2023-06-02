i=int(input())
s=0
pr=1
while i!=0:
    b=i%10
    s=s+b
    pr=pr*b
    i=i//10
if pr==s:
    print("Spy Number")
else:
    print("Not Spy Number")