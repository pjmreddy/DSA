class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(set(nums))==len(nums):
            return False
        return True
        # sol = {}
        # for i in nums:
        #     sol[i]=1+sol.get(i,0)
        #     if sol.get(i)>1:
        #         return True
        # return False
        