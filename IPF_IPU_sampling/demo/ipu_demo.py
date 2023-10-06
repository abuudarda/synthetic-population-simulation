import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def ipu(datafile, constrains):
    df = pd.read_csv(datafile)
    ipf = constrains

    e = np.finfo('float').eps
    for i in ipf:
        if i == 0:
            i = e
    w = np.array(df['Weights'], dtype=np.float32)
    df = df.drop(['Household ID'], axis=1)
    df = df.drop(['Weights'], axis=1)
    ws = np.zeros(6)
    i = 0

    for col  in df.columns:
        x = 0
        for j in range(len(df)) :
            x += w[j]*df[col][j]
        ws[i] = x
        i += 1
    print('weighted sums = ', ws)

    delta = sum((abs(ws-ipf))/ipf)
    print(delta)

    a = df.to_numpy(dtype=np.float32)
    # print(a.shape)
    # print(df.shape)
    print(a)
    print(type(a[1][1]))

    w1 = open("C:\\Users\\abubabu\\Documents\\GitHub\\synthetic-population-simulation\\IPF_IPU_sampling\\demo\\ipu-weights.txt", "w")
    w2 = open("C:\\Users\\abubabu\\Documents\\GitHub\\synthetic-population-simulation\\IPF_IPU_sampling\\demo\\ipu-weighted_sums.txt", "w")
    
    t=1

    while(True):


        delta_prev = delta

        w1.write('iteration'+str(t)+'\n')
        w2.write('iteration'+str(t)+'\n')

        for i in range(df.shape[1]):
            pws = ws[i]
            ws[i] = ipf[i]
            multiplier = ws[i]/pws
            # print(multiplier)
        
            for j in range(df.shape[0]):
                if(a[j][i] == 0):
                    continue
                w[j] *= multiplier
        
            for k in range(df.shape[1]):
                x = 0
                for j in range(df.shape[0]):
                    x += a[j][k]*w[j]
                ws[k] = x
        
            w1.write('weights'+str(i)+str(w)+'\n')
            w2.write("weighted sum"+str(i+1)+str(ws)+'\n')

        delta = sum((abs(ws-ipf))/ipf)
        if(abs(delta_prev-delta) < .0001):
            break
        t+=1


ipf = np.array([4., 5., 3., 7., 4.,9.])
x = ipu('C:\\Users\\abubabu\\Documents\\GitHub\\synthetic-population-simulation\\IPF_IPU_sampling\\demo\\demoipu.csv', ipf)
