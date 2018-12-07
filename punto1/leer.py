import numpy as np
import matplotlib.pyplot as plt

A = list()
for i in range(8):
    a = np.genfromtxt("archivo"+str(i)+".dat")
    A.append(a)
    b=np.linspace(-2,2,100)
    plt.hist(a,density=True)
    plt.plot(b,(np.exp((-b**2)/2))/(np.sqrt(2*np.pi)))
    plt.savefig("archivo"+str(i)+".pdf")
    plt.close()
V=list()
K=list()
for k in range(1,1000):
    B=0
    W=0
    for i in A:
        B=B+((1000/7)*(np.mean(i[0:k])-np.var(i[0:k]))**2)
        W=W+((1/7)*(np.var(i[0:k]))**2)
    V.append(((999/1000)*W)+((9/8000)*B))
    K.append(k)
plt.plot(K,V)
plt.savefig("rubin.pdf")