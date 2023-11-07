from sys import *
from csv import *
def main(file):
    # Initialize a dictionary to store data for each column
    data = {}

    with open(file, newline='') as csvfile:
        csv_reader = reader(csvfile)
        headers = next(csv_reader)[1:]  # Skip the first column (assumed to be identifiers)

        # Initialize lists for each column in the dictionary
        for header in headers:
            data[header] = []

        # Iterate through the remaining rows to collect data
        for row in csv_reader:
            identifier = row[0]
            values = [int(value) for value in row[1:]]  # Skip the first column

            # Store values in the corresponding lists
            for i, header in enumerate(headers):
                data[header].append(values[i])

    print("Headers:", headers)
    for header, col_data in data.items():
        print(f"Column '{header}':", col_data)

if __name__ == "__main__":
  # Replace with the path to your CSV file
    main(argv[1])