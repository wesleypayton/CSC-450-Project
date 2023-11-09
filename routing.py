# Names: Elijah Payton, Gregory Whitehurst
# Description: CSC450 Project
DEBUG = False
from sys import *
from csv import *
def main(top_file):
    # First open file and interpret tree
    # Note: link ordering is u, v, w, x, y, z
    # The network topology is represented as a dictionary of a dictionaries.
    # ex: {'x': {'x': 0, 'y':2, 'z': 7}, 'y': {'x': 2, 'y': 0, 'z': 1}, 'z':{'x': 7, 'y': 1, 'z': 0}}
    
    link_values = {}
    with open(top_file, newline = '') as csvfile:
        
        csv_reader = reader(csvfile)
        node_headers = next(csv_reader)[1:]
        
        # give each node a header for identification
        for header in node_headers:
            link_values[header] = {col: 0 for col in node_headers}
            
        for row in csv_reader:
            # Give an identifier for each node
            identifier = row[0]
            # List of link values for that node
            values = [int(value) for value in row[1:]]
            
            # Put that all into the dictionary link_values
            for i, header in enumerate(node_headers):
                link_values[header][identifier] = values[i]
                
        if DEBUG == True:            
            print("Headers:", node_headers)
            
    if DEBUG == True:        
        for header, col_data in link_values.items():
            print(f"Column '{header}':", col_data)
    
    # Format topology from csv
    topology = {neighbor : link_values[neighbor] for neighbor in link_values}

    # Ask for source node
    source_node = input("Please provide the source node: ")

    # Use Dijkstra's algorithm to find shortest path tree
    #  and cost of least-cost paths for this node
    dijkstra_algorithm(topology, source_node)

    # Print for formatting
    print()

    # Now calculate distance vector for each node in the
    #  network using distance-vector algorithm (Calculate using Bellman-Ford equation)
    compute_distance_vectors(topology)



# This function calculates shortest path tree and lowest cost path to each 
# other node using dijkstra's routing algorithm
def dijkstra_algorithm(topology, source_node):
    # Initialize data structures
    shortest_path_tree = {node: [] for node in topology}
    costs = {node: 9999 for node in topology}  # To store the costs to reach each node
    visited = set()  # To keep track of visited nodes

    # Initialize the source node's cost to zero
    costs[source_node] = 0

    # Main Dijkstra's algorithm loop
    while len(visited) < len(topology):
        # Find the node with the minimum cost that has not been visited
        min_node = None
        min_cost = 9999
        for node in topology:
            if node not in visited and costs[node] < min_cost:
                min_node = node
                min_cost = costs[node]

        # If no reachable unvisited nodes are left, break the loop
        if min_node is None:
            break

        # Mark the node as visited
        visited.add(min_node)

        # Update costs and shortest path tree for neighboring nodes
        for neighbor, cost in topology[min_node].items():
            if costs[min_node] + cost < costs[neighbor]:
                costs[neighbor] = costs[min_node] + cost
                # Update path tree for neighbor node
                shortest_path_tree[neighbor] = shortest_path_tree[min_node] + [min_node]

    # Print the shortest path tree
    shortest_path_tree_strings = []
    print(f"Shortest path tree for node {source_node}:")
    for node, path in shortest_path_tree.items():
        if node != source_node:
            path_str = "".join(path)
            shortest_path_tree_strings.append(f"{path_str}{node}")

    # Format shortest path tree
    shortest_path_tree_strings.sort(key=len)
    for path in shortest_path_tree_strings:
        print(path + ", ", end = " ")

    print()

    # Print the costs of the least-cost paths
    print(f"Costs of the least-cost paths for node {source_node}:")
    for node, cost in costs.items():
        print(f"{node}:{cost}, ", end = " ")
    
    print()



# This function loops through each node and calculates lowest cost path to each 
# other node using distance-vector algorithm
def compute_distance_vectors(topology):
    # Initialize distance vector for each node and set cost to infinity
    distance_vectors = {node: {neighbor: 9999 for neighbor in topology} for node in topology}
    
    # Set up direct links in distance vectors
    for node in topology:
        for neighbor in topology[node]:
            distance_vectors[node][neighbor] = topology[node][neighbor]

    # Set max number of loops to prevent routing loops
    max_loops = len(topology)

    # Iterate through each node in the network
    for startNode in topology:

        for loop in range(max_loops):
            updated = False # Flag to track if any update has occurred during this loop

            # Loop through all target nodes in the network
            for node in topology:
                # Loop through the neighbors of the current node
                for neighbor in topology[node]:
                    # Loop through all possible destinations (nodes)
                    for dest in topology:
                        # Calculate the potential cost to reach the destination
                        potential_cost = distance_vectors[node][neighbor] + distance_vectors[neighbor][dest]
                        # If the calculated cost is less than the current known cost to the destination
                        # update distance vector cost and mark updated
                        if potential_cost < distance_vectors[node][dest]:
                            distance_vectors[node][dest] = potential_cost
                            updated = True
            
            # If no updates were made during this loop, exit the loop early
            if not updated:
                break

    # Once distance vector are calculated for each node, print
    for node in distance_vectors:
        print(f"Distance vector for node {node}: ", end = " ")
        print(*distance_vectors[node].values())


if __name__ == "__main__":
    # Take topography file name and pass to main
    main(argv[1])