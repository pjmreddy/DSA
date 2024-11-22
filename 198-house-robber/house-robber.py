class Solution:
    def rob(self, nums: List[int]) -> int:
        sum1,sum2=0,0
        for i in nums:
            cur=max(sum1,sum2+i)
            sum2, sum1=sum1,cur
        return sum1