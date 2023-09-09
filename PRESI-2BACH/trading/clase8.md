---
marp: true
theme: default
---

# Curso de Python y Trading Algorítmico
## Día 8: Indicadores Técnicos y Backtesting

---

# Agenda

- Repaso del Día 7
- ¿Qué es el Análisis Técnico?
- Librería TA-Lib
- Indicadores Técnicos en Python
- Backtesting de una Estrategia Simple

---

# Repaso del Día 7
- Cargando Datos Financieros en Python
- Visualización con Matplotlib

---

# ¿Qué es el Análisis Técnico?

- Estudio de los precios y patrones del mercado
- Uso de gráficos e indicadores técnicos

---

# Indicadores Técnicos en Python

- Media Móvil
- RSI (Relative Strength Index)
- MACD (Moving Average Convergence Divergence)

---

# Librería TA-Lib (Technical Analysis Library)

- Biblioteca de software de código abierto para análisis técnico
- Proporciona más de 150 funciones de análisis técnico
  - Medias Móviles (SMA, EMA)
  - Osciladores (RSI, MACD)
  - Bandas de Bollinger
  - Patrones de Velas
  - ... y mucho más
- Ampliamente utilizada en la industria financiera

  ```python
  import talib
  
  # Calcular una Media Móvil Simple (SMA)
  sma = talib.SMA(df['Close'], timeperiod=20)
  
  # Calcular el Índice de Fuerza Relativa (RSI)
  rsi = talib.RSI(df['Close'], timeperiod=14)

---

# Backtesting de una Estrategia Simple

- ¿Qué es el Backtesting?

---

# Implementación de backtesting en Python

```python

def backtest(df):
    buy_signals = []
    sell_signals = []
    position = None

    for i in range(len(df)):
        if df['SMA'][i] < df['Close'][i]:
            if position is None:
                buy_signals.append(df['Close'][i])
                position = df['Close'][i]
            else:
                buy_signals.append(None)
            sell_signals.append(None)
        else:
            if position is not None:
                sell_signals.append(df['Close'][i])
                position = None
            else:
                sell_signals.append(None)
            buy_signals.append(None)

    df['Buy_Signal'] = buy_signals
    df['Sell_Signal'] = sell_signals
```

---

# Preguntas

- ¿Alguna pregunta o duda?

---

# Tarea

- Implementar un nuevo indicador en el código de backtesting
