n=int(input())
arr=[]
for i in range(n):
    num=int(input())
    arr.append(num)
j=0
while j<n:
    if j not in arr:
        print(j)
        break
    j+=1
