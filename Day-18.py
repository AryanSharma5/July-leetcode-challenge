from collections import defaultdict, deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
    	self.graph = defaultdict(list)
    	self.count = 0
    	toposort = []

    	def createGraph():
    		for u, v in prerequisites:
    			self.graph[v].append(u)
    	createGraph()

    	indegree = [0]*numCourses
    	for _, e in self.graph.items():
    		for node in e:
    			indegree[e] += 1

    	queue = deque()
    	for node, deg in enumerate(indegree):
    		if deg == 0:
    			queue.append(node)
    	while queue:
    		curNode = queue.popleft()
    		toposort.append(curNode)
    		self.count += 1
    		for neigh in self.graph[curNode]:
    			indegree[neigh] -= 1
    			if indegree[neigh] == 0:
    				queue.append(neigh)
    	if self.count != numCourses:
    		return []
    	return toposort