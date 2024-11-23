class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        cur=[]
        intervals.sort(key=lambda x:x[0])

        pre=intervals[0]

        for i in intervals[1:]:
            if i[0] <= pre[1]:
                pre[1]=max(pre[1],i[1])
            else:
                cur.append(pre)
                pre=i
            
        cur.append(pre)

        return cur