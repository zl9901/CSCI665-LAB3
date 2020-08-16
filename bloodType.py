
"""
Python program for finding min-cut in the given graph
Complexity : (E*(V^3))
Total augmenting path = VE and BFS with adj matrix takes :V^2 times
"""

import math

class Graph:

    def __init__(self, graph):
        """
        self.graph is residual graph
        org_graph is the original graph which is not modified
        """
        self.graph = graph
        self.org_graph = [i[:] for i in graph]
        self.row = len(graph)
        self.column = len(graph[0])
        self.parent={}

    """
    using BFS to implement the maxFlow algorithm
    """
    def BFS(self,source,sink):

        self.parent.clear()
        queue=[]
        visited=set()

        queue.append(source)
        visited.add(source)
        self.parent[source]=None

        while queue:
            u=queue.pop(0)
            for index,value in enumerate(self.graph[u]):
                """
                value > 0 means there is a way between two vertices
                """
                if value>0 and index not in visited:
                    visited.add(index)
                    self.parent[index]=u
                    queue.append(index)
        return True if sink in visited else False

    """
    the goal of this function is to show the residue graph
    """
    def minCut(self,source, sink):
        maxFlow=0

        while self.BFS(source,sink):
            path = math.inf
            self.t=sink
            while self.parent[self.t] is not None:
                u=self.parent[self.t]
                v=self.t
                path=min(path,self.graph[u][v])
                self.t=self.parent[self.t]

            maxFlow+=path

            self.index=sink
            while self.parent[self.index] is not None:
                u = self.parent[self.index]
                v = self.index
                self.graph[u][v]-=path
                self.graph[v][u]+=path
                self.index = self.parent[self.index]

        # for i in range(0,self.row):
        #     for j in range(0,self.column):
        #         if self.graph[i][j]==0 and self.org_graph[i][j]>0:
        #             print(str(i)+"-"+str(j))
        print()
        print("residue graph is shown as followed: ")
        print(self.graph)
        print()
        print("Maxflow is "+str(maxFlow))

def main():
    """
    the adjacent list according to the requirements
    """
    graph = [[0, 50, 36, 11, 8, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, math.inf, math.inf, math.inf, math.inf, 0],
             [0, 0, 0, 0, 0, 0, math.inf, 0, math.inf, 0],
             [0, 0, 0, 0, 0, 0, 0, math.inf, math.inf, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, math.inf, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 45],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 42],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 8],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
             ]
    g = Graph(graph)
    source = 0
    sink = g.row-1
    g.minCut(source, sink)


if __name__ == '__main__':
    main()