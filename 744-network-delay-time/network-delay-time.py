import heapq
class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        heap = []
        adj_list = {}
        for item in times:
            if item[0] not in adj_list:
                adj_list[item[0]] = []
            adj_list[item[0]].append((item[1], item[2]))
        # print(adj_list)
        # Create the heap
        distances = [float('inf')] * (n + 1)
        visited = [False] * (n + 1)
        visited[0] = True
        distances[k] = 0

        heapq.heappush(heap, (0, k))
        while heap:
            current_distance, node = heapq.heappop(heap)
            if visited[node]:
                continue
            visited[node] = True
            for neighbor, weight in adj_list.get(node, []):
                if current_distance + weight < distances[neighbor]:
                    distances[neighbor] = current_distance + weight
                    heapq.heappush(heap, (distances[neighbor], neighbor))
        for i in visited:
            if not i:
                return - 1
        
        return max(distances[1:])
        

        