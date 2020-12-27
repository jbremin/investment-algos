import pandas_datareader.data as web
import datetime
import matplotlib.pyplot as plt

start = datetime.datetime(2020, 1, 1)
end = datetime.datetime(2020, 12, 23)

newton = web.DataReader("NEWTON.ST", 'yahoo', start, end)

newton.head()

newton['Open'].plot(label='Open')
newton['Close'].plot(label='Close')
newton['High'].plot(label='High')
plt.legend()
plt.title('Newton Nordic')
plt.ylabel('Stock Price')
plt.show()
