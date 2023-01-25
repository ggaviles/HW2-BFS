# write tests for bfs
import random

import pytest
import networkx as nx
from search import Graph

@pytest.fixture
def test_bfs_traversal():
    """
    TODO: Write your unit test for a breadth-first
    traversal here. Create an instance of your Graph class 
    using the 'tiny_network.adjlist' file and assert 
    that all nodes are being traversed (ie. returns 
    the right number of nodes, in the right order, etc.)
    """

    # Read '../data/tiny_network.adjlist' into Graph object
    graph = Graph('../data/tiny_network.adjlist')

    # Create list of nodes
    node_list = list(graph.nodes())

    # Select random node from the list of nodes
    random_node = random.choice(node_list)

    # Create list of nodes from breadth-first search
    graph_bfs_list = graph.bfs(random_node)

    # Read '../data/tiny_network.adjlist' in as nx.DiGraph object
    graph_comparison = nx.read_adjlist("../data/tiny_network.adjlist", create_using=nx.DiGraph, delimiter=";")

    # Call built-in bfs_tree method on nx.DiGraph object and store list of traversed nodes
    comparison_node_list = list(nx.bfs_tree(graph_comparison, source=random_node).nodes())

    assert comparison_node_list == graph_bfs_list


def test_bfs():
    """
    TODO: Write your unit test for your breadth-first 
    search here. You should generate an instance of a Graph
    class using the 'citation_network.adjlist' file 
    and assert that nodes that are connected return 
    a (shortest) path between them.
    
    Include an additional test for nodes that are not connected 
    which should return None. 
    """
    graph = Graph('../data/citation_network.adjlist')


    pass
