class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """

        memo = [False] * (len(s) + 1)
        memo[-1] = True

        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                if (i + len(w)) <= len(s) and s[i: i + len(w)] == w:
                    memo[i] = memo[i + len(w)]
                if memo[i]:
                    break
        return memo[0]
        
        