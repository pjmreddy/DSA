class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        sol = {}
        for i in nums:
            sol[i] = 1+sol.get(i,0)
        x=[]
        for num in sol.keys():
            heapq.heappush(x,(sol[num],num))
            if len(x)>k:
                heapq.heappop(x)
        
        res=[]
        for i in range(k):
            res.append(heapq.heappop(x)[1])
        return res
        
        