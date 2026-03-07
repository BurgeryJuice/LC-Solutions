class Solution(object):
    def twoSum(self, nums, target):
        i = 0
        # Preserve original indices
        indexed_nums = list(enumerate(nums))
        # Sort based on values
        indexed_nums.sort(key=lambda x: x[1])

        while i < len(indexed_nums):
            newtarget = target - indexed_nums[i][1]
            beg = i + 1
            end = len(indexed_nums) - 1

            while beg <= end:
                mid = (beg + end) // 2
                if indexed_nums[mid][1] == newtarget:
                    return [indexed_nums[i][0], indexed_nums[mid][0]]
                elif indexed_nums[mid][1] < newtarget:
                    beg = mid + 1
                else:
                    end = mid - 1

            i += 1
        return []