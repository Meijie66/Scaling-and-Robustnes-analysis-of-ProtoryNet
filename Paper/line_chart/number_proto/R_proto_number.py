import matplotlib.pyplot as plt
import numpy as np

# Data
p_10 = [0.639, 0.770, 0.683]
p_20 = [0.572, 0.650, 0.646]
p_30 = [0.679, 0.580, 0.695]
p_40 = [0.638, 0.617, 0.519]
p_50 = [0.679, 0.485, 0.597]
p_60 = [0.576, 0.716, 0.510]
p_80 = [0.543, 0.531, 0.547]
p_100 = [0.514, 0.584, 0.461]
p_120 = [0.477, 0.494, 0.469]
p_150 = [0.555, 0.494, 0.576]
p_200 = [0.469, 0.543, 0.486]
p_300 = [0.473, 0.449, 0.576]
p_500 = [0.469, 0.457, 0.465]

# Calculate averages
avg_10 = np.mean(p_10)
avg_20 = np.mean(p_20)
avg_30 = np.mean(p_30)
avg_40 = np.mean(p_40)
avg_60 = np.mean(p_60)
avg_80 = np.mean(p_80)
avg_100 = np.mean(p_100)
avg_120 = np.mean(p_120)
avg_150 = np.mean(p_150)
avg_200 = np.mean(p_200)
avg_300 = np.mean(p_300)
avg_500 = np.mean(p_500)


# Calculate standard deviations (as error bars)
std_10 = np.std(p_10)
std_20 = np.std(p_20)
std_30 = np.std(p_30)
std_40 = np.std(p_40)
std_60 = np.std(p_60)
std_80 = np.std(p_80)
std_100 = np.std(p_100)
std_120 = np.std(p_120)
std_150 = np.std(p_150)
std_200 = np.std(p_200)
std_300 = np.std(p_300)
std_500 = np.std(p_500)
# X-axis labels (e.g., categories or time points)
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]  # Representing the two datasets

# Averages and errors
averages = [avg_10, avg_20, avg_30, avg_40, avg_50, avg_60, avg_80, avg_100, avg_120, avg_150, avg_200, avg_300, avg_500]
errors = [std_10, std_20, std_30, std_40, std_50, std_60, std_80, std_100, std_120, std_150, std_200, std_300, std_500]

# Plot
plt.errorbar(x, averages, yerr=errors, fmt='o-', capsize=5, color='orange', label='init=\'random\'')

# Add labels and title
plt.xticks(x, ['10','20', '30', '40', '60', '80', '100', '120', '150', '200', '300', '500'])  # Label x-axis
plt.xlabel('Number of prototypes')
plt.ylabel('Accuracy')
#plt.title('Learning_rate')
plt.legend()
plt.savefig("random_proto.png", dpi=300, bbox_inches='tight')
# Show plot
plt.show()