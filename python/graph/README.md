# Graph Breadth First Search Implementation - 04/04/2022

## Challenges

No Challenges

## API

- breadth_first_search
  - Arguments: vertex/node
  - Returns a list of vertex in the order they were visited

## Unit tests

Run command `pytest python/tests/test_graph.py` to run unit tests.

# Graph implementation - 03/29/2022

## Challenges

No Challenges

## API

- add node

  - Arguments: value
  - Returns: The added node
  - Add a node to the graph

- add edge
  - Arguments: 2 nodes to be connected by the edge, weight (optional)
  - Returns: nothing
  - Adds a new edge between two nodes in the graph
  - If specified, assign a weight to the edge
  - Both nodes should already be in the Graph
- get nodes
  - Arguments: none
  - Returns all of the nodes in the graph as a collection (set, list, or similar)
- get neighbors
  - Arguments: node
  - Returns a collection of edges connected to the given node
  - Include the weight of the connection in the returned collection
- size
  - Arguments: none
  - Returns the total number of nodes in the graph

## Unit tests

Run command `pytest tests/test_graph.py` to run unit tests.
