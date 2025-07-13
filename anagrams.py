
strs=input().split()
arr={}
for s in strs:
    key="".join(sorted(s))
    if key in arr:
        arr[key].append(s)
    else:
        arr[key]=[s]
for key in arr.values():
    print(" ".join(key))
    
        
