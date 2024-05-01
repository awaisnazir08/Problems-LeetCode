class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        # Solution 1, 38/40
        # flag = True
        # for i in range(len(gas)):
        #     if gas[i] == cost[i]:
        #         continue
        #     else:
        #         flag = False
        #         break
        
        # if flag:
        #     return 0

        # max_heap = []

        # for i in range(len(gas)):
        #     if gas[i] - cost[i] >=0:
        #         heapq.heappush(max_heap, (-gas[i] + cost[i], i))

        # # Pop elements from the max heap (max element first)
        # while max_heap:
        #     priority_neg, index = heapq.heappop(max_heap)
        #     priority = -priority_neg  # Retrieve original priority (positive value)
        #     # print("Popped item:", value, "with priority:", priority)
        #     start_index = index
        #     j = start_index
        #     result = gas[j]
        #     while True:
        #         result -= cost[j]
        #         j += 1
        #         if j == len(cost):
        #             j = 0
        #         result += gas[j]
        #         if j == start_index:
        #             return start_index
        #         if result == 0 or result < cost[j]:
        #             break
        # return -1

        if sum(gas) < sum(cost):
            return -1
        
        total = 0
        res = 0
        for i in range(len(gas)):
            total += (gas[i] - cost[i])

            if total < 0:
                total = 0
                res = i + 1
        return res


