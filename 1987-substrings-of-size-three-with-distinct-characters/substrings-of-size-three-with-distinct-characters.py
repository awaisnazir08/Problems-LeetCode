class Solution:
    def countGoodSubstrings(self, s: str) -> int:

        count_set = set()

        n = len(s)
        if n < 3:
            return 0
        
        res = 0

        for i in range(n - 2):
            if s[i] != s[i + 1] and s[i + 1] != s[i + 2] and s[i] != s[i + 2]:
                res += 1
        
        return res


        