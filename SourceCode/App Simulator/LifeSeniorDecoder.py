import os
import csv
import time
import queue
import socket
import random
import struct
import threading
import pandas as pd
import tkinter as tk
from threading import *
from tkinter import font
from collections import deque
from typing import Deque, Any
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from colorama import Fore, Back, Style, init
from matplotlib.animation import FuncAnimation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg



##############################################
######### JANELA
##############################################

janela = tk.Tk()
janela.title("LifeSenior Server - v0.1")
janela.geometry("1920x1080")
janela.configure(background='#dde')
fig1, axs = plt.subplots(2, 2)
fig1.set_size_inches(20, 10)
frame1 = tk.Frame(janela)
frame1.pack(side=tk.LEFT, anchor=tk.S)
canvas1 = FigureCanvasTkAgg(fig1, master=frame1)
canvas1_widget = canvas1.get_tk_widget()
canvas1_widget.pack()
##############################################
######### JANELA
##############################################

pack = []
count = 0
countLinhas = 0
num_points = 25
num_displayed = 50
init(autoreset=True)
fifo = queue.Queue()
MAX_SIZE_BUFFER = 2000
plotagem = queue.Queue()

waveTime = queue.Queue()
waveAcex = queue.Queue()
waveAcey = queue.Queue()
waveAcez = queue.Queue()
waveGyx = queue.Queue()
waveGyy = queue.Queue()
waveGyz = queue.Queue()
waveAzi = queue.Queue()
wavePitch = queue.Queue()
waveRoll = queue.Queue()

real_time = deque(maxlen=num_displayed)
yAceleX = deque(maxlen=num_displayed)
yAceleY = deque(maxlen=num_displayed)
yAceleZ = deque(maxlen=num_displayed)
yGyroX = deque(maxlen=num_displayed)
yGyroY = deque(maxlen=num_displayed)
yGyroZ = deque(maxlen=num_displayed)
yAzimuth = deque(maxlen=num_displayed)
yPitch = deque(maxlen=num_displayed)
yRoll = deque(maxlen=num_displayed)
yLabel = deque(maxlen=num_displayed)

################### SERVIDOR
def servidor():
    HOST = socket.gethostbyname(socket.gethostname())
    PORT = 5555
    recebe = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    recebe.bind((HOST, PORT))
    recebe.listen(1)
    print('Aguardando conexão de um cliente...')
    print(HOST)
    print(PORT)
    sc, endereco = recebe.accept()  # Aceita a conexão e obtém o objeto de soquete e o endereço do cliente
    print("Aceitei o cliente")
    while True:
        ler_fifo = sc.recv(1024)
        if ler_fifo == b'exit':#Mudar caso precise --->b'exit'<---
            break
        #dado = ler_fifo.decode("utf-8")
        hex_string = ' '.join(format(byte, '02x') for byte in ler_fifo)
        hex_parts = hex_string.split()# Divida a string formatada em partes individuais usando o espaço em branco como separador
        fifo.put(hex_parts)#colocado dado no buffer
        print(f"Ler_exit: {ler_fifo}")
        #print("Servidor foi chamado e escreveu na FIFO")
        #print(fifo.qsize())
        
            
    print("Servidor Finalizado")
    sc.close()
    recebe.close()
    

