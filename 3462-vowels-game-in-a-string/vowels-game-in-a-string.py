class Solution(object):
    def doesAliceWin(self, s):
        """
        :type s: str
        :rtype: bool
        """

        count_vowels = 0

        vowels = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

        for ch in s:
            if ch in vowels:
                count_vowels += 1
        
        if count_vowels == 0:
            return False
        else:
            return True
        
    
            




