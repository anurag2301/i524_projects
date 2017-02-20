import pandas as pd
import pygal

data = pd.read_csv('2016-first-quarter-citations.csv')
data = data.dropna(how='any')

ages = data['Cited Person Age']
ages = ages[ages < 100]

list = [0]*100
for x in ages:
    list[int(x)] += 1

hist = pygal.Histogram()
values = []

for i in range(0,len(list)):
    values.append((list[i], i, i+1))

hist.add('Ages', values)
hist.render_to_file('histogram.svg')
