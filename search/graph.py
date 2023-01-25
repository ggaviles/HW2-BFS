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

    def bfs(self, start, end_node=None):
        """
        TODO: write a method that performs a breadth first traversal and pathfinding on graph G

        * If there's no end node input, return a list nodes with the order of BFS traversal
        * If there is an end node input and a path exists, return a list of nodes with the order of the shortest path
        * If there is an end node input and a path does not exist, return None

        """

        # filename = input("Enter path to adjlist file: ")

        graph = self.graph  # write terminal prompt for path to file

        # Initialize queue and list
        q = queue.Queue()
        visited = []

        if end_node==None:
            # Add start node to queue and visited list
            q.put(start)
            visited.append(start)

            while q:

                if q.empty():
                    break
                else:
                    # pop off first element of queue
                    v = q.get()
                    print(str(v) + " ", end="")

                    # return list of neighbors of popped off element
                    neighbor_list = [n for n in nx.neighbors(graph, v)]

                    # iterate through neighbors list
                    for neighbors in neighbor_list:
                        # if neighbor is not in visited list
                        if neighbors not in visited:
                            # add neighbor to visited list
                            visited.append(neighbors)
                            # add neighbor to queue
                            q.put(neighbors)
                    q.task_done()
        return


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


