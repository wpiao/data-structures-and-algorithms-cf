from graph.graph import Graph, Vertex, Edge
import pytest

def test_with_empty_graph(empty_graph):
    assert empty_graph.adjacency_list == {}
    assert empty_graph.nodes == []

def test_graph_methods():
    g = Graph()
    # test add_node method
    assert g.size() == 0
    g.add_node('a')
    assert g.size() == 1
    g.add_node('b')
    assert g.size() == 2
    g.add_node('c')
    assert g.size() == 3
    assert g.nodes[0].value == 'a'
    assert g.nodes[1].value == 'b'
    assert g.nodes[2].value == 'c'
    assert len(g.nodes) == 3

    # test add_edge method
    a = g.nodes[0]
    b = g.nodes[1]
    c = g.nodes[2]
    g.add_edge(a, b, 3)
    assert g.adjacency_list[a]['nodes'][0][0] == b
    assert g.adjacency_list[a]['nodes'][0][1] == 3
    assert g.adjacency_list[b]['nodes'][0][0] == a
    assert g.adjacency_list[b]['nodes'][0][1] == 3
    g.add_edge(a, c, 4)
    assert g.adjacency_list[a]['nodes'][1][0] == c
    assert g.adjacency_list[a]['nodes'][1][1] == 4
    assert g.adjacency_list[c]['nodes'][0][0] == a
    assert g.adjacency_list[c]['nodes'][0][1] == 4
    g.add_edge(b, c, 5)
    assert g.adjacency_list[b]['nodes'][1][0] == c
    assert g.adjacency_list[b]['nodes'][1][1] == 5
    assert g.adjacency_list[c]['nodes'][1][0] == b
    assert g.adjacency_list[c]['nodes'][1][1] == 5

    # test get_node method
    assert len(g.get_node()) == 3
    assert g.get_node()[0] == a
    assert g.get_node()[1] == b
    assert g.get_node()[2] == c

    # test get_neighbor method
    assert g.get_neighbor(a)[0].weight == 3
    assert g.get_neighbor(a)[0].v1 == a
    assert g.get_neighbor(a)[0].v2 == b
    assert g.get_neighbor(a)[1].weight == 4
    assert g.get_neighbor(a)[1].v1 == a
    assert g.get_neighbor(a)[1].v2 == c
    assert g.get_neighbor(b)[0].weight == 3
    assert g.get_neighbor(b)[0].v1 == a
    assert g.get_neighbor(b)[0].v2 == b
    assert g.get_neighbor(b)[1].weight == 5
    assert g.get_neighbor(b)[1].v1 == b
    assert g.get_neighbor(b)[1].v2 == c
    assert g.get_neighbor(c)[0].weight == 4
    assert g.get_neighbor(c)[0].v1 == a
    assert g.get_neighbor(c)[0].v2 == c
    assert g.get_neighbor(c)[1].weight == 5
    assert g.get_neighbor(c)[1].v1 == b
    assert g.get_neighbor(c)[1].v2 == c

    # test size method
    assert g.size() == 3
@pytest.fixture
def empty_graph():
    return Graph()
