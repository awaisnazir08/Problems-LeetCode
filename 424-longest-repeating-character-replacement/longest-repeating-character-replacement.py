class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        map = {}

        res = 0

        left = 0
        
        for right in range(len(s)):
            map[s[right]] = 1 + map.get(s[right], 0)

            while right - left + 1 - max(map.values()) > k:
                map[s[left]] -= 1
                left += 1

            res = max(res, right - left + 1)
        
        return res


        