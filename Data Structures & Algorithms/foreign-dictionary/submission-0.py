class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graph=defaultdict(set)
        inDegree={ch:0 for word in words for ch in word}

        for i in range(len(words)-1):
            w1=words[i]
            w2=words[i+1]
            minLen=min(len(w1),len(w2))

            if w1[:minLen] == w2[:minLen] and len(w1) > len(w2):
                return ""

            for j in range(minLen):
                if w1[j] != w2[j]:
                    if w2[j] not in graph[w1[j]]:
                        graph[w1[j]].add(w2[j])
                        inDegree[w2[j]] += 1
                    break

        queue=deque([i for i in inDegree if inDegree[i] ==0])
        order=[]
        while queue:
            node=queue.popleft()
            order.append(node)
            for neighbour in graph[node]:
                inDegree[neighbour] -=1
                if inDegree[neighbour] ==0:
                    queue.append(neighbour)

        

        return "".join(order) if len(order) == len(inDegree) else ""
        

        