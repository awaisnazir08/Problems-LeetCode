class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:

        current_word, current_index = sorted(words[0]), 0
        indexes_to_remove = []
        for i in range(1, len(words)):
            if current_word == sorted(words[i]):
                indexes_to_remove.append(i)
            else:
                current_word, current_index = sorted(words[i]), i
        
        remaining_words = []
        for i in range(len(words)):
            if i not in indexes_to_remove:
                remaining_words.append(words[i])
        
        return remaining_words





        