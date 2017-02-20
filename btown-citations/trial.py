from __future__ import division, print_function
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('2016-first-quarter-citations.csv')
type(data)
data.index
data.columns
data.dtypes
data.shape

data = data.dropna(how='any')
data.shape

from datetime import datetime
data['DateTime Issued'] = data.apply(lambda row: datetime.strptime(row['Date Issued'] + ':' + row['Time Issued'], '%m/%d/%y:%I:%M %p'), axis=1)
data.columns
data['Day of Week Issued'] = data.apply(lambda row: datetime.strftime(row['DateTime Issued'], '%A'), axis=1)


days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
dow_data = [days.index(dow) for dow in data['Day of Week Issued']]
dow_data

#fig = plt.figure()
#ax = fig.add_subplot(1, 1, 1)
#plt.hist(dow_data, bins=len(days))
#plt.xticks(range(len(days)), days)
#plt.show()

ages = data['Cited Person Age']
#fig = plt.figure()
#ax = fig.add_subplot(1, 1, 1)
#plt.hist(ages, bins=int(np.max(ages) - np.min(ages)))
#plt.show()

ages = ages[ages < 100]
#fig = plt.figure()
#ax = fig.add_subplot(1, 1, 1)
#plt.hist(ages, bins=int(np.max(ages) - np.min(ages)))
#plt.show()
#plt.savefig('hist.svg')
#import matplotlib.patches as mpatches
#from matplotlib.backends.backend_pdf import PdfPages
#pp = PdfPages('hist.pdf')
#fig.savefig(pp, format='pdf')
#pp.close()
print(ages)

list = [0]*100
print(list)
i = 0
for x in ages:
    list[int(x)] += 1


import pygal

hist = pygal.Histogram()
xyz = []


for i in range(0,len(list)):
    xyz.append((list[i], i, i+1))
print(xyz)

hist.add('Ages', xyz)
hist.render_to_file('xyz.svg')
