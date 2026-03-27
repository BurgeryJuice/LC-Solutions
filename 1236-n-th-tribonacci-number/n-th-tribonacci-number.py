class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n==1 or n==2:
            return 1
        a = 0
        b = 1
        c = 1
        for i in range(n-2):
            t = a
            a = b
            b = c
            c = a+b+t
        return c