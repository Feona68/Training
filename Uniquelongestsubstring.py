
def longest_substring_with_k_unique(s, k):
    n=len(s)

    if n==0 or k==0:
        return 0
    left=0
    maxlen=0
    charfreq={}

    for right in range(n):
        char=s[right]
        charfreq[char]=charfreq.get(char,0)+1
        while(len(charfreq)>k):
            left_char=charfreq[left]
            charfreq[left_char]-=1
            

# Example usage
s = "aabacbebebe"
k = 3
print("Length of longest substring with exactly", k, "unique characters:", longest_substring_with_k_unique(s, k))
