import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('dummy-ipu.csv')
ipf=np.array([35.,65.,91.,65.,104.])
# print (len(df))
# for index, row in df.iterrows():
#     print(row['h1'], row['h2'])

# for i in range(1,len(df.columns)):
#     print(i)
e=epsilon=np.finfo('float').eps
for i in ipf:
    if i==0: i=e
w=np.array(df['weights'],dtype=np.float32)
df=df.drop(['ID'],axis=1)
df=df.drop(['weights'],axis=1)
ws=np.zeros(5)
i=0

for col in df.columns:
    x=0
    for j in range(len(df)):
        x+=w[j]*df[col][j]
    ws[i]=x
    i+=1
print('weighted sums = ',ws)
a=df.to_numpy(dtype=np.float32)
print(a.shape)
print(df.shape)
print(a)
print(type(a[1][1]))
# print(a[4][5])
# 1=5
# 0=8
for i in range(df.shape[1]):
    pws=ws[i]
    ws[i]=ipf[i]
    multiplier=ws[i]/pws;
    # print(multiplier)
    for j in range(df.shape[0]):
        if(a[j][i]==0):continue
        w[j]*=multiplier
    for k in range(df.shape[1]):
        x=0
        for j in range(df.shape[0]):
            x+=a[j][k]*w[j]
        ws[k]=x
    print('weights',i,w)
    print("weighted sum",i+1,ws)


