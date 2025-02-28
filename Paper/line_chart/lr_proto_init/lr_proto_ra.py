import matplotlib.pyplot as plt
import numpy as np
# Data
l2_10 = [0.564, 0.708, 0.695]
l2_20 = [0.490, 0.712, 0.642]
l2_30 = [0.823, 0.733, 0.774]
l2_40 = [0.617, 0.531, 0.774]
#need to update
l2_50 = [0.646, 0.617, 0.584]
l2_60 = [0.654, 0.683, 0.605]
l2_80 = [0.366, 0.391, 0.617]
l2_100 = [0.379, 0.313, 0.428]
l2_120 = [0.337, 0.259, 0.358]
#need to update
l2_150 = [0.235, 0.251, 0.246]
l2_200 = [0.260, 0.300, 0.189]
l2_300 = [0.250, 0.193, 0.370]
l2_500 = [0.284, 0.251, 0.218]



# Calculate averages
l2avg_10 = np.mean(l2_10)
l2avg_20 = np.mean(l2_20)
l2avg_30 = np.mean(l2_30)
l2avg_40 = np.mean(l2_40)
l2avg_50 = np.mean(l2_50)
l2avg_60 = np.mean(l2_60)
l2avg_80 = np.mean(l2_80)
l2avg_100 = np.mean(l2_100)
l2avg_120 = np.mean(l2_120)
l2avg_150 = np.mean(l2_150)
l2avg_200 = np.mean(l2_200)
l2avg_300 = np.mean(l2_300)
l2avg_500 = np.mean(l2_500)

# Calculate standard deviations (as error bars)
l2std_10 = np.std(l2_10)
l2std_20 = np.std(l2_20)
l2std_30 = np.std(l2_30)
l2std_40 = np.std(l2_40)
l2std_50 = np.std(l2_50)
l2std_60 = np.std(l2_60)
l2std_80 = np.std(l2_80)
l2std_100 = np.std(l2_100)
l2std_120 = np.std(l2_120)
l2std_150 = np.std(l2_150)
l2std_200 = np.std(l2_200)
l2std_300 = np.std(l2_300)
l2std_500 = np.std(l2_500)


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
avg_50 = np.mean(p_50)
avg_60 = np.mean(p_60)
avg_80 = np.mean(p_80)
avg_100 = np.mean(p_100)
avg_120 = np.mean(p_120)
avg_150 = np.mean(p_150)
avg_200 = np.mean(p_200)
avg_300 = np.mean(p_300)
avg_500 = np.mean(p_500)

#for random
# Calculate standard deviations (as error bars)
std_10 = np.std(p_10)
std_20 = np.std(p_20)
std_30 = np.std(p_30)
std_40 = np.std(p_40)
std_50 = np.std(p_50)
std_60 = np.std(p_60)
std_80 = np.std(p_80)
std_100 = np.std(p_100)
std_120 = np.std(p_120)
std_150 = np.std(p_150)
std_200 = np.std(p_200)
std_300 = np.std(p_300)
std_500 = np.std(p_500)

# X-axis labels (e.g., categories or time points)
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]  # Representing the two datasets

# Averages and errors
l2_averages = [l2avg_10, l2avg_20, l2avg_30, l2avg_40, l2avg_50,l2avg_60, l2avg_80, l2avg_100, l2avg_120, l2avg_150, l2avg_200, l2avg_300, l2avg_500]
l2_errors = [l2std_10, l2std_20, l2std_30, l2std_40, l2std_50, l2std_60, l2std_80, l2std_100, l2std_120, l2std_150, l2std_200, l2std_300, l2std_500]

# Averages and errors
r_averages = [avg_10, avg_20, avg_30, avg_40, avg_50, avg_60, avg_80, avg_100, avg_120, avg_150, avg_200, avg_300, avg_500]
r_errors = [std_10, std_20, std_30, std_40, std_50, std_60, std_80, std_100, std_120, std_150, std_200, std_300, std_500]


plt.figure(figsize=(10, 4)) 
# Plot
plt.errorbar(x, r_averages, yerr=r_errors, fmt='o-', capsize=5, color='orange', label='learning_rate=0.0001')

# Plot
plt.errorbar(x, l2_averages, yerr=l2_errors, fmt='o-', capsize=5, color='green', label='learning_rate=0.001')

plt.axhline(y=0.83, color='red', linestyle='--', linewidth=2, label="NB")
# Add labels and title
plt.xticks(x, ['10','20','30', '40','50', '60', '80', '100', '120', '150', '200', '300', '500'])  # Label x-axis
plt.xlabel('Number of prototypes')
plt.ylabel('Accuracy')
#plt.title('Learning_rate')
plt.legend()
plt.savefig("wide_lr_np_random.pdf", dpi=300, bbox_inches='tight')

# Show plot
plt.show()