import os
import queue
import networkx as nx

class Graph:
    """
    Class to contain a graph and your bfs function
    
    You may add any functions you deem necessary to the class
    """
    def __init__(self, filename: str):
        """
        Initialization of graph object 
        """
        self.graph = nx.read_adjlist(filename, create_using=nx.DiGraph, delimiter=";")

    def bfs(self, start, end):
        """
        TODO: write a method that performs a breadth first traversal and pathfinding on graph G

        * If there's no end node input, return a list nodes with the order of BFS traversal
        * If there is an end node input and a path exists, return a list of nodes with the order of the shortest path
        * If there is an end node input and a path does not exist, return None

        """

        # filename = input("Enter path to adjlist file: ")

        graph = self.graph # write terminal prompt for path to file
        q = queue.Queue()
        visited = []
        q.put(start)
        visited.append(start)
        while q:
            v = q.get()
            n = [n for n in nx.neighbors(graph, v)]
            for w in n:
                if w not in visited:
                    visited.append(w)
                    q.put(w)
        print(q)


        """
        add source node to queue
        add source neighbors to queue
        go to first node in queue
        add its neighbors
        go to next node in queue
        add its neighbors to queue
        check if in queue already, don't add
        
        """

        """
        if end is None:
            return *list of nodes with order of BFS traversal*
        else:
            if path exists:
                return *list of nodes with order of shortest path*
            else:
                return None

        return
        """


