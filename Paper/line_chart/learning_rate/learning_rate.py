import matplotlib.pyplot as plt
import numpy as np

# Data
a = [0.560, 0.490, 0.457]
b = [0.403, 0.551, 0.494]
c = [0.453, 0.494, 0.444]
d = [0.290, 0.263, 0.247]


# Calculate averages
avg_a = np.mean(a)
avg_b = np.mean(b)
avg_c = np.mean(c)
avg_d = np.mean(d)

# Calculate standard deviations (as error bars)
std_a = np.std(a)
std_b = np.std(b)
std_c = np.std(c)
std_d = np.std(d)
# X-axis labels (e.g., categories or time points)
x = [1, 2, 3, 4]  # Representing the two datasets

# Averages and errors
averages = [avg_a, avg_b, avg_c, avg_d]
errors = [std_a, std_b, std_c, std_d]

# Plot
plt.errorbar(x, averages, yerr=errors, fmt='o-', capsize=5)

# Add labels and title
plt.xticks(x, ['0.001', '0.0001', '0.00001', '0.000001'])  # Label x-axis
plt.xlabel('Learning rate')
plt.ylabel('Accuracy')
#plt.title('Learning_rate')
plt.legend()
plt.savefig("learning_rate.png", dpi=300, bbox_inches='tight')
# Show plot
plt.show()