class Solution(object):
    def canBeTypedWords(self, text, brokenLetters):
        """
        :type text: str
        :type brokenLetters: str
        :rtype: int
        """

        words = text.split(" ")
        
        bL = set(brokenLetters)

        res = len(words)
        for word in words:
            if list(bL & set(word)):
                res -= 1

        return res



        