import matplotlib.pyplot as plt
from scipy.stats import bernoulli
import numpy as np

th_prob=0.7*0.7*0.7*0.7*0.3

sample_size=10000

throw1=bernoulli.rvs(size=sample_size, p= 0.3)
throw2=bernoulli.rvs(size=sample_size, p= 0.3)
throw3=bernoulli.rvs(size=sample_size, p= 0.3)
throw4=bernoulli.rvs(size=sample_size, p= 0.3)
throw5=bernoulli.rvs(size=sample_size, p= 0.3)

count=0
for i in range(sample_size):
    if throw1[i]==0 and throw2[i]==0 and throw3[i]==0 and throw4[i]==0 and throw5[i]==1:
        count+=1
sim_prob=count/sample_size
print("Probability from simulation =",sim_prob," Probability from theory =", th_prob)

cases=['i']

x = np.arange(len(cases))
plt.bar(x + 0.00, th_prob, color = 'red', width = 0.25, label = 'Theoretical')
plt.bar(x + 1, sim_prob, color = 'yellow', width = 0.25, label = 'Sim')
plt.xlabel('Cases')
plt.ylabel('Probabilities')

plt.legend()
plt.show()