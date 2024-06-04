import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df_2014 = pd.read_csv('./day/SURFACE_ASOS_108_DAY_2014_2014_2015.csv', encoding='CP949')
df_2014 = df_2014[ ['일시', '평균기온(°C)', '일강수량(mm)'] ]
df_2014 = df_2014.rename(columns = {'일시':'date', '평균기온(°C)':'mean(°C)', '일강수량(mm)':'month(mm)'} )
df_2014['date'] = pd.to_datetime(df_2014['date'])
df_2014['year'] = df_2014['date'].dt.year
df_2014['month'] = df_2014['date'].dt.month
df_2014['day'] = df_2014['date'].dt.day
df_2014 = df_2014[ ['year', 'month', 'day', 'mean(°C)', 'month(mm)'] ]

df_2015 = pd.read_csv('./day/SURFACE_ASOS_108_DAY_2015_2015_2016.csv', encoding='CP949')
df_2015 = df_2015[ ['일시', '평균기온(°C)', '일강수량(mm)'] ]
df_2015 = df_2015.rename(columns = {'일시':'date', '평균기온(°C)':'mean(°C)', '일강수량(mm)':'month(mm)'} )
df_2015['date'] = pd.to_datetime(df_2015['date'])
df_2015['year'] = df_2015['date'].dt.year
df_2015['month'] = df_2015['date'].dt.month
df_2015['day'] = df_2015['date'].dt.day
df_2015 = df_2015[ ['year', 'month', 'day', 'mean(°C)', 'month(mm)'] ]

df_2016 = pd.read_csv('./day/SURFACE_ASOS_108_DAY_2016_2016_2017.csv', encoding='CP949')
df_2016 = df_2016[ ['일시', '평균기온(°C)', '일강수량(mm)'] ]
df_2016 = df_2016.rename(columns = {'일시':'date', '평균기온(°C)':'mean(°C)', '일강수량(mm)':'month(mm)'} )
df_2016['date'] = pd.to_datetime(df_2016['date'])
df_2016['year'] = df_2016['date'].dt.year
df_2016['month'] = df_2016['date'].dt.month
df_2016['day'] = df_2016['date'].dt.day
df_2016 = df_2016[ ['year', 'month', 'day', 'mean(°C)', 'month(mm)'] ]

df_2017 = pd.read_csv('./day/SURFACE_ASOS_108_DAY_2017_2017_2018.csv', encoding='CP949')
df_2017 = df_2017[ ['일시', '평균기온(°C)', '일강수량(mm)'] ]
df_2017 = df_2017.rename(columns = {'일시':'date', '평균기온(°C)':'mean(°C)', '일강수량(mm)':'month(mm)'} )
df_2017['date'] = pd.to_datetime(df_2017['date'])
df_2017['year'] = df_2017['date'].dt.year
df_2017['month'] = df_2017['date'].dt.month
df_2017['day'] = df_2017['date'].dt.day
df_2017 = df_2017[ ['year', 'month', 'day', 'mean(°C)', 'month(mm)'] ]

df_2018 = pd.read_csv('./day/SURFACE_ASOS_108_DAY_2018_2018_2019.csv', encoding='CP949')
df_2018 = df_2018[ ['일시', '평균기온(°C)', '일강수량(mm)'] ]
df_2018 = df_2018.rename(columns = {'일시':'date', '평균기온(°C)':'mean(°C)', '일강수량(mm)':'month(mm)'} )
df_2018['date'] = pd.to_datetime(df_2018['date'])
df_2018['year'] = df_2018['date'].dt.year
df_2018['month'] = df_2018['date'].dt.month
df_2018['day'] = df_2018['date'].dt.day
df_2018 = df_2018[ ['year', 'month', 'day', 'mean(°C)', 'month(mm)'] ]

df_2019 = pd.read_csv('./day/SURFACE_ASOS_108_DAY_2019_2019_2020.csv', encoding='CP949')
df_2019 = df_2019[ ['일시', '평균기온(°C)', '일강수량(mm)'] ]
df_2019 = df_2019.rename(columns = {'일시':'date', '평균기온(°C)':'mean(°C)', '일강수량(mm)':'month(mm)'} )
df_2019['date'] = pd.to_datetime(df_2019['date'])
df_2019['year'] = df_2019['date'].dt.year
df_2019['month'] = df_2019['date'].dt.month
df_2019['day'] = df_2019['date'].dt.day
df_2019 = df_2019[ ['year', 'month', 'day', 'mean(°C)', 'month(mm)'] ]

