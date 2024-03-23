import socket
import threading
import time
import csv
import struct
from typing import Deque, Any
from collections import deque
import queue ###   https://www.guru99.com/python-queue-example.html
from colorama import Fore, Back, Style, init


MAX_SIZE_BUFFER = 2000
init(autoreset=True)
fifo = queue.Queue()
count = 0
pack = []
################### SERVIDOR
def servidor():
    HOST = '10.32.162.160'
    PORT = 5555
    recebe = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    recebe.bind(('10.32.162.160', 5555))
    recebe.listen(1)
    print('Aguardando conexão de um cliente...')
    print(HOST)
    print(PORT)
    sc, endereco = recebe.accept()  # Aceita a conexão e obtém o objeto de soquete e o endereço do cliente
    print("Aceitei o cliente")
    while True:
        ler_fifo = sc.recv(1024)
        #dado = ler_fifo.decode("utf-8")
        hex_string = ' '.join(format(byte, '02x') for byte in ler_fifo)
        hex_parts = hex_string.split()# Divida a string formatada em partes individuais usando o espaço em branco como separador
        fifo.put(hex_parts)#colocado dado no buffer
        print(f"Dado colocado na FIFO: {hex_parts}")
        print("Servidor foi chamado e escreveu na FIFO")
        print(fifo.qsize())


################### TIMER
def timer():#chama o decodificador a cada 0.1 ou 0.05 segundos
    print(Fore.GREEN + "Timer chamado!")
    while True:
        if fifo.qsize() >= MAX_SIZE_BUFFER:#CHEIO
            print("Timer chamado: FIFO cheia")
            package =  fifo.get()
            #print(f"Fifo get: {dataFifo}")
            split(package)
            print(f"Fifo Get: {package}")
            print(f"package: {package}")
            time.sleep(0.005)#Acelerando leitura de buffer    0.05
        if fifo.empty():#se fifo estiver vazia
            print(Fore.RED + "Fifo vazia...")
            time.sleep(0.01)
            #time.sleep(1)#
        else:
            #print("Timer chamado: FIFO não cheia")
            '''dataFifo = fifo.get()
            subStr = dataFifo.split()
            package = [int(valor) for valor in subStr]'''
            #print(f"Fifo get: {dataFifo}")
            
            #byte_array = bytes.fromhex(hex_string)
            package =  fifo.get()
            split(package)
            print(f"Fifo Get: {package}")
            time.sleep(0.005)#0.05
        #time.sleep(t)  # Espera "t" milissegundos
