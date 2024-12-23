import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt

ticker = "MINSURI1.LM"
minsur = yf.Ticker(ticker)
historia = minsur.history(period = "1mo")

ultimo_precio = historia["Close"].iloc[-1]/3.7

dias = 50 
forecast = [ultimo_precio]

for _ in range(1, dias):
    cambio = np.random.normal(0,0.1)
    nuevo_precio = forecast[-1]*(1+cambio)
    forecast.append(nuevo_precio)
    
dias_eje = list(range(dias))

plt.figure(figsize=(10,5))

plt.plot(dias_eje,forecast, marker ="o")
plt.title("Proyección Normal en honor a Manuel Arce")
plt.xlabel("Día")
plt.ylabel("Precio (Soles)")

plt.grid(True)
plt.show()
