import pandas as pd
import numpy as np

# Generate 20 random points in XYZ coordinates
num_points = 20
x_coords = np.random.rand(num_points)  # Random X coordinates
y_coords = np.random.rand(num_points)  # Random Y coordinates
z_coords = np.random.rand(num_points)  # Random Z coordinates

# Create a DataFrame
df = pd.DataFrame({'X': x_coords, 'Y': y_coords, 'Z': z_coords})

# Save the DataFrame to a CSV file
output_filename = '../assets/Test0001.xyz'
df.to_csv(output_filename, index=False)

#print(f"Saved {num_points} points to {output_filename}")
