from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt
import mc

train_year = (mc.df["year"] <= 2019)
test_year = (mc.df["year"] >= 2023)

interval = 3

def make_data (data):
    x = []
    y = []
    temps = list(data['mean(°C)'])
    for i in range(len(temps)):
        if i <= interval:continue
        y.append(temps[i])
        xa = []
        for p in range(interval):
            d = i + p - interval
            xa.append(temps[d])
        x.append(xa)
    return(x,y)
train_x, train_y = make_data(mc.df[train_year])
test_x, test_y = make_data(mc.df[test_year])

lr = LinearRegression(normalize = True)
lr.fit(train_x, train_y)
pre_y = lr.predict(test_x)

plt.figure(figsize=(10, 6), dpi = 100)
plt.plot(test_y, c='r')
plt.plot(pre_y, c='b')
plt.savefig('5y_lr.png')
plt.show()