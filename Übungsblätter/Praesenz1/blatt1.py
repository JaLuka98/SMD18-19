import numpy as np
import matplotlib.pyplot as plt
import random
from scipy.stats import chi2

np.random.seed(12)

gewicht, groesse = np.genfromtxt('Groesse_Gewicht.txt', unpack=True)
groesse *= 100
plt.subplot(3, 2, 1)
plt.hist(groesse, bins=5, histtype='stepfilled', label='Größe')
plt.hist(gewicht, bins=5, histtype='stepfilled', label='Gewicht')
plt.grid()
plt.legend()
plt.subplot(3, 2, 2)
plt.hist(groesse, bins=10, histtype='stepfilled', label='Größe')
plt.hist(gewicht, bins=10, histtype='stepfilled', label='Gewicht')
plt.grid()
plt.legend()
plt.subplot(3, 2, 3)
plt.hist(groesse, bins=15, histtype='stepfilled', label='Größe')
plt.hist(gewicht, bins=15, histtype='stepfilled', label='Gewicht')
plt.grid()
plt.legend()
plt.subplot(3, 2, 4)
plt.hist(groesse, bins=20, histtype='stepfilled', label='Größe')
plt.hist(gewicht, bins=20, histtype='stepfilled', label='Gewicht')
plt.grid()
plt.legend()
plt.subplot(3, 2, 5)
plt.hist(groesse, bins=30, histtype='stepfilled', label='Größe')
plt.hist(gewicht, bins=30, histtype='stepfilled', label='Gewicht')
plt.grid()
plt.legend()
plt.subplot(3, 2, 6)
plt.hist(groesse, bins=50, histtype='stepfilled', label='Größe')
plt.hist(gewicht, bins=50, histtype='stepfilled', label='Gewicht')
plt.grid()
plt.legend()
plt.tight_layout()
plt.savefig('histgroessegewicht.pdf')
plt.clf()

a = np.zeros(100000)
a += np.random.randint(1, 100, size=100000)
a = np.log(a)
plt.subplot(3, 2, 1)
plt.hist(a, bins=5, histtype='stepfilled', label='Gleichverteilte Zufallszahlen')
plt.grid()
plt.subplot(3, 2, 2)
plt.hist(a, bins=10, histtype='stepfilled', label='Gleichverteilte Zufallszahlen')
plt.grid()
plt.subplot(3, 2, 3)
plt.hist(a, bins=15, histtype='stepfilled', label='Gleichverteilte Zufallszahlen')
plt.grid()
plt.subplot(3, 2, 4)
plt.hist(a, bins=20, histtype='stepfilled', label='Gleichverteilte Zufallszahlen')
plt.grid()
plt.subplot(3, 2, 5)
plt.hist(a, bins=30, histtype='stepfilled', label='Gleichverteilte Zufallszahlen')
plt.grid()
plt.subplot(3, 2, 6)
plt.hist(a, bins=50, histtype='stepfilled', label='Gleichverteilte Zufallszahlen')
plt.grid()
plt.tight_layout()
plt.savefig('uniformhist.pdf')
plt.clf()

sample = np.random.chisquare(df=5, size=100)
plt.hist(sample, bins=15, normed=True, histtype='stepfilled', label='Chi-Quadrat-Histogram')
entries, binEdges = np.histogram(sample, bins=15)
bincenters = 0.5*(binEdges[1:]+binEdges[:-1])
width = binEdges[1] - binEdges[0]
plt.errorbar(bincenters, entries/(100*width), yerr=np.sqrt(entries)/(100*width), fmt='r.')
# also need to normalize the error bars
xlinspace = np.linspace(0,18,1000)
plt.plot(xlinspace, chi2.pdf(xlinspace, 5), label='Chi-Quadrat-Theorie-pdf')
params = chi2.fit(sample)
plt.plot(xlinspace, chi2.pdf(xlinspace, *params), label='Chi-Quadrat-MLE-pdf')
plt.legend()
plt.grid()
plt.savefig('chisquare.pdf')
