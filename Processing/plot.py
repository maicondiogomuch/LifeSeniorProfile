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
    pathP2 = 'C:\\Users\\Rodrigo Girardi\\Documents\\LifeSeniorDatabase-main\\LifeSenior\\'+ str(ATIVIDADE)+'_'+ str(LETRA)+'_'+ str(INDEX)+'\\V2_'+ str(ATIVIDADE)+'_'+ str(LETRA)+'_'+ str(INDEX)+'.csv'
    pathP3 = 'C:\\Users\\Rodrigo Girardi\\Documents\\LifeSeniorDatabase-main\\LifeSenior\\'+ str(ATIVIDADE)+'_'+ str(LETRA)+'_'+ str(INDEX)+'\\V3_'+ str(ATIVIDADE)+'_'+ str(LETRA)+'_'+ str(INDEX)+'.csv'
    pathP4 = 'C:\\Users\\Rodrigo Girardi\\Documents\\LifeSeniorDatabase-main\\LifeSenior\\'+ str(ATIVIDADE)+'_'+ str(LETRA)+'_'+ str(INDEX)+'\\V4_'+ str(ATIVIDADE)+'_'+ str(LETRA)+'_'+ str(INDEX)+'.csv'
    pathP5 = 'C:\\Users\\Rodrigo Girardi\\Documents\\LifeSeniorDatabase-main\\LifeSenior\\'+ str(ATIVIDADE)+'_'+ str(LETRA)+'_'+ str(INDEX)+'\\V5_'+ str(ATIVIDADE)+'_'+ str(LETRA)+'_'+ str(INDEX)+'.csv'
    pathP6 = 'C:\\Users\\Rodrigo Girardi\\Documents\\LifeSeniorDatabase-main\\LifeSenior\\'+ str(ATIVIDADE)+'_'+ str(LETRA)+'_'+ str(INDEX)+'\\V6_'+ str(ATIVIDADE)+'_'+ str(LETRA)+'_'+ str(INDEX)+'.csv'
    pathP7 = 'C:\\Users\\Rodrigo Girardi\\Documents\\LifeSeniorDatabase-main\\LifeSenior\\'+ str(ATIVIDADE)+'_'+ str(LETRA)+'_'+ str(INDEX)+'\\V7_'+ str(ATIVIDADE)+'_'+ str(LETRA)+'_'+ str(INDEX)+'.csv'
    pathP8 = 'C:\\Users\\Rodrigo Girardi\\Documents\\LifeSeniorDatabase-main\\LifeSenior\\'+ str(ATIVIDADE)+'_'+ str(LETRA)+'_'+ str(INDEX)+'\\V8_'+ str(ATIVIDADE)+'_'+ str(LETRA)+'_'+ str(INDEX)+'.csv'
    pathP9 = 'C:\\Users\\Rodrigo Girardi\\Documents\\LifeSeniorDatabase-main\\LifeSenior\\'+ str(ATIVIDADE)+'_'+ str(LETRA)+'_'+ str(INDEX)+'\\V9_'+ str(ATIVIDADE)+'_'+ str(LETRA)+'_'+ str(INDEX)+'.csv'
    pathP10= 'C:\\Users\\Rodrigo Girardi\\Documents\\LifeSeniorDatabase-main\\LifeSenior\\'+ str(ATIVIDADE)+'_'+ str(LETRA)+'_'+ str(INDEX)+'\\V10_'+ str(ATIVIDADE)+'_'+ str(LETRA)+'_'+ str(INDEX)+'.csv'

    dfP1 = pd.read_csv(pathP1)
    dfP2 = pd.read_csv(pathP2)
    dfP3 = pd.read_csv(pathP3)
    dfP4 = pd.read_csv(pathP4)
    dfP5 = pd.read_csv(pathP5)
    dfP6 = pd.read_csv(pathP6)
    dfP7 = pd.read_csv(pathP7)
    dfP8 = pd.read_csv(pathP8)
    dfP9 = pd.read_csv(pathP9)
    dfP10 = pd.read_csv(pathP10)

    xP1= dfP1.index
    xP2= dfP2.index
    xP3= dfP3.index
    xP4= dfP4.index
    xP5= dfP5.index
    xP6= dfP6.index
    xP7= dfP7.index
    xP8= dfP8.index
    xP9= dfP9.index
    xP10= dfP10.index

    plt.figure(figsize=(15, 9))  # Define o tamanho da figura
    plt.plot(xP1, dfP1['acc_y'],  label= 'Paciente 1')  # Gráfico de linha
    plt.plot(xP2, dfP2['acc_y'],  label='Paciente 2')  # Gráfico de linha
    plt.plot(xP3, dfP3['acc_y'],  label='Paciente 3')  # Gráfico de linha
    plt.plot(xP4, dfP4['acc_y'],  label='Paciente 4')  # Gráfico de linha
    plt.plot(xP5, dfP5['acc_y'],  label='Paciente 5')  # Gráfico de linha
    plt.plot(xP6, dfP6['acc_y'],  label='Paciente 6')  # Gráfico de linha
    plt.plot(xP7, dfP7['acc_y'],  label='Paciente 7')  # Gráfico de linha
    plt.plot(xP8, dfP8['acc_y'],  label='Paciente 8')  # Gráfico de linha
    plt.plot(xP9, dfP9['acc_y'],  label='Paciente 9')  # Gráfico de linha
    plt.plot(xP10, dfP10['acc_y'],  label='Paciente 10')  # Gráfico de linha

    # Adicionando detalhes
    plt.xlabel('Pontos')
    plt.ylabel('acc_y')
    plt.title(str(ATIVIDADE)+'_'+ str(LETRA)+'_'+ str(INDEX))
    plt.legend()

    plt.savefig('C:\\Users\\Rodrigo Girardi\\Desktop\\Pacientes para Analise\\Accy\\' + str(ATIVIDADE)+'_'+ str(LETRA)+'_'+ str(INDEX) +'.png', dpi=300)
    # Mostrando o gráfico
    x+=1