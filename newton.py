import pandas_datareader.data as web
import datetime
import matplotlib.pyplot as plt
import pandas as pd


from pandas.plotting import scatter_matrix

start = datetime.datetime(2019, 1, 1)
end = datetime.datetime(2020, 12, 23)

newton = web.DataReader("NEWTON.ST", 'yahoo', start, end)
vitec = web.DataReader("VTC.L", 'yahoo', start, end)
fuji = web.DataReader("FUJIY", 'yahoo', start, end)

newton.head()

newton['Open'].plot(label='Open')
newton['Close'].plot(label='Close')
newton['High'].plot(label='High')
newton['Low'].plot(label='Low')
plt.legend()
plt.title('Newton Nordic')
plt.ylabel('Stock Price')
plt.show()

newton['Volume'].plot(label='Volume traded')
plt.legend()
plt.title('Newton Nordic')
plt.show()

newton['Open'].plot(label='Open')
newton['MA5'] = newton['Open'].rolling(5).mean()
newton['MA5'].plot(label='Moving Average 5')
newton['MA20'] = newton['Open'].rolling(20).mean()
newton['MA20'].plot(label='Moving Average 20')
plt.legend()
plt.show()

cam_comp = pd.concat([newton['Open'], vitec['Open'], fuji['Open']], axis=1)
cam_comp.columns = ['Newton Open', 'Vitec Open', 'Fujifilm Open']
scatter_matrix(cam_comp, hist_kwds={'bins': 50})
plt.legend()
plt.show()
