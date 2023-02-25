
import pandas as pd
from ipfn import ipfn
import numpy as np
#a=pd.read_csv("/content/2D Ipf - Untitled spreadsheet - Sheet1.csv")
n=np.ones()


xipp=np.array([4200,3446])
xpjp=np.array([2005,2000,1958,2043])
xppk=np.array([4250,4500])
xijp=np.array([[975,981,974,975],[946,952,947,946]])
xpjk=np.array([[1200,1183],[1000,950],[900,1050],[950,1109]])

n=np.array(n)
aggregates=[xipp,xpjp,xppk,xijp,xpjk]
dimensions=[[0],[1],[2],[0,1],[1,2]]
IPF=ipfn.ipfn(n,aggregates,dimensions,convergence_rate=1e-6)
n=IPF.iteration()
print(n)
