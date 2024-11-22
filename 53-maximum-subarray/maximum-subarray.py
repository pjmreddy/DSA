class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur=0
        maxsum= -inf
        for num in nums:
            cur=max(cur+num, num)
            maxsum=max(cur,maxsum)
        return maxsum
        