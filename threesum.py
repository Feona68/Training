n=int(input())
nums=list(map(int,input().split()))

res=[]
nums.sort()

for i in range(len(nums)):
    if i>0 and nums[i]==nums[i-1]:
        continue
    j=i+1
    k=len(nums)-1
    while(j<k):
        total=nums[i]+nums[j]+nums[k]
        if total>0:
            k=k-1
        elif total<0:
            j=j+1
        else:
            res.append([nums[i],nums[j],nums[k]])
            j=j+1
            while j<k and nums[j]==nums[j-1]:
                j=j+1

print(res)
