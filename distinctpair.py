def distinctpair(arr,k):
    narr=[]
    count=0
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if abs(arr[i]-arr[j])==k and ((arr[i],arr[j])or (arr[j],arr[i]) not in narr):
                count+=1
                narr.append((i,j))
    return count


k=int(input("k:"))
arr=list(map(int,input().split()))
print(distinctpair(arr,k))

