import pandas as pd
import os
import matplotlib.pyplot as plt
from datetime import datetime
x=10
for i in range(3):
    ATIVIDADE = 'QD'
    LETRA = 'G'
    INDEX = x

    pathP1 = 'C:\\Users\\Rodrigo Girardi\\Documents\\LifeSeniorDatabase-main\\LifeSenior\\'+ str(ATIVIDADE)+'_'+ str(LETRA)+'_'+ str(INDEX)+'\\V1_'+ str(ATIVIDADE)+'_'+ str(LETRA)+'_'+ str(INDEX)+'.csv'    
    pathP4 = 'C:\\Users\\Rodrigo Girardi\\Documents\\LifeSeniorDatabase-main\\LifeSenior\\'+ str(ATIVIDADE)+'_'+ str(LETRA)+'_'+ str(INDEX)+'\\V4_'+ str(ATIVIDADE)+'_'+ str(LETRA)+'_'+ str(INDEX)+'.csv'

    dfP1 = pd.read_csv(pathP1)
    dfP4 = pd.read_csv(pathP4)
    
    dfP1['acc_y'] = dfP1['acc_y'] * -1
    dfP4['acc_y'] = dfP4['acc_y'] * -1

    dfP1.to_csv('C:\\Users\\Rodrigo Girardi\\Documents\\LifeSeniorDatabase-main\\LifeSenior\\'+ str(ATIVIDADE)+'_'+ str(LETRA)+'_'+ str(INDEX)+'\\V1_'+ str(ATIVIDADE)+'_'+ str(LETRA)+'_'+ str(INDEX)+'.csv', index=False)
    dfP4.to_csv('C:\\Users\\Rodrigo Girardi\\Documents\\LifeSeniorDatabase-main\\LifeSenior\\'+ str(ATIVIDADE)+'_'+ str(LETRA)+'_'+ str(INDEX)+'\\V4_'+ str(ATIVIDADE)+'_'+ str(LETRA)+'_'+ str(INDEX)+'.csv', index=False)
    x +=1