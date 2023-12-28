l1=[]
n=int(input("ennter the no of elements:"))
for i in range(n):
     l1.append(int(input("enter elements:")))
     print(l1)
l2=[]
n=int(input("enter the no of elements:"))
for i in range (n):
    l2.append(int(input("enter the elements:")))
    print(l2)
for i in range(len(l1)):
    a=l1[i]+l2[i]
    print(a)
    
    