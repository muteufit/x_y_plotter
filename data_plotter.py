import matplotlib.pyplot as plt
import pandas as pd

excel_file = input('Enter excel file name with extension: ')

df = pd.read_excel(excel_file)

# Data for the first curve
x = df['X'].tolist()
y = df['Y'].tolist()

# Create the first curve
plt.plot(x, y)

# Setting imits for the x-axis
plt.xlim(x[0], x[-1])

# Customize the plot
x_label = input('Enter label on the x axis: ')
y_label = input('Enter label on the y axis: ')
plt.xlabel(x_label)
plt.ylabel(y_label)
title = input('Enter graph title: ')
plt.title(title)

# Save the figure
plt.savefig(f'{title}.png')

# Show the plot
plt.show()
