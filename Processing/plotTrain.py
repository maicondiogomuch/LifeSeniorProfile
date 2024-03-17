import re
import csv
import pandas as pd
import matplotlib.pyplot as plt

path = 'C:\\ML\\Realtime-Fall-Detection-for-RNN-master\\train_logs\\202402291525.logs'
path2 = 'C:\\ML\\Realtime-Fall-Detection-for-RNN-master\\plot.csv'
with open(path, 'r') as arquivo:
    loss = []
    accuracy = []
    step = []
    for linha in arquivo:
        linha = linha.strip()
        parteS = linha.split('train step = ')
        parteA = linha.split('loss = ')
        parteL = linha.split('accuracy = ')

        if len(parteS) and len(parteA) and len(parteL) == 2:
            dataStep = parteS[1]
            step.append(dataStep)
dados = []
print(f"STEP :::", step[0])

x=0
for i in range(len(step)):
    numeros = re.findall(r"[\d\.]+", step[x])
    numeros_float = [float(num) for num in numeros]
    data = ",".join(map(str, numeros_float))
    dados.append(data)
    x+=1

y=0
print("Dados preenchidos!")
with open('plot.csv', mode = 'w', newline='', encoding='utf-8') as arquivo_csv:
    escritor = csv.writer(arquivo_csv)
    escritor.writerow(['step','loss','accuracy'])
    for i in range(len(dados)):
        arquivo_csv.write(dados[y] + '\n')
        y+=1



dataFrame = pd.read_csv(path2)
x = dataFrame['step']#line
y1 = dataFrame['loss']#loss
y2 = dataFrame['accuracy']#accuracy

fig, axs = plt.subplots(1, 2, figsize=(15, 9))


#scatter== grafico de pontos 
#plot == grafico de linhas
axs[0].scatter(x, y1,s=1)
axs[0].set_title('Loss')

axs[1].scatter(x, y2,s=1)
axs[1].set_title('Accuracy')


plt.tight_layout()

plt.show()
#plt.savefig('C:\\ML\\Realtime-Fall-Detection-for-RNN-master\\train_logs\\plot.png', dpi=300)