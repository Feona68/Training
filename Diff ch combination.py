def combination(s):
    d={')':'(',']':'[','}':'{'}
    stack=[]
    for ch in s:
        if ch in ['(','[','{']:
            stack.append(ch)
        elif ch in [')',']','}']:
            if len(stack)==0 or stack[-1]!=d[ch]:
                return "Not matching"
            else:
                stack.pop()
    return "Matching"

s=input()
print(combination(s))
            
