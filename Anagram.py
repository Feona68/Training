'''def anagram(Str1,str2):
    dict1={}

    if len(str1)!=len(str2):
        return "Not anagrams"
    for i in str1:
        dict1[i]=dict1.get(i,0)+1
        

    for i in str2:
        dict1[i]=dict1.get(i,0)-1

    for key in dict1:
        if dict1[key]==0:
            return "The strings are anagrams of each other"
        else:
            return "The strings are not anagrams of each other"
    
str1=input()
str2=input()
print(anagram(str1,str2))'''

from collections import Counter
str1=input()
str2=input()

if Counter(str1)==Counter(str2):
    print("Anagrams")
else:
    print("Not anagrams")
