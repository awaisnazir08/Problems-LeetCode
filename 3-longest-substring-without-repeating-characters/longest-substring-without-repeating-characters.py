class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        left = 0
        max_length = 0
        freq = {}

        for right in range(len(s)):
            freq[s[right]] = freq.get(s[right], 0) + 1

            if freq[s[right]] == 1:
                max_length = max(max_length, right - left + 1)
            else:
                while left < right and freq[s[right]] > 1:
                    freq[s[left]] -= 1
                    left += 1
                max_length = max(max_length, right - left + 1)
        
        return max_length



