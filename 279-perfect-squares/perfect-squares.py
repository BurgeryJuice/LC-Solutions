import math as m
class Solution:
    def numSquares(self, n: int) -> int:
        mem = {}
        def s(num):
            if num <0:
                return float("inf")
            if num == 0:
                return 0
            elif num in mem:
                return mem[num]
            else:
                mn = float("inf")
                for i in range(1,int(m.sqrt(num))+1):
                    mn = min(mn,s(num-i*i))
                mem[num] = mn+1
                return mem[num]
        return s(n)

            