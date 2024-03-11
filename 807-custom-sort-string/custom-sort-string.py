class Solution(object):
    def customSortString(self, order, s):
        """
        :type order: str
        :type s: str
        :rtype: str
        """
        # i = 0
        # s = list(s)
        # for element in order:
        #     index_location = s.find(element)
        #     if index_location == -1:
        #         continue
        #     s[i], s[index_location] = s[index_location], s[i]
        #     i += 1
        # return ''.join(s)
        
        my_dict = {}
        for element in s:
            if element not in my_dict:
                my_dict[element] = 1
            else:
                my_dict[element] +=1
                
        result = []
        for letter in order:
            if letter in my_dict:
                while my_dict[letter] > 0:
                    result.append(letter)
                    my_dict[letter] -= 1
        for key in my_dict:
            while my_dict[key] > 0:
                result.append(key)
                my_dict[key] -= 1
        return ''.join(result)
                