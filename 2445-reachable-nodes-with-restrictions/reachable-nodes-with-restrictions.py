from collections import deque
from typing import List

class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        dictionary = {i: [] for i in range(n)}
        restricted_set = set(restricted)

        for u, v in edges:
            dictionary[u].append(v)
            dictionary[v].append(u)

        visited = set(restricted)  # mark restricted nodes as visited
        q = deque([0])
        visited.add(0)

        while q:
            node = q.popleft()
            for neighbor in dictionary[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    q.append(neighbor)

        return len(visited) - len(restricted)  # subtract restricted nodes
