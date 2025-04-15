from collections import defaultdict
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        p_dict = {}
        # p_set = set()
        s_dict = {}
        indices = []
        for letter in p:
            if letter not in p_dict:
                p_dict[letter] = 0
            p_dict[letter] += 1
            # p_set.add(letter)
        window_size = len(p)
        for i in range(len(s)):
            if i - window_size >= 0:
                prev = s[i - window_size]
                s_dict[prev] -= 1
                if s_dict[prev] == 0:
                    del s_dict[prev]
            if s[i] not in s_dict:
                s_dict[s[i]] = 0
            s_dict[s[i]] += 1
            if s_dict == p_dict:
                indices.append(i - window_size + 1)
        
        return indices






      