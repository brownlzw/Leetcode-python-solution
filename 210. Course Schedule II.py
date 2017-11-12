from collections import defaultdict,deque


class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        graph, indegrees = defaultdict(list), [0 for _ in range(numCourses)]
        for c1, c2 in prerequisites:
            graph[c2].append(c1)
            indegrees[c1] += 1
        indegrees_0 = deque()
        for course, degree in enumerate(indegrees):
            if not degree:
                indegrees_0.append(course)
        orders = []
        count = 0
        while indegrees_0:
            course = indegrees_0.popleft()
            count += 1
            orders.append(course)
            for conn in graph[course]:
                indegrees[conn] -= 1
                if not indegrees[conn]:
                    indegrees_0.append(conn)
        return orders if count == numCourses else []
