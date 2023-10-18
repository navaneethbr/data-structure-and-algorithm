a = []
n=int(input("Enter the size of array"))
for i in range(n):
    t = int(input("Enter the number"))
    a.append(t)
print(a)
############selection sort###############
for i in range(len(a)):
    j=i
    min_ind=j
    while j<len(a):
        if a[min_ind]<a[j]:
            min_ind=j
        j+=1
    a[i], a[min_ind]=a[min_ind], a[i]

print(a)