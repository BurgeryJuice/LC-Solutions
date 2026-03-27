class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        mem = {}
        def r(i,cc):
            if cc<0 or i>= len(coins):
                return float("inf")
            if cc == 0:
                return 0
            if (cc,i) in mem:
                return mem[(cc,i)]
            mem[cc,i] = min(r(i+1,cc),1+r(i,cc-coins[i]))
            return mem[(cc,i)]
        if r(0,amount) == float("inf"):
            return -1
        return r(0,amount)

