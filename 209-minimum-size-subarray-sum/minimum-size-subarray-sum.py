class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        mins = float("inf")
        cs = 0
        
        k = 0
        for j in range(len(nums)):
            cs+=nums[j]
            if cs<target:
                continue
            if cs>=target:
                while cs>=target:
                    cs-=nums[k]
                    k+=1
                mins = min(mins,j-k+2)
        if mins == float("inf"):
            return 0
        return mins


        
        