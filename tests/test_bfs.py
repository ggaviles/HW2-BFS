# write tests for bfs
import random
import pytest
import networkx as nx
from search import Graph

def test_bfs_traversal():
    """
    TODO: Write your unit tests for a breadth-first
    traversal here. Create an instance of your Graph class 
    using the 'tiny_network.adjlist' file and assert 
    that all nodes are being traversed (i.e. returns
    the right number of nodes, in the right order, etc.)
    """

    # Read '../data/tiny_network.adjlist' in as Graph object
    graph = Graph('../data/tiny_network.adjlist')

    # Create list of nodes in Graph object
    node_list = list(graph.nodes())

    # Select random node from the list of nodes
    random_node = random.choice(node_list)

    # Call your own bfs method on Graph object and store list of traversed nodes
    graph_bfs_list = graph.bfs(random_node)

    # Read '../data/tiny_network.adjlist' in as nx.DiGraph object
    graph_comparison = nx.read_adjlist("../data/tiny_network.adjlist", create_using=nx.DiGraph, delimiter=";")

    # Call built-in bfs_tree method on nx.DiGraph object and store list of traversed nodes
    comparison_node_list = list(nx.bfs_tree(graph_comparison, source=random_node).nodes())

    # Compare lists of traversed nodes using bfs method you wrote vs bfs method built into nx.DiGraph object
    assert comparison_node_list == graph_bfs_list


def test_bfs():
    """
    TODO: Write your unit tests for your breadth-first
    search here. You should generate an instance of a Graph
    class using the 'citation_network.adjlist' file 
    and assert that nodes that are connected return 
    a (shortest) path between them.
    
    Include an additional tests for nodes that are not connected
    which should return None. 
    """
    # Read '../data/tiny_network.adjlist' in as Graph object
    graph = Graph('../data/citation_network.adjlist')

    # Read '../data/tiny_network.adjlist' in as nx.DiGraph object
    graph_comparison = nx.read_adjlist("../data/citation_network.adjlist", create_using=nx.DiGraph, delimiter=";")

    # Create list of nodes in Graph object
    node_list = list(graph.nodes())

    # Select random start node from the list of nodes
    random_start_node = random.choice(node_list)

    # Select random end node from the list of nodes
    random_end_node = random.choice(node_list)

    if nx.has_path(graph_comparison, source=random_start_node, target=random_end_node) is False:
        pass
    else:
        # Call your own bfs method on Graph object and store list of traversed nodes
        graph_bfs_list = graph.bfs(random_start_node, random_end_node)

        # Call built-in shortest_path method on nx.DiGraph object and store list of traversed nodes
        comparison_node_list = list(
            nx.shortest_path(graph_comparison, source=random_start_node, target=random_end_node, weight=None))

        # Compare lists of traversed nodes using bfs method you wrote vs shortest_path method built into nx.DiGraph object
        assert comparison_node_list == graph_bfs_list
