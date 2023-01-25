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

    def bfs(self, start, end=None):
        """
        TODO: write a method that performs a breadth first traversal and pathfinding on graph G

        * If there's no end node input, return a list nodes with the order of BFS traversal
        * If there is an end node input and a path exists, return a list of nodes with the order of the shortest path
        * If there is an end node input and a path does not exist, return None

        """

        # filename = input("Enter path to adjlist file: ")

        graph = self.graph

        # Initialize queue and list
        q = queue.Queue()
        visited = []

        if end is None:
            # Add start node to queue and visited list
            q.put(start)
            visited.append(start)

            while q:
                # break out of while loop once you have emptied the queue
                if q.empty():
                    return visited
                else:
                    # pop off first element of queue
                    v = q.get()

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

        elif end is not None and nx.has_path(graph, start, end):

            path_list = [[start]]
            index = 0

            # to keep track of previously visited nodes
            prev_nodes = {start}

            if start == end:
                return path_list[0]

            while index < len(path_list):
                curr_path = path_list[index]
                last_node = curr_path[-1]
                next_node_list = graph[last_node]

                if end in next_node_list:
                    curr_path.append(end)
                    return curr_path

                for next_node in next_node_list:
                    if next_node not in prev_nodes:
                        updated_path = curr_path[:]
                        updated_path.append(next_node)
                        path_list.append(updated_path)

                        prev_nodes.add(next_node)
                index += 1
            return []
        else:
            return None


