from hashtable.hashtable import Hashtable
import pytest

def test_hashtable(hashtable):
    assert hashtable.size == 1024
    assert hashtable.buckets[0] == None
    assert hashtable.buckets[1023] == None
    assert len(hashtable.buckets) == 1024

    # test hash method
    assert hashtable.hash('cat') == 652
    assert hashtable.hash('DOG') == 498

    # test add method
    hashtable.add('cat', 'cat is stored at index 652')
    hashtable.add('DOG', 'DOG is stored at index 498')
    assert hashtable.buckets[652].head.value == {'cat': 'cat is stored at index 652'}
    assert hashtable.buckets[498].head.value == {'DOG': 'DOG is stored at index 498'}

    # test add method with duplicate key
    hashtable.add('cat', 'Duplicate: cat is stored at index 652')
    assert hashtable.buckets[652].head.value == {'cat': 'Duplicate: cat is stored at index 652'}

    # test get method with key that exists in the hashtable
    assert hashtable.get('cat') == 'Duplicate: cat is stored at index 652'
    assert hashtable.get('DOG') == 'DOG is stored at index 498'

    # test get method with key that doesn't exist in the hashtable
    with pytest.raises(KeyError, match='key tiger does not exist in this hashtable!'):
        hashtable.get('tiger')

    # test keys method
    assert hashtable.keys() == ['DOG', 'cat']

    # test contains method
    assert hashtable.contains('cat') == True
    assert hashtable.contains('DOG') == True
    assert hashtable.contains('dog') == False

@pytest.fixture
def hashtable():
    return Hashtable()