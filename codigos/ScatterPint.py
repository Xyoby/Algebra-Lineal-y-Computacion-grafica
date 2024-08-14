import numpy as np
import matplotlib.pyplot as plt

# Generate random data
#np.random.seed(0)
x = np.random.rand(100)
y = np.random.rand(100)

# Add noise to the data
noise = np.random.normal(0, 0.9, 100)
y = y + noise

# Calculate the correlation coefficient
r = np.corrcoef(x, y)[0, 1]

# Calculate the linear regression line
m, b = np.polyfit(x, y, 1)

# Plot the data and regression line
plt.scatter(x, y, s=10)
plt.plot(x, m*x + b, color='red')
plt.xlim(-0.5, 1)
plt.ylim(-1, 2)
# Add labels and title
plt.xlabel('X')
plt.ylabel('Y')
plt.title(f'100-point scatter plot with r={r:.2f} and linear regression line with slope m={m:.2f}')


plt.show()
