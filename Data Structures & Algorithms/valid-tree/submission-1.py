class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n == 0:
            return False
        if len(edges) != n-1:
            return False
        graph=defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited=set()
        q=deque([0])
        while q:
            node=q.popleft()
            if node in visited:
                continue
            visited.add(node)
            for neighbour in graph[node]:
                if neighbour not in visited:
                    q.append(neighbour)
                else:
                    graph[neighbour].remove(node)

        return len(visited) == n
        