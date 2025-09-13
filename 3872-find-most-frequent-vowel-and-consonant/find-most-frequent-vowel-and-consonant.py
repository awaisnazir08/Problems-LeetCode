class Solution(object):
    def maxFreqSum(self, s):
        """
        :type s: str
        :rtype: int
        """
        vowels = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

        consonants = {'b': 0}

        for ch in s:
            if ch in vowels:
                vowels[ch] += 1
            else:
                consonants[ch] = consonants.get(ch, 0) + 1
        
        return max(vowels.values()) + max(consonants.values())