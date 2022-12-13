import pandas as pd
import matplotlib.pyplot as plt


plt.style.use('seaborn-v0_8')
games = pd.read_csv('Video_Games_Sales_as_at_22_Dec_2016.csv')

#Выборка наиболее продаваемых игр не от компании Nintendo
games = games[games['Global_Sales'].notna()] #Убираем все строки в которых общие продажи неизвестны
games.sort_values('Global_Sales')
df = games.loc[games['Publisher'] != 'Nintendo']

#Гипотеза - при наличии в игре портов на PS3 и X360,
#версия на PS3 в среднем продавалась лучше, чем на X360

df2 = games.loc[games['Platform'] == 'PS3']
df3 = games.loc[games['Platform'] == 'X360']

s1 = pd.merge(df2, df3, how='inner', on=['Name'])
df2 = df2.loc[df2['Name'].isin(s1['Name'])]
df3 = df3.loc[df3['Name'].isin(s1['Name'])]
print('Средние продажи на PS3', df2['Global_Sales'].mean())
print('Средние продажи на X360', df3['Global_Sales'].mean())

#По итогу оказалось, что средние продажи на данных платформах примерно одинаковы,
#X360 ведёт лишь с небольшим отрывом


#Визуализация графика в MatPlotLib
df1 = df.head(15)
plt.bar(df1['Name'], df1['Global_Sales'])
plt.show()
