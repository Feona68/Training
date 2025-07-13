def combination(s):
    count=0
    for ch in s:
        if ch=='{':
            count+=1
        elif ch=='}':
            count-=1
        if count<0:
            return "not well formed"
        
    if count==0:
        return "well formed"
    else:
        return "not well formed"
s=input()
print(combination(s))
