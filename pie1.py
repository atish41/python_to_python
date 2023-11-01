#creating pie chart

import matplotlib.pyplot as plt

students=['daniel','prasad','srinu']
points=[62,48,36]

c=['y','r','b']

plt.pie(points,labels=students,colors=c,shadow=True,
explode=(0.05,0.05,0.05),autopct='%1.1f%%')

plt.axis('equal')
plt.legend()
plt.show()