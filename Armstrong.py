n=int(input("Enter a number: "))
l=len(str(n))
sum=0
dup=n
while n>0:
    digit=n%10
    sum+=digit**l
    n=n//10
if sum==dup:
    print(dup,"is an Armstrong number")
else:
    print(dup,"is not an Armstrong number")