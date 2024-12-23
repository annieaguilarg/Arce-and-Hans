import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt


tickers = ["MINSURI1.LM", "ALICORC1.LM", "NEXAPEC1.LM"]

diccionario = {}
for ticker in tickers:
    precio = yf.Ticker(ticker) 
    historia = precio.history(period = "1mo") /3.7
    diccionario[ticker] = historia["Close"].iloc[-1] 
    
#Simulacion
dias = 30
sigma = 0.25
eje_x = list(range(dias))
colores = ("blue", "red", "green")

forecast = {}

for ticker, ultimo_precio in diccionario.items():
    precio_proyectado = [ultimo_precio]
    for _ in range(1, dias):
        variacion_arce = np.random.normal(0,sigma)
        nuevo_precio = precio_proyectado[-1] * (1+variacion_arce) 
        precio_proyectado.append(nuevo_precio)
        
    forecast[ticker] = precio_proyectado

plt.figure(figsize=(10,5))

for ticker, color in zip(tickers, colores):
    plt.plot(eje_x, forecast[ticker], marker = ".", label = ticker, color = color)

plt.title("Proyecciones en honor a Manuel Arce para los Próximos 30 Días")
plt.xlabel("Día")
plt.ylabel("Precio Futuro (Dolares)")
plt.legend()
plt.grid(True)
plt.show()

