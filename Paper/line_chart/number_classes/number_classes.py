import matplotlib.pyplot as plt

# Data
categories = ['2', '3', '5', '10', '20', '50', '200']
values = [0.502, 0.483, 0.464, 0.267]

# Create the bar plot
plt.bar(categories, values, width=0.6)
plt.plot(categories, values, color='orange', marker='o', label='Line Data', linewidth=2)

# Add labels and title
plt.xlabel('learning rate')
plt.ylabel('Accuracy')
plt.title('Learning Rate')

plt.savefig('learning_rate.png')
# Show the plot
plt.show()