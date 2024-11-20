class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
     """
        maxc=0
        minc=prices[0]
        mp=0
        for i in prices:
            if i<minc:
                minc=i
                maxc=i
            elif i>maxc:
                maxc=i
                mp=max(mp,maxc - minc)
        return mp
    