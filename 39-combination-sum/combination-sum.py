class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        als = []
        def a(su,i,arr):
            
            if su == target:
                als.append(arr)
                return
            if i >=len(nums) or su > target:
                return
            n = arr[:]
            n.append(nums[i])
            a(su+nums[i],i,n)
            a(su,i+1,arr[:])
            return
        a(0,0,[])
        return als

        