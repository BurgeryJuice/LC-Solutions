class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        tup = [0 for i in range(26)]
        fm = [0 for i in range(26)]
        for i in s1:
            tup[ord(i)-97] +=1
        lm = len(s1)
        for i in range(lm):
            fm[ord(s2[i])-97] +=1
        for i in range(len(s2)-lm+1):
            if tup == fm:
                return True
            if i+lm>=len(s2):
                break
            fm[ord(s2[i])-97] -=1
            fm[ord(s2[i+lm])-97]+=1
        return False
