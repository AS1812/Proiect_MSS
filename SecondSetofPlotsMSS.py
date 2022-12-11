import matplotlib.pyplot as plt
import pandas as pd
from statsmodels.tsa.seasonal import seasonal_decompose

df = pd.read_csv('DataProiectMSS.csv', parse_dates=['Data'], index_col='Data')
result_mul = seasonal_decompose(df['Valoare'], model='multiplicative', extrapolate_trend='freq')

# Additive Decomposition
result_add = seasonal_decompose(df['Valoare'], model='additive', extrapolate_trend='freq')

# Plot
plt.rcParams.update({'figure.figsize': (10, 10)})
result_mul.plot().suptitle('Decompoziția Multiplicativă', fontsize=12)
result_add.plot().suptitle('Decompoziția Aditivă', fontsize=12)

plt.show()

result_mul = seasonal_decompose(df['Valoare'], model='multiplicative', extrapolate_trend='freq')
detrended = df.Valoare.values - result_mul.trend
plt.plot(detrended)
plt.title(
    'Efectivul salariatilor din domeniul profesional științific și tehnic din România per an (2000-2022) \n Fără componenta de trend',
    fontsize=12)
plt.show()

# Time Series Decomposition
result_mul = seasonal_decompose(df['Valoare'], model='multiplicative', extrapolate_trend='freq')

# Deseasonalize
deseasonalized = df.Valoare.values / result_mul.seasonal

# Plot
plt.plot(deseasonalized)
plt.title(
    'Efectivul salariatilor din domeniul profesional științific și tehnic din România per an (2000-2022) \n Fără componenta de sezonalitate',
    fontsize=16)
plt.plot()
plt.show()