def animate(i, ax1, ax2, ax3, ax4, num_points,count=0):

    count += 1

    maxGraphU = 20
    maxGraphL = -20
    i = 0
    print(f'Contador: {i}')
    
    #eixo x
    ax1.clear()
    if waveTime.empty() == False:
        #print(f"time= {waveTime.get()}")
        real_time.append(waveTime.get())#waveTime.get()
        real_time.append(waveTime.get())#waveTime.get()
        '''real_time.append(waveTime.get())#waveTime.get()
        real_time.append(waveTime.get())#waveTime.get()
        real_time.append(waveTime.get())#waveTime.get()'''
    '''if waveTime.empty() == True:
        real_time.append(count)#waveTime.get()'''
    ############ace
    if waveAcex.empty() == False:
        #print(f"acex={waveAcex.get()}")
        yAceleX.append(waveAcex.get())#waveAcex.get()
        yAceleX.append(waveAcex.get())#waveAcex.get()
        '''yAceleX.append(waveAcex.get())#waveAcex.get()
        yAceleX.append(waveAcex.get())#waveAcex.get()
        yAceleX.append(waveAcex.get())#waveAcex.get()'''
        ax1.plot(real_time, yAceleX, label='AceleX')
    '''if waveAcex.empty() == True:
        yAceleX.append(0)#waveAcex.get()
        ax1.plot(real_time, yAceleX, label='AceleX')'''

    if waveAcey.empty() == False:
        yAceleY.append(waveAcey.get())#waveAcey.get()
        yAceleY.append(waveAcey.get())#waveAcey.get()
        '''yAceleY.append(waveAcey.get())#waveAcey.get()
        yAceleY.append(waveAcey.get())#waveAcey.get()
        yAceleY.append(waveAcey.get())#waveAcey.get()'''
        ax1.plot(real_time, yAceleY, label='AceleY')
    '''if waveAcey.empty() == True:
        yAceleY.append(0)#waveAcey.get()
        ax1.plot(real_time, yAceleY, label='AceleY')'''

    if waveAcez.empty() == False:
        yAceleZ.append(waveAcez.get())#waveAcex.get()
        yAceleZ.append(waveAcez.get())#waveAcex.get()
        '''yAceleZ.append(waveAcez.get())#waveAcex.get()
        yAceleZ.append(waveAcez.get())#waveAcex.get()
        yAceleZ.append(waveAcez.get())#waveAcex.get()'''
        ax1.plot(real_time, yAceleZ, label='AceleZ')
        ax1.legend()
        ax1.set_title('Gráfico 1: Acelerometria XYZ')
        ax1.set_xlim(min(real_time), max(real_time))
        ax1.set_ylim(maxGraphL, maxGraphU)
    '''if waveAcez.empty() == True:
        yAceleZ.append(0)#waveAcex.get()
        ax1.plot(real_time, yAceleZ, label='AceleZ')
        ax1.legend()
        ax1.set_title('Gráfico 1: Acelerometria XYZ')
        ax1.set_xlim(min(real_time), max(real_time))
        ax1.set_ylim(maxGraphL, maxGraphU)'''

    ###################gy
    ax2.clear()
    if waveGyx.empty() == False:
        yGyroX.append(waveGyx.get())#waveGyx.get()
        ax2.plot(real_time, yGyroX, label='GyroX')
    if waveGyy.empty() == False:
        yGyroY.append(waveGyy.get())#waveGyy.get()
        ax2.plot(real_time, yGyroY, label='GyroY')
    if waveGyz.empty() == False:
        yGyroZ.append(waveGyz.get())#waveGyz.get()
        ax2.plot(real_time, yGyroZ, label='GyroZ')
        ax2.legend()
        ax2.set_title('Gráfico 2: Giroscopio XYZ')
        ax2.set_xlim(min(real_time), max(real_time))
        ax2.set_ylim(maxGraphL, maxGraphU)

    ##################mag
    '''ax3.clear()
    if waveAzi.empty() == False:
        yAzimuth.append(random.randint(1, 100))#waveAzi.get()
        ax3.plot(real_time, yAzimuth, label='Azimuth')
        ax3.legend()
        ax3.set_title('Gráfico 3: Azimuth')
        ax3.set_ylim(-10, 370)
    ax4.clear()   
    if wavePitch.empty() == False:
        yPitch.append(random.randint(1, 100))#wavePitch.get()
        ax4.plot(real_time, yPitch, label='Pitch') 
    if waveRoll.empty() == False:
        yRoll.append(random.randint(1, 100))#waveRoll.get()
        ax4.plot(real_time, yRoll, label='Roll')
        ax4.legend()
        ax4.set_title('Gráfico 4: Pitch, Roll')
        ax4.set_ylim(-200, 200)'''


    #count = 0
    '''real_time.append(random.randint(1, 100))
    yAceleX.append(random.randint(1, 100))
    yAceleY.append(random.randint(1, 100))
    yAceleZ.append(random.randint(1, 100))
    yGyroX.append(random.randint(1, 100))
    yGyroY.append(random.randint(1, 100))
    yGyroZ.append(random.randint(1, 100))
    #yAzimuth.append(float(a['azimuth']))
    #yPitch.append(float(a['pitch']))
    #yRoll.append(float(a['roll']))
    #yLabel.append(str(a['label']))'''
        #Data.drop(axis='index')
    

    #ax5.clear()
    #ax5.plot(real_time, yRoll, label='Roll')
    #ax5.legend()
    #ax5.set_title('Gráfico 5: Roll')
    #ax5.set_ylim(-70, 70)

    #ax6.clear()
    #ax6.plot(real_time, yLabel, label='Label', color='red', linestyle='dashed', linewidth=2, markersize=12)
    #ax6.legend()
    #ax6.set_title('ATIVIDADE')


    # Inicialização dos subplots
    #fig1, axs = plt.subplots(2, 3, figsize=(50, 10))

