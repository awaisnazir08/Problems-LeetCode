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
                vowels[ch] += 1
                count_vowels += 1
        
        if count_vowels == 0:
            return False
        elif count_vowels % 2 != 0:
            return True
        return True
        
        turn = 1
        win = False
        count = 0
        for i, ch in enumerate(s):
            if ch in vowels:
                count += 1
            if (turn == 1) and (count % 2 != 0):
                win = True
                count = 0
                turn = 0
            elif (turn == 0) and (count % 2 == 0):
                win = False
                count = 0
                turn = 1
        
        return win
    
            




