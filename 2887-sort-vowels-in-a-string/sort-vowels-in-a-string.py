class Solution(object):
    def sortVowels(self, s):
        """
        :type s: str
        :rtype: str
        """

        vowels = "AaEeIiOoUu"

        vows = ''
        for i, ch in enumerate(s):
            if s[i] in vowels:
                vows += s[i]
        
        vows = sorted(vows)

        loc = 0
        res = ''
        for i, ch in enumerate(s):
            if ch in vowels:
                res += vows[loc]
                loc += 1
            else:
                res += ch

        
        return res

        
        