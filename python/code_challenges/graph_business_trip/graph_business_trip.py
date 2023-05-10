from data_structures.queue.queue import Queue

def direct_flights(graph, arr):
    """
    Determines whether the trip is possible with direct flights, and how much it would cost.
    Arguments: graph, array of city names
    Return: the cost of the trip (if possible) or null (if not)
    """
    nodes = graph.get_nodes()
    start = arr[0]

    trip_possible = False
    cost_of_trip = 0

    if len(arr) == 2:
        destination = arr[1]
        for node in nodes:
            if node.value == start:
                neighbors = graph.get_neighbors(node)
                for neighbor in neighbors:
                    if neighbor.vertex.value == destination:
                        cost_of_trip += neighbor.weight
                        trip_possible = True
                        break

    if len(arr) > 2:
        # Use list comprehension to filter nodes in a graph based on values
        filtered_nodes = [node for node in graph.get_nodes() if node.value in arr]

        filtered_nodes.sort(key=lambda node: arr.index(node.value))
        # Loops through the range of the filtered nodes
        for i in range(len(filtered_nodes) - 1):
            # Grabs neighbors from each filtered node
            neighbors = graph.get_neighbors(filtered_nodes[i])

            if filtered_nodes[i+1] not in graph.get_neighbors(filtered_nodes[i]):
                return (trip_possible, cost_of_trip)

            # loops through each edge of neighbors
            for edge in neighbors:
                # if the vertex is equal to every city except starting city
                if edge.vertex == filtered_nodes[i+1]:
                    cost_of_trip += edge.weight
                    trip_possible = True
                    break

    return (trip_possible, cost_of_trip)
