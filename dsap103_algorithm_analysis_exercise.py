"""
第三章 算法分析

"""
from matplotlib import pyplot as plt
import numpy as np
# %% R-3.1 plot graph of 8n/4n*log(n)/2n^2/n^3/2^n; x&y axis to logarithmic scale
x=np.arange(2,102,1)
x_log=np.log2(x)
y=np.empty([len(x),5])
y[:,0]=8*x; y[:,1]=4*x*x_log; y[:,2]=2*x**2; y[:,3]=x**3; y[:,4]=2**x
y_log=np.log(y)
plt.plot(x_log,y_log)
# plt.xlim((1,10)); plt.ylim((1,10))
plt.xlabel('log2(x)'); plt.ylabel('log2(y)')
plt.legend(labels=['8n','4n*log(n)','2n^2','n^3','2^n'])
plt.show()
# %% R-3.2 find min(n0) that 8*n0*log(n0)<2*n0^2


# %% test


