class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def pc(i):
            l = 0
            d = 0
            for j in weights:
                if l+j>i:
                    l = 0
                    
                    d+=1
                l+=j
                

            return d+1
        a = max(weights)
        b = sum(weights)
        c = None
        while a<=b:
            mid = (a+b)//2
            if pc(mid)<=days:
                c = mid
                b = mid-1
            else:
                a = mid+1
        return c
