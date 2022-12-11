import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

df = pd.read_csv('DataProiectMSS.csv')
df['Data'] = pd.to_datetime(df['Data'])  # Setarea datasetului

############ Configurarea primului grafic ######################

ax = df.plot(x='Data', y='Valoare', figsize=(12, 6))
plt.title('Efectivul salariatilor din domeniul profesional științific și tehnic'
          ' la sfarsitul lunii, din România, în perioada 2000-2022 ', fontsize=12)
plt.xlabel("Perioada")
plt.legend(['Numărul de angajați (Mii de persoane)'])
plt.ylabel("Numărul de angajați (mii)")
ax.tick_params(axis="x", direction="in", length=10, width=2, color="turquoise")
ax.tick_params(axis="y", direction="in", length=6, width=4, color="orange")
ax.grid(axis="x", color="green", alpha=.3, linewidth=2, linestyle=":")
ax.grid(axis="y", color="black", alpha=.5, linewidth=.5)

############ Configurarea celui de-al doilea grafic ######################

x = df['Data']
y = df['Valoare']
y1 = df['Valoare'].values
fig = plt.figure()
ax = fig.gca()
plt.fill_between(x, y1=y1, y2=-y1, alpha=0.55, linewidth=1.5, color='darkblue')
plt.ylim(-200, 200)
plt.title('Efectivul salariatilor din domeniul profesional științific și tehnic'
          ' la sfarsitul lunii, din România, în perioada 2000-2022 ', fontsize=12)
ax.tick_params(axis="x", direction="in", length=10, width=2, color="turquoise")
ax.tick_params(axis="y", direction="in", length=6, width=4, color="orange")
plt.xlabel("Perioada")
plt.ylabel("Numărul de angajați (mii)")
plt.axhline(y=0, color='orange', alpha=.5, linestyle='dashdot')
ax.grid(axis="x", color="green", alpha=.3, linewidth=1, linestyle=":")

############# Configurarea celui de-al treilea grafic ######################


df['year'] = [d.year for d in df.Data]
df['month'] = [d.strftime('%b') for d in df.Data]
years = df['year'].unique()
# Prep Colors
np.random.seed(100)
mycolors = np.random.choice(list(mpl.colors.XKCD_COLORS.keys()), len(years), replace=False)

# Draw Plot
plt.figure(figsize=(16, 12), dpi=80)
for i, y in enumerate(years):
    if i > 0:
        plt.plot('month', 'Valoare', data=df.loc[df.year == y, :], color=mycolors[i], label=y)
        plt.text(df.loc[df.year == y, :].shape[0] - .9, df.loc[df.year == y, 'Valoare'][-1:].values[0], y, fontsize=12,
                 color=mycolors[i])

# Decoration
plt.gca().set(ylabel='Număr de angajați (mii)', xlabel='Lună')
plt.yticks(fontsize=12, alpha=.7)
plt.title("Efectivul salariatilor din domeniul profesional științific și tehnic din România per an (2000-2022)",
          fontsize=20)
plt.show()

############# Configurarea graficului 4 & 5 ######################


df['year'] = [d.year for d in df.Data]
df['month'] = [d.strftime('%b') for d in df.Data]
years = df['year'].unique()

# Draw Plot
fig, axes = plt.subplots(1, 2, figsize=(20, 7), dpi=80)
sns.boxplot(x='year', y='Valoare', data=df, ax=axes[0])
sns.boxplot(x='month', y='Valoare', data=df.loc[~df.year.isin([2000, 2022]), :])

# Setarea titlului și etichetelor
axes[0].set_title('Grafic lumânare din punct de vedere al anului\n(Trendul)', fontsize=18);
axes[0].set_xlabel('An')
axes[0].set_ylabel('Număr de angajați (mii)')
axes[1].set_title('Grafic lumânare din punct de vedere al lunii\n(Sezonalitatea)', fontsize=18)
axes[1].set_xlabel('Lună')
axes[1].set_ylabel('Număr de angajați (mii)')
plt.show()
