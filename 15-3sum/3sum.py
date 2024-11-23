class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        for i in range(len(nums)-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            l=i+1
            r=len(nums)-1
            while l<r:
                totalsum=nums[i]+nums[l]+nums[r]
                if totalsum<0:
                    l+=1
                elif totalsum>0:
                    r-=1
                else:
                    newl=[nums[i],nums[l],nums[r]]
                    res.append(newl)
                    while l<r and nums[l]==newl[1]:
                        l+=1
                    while l<r and nums[r]==newl[2]:
                        r-=1
        return res
