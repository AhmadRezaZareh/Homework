n = int(input("enter numbers :"))
sum = 0
for i in range (1,n+1):
    if n%i==0:
        sum = sum+1
    

if sum == n :
    print("addad kamel ast")
else :
    print("adadd kamel nist ")