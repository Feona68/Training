def numsum(arr,K):
    arr.sort()
    
    for i in range(0,len(arr)):
        k=i
        j=len(arr)-1
        while k<=j:
            sum=arr[i]+arr[k]+arr[j]
            if sum<K:
                k+=1
            elif sum>K:
                j-=1
            elif sum==K:
                return True
    return False
            

arr=list(map(int,input().split(',')))
K=int(input())
print(numsum(arr,K))
