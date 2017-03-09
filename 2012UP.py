import matplotlib.pyplot as plt
#Plotting data partywise
labels= ['Samajwadi Party','Bahujan Samaj Party','Bharatiya Janata Party',
'Indian National Congress','Rashtriya Lok Dal','Others']
seats= [224,80,47,28,9,19]
colors= ['gold','lightgreen','lightcoral','magenta','lightskyblue','pink']

#Plot
plt.pie(seats,labels=labels,colors=colors,autopct='%1.1f%%',shadow=True,startangle=140)
plt.title("2012 Legislative Elections Seat Distribution Partywise")
plt.axis('equal')
plt.show()
