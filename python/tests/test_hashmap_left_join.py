from hashtable.hashmap_left_join import hashmap_left_join
from hashtable.hashtable import Hashtable
import pytest

def test_when_hmap2_is_empty(hmap1, empty_hashtable):
    left_joined = hashmap_left_join(hmap1, empty_hashtable)
    assert len(left_joined.keys()) == 3
    assert left_joined.get("diligent") == ["employed", None]
    assert left_joined.get("fond") == ["enamored", None]
    assert left_joined.get("outfit") == ["grab", None]

def test_when_hmap1_is_empty(empty_hashtable, hmap2):
    left_joined = hashmap_left_join(empty_hashtable, hmap2)
    assert len(left_joined.keys()) == 0

def test_when_hmap1_hmap2_are_not_empty(hmap1, hmap2):
    left_joined = hashmap_left_join(hmap1, hmap2)
    assert len(left_joined.keys()) == 3
    assert left_joined.get("diligent") == ["employed", "idle"]
    assert left_joined.get("fond") == ["enamored", "averse"]
    assert left_joined.get("outfit") == ["grab", None]

@pytest.fixture
def empty_hashtable():
    empty = Hashtable()
    return empty

@pytest.fixture
def hmap1():
    hmap = Hashtable()
    hmap.add("diligent", "employed")
    hmap.add("fond", "enamored")
    hmap.add("outfit", "grab")
    return hmap

@pytest.fixture
def hmap2():
    hmap = Hashtable()
    hmap.add("diligent", "idle")
    hmap.add("fond", "averse")
    hmap.add("flow", "jam")
    return hmap