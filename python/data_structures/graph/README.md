# Graph

Implementation of Graph.

## Methods

add_node()
  - Arguments: value
  - Returns: The added node
  - Add a node to the graph

add_edge()
  - Arguments: 2 nodes to be connected by the edge, weight (optional)
  - Returns: nothing
  - Adds a new edge between two nodes in the graph
  - If specified, assign a weight to the edge
  - Both nodes should already be in the Graph

get_nodes()
  - Arguments: none
  - Returns all of the nodes in the graph as a collection (set, list, or similar)
  - Empty collection returned if there are no nodes

get_neighbors()
  - Arguments: node
  - Returns a collection of edges connected to the given node
    - Include the weight of the connection in the returned collection
  - Empty collection returned if there are no nodes

size()
  - Arguments: none
  - Returns the total number of nodes in the graph
  - 0 if there are none

breadth_first()
  - Arguments: Node
  - Return: A collection of nodes in the order they were visited.
  - Display the collection
