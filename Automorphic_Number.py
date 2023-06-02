n=int(input())
a=len(str(n))
s=n**2
ld=s%(10**a)
if ld==n:
    print("Automorphic Number");
else:
    print("Not an Automorphic Number");