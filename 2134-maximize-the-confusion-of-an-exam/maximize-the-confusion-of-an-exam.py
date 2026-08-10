class Solution(object):
    def maxConsecutiveAnswers(self, answerKey, k):
        """
        :type answerKey: str
        :type k: int
        :rtype: int
        """
        
        dictionary = {}

        res = 0

        left = 0

        for right in range(len(answerKey)):
            dictionary[answerKey[right]] = dictionary.get(answerKey[right], 0) + 1

            while (right - left + 1) - max(dictionary.values()) > k:
                dictionary[answerKey[left]] -= 1
                left += 1
            res = max(res, right - left + 1)

        return res            
