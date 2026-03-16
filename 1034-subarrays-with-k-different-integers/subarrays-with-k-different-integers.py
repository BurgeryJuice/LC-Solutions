class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        ak = 0
        ak1 = 0
        hm = {}
        l = 0
        j = 0
        for i in range(len(nums)):
            if nums[i] not in hm:
                hm[nums[i]] = 1
            else:
                hm[nums[i]]+=1
            if len(hm)>k:
                while len(hm)>k:
                    
                    if hm[nums[j]] == 1:
                        del hm[nums[j]]
                        
                    else:
                        hm[nums[j]]-=1
                        
                    j+=1
            ak += (i - j + 1)
        hm = {}
        j = 0
        for i in range(len(nums)):
            if nums[i] not in hm:
                hm[nums[i]] = 1
            else:
                hm[nums[i]]+=1
            if len(hm)>k-1:
                while len(hm)>k-1:
                    if hm[nums[j]] == 1:
                        del hm[nums[j]]
                        
                    else:
                        hm[nums[j]]-=1
                        
                    j+=1
            ak1 += (i - j + 1)
        return ak-ak1
