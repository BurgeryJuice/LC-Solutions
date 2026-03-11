class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nr = []
        nums.sort()
        hs = set()
        for i in range(len(nums)):
            if nums[i] in hs:
                continue
            hs.add(nums[i])
            a = i+1
            b = len(nums)-1
            while a<b:
                
                if nums[a]+nums[b]+nums[i]==0:
                    nr.append([nums[a],nums[b],nums[i]])
                    while a<b and nums[a]==nums[a+1]:
                        a+=1
                    while a<b and nums[b] == nums[b-1]:
                        b-=1
                    a+=1
                    b-=1
                elif nums[a]+nums[b]+nums[i]>0:
                    b-=1
                else :
                    a+=1
        return nr
                



