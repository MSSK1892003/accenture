arr=list(map(int,input().split()))
product=1
for i in arr:
    if i==0:
        product=0
        break
    product=product*i
print(product)