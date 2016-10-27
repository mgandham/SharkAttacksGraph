import pandas as pd
import matplotlib.pyplot as plt

# series1 = pd.Series(['My','Name','Is','Manu'],index=['a','b','c','d'])
#
# df = pd.DataFrame({'words':series1.values,'more words':series1.values},columns=['more words','words'])

df = pd.read_csv('attacks.csv')
df = df[df['Type']=='Unprovoked']
df = df[df['Fatal (Y/N)'] == 'Y']

years = df.loc[:,['Year']]
years = years[years['Year']>1800]
grouped_years = years.groupby('Year').size()

grouped_years.plot(label="Unprovoked Fatalities")

rolling_avg = pd.rolling_mean(grouped_years,10)
rolling_avg.plot(label="rolling mean")

plt.legend(loc='upper left')
plt.show()
