import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats
from scipy.stats import chi2_contingency
data = pd.read_csv('sourpks.csv')


data = data.set_axis(data.iloc[0],axis=1)
data = data.drop(index=0)
data = data.drop(index=403)
data = data.drop(index=402)
data = data.drop(index=401)
data = data.drop(data.columns[0], axis=1)
data['BLUE'] = pd.to_numeric(data['BLUE'], errors='coerce')
data['GREEN'] = pd.to_numeric(data['GREEN'], errors='coerce')
data['YELLOW'] = pd.to_numeric(data['YELLOW'], errors='coerce')
data['ORANGE'] = pd.to_numeric(data['ORANGE'], errors='coerce')
data['RED'] = pd.to_numeric(data['RED'], errors='coerce')
data['TOTAL'] = pd.to_numeric(data['TOTAL'], errors='coerce')
data.tail()

blue = data['BLUE'].sum()
green = data['GREEN'].sum()
yellow = data['YELLOW'].sum()
orange = data['ORANGE'].sum()
red = data['RED'].sum()
color_total = [blue, green, yellow, orange, red]
color_names = ['Blue', 'Green', 'Yellow', 'Orange', 'Red']
color_values = [(0.3, 0.594, 0.814), (0.28, 0.77, 0.17), (0.954, 0.788, 0.302), (0.896, 0.571, 0.3), (0.896, 0.3, 0.3)]

plt.pie(color_total, labels=color_names, colors=color_values, autopct='%1.1f%%', textprops={'fontsize': 14})

plt.title('Sour Patch Kids Color Distribution', fontsize=18)

plt.show()
