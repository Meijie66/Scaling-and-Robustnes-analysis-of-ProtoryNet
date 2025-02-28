import matplotlib.pyplot as plt

# Data
categories = ['heuristic', 'random']
values = [0.483, 0.587]

# Create the bar plot
plt.bar(categories, values, width=0.5)

# Add labels and title
plt.xlabel('Clustering initialization method')
plt.ylabel('Accuracy')
plt.title('Cluster_initialization')

plt.savefig('ckuster_init.png')
# Show the plot
plt.show()