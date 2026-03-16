class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxl = 0
        j = 0
        a = set()
        for i in range(len(s)):
            if s[i] in a:
                while s[i] in a:
                     
                    a.discard(s[j])
                    j+=1
                a.add(s[i])
            else:
                a.add(s[i])
            maxl = max(maxl,len(a))
        return maxl