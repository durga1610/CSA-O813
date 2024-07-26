n1=int(input("enter the value of n1"))
n2=int(input("enter the value of n2"))
sum=0
for i in range(n1,n2+1):
    if i%2==0:
        print(i)
        sum=sum+i
print("sum of even numbers in range=",sum)
