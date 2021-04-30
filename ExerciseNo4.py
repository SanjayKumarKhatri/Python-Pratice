a = int(input("enter your no: "))
p = list("range No")
b=[]
for i in p:
    if a%i==0:
       b.append(i)
print(b)