import matplotlib.pyplot as plt
import numpy as np
# Data
lp_10 = [10,10,10]
lp_20 = [19,17,20]
lp_30 = [28,26,28]
lp_40 = [12,33,29]
lp_50 = [29,39,34]
lp_60 = [33,27,12]
lp_80 = [28,20,46]
lp_100 = [25,24,31]
lp_120 = [27,14,32]
lp_150 = [34,20,20]
lp_200 = [20,16,32]
lp_300 = [30,33,30]
lp_500 = [32,40,40]



# Calculate averages
lavg_10 = np.mean(lp_10)
lavg_20 = np.mean(lp_20)
lavg_30 = np.mean(lp_30)
lavg_40 = np.mean(lp_40)
lavg_50 = np.mean(lp_50)
lavg_60 = np.mean(lp_60)
lavg_80 = np.mean(lp_80)
lavg_100 = np.mean(lp_100)
lavg_120 = np.mean(lp_120)
lavg_150 = np.mean(lp_150)
lavg_200 = np.mean(lp_200)
lavg_300 = np.mean(lp_300)
lavg_500 = np.mean(lp_500)

# Calculate standard deviations (as error bars)
lstd_10 = np.std(lp_10)
lstd_20 = np.std(lp_20)
lstd_30 = np.std(lp_30)
lstd_40 = np.std(lp_40)
lstd_50 = np.std(lp_50)
lstd_60 = np.std(lp_60)
lstd_80 = np.std(lp_80)
lstd_100 = np.std(lp_100)
lstd_120 = np.std(lp_120)
lstd_150 = np.std(lp_150)
lstd_200 = np.std(lp_200)
lstd_300 = np.std(lp_300)
lstd_500 = np.std(lp_500)


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
l_averages = [lavg_10, lavg_20, lavg_30, lavg_40, lavg_50,lavg_60, lavg_80, lavg_100, lavg_120, lavg_150, lavg_200, lavg_300, lavg_500]
l_errors = [lstd_10, lstd_20, lstd_30, lstd_40, lstd_50, lstd_60, lstd_80, lstd_100, lstd_120, lstd_150, lstd_200, lstd_300, lstd_500]

# Averages and errors
r_averages = [avg_10, avg_20, avg_30, avg_40, avg_50, avg_60, avg_80, avg_100, avg_120, avg_150, avg_200, avg_300, avg_500]
r_errors = [std_10, std_20, std_30, std_40, std_50, std_60, std_80, std_100, std_120, std_150, std_200, std_300, std_500]


plt.figure(figsize=(10, 4)) 
# Plot
plt.errorbar(x, r_averages, yerr=r_errors, fmt='o-', capsize=5, color='orange', label='init=\'0.0001\'')

# Plot
plt.errorbar(x, l_averages, yerr=l_errors, fmt='o-', capsize=5, color='green', label='init=\'0.001\'')

#plt.axhline(y=0.83, color='red', linestyle='--', linewidth=2, label="NB")
# Add labels and title
plt.xticks(x, ['10','20','30', '40','50', '60', '80', '100', '120', '150', '200', '300', '500'])  # Label x-axis
plt.xlabel('Number of init prototypes')
plt.ylabel('Unique number of prototypes')
#plt.title('Learning_rate')
plt.legend()
plt.savefig("unique_proto_lr.pdf", dpi=300, bbox_inches='tight')

# Show plot
plt.show()