class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        result = []

        if len(s) > 12:
            return result
        
        def backtrack(i, dots, curIP):
            if dots == 4 and i == len(s):
                result.append(curIP[:-1])
                return
            if dots > 4:
                return
            for j in range(i, min(i + 3, len(s))):
                if int(s[i: j + 1]) <= 255:
                    if s[i] == '0' and i != j:
                        continue
                    backtrack(j + 1, dots + 1, curIP + s[i:j+1] + '.')

        backtrack(0,0,'')
        return result
        