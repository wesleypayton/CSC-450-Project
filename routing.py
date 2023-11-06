# Names: Elijah Payton, Gregory Whitehurst
# Description: CSC450 Project

from sys import *
from csv import *
def main(file):
    # First open file and interpret tree
    # Note: link ordering is u, v, w, x, y, z
    top_file = file
    [u_links, v_links, w_links, x_links, y_links, z_links] = [[],[],[],[],[],[]]
    with open(top_file, newline = '') as csvfile:
        csv_reader = reader(csvfile)
        exclude_col = True
        for row in csv_reader:
            # First run is to give identifier for each node
            if exclude_col == True:
                '''[u_node, v_node, w_node, x_node, y_node, z_node] = [row[1], row[2], row[3], row[4], row[5], row[6]]
                [u_links.append(u_node), v_links.append(v_node), w_links.append(w_node), x_links.append(x_node), y_links.append(y_node), z_links.append(z_node)]'''
                exclude_col = False
            else:
                [u_node, v_node, w_node, x_node, y_node, z_node] = [int(row[1]), int(row[2]), int(row[3]), int(row[4]), int(row[5]), int(row[6])]
                [u_links.append(u_node), v_links.append(v_node), w_links.append(w_node), x_links.append(x_node), y_links.append(y_node), z_links.append(z_node)]      
            
    #print([u_links, v_links, w_links, x_links, y_links, z_links])
    links = {"u":u_links, "v":v_links, "w":u_links, "x":u_links, "y":u_links, "z":u_links}
    print(links)
    # Now take input for source node
    n_prime = input("Please provide the source node: ")


    # Use Dijkstra's algorithm to find shortest path tree
    #  and cost of least-cost paths for this node



    # Now calculate distance vector for each node in the
    #  network using distance-vector algorithm (Calculate using Bellman-Ford equation)

    
    
    pass

if __name__ == "__main__":
    # Take topography file name and pass to main
    main(argv[1])