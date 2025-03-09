class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """

        my_dict = {1: "1"}
        for i in range(2, n + 1):

            to_count = my_dict[i - 1]

            left = 0
            current_string = ""
            current_count = 1
            for j in range(1, len(to_count)):
                if to_count[left] == to_count[j]:
                    current_count += 1
                else:
                    current_string += str(current_count)
                    current_string += to_count[left]
                    left = j
                    current_count = 1

            # if current_count > 1 or left == 0:
            current_string += str(current_count)
            current_string += to_count[-1]

            my_dict[i] = current_string

        return my_dict[n]