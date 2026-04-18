class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        nums = nums[::-1]
        md = float("inf")
        hm = {}
        for i in range(len(nums)):
            a = int(str(nums[i])[::-1])
            if a in hm:
                md = min(md,i-hm[a])
            hm[nums[i]] = i
        if md == float("inf"):
            return -1
        return md