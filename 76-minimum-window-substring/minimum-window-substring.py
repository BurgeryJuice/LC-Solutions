class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def hmc(a,b):
            for i in range(52):
                if a[i]<b[i]:
                    return False
            return True
        if len(t)>len(s):
            return ""
        ma = 0
        mb = float("inf")
        a = [0 for i in range(52)]
        b = [0 for i in range(52)]
        for i in t:
            o = ord(i)
            if o>96:
                a[o-97+26]+=1
            else:
                a[o-65]+=1
        j = 0

        for i in range(len(s)):
            o = ord(s[i])
            if o>96:
                b[o-97+26]+=1
            else:
                b[o-65]+=1
            if hmc(b,a):
                
                while hmc(b,a):
                    if (i - j + 1) < (mb - ma):
                        ma,mb = j,i + 1
                    o = ord(s[j])
                    if o>96:
                        b[o-97+26]-=1
                    else:
                        b[o-65]-=1
                    j+=1
            
        if mb-ma == float("inf"):
            return ""
        else:
            return s[ma:mb]