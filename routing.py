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


    # We will use this to determine when to stop looking for shortest path
    max_paths = 10

    # Loop through each node and calculate distance vector
    for node in topology:
        # Create vector
        distance_vector = [0] * len(topology)


        # Calculate lowest cost path to each node
        for node in topology:
        
            neighborNodes = []


            for neighborNode in topology[node]:
                for dest in topology:
                    pass

        # Once distance vector is calculated for node, print
        print("Distance vector for node u: " + distance_vector)
    pass


if __name__ == "__main__":
    # Take topography file name and pass to main
    main(argv[1])