################### TIMER
def timer():#chama o decodificador a cada 0.1 ou 0.05 segundos
    #print(Fore.GREEN + "Timer chamado!")
    while True:
        if fifo.qsize() >= MAX_SIZE_BUFFER:#CHEIO
            print("Timer chamado: FIFO cheia")
            package =  fifo.get()
            #print(f"Fifo get: {dataFifo}")
            split(package)
            
            #ani = FuncAnimation(fig1, animate, fargs=(axs[0, 0], axs[0, 1], axs[1, 0], axs[1, 1], num_points), interval=500)
            #print(f"Fifo Get: {package}")
            #print(f"package: {package}")
            time.sleep(0.005)#Acelerando leitura de buffer    0.05
        if fifo.empty():#se fifo estiver vazia
            print(Fore.RED + "Fifo vazia...")
            time.sleep(0.05)
            #time.sleep(1)
            '''if semaphorePlot.acquire(blocking=False):
            ani = FuncAnimation(fig1, animate, fargs=(axs[0, 0], axs[0, 1], axs[1, 0], axs[1, 1], num_points), interval=500)
            semaphorePlot.acquire()
            semaphorePlot.acquire()
            return ani'''
        else:
            print("Timer chamado: FIFO não cheia")
            '''dataFifo = fifo.get()
            subStr = dataFifo.split()
            package = [int(valor) for valor in subStr]'''
            #print(f"Fifo get: {dataFifo}")
            
            #byte_array = bytes.fromhex(hex_string)
            package =  fifo.get()
            #print(f"Fifo Get: {package}")
            split(package)
            #ani = FuncAnimation(fig1, animate, fargs=(axs[0, 0], axs[0, 1], axs[1, 0], axs[1, 1], num_points), interval=500)
            time.sleep(0.05)#0.05
        #time.sleep(t)  # Espera "t" milissegundos

################### Funcao de escrita no arquivo
arq = "C:Decoder\packOk.csv"
semaphorePlot = Semaphore(2)
semaphorePlot.acquire()
semaphorePlot.acquire()
#semaphorePlot.acquire()
def escrita(pack):
    #print(f"Escrevi e Mandei para PLotar: = {pack}")
    with open(arq, mode='a', newline='') as arquivo_csv:
        escritor_csv = csv.writer(arquivo_csv)
        escritor_csv.writerow(pack)

    waveTime.put(pack[0])#(pack(0))
    #print(f"time= {waveTime.get()}")
    waveAcex.put(pack[1])#(pack(1))
    #print(f"acex={waveAcex.get()}")
    waveAcey.put(pack[2])#(pack(2))
    #print(f"acey = {waveAcey.get()}")
    waveAcez.put(pack[3])#(pack(3))
    #print(f"acez = {waveAcez.get()}")
    waveGyx.put(pack[4])#(pack(4))
    #print(f"gyx = {waveGyx.get()}")
    waveGyy.put(pack[5])#(pack(5))
    #print(f"gyy = {waveGyy.get()}")
    waveGyz.put(pack[6])#(pack(6))
    #print(f"gyz = {waveGyz.get()}")
    ''' waveAzi.put(pack[7])#(pack(7))
    #print(f"azi = {waveAzi.get()}")
    wavePitch.put(pack[8])#(pack(8))
    #print(f"pitch = {wavePitch.get()}")
    waveRoll.put(pack[9])#(pack(9))'''
    #print(f"Roll = {waveRoll.get()}")
    #ani.resume()

    '''print(f"Linhas escritas = {countLinhas}")
    if countLinhas > 100:
        semaphorePlot.release()
        print(Fore.GREEN + "LIBEREI")'''
    
    '''
    plotagem.put(pack)
    '''
#if semaphorePlot.acquire(blocking=False):
#    ani = FuncAnimation(fig1, animate, fargs=(axs[0, 0], axs[0, 1], axs[1, 0], axs[1, 1], num_points), interval=500)


