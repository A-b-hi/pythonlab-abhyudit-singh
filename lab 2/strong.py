sum1=0
num=int(input("Enter a number:"))
temp=num
while(num):
    i=1
    fact=1
    r=num%10
    while(i<=r):
        fact=fact*i
        i=i+1
    sum1=sum1+fact
    num=num//10
if(sum1==temp):
    print("The number is a strong number")
else:
    print("The number is not a strong number")