# coding: utf-8
import matplotlib.pyplot as plt
#Plotting data partywise
labels=['Samajwadi Party','Bahujan Samaj Party','Bharatiya Janata Party','Indian National Congress','Rashtriya Lok Dal','Others']
seats=[47,19,312,7,1,17]
colors=['green','blue','orange','lightskyblue','magenta','gold']
#Plot
plt.pie(seats,labels=labels,colors=colors,autopct='%1.1f%%',shadow=True,startangle=140)
plt.title("2017 Uttar Pradesh Legislative LEection Seat Distribution Partywise")
plt.axis('equal')
plt.show()
