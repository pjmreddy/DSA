class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res = {}
        for ix, num in enumerate(nums):
            if target -  num in res:
                return [ix,res[target-num]]
            res[num] = ix        