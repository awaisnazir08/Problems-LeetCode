class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        prefix = strs[0]

        for s in strs:
            current = ''
            for i in range(min(len(s), len(prefix))):
                if s[i] == prefix[i]:
                    current += (s[i])
                else: 
                    break
            prefix = current
        return prefix

        