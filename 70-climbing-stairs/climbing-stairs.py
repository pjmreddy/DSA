class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1:
            return 1
        a=1
        b=1
        total=0
        for i in range(n-1):
            total=a+b
            b=a
            a=total
        return total