class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = set()

        if len(s) <= 10:
            return []
        
        i = 0
        j = 10
        map = {}
        while j <= len(s):
            if s[i:j] not in map:
                map[s[i:j]] = 1
            else:
                res.add(s[i:j])
            i += 1
            j += 1
        
        return list(res)

        