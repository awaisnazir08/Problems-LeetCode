class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:

        res = []

        target = len(graph) - 1

        def dfs(node, path):
            if path[-1] == target:
                res.append(list(path))
                return
            
            for vertice in graph[node]:
                path.append(vertice)
                dfs(vertice, path)
                path.pop()
        
        dfs(0, [0])

        return res

        