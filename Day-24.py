from collections import defaultdict
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        self.ans = []
        
        def createGraph():
            self.g = defaultdict(list)
            for idx, nodelist in enumerate(graph):
                for node in nodelist:
                    self.g[idx].append(node)
        
        def dfs(source, destination, path):
            if source == destination:
                self.ans.append(path)
                return
            for adj in self.g[source]:
                dfs(adj, destination, path + [adj])
        
        createGraph()
        dfs(0, len(graph)-1, [0])
        return self.ans