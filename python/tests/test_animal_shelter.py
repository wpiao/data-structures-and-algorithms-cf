from stack_and_queue.animal_shelter import Cat, Dog, AnimalShelter
import pytest

def test_animalshelter(empty_animalshelter, dog, cat):
    # test enqueue method
    assert empty_animalshelter.front == None
    empty_animalshelter.enqueue(dog)
    assert empty_animalshelter.front.value.animal_name == "dog"
    assert empty_animalshelter.front.next == None
    empty_animalshelter.enqueue(cat)
    assert empty_animalshelter.front.value.animal_name == "dog"
    assert empty_animalshelter.front.next.value.animal_name == "cat"
    empty_animalshelter.enqueue(cat)
    assert empty_animalshelter.front.next.next.value.animal_name == "cat"
    assert empty_animalshelter.front.next.next.next == None

    # test dequeue method
    # front <- {dog} <- {cat} <- {cat}
    assert empty_animalshelter.front.value.animal_name == "dog"
    dequeued = empty_animalshelter.dequeue("lion")
    assert dequeued.value.animal_name == "dog"
    assert empty_animalshelter.front.value.animal_name == "cat"
    assert empty_animalshelter.front.next.value.animal_name == "cat"
    assert empty_animalshelter.front.next.next == None
    dequeued = empty_animalshelter.dequeue("dog")
    assert dequeued == None
    dequeued = empty_animalshelter.dequeue("cat")
    assert dequeued.value.animal_name == "cat"
    assert empty_animalshelter.front.value.animal_name == "cat"
    assert empty_animalshelter.front.next == None
    dequeued = empty_animalshelter.dequeue("dog")
    assert dequeued == None
    dequeued = empty_animalshelter.dequeue("cat")
    assert dequeued.value.animal_name == "cat"
    assert empty_animalshelter.front == None

@pytest.fixture
def dog():
    return Dog()

@pytest.fixture
def cat():
    return Cat()

@pytest.fixture
def empty_animalshelter():
    return AnimalShelter()
