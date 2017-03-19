# coding: utf-8
import matplotlib.pyplot as plt
# Plotting vote percentage partywise
parties=['Samajwadi PArty','Bahujan Samaj Party','Bharatiya Janata Party','Indian National Congress','Rashtriya Lok dal','Others']
vote_percentage=[29.15,25.91,15,11.63,2.33,15.98]
# Plot
colors=['gold','lightgreen','lightcoral','magenta','lightskyblue','pink']
plt.pie(vote_percentage,labels=parties,colors=colors,autopct='%1.1f%%',shadow=False,startangle=140)
plt.title("2012 Legislative Elections Vote Distribution Partywise")
plt.axis('equal')
plt.show()
