from collections import Counter
s=input()
freqdict=Counter(s)
oddfreq=0

for i in freqdict.values():
    if i%2==1:
        oddfreq+=1
if oddfreq>1:
    print(False)
else:
    print(True)
