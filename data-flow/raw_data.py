# Biblíotecas
from sys import displayhook
from numpy import source
from pandas_datareader import data as web
import matplotlib.pyplot as plt
import os
import time

bovespa = web.DataReader('^BVSP', data_source='yahoo', start="01-01-2020", end="01-01-2021")
ticket_bovespa = bovespa["Adj Close"].plot()
plt.show()