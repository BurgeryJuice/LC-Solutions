class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        a = 0
        b = 0
        c = 0
        d = 1
        for i in range(len(cost)-1):
           t = a 
           a = b
           b = min(t+cost[c],a+cost[d])
           c+=1
           d+=1
        return b 

