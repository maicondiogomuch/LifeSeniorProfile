import pandas as pd
import os
from datetime import datetime


# Caminho para o seu arquivo CSV
x=1
for i in range(10):
    PARTICIPANTE = x
    INDEX = 12
    LETRA = 'G'
    ATIVIDADE = 'QD'

    path = 'C:\\Users\\Rodrigo Girardi\\Documents\\LifeSeniorDatabase-main\\LifeSenior\\'+ str(ATIVIDADE)+'_'+ str(LETRA)+'_'+ str(INDEX)+'\\V'+ str(PARTICIPANTE) +'_'+ str(ATIVIDADE)+'_'+ str(LETRA)+'_'+ str(INDEX) +'.csv'

    # Lendo o arquivo CSV
    df = pd.read_csv(path)
    #####ACE
    acc_x = 'acc_x'
    acc_y = 'acc_y'
    acc_z = 'acc_z'
    #####BVP
    bvp = 'bvp'
    #####EDA
    eda = 'eda'
    #####HR
    hr =  'hr'
    #####TEMP
    temp = 'temp'

    ##############################
    ########   EXECUCAO DA FORMULA
    ##############################
    ######## MIN E MAX
    ##ACC == -128 / 128
    ##BVP == -500 / 500
    ##EDA == 0.01 / 100
    ##HR ==     0 / 300
    ##TEMP == -40 / 115

    df['acc_x'] = df['acc_x'].apply(lambda x: (x-(-2))/(2-(-2)))###acelerometria
    df['acc_y'] = df['acc_y'].apply(lambda x: (x-(-2))/(2-(-2)))###acelerometria
    df['acc_z'] = df['acc_z'].apply(lambda x: (x-(-2))/(2-(-2)))###acelerometria

    df['bvp'] = df['bvp'].apply(lambda x: (x-(-500))/(500-(-500)))###acelerometria

    df['eda'] = df['eda'].apply(lambda x: (x-0.01)/(100-0.01))###acelerometria

    df['hr'] = df['hr'].apply(lambda x: (x-0)/(300-0))###acelerometria

    df['temp'] = df['temp'].apply(lambda x: (x-(-40))/(115-(-40)))###acelerometria

    df.to_csv('C:\\Users\\Rodrigo Girardi\\Documents\\LifeSeniorDatabase-main\\FakeDataSet\\'+ str(ATIVIDADE)+'_'+ str(LETRA)+'_'+ str(INDEX) +'\\V'+str(PARTICIPANTE)+'_'+ str(ATIVIDADE)+'_'+ str(LETRA)+'_'+ str(INDEX) +'.csv', float_format='%.6f', index=False)
    x += 1