df_2020 = pd.read_csv('./day/SURFACE_ASOS_108_DAY_2020_2020_2021.csv', encoding='CP949')
df_2020 = df_2020[ ['일시', '평균기온(°C)', '일강수량(mm)'] ]
df_2020 = df_2020.rename(columns = {'일시':'date', '평균기온(°C)':'mean(°C)', '일강수량(mm)':'month(mm)'} )
df_2020['date'] = pd.to_datetime(df_2020['date'])
df_2020['year'] = df_2020['date'].dt.year
df_2020['month'] = df_2020['date'].dt.month
df_2020['day'] = df_2020['date'].dt.day
df_2020 = df_2020[ ['year', 'month', 'day', 'mean(°C)', 'month(mm)'] ]

df_2021 = pd.read_csv('./day/SURFACE_ASOS_108_DAY_2021_2021_2022.csv', encoding='CP949')
df_2021 = df_2021[ ['일시', '평균기온(°C)', '일강수량(mm)'] ]
df_2021 = df_2021.rename(columns = {'일시':'date', '평균기온(°C)':'mean(°C)', '일강수량(mm)':'month(mm)'} )
df_2021['date'] = pd.to_datetime(df_2021['date'])
df_2021['year'] = df_2021['date'].dt.year
df_2021['month'] = df_2021['date'].dt.month
df_2021['day'] = df_2021['date'].dt.day
df_2021 = df_2021[ ['year', 'month', 'day', 'mean(°C)', 'month(mm)'] ]

df_2022 = pd.read_csv('./day/SURFACE_ASOS_108_DAY_2022_2022_2023.csv', encoding='CP949')
df_2022 = df_2022[ ['일시', '평균기온(°C)', '일강수량(mm)'] ]
df_2022 = df_2022.rename(columns = {'일시':'date', '평균기온(°C)':'mean(°C)', '일강수량(mm)':'month(mm)'} )
df_2022['date'] = pd.to_datetime(df_2022['date'])
df_2022['year'] = df_2022['date'].dt.year
df_2022['month'] = df_2022['date'].dt.month
df_2022['day'] = df_2022['date'].dt.day
df_2022 = df_2022[ ['year', 'month', 'day', 'mean(°C)', 'month(mm)'] ]

df_2023 = pd.read_csv('./day/SURFACE_ASOS_108_DAY_2023_2023_2024.csv', encoding='CP949')
df_2023 = df_2023[ ['일시', '평균기온(°C)', '일강수량(mm)'] ]
df_2023 = df_2023.rename(columns = {'일시':'date', '평균기온(°C)':'mean(°C)', '일강수량(mm)':'month(mm)'} )
df_2023['date'] = pd.to_datetime(df_2023['date'])
df_2023['year'] = df_2023['date'].dt.year
df_2023['month'] = df_2023['date'].dt.month
df_2023['day'] = df_2023['date'].dt.day
df_2023 = df_2023[ ['year', 'month', 'day', 'mean(°C)', 'month(mm)'] ]

df = pd.concat([df_2019, df_2020, df_2021, df_2022, df_2023])

md = {}
for i, row in df.iterrows():
    m, d, mc, mm = (int(row['month']), int(row['day']), float(row['mean(°C)']), float(row['month(mm)']))
    key = str(m) + '/' + str(d)
    if not(key in md) : md[key] = []
    md[key] += [mc]
    #md[key] += [mm]

avs = {}
for key in md:
    mc = avs[key] = sum(md[key]) / len(md[key])
   # mm = avs[key] = sum(md[key]) / len(md[key])
    print("{0} : {1}".format(key, mc))
    #print("{0} : {1}".format(key, mm))
#avs['6/1']

g = df.groupby(['month'])['mean(°C)']
g_avg = g.sum() / g.count()
print(g_avg)

g_avg.plot()
plt.savefig('5y_month_avg.png')
plt.show()
