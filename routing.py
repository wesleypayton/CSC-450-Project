# Names: Elijah Payton, Gregory Whitehurst
# Description: CSC450 Project

from sys import *
from csv import *

def main(file):
    # First open file and interpret tree
    # Note: list[1] = link to u, list[2] = link to v, list[3] = link to w, etc.
    top_file = file
    [u_links, v_links, w_links, x_links, y_links, z_links] = [[],[],[],[],[],[]]
    with open(top_file, newline = '') as csvfile:
        csv_reader = reader(csvfile)
        first_run = True
        for row in csv_reader:
            if first_run == True:
                [u_node, v_node, w_node, x_node, y_node, z_node] = [row[1], row[2], row[3], row[4], row[5], row[6]]
                [u_links.append(u_node), v_links.append(v_node), w_links.append(w_node), x_links.append(x_node), y_links.append(y_node), z_links.append(z_node)]
                first_run = False
            else:
                [u_node, v_node, w_node, x_node, y_node, z_node] = [int(row[1]), int(row[2]), int(row[3]), int(row[4]), int(row[5]), int(row[6])]
                [u_links.append(u_node), v_links.append(v_node), w_links.append(w_node), x_links.append(x_node), y_links.append(y_node), z_links.append(z_node)]      
            
    print([u_links, v_links, w_links, x_links, y_links, z_links])

    # Now take input for source node
    


    # Use Dijkstra's algorithm to find shortest path tree
    #  and cost of least-cost paths for this node



    # Now calculate distance vector for each node in the
    #  network using distance-vector algorithm (Calculate using Bellman-Ford equation)

    
    
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