import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
from scipy.special import gamma

plt.close('all')

# Tegner Weibulltettheten (en høyreskjev fordeling som ligner på en gammafordeling)
# med formparameter 𝛼=2 og skalaparameter 𝛽=5 og beregner forventning og median.
# Fordelingen weibull_min i scipy.stats har en ekstra lokasjonsparameter,
# som vi setter lik 0; da får vi den Weibull-tettheten vi ønsker.
alpha   = 2
beta    = 5
x       = np.linspace(0,15,1000)
f       = stats.weibull_min.pdf(x, alpha, loc=0, scale=beta)
forv    = beta*gamma(1 + 1/alpha)
med     = beta*(np.log(2))**(1/alpha)
print(forv, med)
plt.plot(x, f)
plt.show()

width   = 0.05
meanX   = np.empty(shape=(10000,5))
medianX = np.empty(shape=(10000,5))
i = 0

# Small change here

# Genererer 1000 datasett hver av størrelse n=5,10,20,30, beregner gjennomsnitt og
# median for hvert av datasettene, og tegner histogram som viser fordelingene til disse:
for n in np.array([5, 10, 20, 30, 100]):

    X            = stats.weibull_min.rvs(alpha, loc=0, scale=beta, size=(n,10000))
    meanX[:,i]   = np.mean(X, axis=0)
    medianX[:,i] = np.median(X, axis=0)
    plt.figure()
    plt.hist(meanX[:,i], color='r', edgecolor='black', density=True,
             bins=np.arange(np.amin([meanX[:,i], medianX[:,i]]), np.amax([meanX[:,i], medianX[:,i]]) + width, width))
    plt.hist(medianX[:,i], color='b', edgecolor='black', density=True, alpha=0.6,
             bins=np.arange(np.amin([meanX[:,i], medianX[:,i]]), np.amax([meanX[:,i], medianX[:,i]]) + width, width))
    plt.title(r'Weibull distribution with $\alpha=$' + str(alpha) + r' and $\beta=$' + str(beta))
    plt.legend(['Mean', 'Median'], title='Sample size $n = $' + str(n), fontsize=12)
    plt.show()
    i += 1
