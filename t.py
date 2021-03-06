import numpy as np
from ipfn import ipfn
import pandas as pd
DP05 = pd.read_csv('DP05.csv')
B01001 = pd.read_csv('B01001.csv')
B01001=B01001.drop(['B01001_001M','GEO_ID','NAME'],axis=1)
print(B01001['B01001_026E'][1])

# B01001=pd.to_numeric(B01001);
# B01001.iloc[1].apply(int)
B01001.iloc[1] = pd.to_numeric(B01001.iloc[1])
print(type(B01001['B01001_003E'][1]))
m = [
    [B01001['B01001_003E'][1], B01001['B01001_004E'][1], B01001['B01001_005E'][1], B01001['B01001_006E'][1]+
     B01001['B01001_007E'][1], B01001['B01001_008E'][1]+ B01001['B01001_009E'][1]+ B01001['B01001_010E'][1],
     B01001['B01001_011E'][1]+ B01001['B01001_012E'][1], B01001['B01001_013E'][1]+ B01001['B01001_014E'][1],
     B01001['B01001_015E'][1]+ B01001['B01001_016E'][1], B01001['B01001_017E'][1], B01001['B01001_018E'][1]+ 
     B01001['B01001_019E'][1], B01001['B01001_020E'][1]+ B01001['B01001_021E'][1]+ B01001['B01001_022E'][1], 
     B01001['B01001_023E'][1]+ B01001['B01001_024E'][1], B01001['B01001_025E'][1] 
     ],
    [B01001['B01001_027E'][1], B01001['B01001_028E'][1], B01001['B01001_029E'][1], B01001['B01001_030E'][1]+
     B01001['B01001_031E'][1], B01001['B01001_032E'][1]+ B01001['B01001_033E'][1]+ B01001['B01001_034E'][1],
     B01001['B01001_035E'][1]+ B01001['B01001_036E'][1], B01001['B01001_037E'][1]+ B01001['B01001_038E'][1],
     B01001['B01001_039E'][1]+ B01001['B01001_040E'][1], B01001['B01001_041E'][1], B01001['B01001_042E'][1]+ 
     B01001['B01001_043E'][1], B01001['B01001_044E'][1]+ B01001['B01001_045E'][1]+ B01001['B01001_046E'][1], 
     B01001['B01001_047E'][1]+ B01001['B01001_048E'][1], B01001['B01001_049E'][1] 
     ]
]
m = np.array(m)
print('initial mat')
print(m)

xip = np.array([B01001['B01001_002E'][1], B01001['B01001_026E'][1]])
xpj = np.array([
    DP05['DP05_0005E'][1], DP05['DP05_0006E'][1], DP05['DP05_0007E'][1], DP05['DP05_0008E'][1],
    DP05['DP05_0009E'][1], DP05['DP05_0010E'][1], DP05['DP05_0011E'][1], DP05['DP05_0012E'][1],
    DP05['DP05_0013E'][1], DP05['DP05_0014E'][1], DP05['DP05_0015E'][1], DP05['DP05_0016E'][1],
    DP05['DP05_0017E'][1]
])

aggregates = [xip, xpj]
dimensions = [[0], [1]]

IPF = ipfn.ipfn(m, aggregates, dimensions, convergence_rate=1e-6)
m = IPF.iteration()
print("after ipf")
print(m)
