import numpy as np
import matplotlib.pyplot as plt
 
# Make a fake dataset:
height = [3, 12, 5, 18, 45]
bars = ('A', 'B', 'C', 'D', 'E')
y_pos = np.arange(len(bars))
 
# Create bars
plt.bar(y_pos, height)

# Add title and axis names
plt.xlabel('categories')
plt.ylabel('values')

# Create names on the x-axis
plt.xticks(y_pos, bars)
 
# Show graphic
plt.show()

