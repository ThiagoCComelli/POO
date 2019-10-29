import json
import requests
import matplotlib.pyplot as plt
import time
import threading

tot = 0

def vai():
    global tot
    while True:
        valor = []
        r = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=MSFT&interval=5min&apikey=demo")
        data = r.json()

        timeSeries = data["Time Series (5min)"]
        open = [float(dado["1. open"]) for dado in timeSeries.values()]

        for i in range(len(open)):
            valor.append(i)

        plt.plot(valor,open)
        plt.show()
        plt.savefig('images/'+'c'+str(tot)+'books_read.jpeg')

        tot += 1

        time.sleep(1)

thread1 = threading.Thread(target=vai)
thread1.start()
