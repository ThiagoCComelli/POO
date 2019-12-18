import  matplotlib.pyplot as plt
import json
import tkinter as tk
import tkinter
from tkinter import *

valor = []
arq = open("query.json","r")
data = json.load(arq)
arq.close()

timeSeries = data["Time Series (5min)"]
open = [float(dado["1. open"]) for dado in timeSeries.values()]
high = [float(dado["2. high"]) for dado in timeSeries.values()]
low = [float(dado["3. low"]) for dado in timeSeries.values()]
close = [float(dado["4. close"]) for dado in timeSeries.values()]
volume = [float(dado["5. volume"]) for dado in timeSeries.values()]


for i in range(1170):
    valor.append(i)

plt.plot(valor,open)
plt.show()

plt.plot(valor,high)
plt.show()

plt.plot(valor,low)
plt.show()

plt.plot(valor,close)
plt.show()

plt.plot(valor,volume)
plt.show()