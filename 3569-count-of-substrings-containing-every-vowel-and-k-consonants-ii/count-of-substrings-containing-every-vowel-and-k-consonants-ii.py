class Solution(object):
    def countOfSubstrings(self, word, k):
        """
        :type word: str
        :type k: int
        :rtype: int
        """

        def atleastk(k):
            vowels = defaultdict(int)
            consonants = 0
            result = 0
            left = 0
            for right in range(len(word)):
                if word[right] in "aeiou":
                    vowels[word[right]] += 1
                else:
                    consonants += 1
                
                while len(vowels) == 5 and consonants >= k:
                    result += (len(word) - right)

                    if word[left] in 'aeiou':
                        vowels[word[left]] -= 1
                        if vowels[word[left]] == 0:
                            vowels.pop(word[left])
                    else:
                        consonants -= 1
                    
                    left += 1
            return result
        
        return atleastk(k) - atleastk(k + 1)

        
        