a = []
n=int(input("Enter the size of array"))
for i in range(n):
    t = int(input("Enter the number"))
    a.append(t)
print(a)
###########bubble sort############
for i in range(len(a)):
    j=0
    while j<len(a)-i-1:
        if a[j]>a[j+1]:
            temp=a[j]
            a[j]=a[j+1]
            a[j+1]=temp
        j+=1
print(a)