import pandas as pd
import numpy as numpy
import matplotlib.pylab as plt
#%matplotlib inline
from matplotlib.pylab import rcParams
#rcParams['figure.figsize'] = 15, 6

data = pd.read_csv('AirPassengers.csv')

#print('dtypes: \n', data.dtypes)

dateparse = lambda dates: pd.datetime.strptime(dates, '%Y-%m')
data = pd.read_csv('AirPassengers.csv', parse_dates=['Month'], index_col='Month',date_parser=dateparse)
#print (data.head())
#print (data.index)

ts = data['#Passengers']
print (ts)
plt.plot(ts)
plt.show()
