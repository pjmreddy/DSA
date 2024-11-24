class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start=0
        check=set()
        mlen=0

        for i in range(len(s)):
            while s[i] in check:
                check.remove(s[start])
                start+=1

            check.add(s[i])
            mlen=max(mlen,(i-start+1))
        return mlen
        