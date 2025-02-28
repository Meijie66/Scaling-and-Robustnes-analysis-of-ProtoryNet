import matplotlib.pyplot as plt
import numpy as np
# Data
hp_10 = [1,1,1]
hp_20 = [5,6,8]
hp_30 = [5,6,7]
hp_40 = [11,10,11]
hp_50 = [11,5,9]
hp_60 = [8,6,10]
hp_80 = [12,9,7]
hp_100 = [11,7,9]
hp_120 = [11,11,14]
hp_150 = [14,15,13]
hp_200 = [13,9,16]
hp_300 = [11,15,24]
hp_500 = [17,37,18]



# Calculate averages
havg_10 = np.mean(hp_10)
havg_20 = np.mean(hp_20)
havg_30 = np.mean(hp_30)
havg_40 = np.mean(hp_40)
havg_50 = np.mean(hp_50)
havg_60 = np.mean(hp_60)
havg_80 = np.mean(hp_80)
havg_100 = np.mean(hp_100)
havg_120 = np.mean(hp_120)
havg_150 = np.mean(hp_150)
havg_200 = np.mean(hp_200)
havg_300 = np.mean(hp_300)
havg_500 = np.mean(hp_500)

# Calculate standard deviations (as error bars)
hstd_10 = np.std(hp_10)
hstd_20 = np.std(hp_20)
hstd_30 = np.std(hp_30)
hstd_40 = np.std(hp_40)
hstd_50 = np.std(hp_50)
hstd_60 = np.std(hp_60)
hstd_80 = np.std(hp_80)
hstd_100 = np.std(hp_100)
hstd_120 = np.std(hp_120)
hstd_150 = np.std(hp_150)
hstd_200 = np.std(hp_200)
hstd_300 = np.std(hp_300)
hstd_500 = np.std(hp_500)


# Data
p_10 = [10,10,10]
p_20 = [11,17,18]
p_30 = [17,23,16]
p_40 = [20,22,16]
p_50 = [22,15,23]
p_60 = [26,22,18]
p_80 = [11,16,9]
p_100 = [18,20,21]
p_120 = [17,14,11]
p_150 = [32,16,22]
p_200 = [9,17,27]
p_300 = [25,13,18]
p_500 = [20,20,13]

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
h_averages = [havg_10, havg_20, havg_30, havg_40, havg_50,havg_60, havg_80, havg_100, havg_120, havg_150, havg_200, havg_300, havg_500]
h_errors = [hstd_10, hstd_20, hstd_30, hstd_40, hstd_50, hstd_60, hstd_80, hstd_100, hstd_120, hstd_150, hstd_200, hstd_300, hstd_500]

# Averages and errors
r_averages = [avg_10, avg_20, avg_30, avg_40, avg_50, avg_60, avg_80, avg_100, avg_120, avg_150, avg_200, avg_300, avg_500]
r_errors = [std_10, std_20, std_30, std_40, std_50, std_60, std_80, std_100, std_120, std_150, std_200, std_300, std_500]


plt.figure(figsize=(10, 4)) 
# Plot
plt.errorbar(x, r_averages, yerr=r_errors, fmt='o-', capsize=5, color='orange', label='init=\'random\'')

# Plot
plt.errorbar(x, h_averages, yerr=h_errors, fmt='o-', capsize=5, label='init=\'heuristic\'')

#plt.axhline(y=0.83, color='red', linestyle='--', linewidth=2, label="NB")
# Add labels and title
plt.xticks(x, ['10','20','30', '40','50', '60', '80', '100', '120', '150', '200', '300', '500'])  # Label x-axis
plt.xlabel('Number of init prototypes')
plt.ylabel('Unique number of prototypes')
#plt.title('Learning_rate')
plt.legend()
plt.savefig("unique_proto_init.pdf", dpi=300, bbox_inches='tight')

# Show plot
plt.show()