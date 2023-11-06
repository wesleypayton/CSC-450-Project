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
            link_values[header] = []
            
        for row in csv_reader:
            # Give an identifier for each node
            identifier = row[0]
            # List of link values for that node
            values = [int(value) for value in row[1:]]
            
            # Put that all into the dictionary link_values
            for i, header in enumerate(node_headers):
                link_values[header].append(values[i])
                
        if DEBUG == True:            
            print("Headers:", node_headers)
            
    if DEBUG == True:        
        for header, col_data in link_values.items():
            print(f"Column '{header}':", col_data)
    
    n_prime = input("Please provide the source node: ")


    # Use Dijkstra's algorithm to find shortest path tree
    #  and cost of least-cost paths for this node



    # Now calculate distance vector for each node in the
    #  network using distance-vector algorithm (Calculate using Bellman-Ford equation)

    
    
    pass

if __name__ == "__main__":
    # Take topography file name and pass to main
    main(argv[1])