################### Funcao de escrita no arquivo
arq = "packOk.csv"
def escrita(pack):
    with open(arq, mode='a', newline='') as arquivo_csv:
        escritor_csv = csv.writer(arquivo_csv)
        # Escreva os dados no arquivo CSV
        escritor_csv.writerow(pack)
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
        print(f"timestamp = {timestamp}")
        #pack.append(timestamp)
        #float_value = hex_to_float(timestamp)
        #time = float_value

        acex1 = parts[6]
        acex2 = parts[7]
        acex3 = parts[8]
        acex4 = parts[9]
        concatenado = str(acex4) + str(acex3) + str(acex2) + str(acex1)#big endian
        print(f"Accex = {concatenado}")
        float_value = hex_to_float(concatenado)
        acex = float_value

        acey1 = parts[10]
        acey2 = parts[11]
        acey3 = parts[12]
        acey4 = parts[13]
        concatenado = str(acey4) + str(acey3) + str(acey2) + str(acey1)#big endian
        print(f"Accey = {concatenado}")
        float_value = hex_to_float(concatenado)
        acey = float_value
        #acey = "{:.{}f}".format(acey, precisao)

        acez1 = parts[14]
        acez2 = parts[15]
        acez3 = parts[16]
        acez4 = parts[17]
        concatenado = str(acez4) + str(acez3) + str(acez2) + str(acez1)#big endian
        print(f"Accez = {concatenado}")
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
        print(f"count: {count}")
        print(f"Pacote: {pack}")
    if parts[0] == '03': #gyroscope
        gyx1 = parts[6]
        gyx2 = parts[7]
        gyx3 = parts[8]
        gyx4 = parts[9]
        concatenado = str(gyx4) + str(gyx3) + str(gyx2) + str(gyx1)#big endian
        print(f"Gyx = {concatenado}")
        float_value = hex_to_float(concatenado)
        gyx = float_value
        #gyx = "{:.{}f}".format(gyx, precisao)

        gyy1 = parts[10]
        gyy2 = parts[11]
        gyy3 = parts[12]
        gyy4 = parts[13]
        concatenado = str(gyy4) + str(gyy3) + str(gyy2) + str(gyy1)#big endian
        print(f"Gyy = {concatenado}")
        float_value = hex_to_float(concatenado)
        gyy = float_value
        #gyy = "{:.{}f}".format(gyy, precisao)

        gyz1 = parts[14]
        gyz2 = parts[15]
        gyz3 = parts[16]
        gyz4 = parts[17]
        concatenado = str(gyz4) + str(gyz3) + str(gyz2) + str(gyz1)#big endian
        print(f"Gyz = {concatenado}")
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
        print(f"count: {count}")
        print(f"Pacote: {pack}")
    if parts[0] == '04': #mag =>azimuth pitch roll 
        mag1 = parts[6]
        mag2 = parts[7]
        mag3 = parts[8]
        mag4 = parts[9]
        concatenado = str(mag4) + str(mag3) + str(mag2) + str(mag1)#big endian
        print(f"azi = {concatenado}")
        float_value = hex_to_float(concatenado)
        azi = float_value
        #azi = "{:.{}f}".format(azi, precisao)

        mag1 = parts[10]
        mag2 = parts[11]
        mag3 = parts[12]
        mag4 = parts[13]
        concatenado = str(mag4) + str(mag3) + str(mag2) + str(mag1)#big endian
        print(f"pit = {concatenado}")
        float_value = hex_to_float(concatenado)
        pit = float_value
        #pit = "{:.{}f}".format(gyy, precisao)

        mag1 = parts[14]
        mag2 = parts[15]
        mag3 = parts[16]
        mag4 = parts[17]
        concatenado = str(mag4) + str(mag3) + str(mag2) + str(mag1)#big endian
        print(f"Roll = {concatenado}")
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
        print(f"Pacote: {pack}")
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
        print(f"count: {count}")
        print(f"Pacote: {pack}")
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
        print(f"count: {count}")
        print(f"Pacote: {pack}")
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
                    print(f"Pacote OK: {pacoteOk}")
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
            #time.sleep(3)
        else:#cmd inconsistente
            vet.pop(0)
            #print(f"Valor cmd: {cmd} inconsistente")
            #vai sair do else e cair no while e seguir o baile
            '''for size in vet:
                vet.pop(size)
            vet.pop(cmd)'''
        #time.sleep(3)

################### Crie as thread para as funções
thread1 = threading.Thread(target=servidor)
thread2 = threading.Thread(target=timer)
################### Inicia as threads
thread1.start()# Inicie o paralelismo para o servidor
time.sleep(0.5) 
thread2.start()# Inicie o paralelismo para o decodificador
time.sleep(0.5)

'''Exemplo de input
02,11,01,00,00,00,c8,22,b4,bf,90,d4,19,41,f0,8b,05,c0,51
03,11,01,00,00,00,69,7e,b9,42,cc,84,13,c2,74,db,3b,c1,33
04,11,01,00,00,00,86,1e,58,bf,1c,8d,d1,3e,1c,06,b1,3d,83
02,11,02,00,00,00,6a,03,b4,bf,af,ce,19,41,a6,68,05,c0,41
03,11,02,00,00,00,25,69,b8,42,75,e1,15,c2,bc,6f,3d,c1,ca
04,11,02,00,00,00,30,07,36,bf,3e,a6,b1,3e,aa,61,9c,3d,d4
'''


'''

    acc_x               acc_y           acc_z           gyro_x      gyro_y     gyro_z   azimuth       pitch     roll        pos
-1.40731141481685,9.61439536784802,-2.08666605302268,-0.84421575,0.4092797,0.086437434,92.746895,-36.879684,-11.741077,STD
-1.40635420147249,9.61295953908573,-2.08451231237802,-0.7110472,0.34697145,0.076358154,92.20536,-37.470173,-11.839779,STD
-1.4053799531376,9.61149815768199,-2.08232024281567,-0.59895337,0.093462385,0.025045475,91.74305,-38.09079,-11.880902,STD
-1.40443154439509,9.61007553590291,-2.08018631262285,-0.12889257,-0.01282817,-0.002443461,91.26732,-38.842915,-11.933741,STD
-1.40348409267452,9.60865434966548,-2.07805453574002,0.049480084,0.018325957,0.016493361,90.81968,-39.538643,-11.957446,STD
'''


'''
Pacote OK: ['03', '11', '01', '00', '00', '00', '69', '7e', 'b9', '42', 'cc', '84', '13', 'c2', '74', 'db', '3b', 'c1', '33']
Gyx = 42b97e69
Gyy = c21384cc
Gyz = c13bdb74

'''