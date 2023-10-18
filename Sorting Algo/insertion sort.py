a = []
n=int(input("Enter the size of array"))
for i in range(n):
    t = int(input("Enter the number"))
    a.append(t)
print(a)

##############Insertion Sort###############
for i in range(len(a)):
    j=i
    while j>0 and a[j-1]>a[j]:
        a[j-1], a[j] = a[j], a[j-1]
        j-=1
print(a)
        