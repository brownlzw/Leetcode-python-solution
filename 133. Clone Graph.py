# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []


class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):

        if node == None:
            return None
        root = UndirectedGraphNode(node.label)
        dic = {root.label: root}
        st = []
        st.append(node)
        while st:
            cur = st.pop()
            for neighbour in cur.neighbours:
                if neighbour.label not in dic:
                    copy = UndirectedGraphNode(neighbour.label)
                    dic[neighbour.label] = copy
                dic[cur.label].neighbors.append(dic[neighbour.label])
                st.append(neighbour)
        return root

        return root

    # dfs O(n), O(1)

    def bfs(self, que, dic):
        while len(que) > 0:
            node = que.pop()
            for neighbor in node.neighbors:
                if neighbor in dic:
                    dic[node].neighbors.append(dic[neighbor])
                else:
                    nodecopy = UndirectedGraphNode(neighbor.label)
                    dic[neighbor] = nodecopy
                    dic[node].neighbors.append(dic[neighbor])
                    que.append(neighbor)
