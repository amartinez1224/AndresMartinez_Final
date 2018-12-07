import numpy as np
import matplotlib.pyplot as plt

A = np.genfromtxt("datos_observacionales.dat")
#derivar
n1 = ((A[:,1])[2:]-(A[:,1])[:np.size((A[:,1]))-2])/0.1
n2 = ((A[:,2])[2:]-(A[:,2])[:np.size((A[:,2]))-2])/0.1
n3 = ((A[:,3])[2:]-(A[:,3])[:np.size((A[:,3]))-2])/0.1
#MonteCarlo
def fun1(o):
    return np.sum(np.exp(-((o*(A[:,2]-A[:,1])[1:-1]-n1)**2)))
def fun2(o):
    return np.sum(np.exp(-(((A[:,1]*(o-A[:,3])-A[:,2])[1:-1]-n2)**2)))
def fun2(o):
    return np.sum(np.exp(-((A[:,1]*A[:,2]-o*A[:,3])[1:-1]-n3)**2))
s=[10]
r=[10]
b=[10]
for i in range(1,1000):
    st = np.random.normal(s[i-1],1)
    rt = np.random.normal(r[i-1],1)
    bt = np.random.normal(b[i-1],1)
    if (fun1(st)>fun1(s[i-1]) or (fun1(st)/fun1(s[i-1]))>np.random.rand()):
        s.append(st)
    else:
        s.append(s[i-1])
        
    if (fun1(rt)>fun1(r[i-1]) or (fun1(rt)/fun1(r[i-1]))>np.random.rand()):
        r.append(rt)
    else:
        r.append(r[i-1])
        
    if (fun1(bt)>fun1(b[i-1]) or (fun1(bt)/fun1(b[i-1]))>np.random.rand()):
        b.append(bt)
    else:
        b.append(b[i-1])


plt.hist(s)
plt.hist(r)
plt.hist(b)
plt.title("Sigma: "+np.mean(np.array(s))+", Rho: "+np.mean(np.array(r))+", Beta: "+np.mean(np.array(b)))
plt.savefig("a")
plt.close()
plt.plot(A[:,1])
plt.plot(A[:,2])
plt.plot(A[:,3])
plt.savefig("b")
