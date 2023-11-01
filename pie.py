#pie chart

import matplotlib.pyplot as plt

students=['Daniel','prasad','srinu']
points=[62,48,36]

plt.pie(points,labels=students)

plt.axis('equal')
plt.show()