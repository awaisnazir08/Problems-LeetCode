class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        map = {}

        l = 0
        res = 0

        for r in range(len(s)):
            map[s[r]] = map.get(s[r], 0) + 1

            h = max(map.values())

            if h == 1:
                res = max(res, r - l + 1)
            else:
                while h > 1:
                    map[s[l]] -= 1
                    l += 1
                    h = max(map.values())
            
        
        return res

                



        