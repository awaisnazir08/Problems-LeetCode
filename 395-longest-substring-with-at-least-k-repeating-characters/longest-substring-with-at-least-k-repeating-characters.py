class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if len(s) < k:
            return 0
        freq = {}

        for c in s:
            freq[c] = freq.get(c, 0) + 1
        
        for c in s:
            if freq[c] < k:
                return max(self.longestSubstring(t, k) for t in s.split(c))
        
        return len(s)


        