#we can label x-axis and y-axis by using xlabel and ylabel

import matplotlib.pyplot as plt

x=[5,6,9]
y=[5,6,20]

plt.title("$Boss it is a line graph")

plt.xlabel("X values")
plt.ylabel("y values")

plt.plot(x,y,marker="*")
plt.show()