'''while countLinhas < 50 and semaphorePlot.acquire(blocking=True):
    semaphorePlot.acquire()
    ani = FuncAnimation(fig1, animate, fargs=(axs[0, 0], axs[0, 1], axs[1, 0], axs[1, 1], num_points), interval=500)
    break'''

################### Converte para ponto flutuante o hexa
def hex_to_float(hex_string):
    # Converte a string hexadecimal para bytes
    hex_bytes = bytes.fromhex(hex_string)
    
    # Desempacota os 8 bytes em um float usando o formato 'd'
    float_value = struct.unpack('!f', hex_bytes)[0]
    return float_value
################### Monta para escrever no arquivo
pack = [0] * 11
#count = 0
def assembly(parts):
    if parts[0] == '02':#acelerometria
        timestamp = 0
        time1 = int(parts[2],16)
        time2 = int(parts[3],16)
        time3 = int(parts[4],16)
        time4 = int(parts[5],16)
        timestamp += time1
        timestamp += time2 * 256
        timestamp += time3 * 256 * 256
        timestamp += time4 * 256 * 256 *256
        #print(f"timestamp = {timestamp}")
        #pack.append(timestamp)
        #float_value = hex_to_float(timestamp)
        #time = float_value

        acex1 = parts[6]
        acex2 = parts[7]
        acex3 = parts[8]
        acex4 = parts[9]
        concatenado = str(acex4) + str(acex3) + str(acex2) + str(acex1)#big endian
        #print(f"Accex = {concatenado}")
        float_value = hex_to_float(concatenado)
        acex = float_value

        acey1 = parts[10]
        acey2 = parts[11]
        acey3 = parts[12]
        acey4 = parts[13]
        concatenado = str(acey4) + str(acey3) + str(acey2) + str(acey1)#big endian
        #print(f"Accey = {concatenado}")
        float_value = hex_to_float(concatenado)
        acey = float_value
        #acey = "{:.{}f}".format(acey, precisao)

        acez1 = parts[14]
        acez2 = parts[15]
        acez3 = parts[16]
        acez4 = parts[17]
        concatenado = str(acez4) + str(acez3) + str(acez2) + str(acez1)#big endian
        #print(f"Accez = {concatenado}")
        float_value = hex_to_float(concatenado)
        acez = float_value
        #acez = "{:.{}f}".format(acez, precisao)

        #pack.append(timestamp)#0 
        #pack.append(acex)#1
        #pack.append(acey)#2
        #pack.append(acez)#3

        pack.insert(0,timestamp)
        pack.insert(1,acex)
        pack.insert(2,acey)
        pack.insert(3,acez)

        #count = count + 1
        #print(f"count: {count}")
        #print(f"Pacote: {pack}")
    if parts[0] == '03': #gyroscope
        gyx1 = parts[6]
        gyx2 = parts[7]
        gyx3 = parts[8]
        gyx4 = parts[9]
        concatenado = str(gyx4) + str(gyx3) + str(gyx2) + str(gyx1)#big endian
        #print(f"Gyx = {concatenado}")
        float_value = hex_to_float(concatenado)
        gyx = float_value
        #gyx = "{:.{}f}".format(gyx, precisao)

        gyy1 = parts[10]
        gyy2 = parts[11]
        gyy3 = parts[12]
        gyy4 = parts[13]
        concatenado = str(gyy4) + str(gyy3) + str(gyy2) + str(gyy1)#big endian
        #print(f"Gyy = {concatenado}")
        float_value = hex_to_float(concatenado)
        gyy = float_value
        #gyy = "{:.{}f}".format(gyy, precisao)

        gyz1 = parts[14]
        gyz2 = parts[15]
        gyz3 = parts[16]
        gyz4 = parts[17]
        concatenado = str(gyz4) + str(gyz3) + str(gyz2) + str(gyz1)#big endian
        #print(f"Gyz = {concatenado}")
        float_value = hex_to_float(concatenado)
        gyz = float_value
        #gyz = "{:.{}f}".format(gyz, precisao)

        pack.insert(4,gyx)#posicao/valor
        pack.insert(5,gyy)#posicao/valor
        pack.insert(6,gyz)#posicao/valor
        #pack[4]=gyx
        #pack[5]=gyy
        #pack[6]=gyz
        #count = count + 1
        #print(f"count: {count}")
        #print(f"Pacote: {pack}")
    if parts[0] == '04': #mag =>azimuth pitch roll 
        mag1 = parts[6]
        mag2 = parts[7]
        mag3 = parts[8]
        mag4 = parts[9]
        concatenado = str(mag4) + str(mag3) + str(mag2) + str(mag1)#big endian
        #print(f"azi = {concatenado}")
        float_value = hex_to_float(concatenado)
        azi = float_value
        #azi = "{:.{}f}".format(azi, precisao)

        mag1 = parts[10]
        mag2 = parts[11]
        mag3 = parts[12]
        mag4 = parts[13]
        concatenado = str(mag4) + str(mag3) + str(mag2) + str(mag1)#big endian
        #print(f"pit = {concatenado}")
        float_value = hex_to_float(concatenado)
        pit = float_value
        #pit = "{:.{}f}".format(gyy, precisao)

        mag1 = parts[14]
        mag2 = parts[15]
        mag3 = parts[16]
        mag4 = parts[17]
        concatenado = str(mag4) + str(mag3) + str(mag2) + str(mag1)#big endian
        #print(f"Roll = {concatenado}")
        float_value = hex_to_float(concatenado)
        roll = float_value
        #roll = "{:.{}f}".format(roll, precisao)

        pack.insert(7,azi)#posicao/valor
        pack.insert(8,pit)#posicao/valor
        pack.insert(9,roll)#posicao/valor
        #pack[7]=azi
        #pack[8]=pit
        #pack[9]=roll
        #count = count + 1
        print(f"count: {count}")
        #print(f"Pacote: {pack}")
    if parts[0] == '05': #label
        #l1 = parts[6]
        #l2 = parts[7]
        #l3 = parts[8]
        #l4 = parts[9]
        #concatenado = str(l4) + str(l3) + str(l2) + str(l1)#big endian
        #print(f"Accex = {concatenado}")
        #float_value = hex_to_float(concatenado)
        #label = float_value
        #label = "{:.{}f}".format(label, precisao)
        if parts[6] == '00':    
            pack.insert(10,'BSC')#posicao/valor
        if parts[6] == '01':    
            pack.insert(10,'CHU')#posicao/valor
        if parts[6] == '02':    
            pack.insert(10,'CSI')#posicao/valor
        if parts[6] == '03':    
            pack.insert(10,'CSO')#posicao/valor
        if parts[6] == '04':    
            pack.insert(10,'FKL')#posicao/valor
        if parts[6] == '05':    
            pack.insert(10,'FOL')#posicao/valor
        if parts[6] == '06':    
            pack.insert(10,'JOG')#posicao/valor
        if parts[6] == '07':    
            pack.insert(10,'JUM')#posicao/valor
        if parts[6] == '08':    
            pack.insert(10,'SBE')#posicao/valor
        if parts[6] == '09':    
            pack.insert(10,'SBW')#posicao/valor
        if parts[6] == '0A':    
            pack.insert(10,'SCH')#posicao/valor
        if parts[6] == '0B':    
            pack.insert(10,'SDL')#posicao/valor
        if parts[6] == '0C':    
            pack.insert(10,'SIT')#posicao/valor
        if parts[6] == '0D':    
            pack.insert(10,'SLH')#posicao/valor
        if parts[6] == '0E':    
            pack.insert(10,'SLW')#posicao/valor
        if parts[6] == '0F':    
            pack.insert(10,'SRH')#posicao/valor
        if parts[6] == '10':    
            pack.insert(10,'STD')#posicao/valor
        if parts[6] == '11':    
            pack.insert(10,'STN')#posicao/valor
        if parts[6] == '12':    
            pack.insert(10,'STU')#posicao/valor
        if parts[6] == '13':    
            pack.insert(10,'WAL')#posicao/valor
        if parts[6] == '14':    
            pack.insert(10,'LYI')#posicao/valor
        #count = count + 1
        #print(f"count: {count}")
        #print(f"Pacote: {pack}")
    if parts[0] == '06': #position
        #p1 = parts[6]
        #p2 = parts[7]
        #p3 = parts[8]
        #p4 = parts[9]
        #concatenado = str(p4) + str(p3) + str(p2) + str(p1)#big endian
        #print(f"Accex = {concatenado}")
        #float_value = hex_to_float(concatenado)
        #position = float_value
        #position = "{:.{}f}".format(position, precisao)

        if parts[6] == '00':    
            pack.insert(11,'ROM')#posicao/valor
        if parts[6] == '01':    
            pack.insert(11,'LRM')#posicao/valor
        if parts[6] == '02':    
            pack.insert(11,'KTC')#posicao/valor
        if parts[6] == '03':    
            pack.insert(11,'BTH')#posicao/valor
        if parts[6] == '04':    
            pack.insert(11,'GRG')#posicao/valor
        #count = count + 1
        #print(f"count: {count}")
        #print(f"Pacote: {pack}")
        escrita(pack)

        pack.clear()
    #if count == 5:
        
    
        

