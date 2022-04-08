from graph.graph import Graph
from graph.business_trip import business_trip
import pytest

def test_business_trip_function(cities):
    assert business_trip(cities, ['los angeles', 'seattle']) == (True, '$82')
    assert business_trip(cities, ['chicago', 'MIami', 'las vegas']) == (True, '$115')
    assert business_trip(cities, ['las vegas', 'seattle']) == (False, '$0')
    assert business_trip(cities, ['san diego', 'chicaGo', 'las vegas']) == (False, '$0')
    assert business_trip(cities, ['seaTTle', 'chicago', 'las vegas']) == (False, '$0')
    assert business_trip(cities, ['new york', 'boston']) == (False, '$0')

@pytest.fixture
def cities():
    g = Graph()
    seattle = g.add_node('Seattle')
    chicago = g.add_node('Chicago')
    los_angeles = g.add_node('Los Angeles')
    miami = g.add_node('Miami')
    san_diego = g.add_node('San Diego')
    las_vegas = g.add_node('Las Vegas')
    g.add_edge(seattle, chicago, 150)
    g.add_edge(seattle, los_angeles, 82)
    g.add_edge(chicago, los_angeles, 99)
    g.add_edge(chicago, miami, 42)
    g.add_edge(los_angeles, miami, 105)
    g.add_edge(los_angeles, las_vegas, 26)
    g.add_edge(los_angeles, san_diego, 37)
    g.add_edge(miami, las_vegas, 73)
    g.add_edge(miami, san_diego, 250)
    return g