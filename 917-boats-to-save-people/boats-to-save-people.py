class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """

        """Solution 1"""
        # people.sort(reverse = True)
        # dic = {}
        # for person in people:
        #     if person not in dic:
        #         dic[person] = 1
        #     else:
        #         dic[person] += 1
        # boats = 0
        # for person in people:
        #     if dic[person] == 0:
        #         continue
        #     dic[person] -= 1
        #     if person == limit:
        #         boats += 1
        #         continue
        #     elif person < limit:
        #         rem = limit - person
        #         temp = rem
        #         while True:
        #             if temp in dic and dic[temp] > 0:
        #                 dic[temp] -= 1
        #                 boats += 1
        #                 break
        #             else:
        #                 temp -= 1
        #                 if temp == 0:
        #                     boats += 1
        #                     break

        # return boats
        """ Solution 2"""
        people.sort()
        right = len(people) - 1
        left = res = 0
        while left <= right:
            res += 1
            if people[left] + people[right] <= limit:
                left += 1
            right -= 1
        return res



                    

        