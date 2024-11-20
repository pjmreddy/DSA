class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack=[]
        map={'}':'{',')':'(',']':'['}
        for i in s:
            if i in map:
                if stack:
                    top=stack.pop()
                else:
                    top="x"

                if map[i]!=top:
                    return False
            else:
                stack.append(i)
                
        return not stack

        