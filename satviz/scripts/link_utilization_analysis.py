import numpy as np
import matplotlib.pyplot as plt

# List of files to process
file_names = ["link_utilization_isl_1000_gw_50.txt","link_utilization_isl_1000_gw_500.txt"]

# Initialize the plot
plt.figure(figsize=(8, 6))

# Loop through each file to read the data and plot the CDF
for file_name in file_names:
    utilization_values = []

    # Open the file and read the data
    with open(file_name, "r") as file:
        for line in file:
            # Each line has the format: sat1,sat2,utilization,hex_col
            parts = line.strip().split(",")
            utilization = float(parts[2])  # Extract the utilization value
            utilization_values.append(utilization)

    # Convert the utilization values to a numpy array for analysis
    utilization_values = np.array(utilization_values)

    # Compute the CDF
    sorted_utilization = np.sort(utilization_values)
    cdf = np.arange(1, len(sorted_utilization) + 1) / len(sorted_utilization)

    # Plot the CDF for the current file
    plt.plot(sorted_utilization, cdf, linestyle='-', label=f"{file_name}")  # Add a label for each file (using file number)

# Add labels and title
plt.title("CDF of Link Utilization from Multiple Files")
plt.xlabel("Link Utilization")
plt.ylabel("Cumulative Probability")
plt.xlim(0, 1)
plt.ylim(0, 1)
plt.grid(True)

# Show the legend
plt.legend()

# Show the plot
plt.show()
