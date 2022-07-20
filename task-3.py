arr=[2,3,4,5,5,6,7]
l=[]
for i in range(len(arr)):
    if (arr[i]<max(arr)):
        l.append(arr[i])
print (max(l))