################### SPLIT
crcV = 0
pacoteOk = []
def split(vet):
    while len(vet) > 0:
        crcV = 0
        cmd1 = vet[0]
        size1 = vet[1]
        cmd = int(vet[0], 16)
        size = int(vet[1], 16)
        posCrc = size + 1
        crc = int(vet[posCrc], 16)
        crc1 = vet[posCrc]
        #print(f"Valor Comando: {cmd}")
        #print(f"Valor size: {size}")
        #print(f"Valor crc: {crc}")
        if cmd >= 0 and cmd <= 6: #cmd correto
            #print(f"Valor Comando: {cmd}")
            pacoteOk.append(cmd1)
            #time.sleep(3)
            if size >= 0 and size <= 99:
                #print(f"Valor Size: {size}")
                pacoteOk.append(size1)
                #time.sleep(3)
                crcV = crcV ^ cmd
                #print(f"Resultado: {crcV} ^ {cmd} -> {crcV}")
                crcV = crcV ^ size
                #print(f"Resultado: {crcV} ^ {size} -> {crcV}")
                i = 1
                pos = 2
                while (i < size):
                    crcP = crcV
                    crcV = crcV ^ int(vet[pos], 16)
                    pacoteOk.append(vet[pos])
                    #print(f"Resultado verifi: {crcP} ^ {int(vet[pos], 16)} -> {crcV}")
                    i += 1
                    pos += 1
                    #time.sleep(3)
                if crcV == crc:
                    #print(f"Valor CRC: {crc}")
                    pacoteOk.append(crc1)
                    for item in pacoteOk:
                        if item in vet:
                            vet.remove(item)
                    #time.sleep(3)
                    
                    #print(f"Pacote da fifo: {vet}")
                    #print(f"Dado consistente.")
                    #escrita(pacoteOk)
                    #print(f"Pacote OK: {pacoteOk}")
                    assembly(pacoteOk)
                    pacoteOk.clear()#limpa para a proxima iteração

                else:
                    pacoteOk.append(crc1)
                    for item in pacoteOk:
                        if item in vet:
                            vet.remove(item)
                    pacoteOk.clear()#limpa para a proxima iteração
                    #print("Falhei na verificação de crc")
                    #print(f"Pacote OK: {pacoteOk}")
                    #print(f"Valor CRC: {crc}")
                    #print(f"Pacote da fifo: {vet}")
                    #print(f"Dado inconsistente.")
                    #time.sleep(3)
            else:#size inconsistente
                vet.pop(1)
                #print(f"Valor Size: {size} inconsistente")
                '''crcV = 0
                crcV = crcV ^ cmd
                #print(f"Resultado: {crcV} ^ {cmd} -> {crcV}")
                crcV = crcV ^ size
                #print(f"Resultado: {crcV} ^ {size} -> {crcV}")
                for size in vet:
                    crcV = crcV ^ vet[size]'''

        else:#cmd inconsistente
            vet.pop(0)
            #print(f"Valor cmd: {cmd} inconsistente")
            #vai sair do else e cair no while e seguir o baile
            '''for size in vet:
                vet.pop(size)
            vet.pop(cmd)'''


            


thread1 = threading.Thread(target=servidor)
time.sleep(0.5)
thread2 = threading.Thread(target=timer)
time.sleep(0.5)
#thread3 = threading.Thread(target=animate)
time.sleep(0.5)
thread1.start()# Inicie o paralelismo para o servidor
thread2.start()# Inicie o paralelismo para o decodificador

ani = FuncAnimation(fig1, animate, fargs=(axs[0, 0], axs[0, 1], axs[1, 0], axs[1, 1], num_points), interval=500)#0.5 segundos  === interval = 500
#ani.pause()
#thread3.start()
# Inicie o paralelismo para o servidor
#time.sleep(0.5) 
################### Crie as thread para as funções
janela.mainloop()

