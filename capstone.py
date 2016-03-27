import numpy as np
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
import scipy.stats as stats
import math


df = pd.read_csv('Data.csv', names =['location', 'year', 'month', 'transactions', 'livedeals'])
chi = df[0:24]
la = df[25:49]
ny = df[50:74]
sf = df[75:99]
dc = df[100:124]

df["location"] = df["location"].astype('category')

###All points###
txns = df['transactions']
ld = df['livedeals']
loc = df['location']
X = ld
y = txns

model = sm.OLS(y, X)
f = model.fit()
print "All Regions OLF Summary"
print f.summary()

fig, ax = plt.subplots()
fit = np.polyfit(X, y, deg=1)
plt.xlabel('# of Live Deals')
plt.ylabel('Transactions')
plt.title('Transactions x # of Live Deals for all Regions')
plt.scatter(X, y)
plt.plot(X, fit[0] * X + fit[1], color='red')
plt.show()


###Chicago###
txns = chi['transactions']
ld = chi['livedeals']
loc = chi['location']
X_chi = ld
y_chi = txns

model = sm.OLS(y_chi, X_chi)
f_chi = model.fit()
print "Chicago OLF Summary"
print f_chi.summary()

fig_chi, ax_chi = plt.subplots()
fit_chi = np.polyfit(X_chi, y_chi, deg=1)
plt.xlabel('# of Live Deals')
plt.ylabel('Transactions')
plt.title('Transactions x # of Live Deals for Chicago')
plt.scatter(X_chi, y_chi)
plt.plot(X_chi, fit_chi[0] * X_chi + fit_chi[1], color='red')
plt.show()


###Los Angeles###
txns = la['transactions']
ld = la['livedeals']
loc = la['location']
X_la = ld
y_la = txns

model = sm.OLS(y_la, X_la)
f_la = model.fit()
print "Los Angeles OLF Summary"
print f_la.summary()

fig_la, ax_la = plt.subplots()
fit_la = np.polyfit(X_la, y_la, deg=1)
plt.xlabel('# of Live Deals')
plt.ylabel('Transactions')
plt.title('Transactions x # of Live Deals for Los Angeles')
plt.scatter(X_la, y_la)
plt.plot(X_la, fit_la[0] * X_la + fit_la[1], color='red')
plt.show()


###New York###
txns = ny['transactions']
ld = ny['livedeals']
loc = ny['location']
X_ny = ld
y_ny= txns

model = sm.OLS(y_ny, X_ny)
f_ny = model.fit()
print "New York OLF Summary"
print f_ny.summary()

fig_ny, ax_ny = plt.subplots()
fit_ny = np.polyfit(X_ny, y_ny, deg=1)
plt.xlabel('# of Live Deals')
plt.ylabel('Transactions')
plt.title('Transactions x # of Live Deals for New York')
plt.scatter(X_ny, y_ny)
plt.plot(X_ny, fit_ny[0] * X_ny + fit_ny[1], color='red')
plt.show()


###San Francisco Bay Area###
txns = sf['transactions']
ld = sf['livedeals']
loc = sf['location']
X_sf = ld
y_sf= txns

model = sm.OLS(y_sf, X_sf)
f_sf = model.fit()
print "San Francisco Bay Area OLF Summary"
print f_sf.summary()

fig_sf, ax_sf = plt.subplots()
fit_sf = np.polyfit(X_sf, y_sf, deg=1)
plt.xlabel('# of Live Deals')
plt.ylabel('Transactions')
plt.title('Transactions x # of Live Deals for San Francisco Bay Area')
plt.scatter(X_sf, y_sf)
plt.plot(X_sf, fit_sf[0] * X_sf + fit_sf[1], color='red')
plt.show()


###Washington DC###
txns = dc['transactions']
ld = dc['livedeals']
loc = dc['location']
X_dc = ld
y_dc= txns

model = sm.OLS(y_dc, X_dc)
f_dc = model.fit()
print "Washington DC OLF Summary"
print f_dc.summary()

fig_dc, ax_dc = plt.subplots()
fit_dc = np.polyfit(X_dc, y_dc, deg=1)
plt.xlabel('# of Live Deals')
plt.ylabel('Transactions')
plt.title('Transactions x # of Live Deals for Washington DC')
plt.scatter(X_dc, y_dc)
plt.plot(X_dc, fit_dc[0] * X_dc + fit_dc[1], color='red')
plt.show()