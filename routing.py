# Names: Elijah Payton, Gregory Whitehurst
# Description: CSC450 Project
DEBUG = True
from sys import *
from csv import *
def main(top_file):
    # First open file and interpret tree
    # Note: link ordering is u, v, w, x, y, z
    
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
    
    topology = {neighbor : link_values[neighbor] for neighbor in link_values}

    n_prime = input("Please provide the source node: ")


    # Use Dijkstra's algorithm to find shortest path tree
    #  and cost of least-cost paths for this node



    # Now calculate distance vector for each node in the
    #  network using distance-vector algorithm (Calculate using Bellman-Ford equation)
    compute_distance_vectors(topology)
    
    
    pass

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
        print(distance_vectors[node])


if __name__ == "__main__":
    # Take topography file name and pass to main
    main(argv[1])