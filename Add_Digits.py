def add_digits(n):
    sum=n
    while sum>=10:
        d=[int(d)for d in str(sum)]
        sum=sum_of_digits(d)
    return sum
def sum_of_digits(d):
    return sum(d)
n=int(input())
r=add_digits(n)
print(r)
