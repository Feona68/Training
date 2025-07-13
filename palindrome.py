str=input()
nstr=""
for s in str:
    if s.isalpha():
        nstr+=(s.lower())
    elif s.isdigit():
        nstr+=s
if nstr[::]==nstr[::-1]:
    print(True)
else:
    print(False)
