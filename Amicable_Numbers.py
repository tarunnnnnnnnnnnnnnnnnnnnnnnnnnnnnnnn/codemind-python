X=int(input())
Y=int(input())
sum1=0
sum2=0
for i in range(1,X):
    if X%i==0:
        sum1+=i
for j in range(1,Y):
    if Y%j==0:
        sum2+=j
if(sum1==Y and sum2==X):
    print('Amicable')
else:
    print('Not Amicable')