from collections import deque
class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        dictionary = {}
        visited = set(restricted)
        q = deque()
        q.append(0)

        for edge in edges:
            n1, n2 = edge
            if n1 not in dictionary:
                dictionary[n1] = []
            if n2 not in dictionary:
                dictionary[n2] = []
            dictionary[n1].append(n2)
            dictionary[n2].append(n1)
        visited.add(0)
        
        while q:
            node = q.popleft()
            visited.add(node)
            for adjacent_node in dictionary[node]:
                if adjacent_node not in visited:
                    q.append(adjacent_node)
        
        return len(visited) - len(restricted)

        
        
