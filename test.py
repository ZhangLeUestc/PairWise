
import random, csv, time, os

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from scipy import optimize

def append_pair(comp, name1, name2, name_to_num):
    if comp == '-1':
        return((name_to_num[name2], name_to_num[name1]))
    if comp == '1':
        return((name_to_num[name1], name_to_num[name2]))
name_to_num = dict()
# Here pairs will be a list of 5 lists correpesonding to each of the 5 traits
global pairs
pairs = [[],[],[],[],[]]

j = 0
path = '/media/m2a02/2TB/AutomaticPersonalityAnalysisBaseline-master/data/'
files = [f for f in os.listdir(path) if f.endswith('.csv')]

for file in files:
    with open(path+file, 'r') as csvfile:
        reader = csv.reader(csvfile )
        for row in reader:
            
            
              if not row[1] in name_to_num:
                 name_to_num[row[1]] = j
                 j += 1
              if not row[2] in name_to_num:
                 name_to_num[row[2]] = j
                 j += 1
              for i in range(3,5):
                 pair = append_pair(row[i],row[1],row[2],name_to_num)
                 if pair != None:
                    pairs[i-3].append(pair)
video_num = j
print(pairs)
print(video_num)

def mle(w):
    out=-1
    comp=pairs[0]
    for pair in comp:
        print(pair)
        out*=1/(1+np.exp(-w[pair[0]]+w[pair[1]]))
    return out

w=np.random.uniform(-5,-5,4)
bnds=((0,None),(0,None))
bnds=()
cons=()
for i in range(4):
    bnds+=((-5.0,5.0),)

cons+=({'type':'ineq', 'fun': lambda w: np.abs(np.sum(w))},)

res=optimize.minimize(mle,w,bounds=bnds,options={'disp': True})
print(res['x'])
