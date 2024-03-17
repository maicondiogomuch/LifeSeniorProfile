import os
import random
import shutil

def selecionar_e_transferir(origem, destino, percentual=1):
    # Lista todos os arquivos na pasta de origem
    arquivos = os.listdir(origem)
    
    # Calcula o número de arquivos a serem transferidos (70%)
    num_arquivos_a_transferir = int(len(arquivos) * percentual)
    
    # Seleciona aleatoriamente os arquivos a serem transferidos
    arquivos_selecionados = random.sample(arquivos, num_arquivos_a_transferir)
    
    # Cria a pasta de destino, se ainda não existir
    if not os.path.exists(destino):
        os.makedirs(destino)
    
    # Transfere os arquivos selecionados para a pasta de destino
    for arquivo in arquivos_selecionados:
        caminho_origem = os.path.join(origem, arquivo)
        caminho_destino = os.path.join(destino, arquivo)
        shutil.move(caminho_origem, caminho_destino)
        print(f"Transferido: {arquivo}")

# Exemplo de uso
pasta_origem = r'D:\\tese_maicon\\IA_Data_Analysis\\lifesenior-dataset-originalfiles\\dataset_split\\AVD_A_1'
pasta_destino = r'D:\\tese_maicon\\IA_Data_Analysis\\lifesenior-dataset-originalfiles\\dataset_split\\test'
selecionar_e_transferir(pasta_origem, pasta_destino)

pasta_origem = r'D:\\tese_maicon\\IA_Data_Analysis\\lifesenior-dataset-originalfiles\\dataset_split\\AVD_A_2'
pasta_destino = r'D:\\tese_maicon\\IA_Data_Analysis\\lifesenior-dataset-originalfiles\\dataset_split\\test'
selecionar_e_transferir(pasta_origem, pasta_destino)

pasta_origem = r'D:\\tese_maicon\\IA_Data_Analysis\\lifesenior-dataset-originalfiles\\dataset_split\\AVD_A_3'
pasta_destino = r'D:\\tese_maicon\\IA_Data_Analysis\\lifesenior-dataset-originalfiles\\dataset_split\\test'
selecionar_e_transferir(pasta_origem, pasta_destino)

pasta_origem = r'D:\\tese_maicon\\IA_Data_Analysis\\lifesenior-dataset-originalfiles\\dataset_split\\AVD_A_4'
pasta_destino = r'D:\\tese_maicon\\IA_Data_Analysis\\lifesenior-dataset-originalfiles\\dataset_split\\test'
selecionar_e_transferir(pasta_origem, pasta_destino)

pasta_origem = r'D:\\tese_maicon\\IA_Data_Analysis\\lifesenior-dataset-originalfiles\\dataset_split\\AVD_A_5'
pasta_destino = r'D:\\tese_maicon\\IA_Data_Analysis\\lifesenior-dataset-originalfiles\\dataset_split\\test'
selecionar_e_transferir(pasta_origem, pasta_destino)

pasta_origem = r'D:\\tese_maicon\\IA_Data_Analysis\\lifesenior-dataset-originalfiles\\dataset_split\\AVD_D_1'
pasta_destino = r'D:\\tese_maicon\\IA_Data_Analysis\\lifesenior-dataset-originalfiles\\dataset_split\\test'
selecionar_e_transferir(pasta_origem, pasta_destino)

pasta_origem = r'D:\\tese_maicon\\IA_Data_Analysis\\lifesenior-dataset-originalfiles\\dataset_split\\AVD_D_2'
pasta_destino = r'D:\\tese_maicon\\IA_Data_Analysis\\lifesenior-dataset-originalfiles\\dataset_split\\test'
selecionar_e_transferir(pasta_origem, pasta_destino)

pasta_origem = r'D:\\tese_maicon\\IA_Data_Analysis\\lifesenior-dataset-originalfiles\\dataset_split\\AVD_D_3'
pasta_destino = r'D:\\tese_maicon\\IA_Data_Analysis\\lifesenior-dataset-originalfiles\\dataset_split\\test'
selecionar_e_transferir(pasta_origem, pasta_destino)

pasta_origem = r'D:\\tese_maicon\\IA_Data_Analysis\\lifesenior-dataset-originalfiles\\dataset_split\\AVD_D_4'
pasta_destino = r'D:\\tese_maicon\\IA_Data_Analysis\\lifesenior-dataset-originalfiles\\dataset_split\\test'
selecionar_e_transferir(pasta_origem, pasta_destino)

pasta_origem = r'D:\\tese_maicon\\IA_Data_Analysis\\lifesenior-dataset-originalfiles\\dataset_split\\AVD_D_5'
pasta_destino = r'D:\\tese_maicon\\IA_Data_Analysis\\lifesenior-dataset-originalfiles\\dataset_split\\test'
selecionar_e_transferir(pasta_origem, pasta_destino)

pasta_origem = r'D:\\tese_maicon\\IA_Data_Analysis\\lifesenior-dataset-originalfiles\\dataset_split\\AVD_G_1'
pasta_destino = r'D:\\tese_maicon\\IA_Data_Analysis\\lifesenior-dataset-originalfiles\\dataset_split\\test'
selecionar_e_transferir(pasta_origem, pasta_destino)

pasta_origem = r'D:\\tese_maicon\\IA_Data_Analysis\\lifesenior-dataset-originalfiles\\dataset_split\\AVD_G_2'
pasta_destino = r'D:\\tese_maicon\\IA_Data_Analysis\\lifesenior-dataset-originalfiles\\dataset_split\\test'
selecionar_e_transferir(pasta_origem, pasta_destino)

pasta_origem = r'D:\\tese_maicon\\IA_Data_Analysis\\lifesenior-dataset-originalfiles\\dataset_split\\AVD_G_3'
pasta_destino = r'D:\\tese_maicon\\IA_Data_Analysis\\lifesenior-dataset-originalfiles\\dataset_split\\test'
selecionar_e_transferir(pasta_origem, pasta_destino)

pasta_origem = r'D:\\tese_maicon\\IA_Data_Analysis\\lifesenior-dataset-originalfiles\\dataset_split\\AVD_G_4'
pasta_destino = r'D:\\tese_maicon\\IA_Data_Analysis\\lifesenior-dataset-originalfiles\\dataset_split\\test'
selecionar_e_transferir(pasta_origem, pasta_destino)

pasta_origem = r'D:\\tese_maicon\\IA_Data_Analysis\\lifesenior-dataset-originalfiles\\dataset_split\\AVD_G_5'
pasta_destino = r'D:\\tese_maicon\\IA_Data_Analysis\\lifesenior-dataset-originalfiles\\dataset_split\\test'
selecionar_e_transferir(pasta_origem, pasta_destino)

pasta_origem = r'D:\\tese_maicon\\IA_Data_Analysis\\lifesenior-dataset-originalfiles\\dataset_split\\PDE_A_6'
pasta_destino = r'D:\\tese_maicon\\IA_Data_Analysis\\lifesenior-dataset-originalfiles\\dataset_split\\test'
selecionar_e_transferir(pasta_origem, pasta_destino)

pasta_origem = r'D:\\tese_maicon\\IA_Data_Analysis\\lifesenior-dataset-originalfiles\\dataset_split\\PDE_A_7'
pasta_destino = r'D:\\tese_maicon\\IA_Data_Analysis\\lifesenior-dataset-originalfiles\\dataset_split\\test'
selecionar_e_transferir(pasta_origem, pasta_destino)

pasta_origem = r'D:\\tese_maicon\\IA_Data_Analysis\\lifesenior-dataset-originalfiles\\dataset_split\\PDE_A_8'
pasta_destino = r'D:\\tese_maicon\\IA_Data_Analysis\\lifesenior-dataset-originalfiles\\dataset_split\\test'
selecionar_e_transferir(pasta_origem, pasta_destino)

pasta_origem = r'D:\\tese_maicon\\IA_Data_Analysis\\lifesenior-dataset-originalfiles\\dataset_split\\PDE_A_9'
pasta_destino = r'D:\\tese_maicon\\IA_Data_Analysis\\lifesenior-dataset-originalfiles\\dataset_split\\test'
selecionar_e_transferir(pasta_origem, pasta_destino)

pasta_origem = r'D:\\tese_maicon\\IA_Data_Analysis\\lifesenior-dataset-originalfiles\\dataset_split\\PDE_D_6'
pasta_destino = r'D:\\tese_maicon\\IA_Data_Analysis\\lifesenior-dataset-originalfiles\\dataset_split\\test'
selecionar_e_transferir(pasta_origem, pasta_destino)

pasta_origem = r'D:\\tese_maicon\\IA_Data_Analysis\\lifesenior-dataset-originalfiles\\dataset_split\\PDE_D_7'
pasta_destino = r'D:\\tese_maicon\\IA_Data_Analysis\\lifesenior-dataset-originalfiles\\dataset_split\\test'
selecionar_e_transferir(pasta_origem, pasta_destino)

pasta_origem = r'D:\\tese_maicon\\IA_Data_Analysis\\lifesenior-dataset-originalfiles\\dataset_split\\PDE_D_8'
pasta_destino = r'D:\\tese_maicon\\IA_Data_Analysis\\lifesenior-dataset-originalfiles\\dataset_split\\test'
selecionar_e_transferir(pasta_origem, pasta_destino)

pasta_origem = r'D:\\tese_maicon\\IA_Data_Analysis\\lifesenior-dataset-originalfiles\\dataset_split\\PDE_D_9'
pasta_destino = r'D:\\tese_maicon\\IA_Data_Analysis\\lifesenior-dataset-originalfiles\\dataset_split\\test'
selecionar_e_transferir(pasta_origem, pasta_destino)

pasta_origem = r'D:\\tese_maicon\\IA_Data_Analysis\\lifesenior-dataset-originalfiles\\dataset_split\\PDE_G_6'
pasta_destino = r'D:\\tese_maicon\\IA_Data_Analysis\\lifesenior-dataset-originalfiles\\dataset_split\\test'
selecionar_e_transferir(pasta_origem, pasta_destino)

pasta_origem = r'D:\\tese_maicon\\IA_Data_Analysis\\lifesenior-dataset-originalfiles\\dataset_split\\PDE_G_7'
pasta_destino = r'D:\\tese_maicon\\IA_Data_Analysis\\lifesenior-dataset-originalfiles\\dataset_split\\test'
selecionar_e_transferir(pasta_origem, pasta_destino)

pasta_origem = r'D:\\tese_maicon\\IA_Data_Analysis\\lifesenior-dataset-originalfiles\\dataset_split\\PDE_G_8'
pasta_destino = r'D:\\tese_maicon\\IA_Data_Analysis\\lifesenior-dataset-originalfiles\\dataset_split\\test'
selecionar_e_transferir(pasta_origem, pasta_destino)

pasta_origem = r'D:\\tese_maicon\\IA_Data_Analysis\\lifesenior-dataset-originalfiles\\dataset_split\\PDE_G_9'
pasta_destino = r'D:\\tese_maicon\\IA_Data_Analysis\\lifesenior-dataset-originalfiles\\dataset_split\\test'
selecionar_e_transferir(pasta_origem, pasta_destino)

pasta_origem = r'D:\\tese_maicon\\IA_Data_Analysis\\lifesenior-dataset-originalfiles\\dataset_split\\QD_A_10'
pasta_destino = r'D:\\tese_maicon\\IA_Data_Analysis\\lifesenior-dataset-originalfiles\\dataset_split\\test'
selecionar_e_transferir(pasta_origem, pasta_destino)

pasta_origem = r'D:\\tese_maicon\\IA_Data_Analysis\\lifesenior-dataset-originalfiles\\dataset_split\\QD_A_11'
pasta_destino = r'D:\\tese_maicon\\IA_Data_Analysis\\lifesenior-dataset-originalfiles\\dataset_split\\test'
selecionar_e_transferir(pasta_origem, pasta_destino)

pasta_origem = r'D:\\tese_maicon\\IA_Data_Analysis\\lifesenior-dataset-originalfiles\\dataset_split\\QD_A_12'
pasta_destino = r'D:\\tese_maicon\\IA_Data_Analysis\\lifesenior-dataset-originalfiles\\dataset_split\\test'
selecionar_e_transferir(pasta_origem, pasta_destino)

pasta_origem = r'D:\\tese_maicon\\IA_Data_Analysis\\lifesenior-dataset-originalfiles\\dataset_split\\QD_D_10'
pasta_destino = r'D:\\tese_maicon\\IA_Data_Analysis\\lifesenior-dataset-originalfiles\\dataset_split\\test'
selecionar_e_transferir(pasta_origem, pasta_destino)

pasta_origem = r'D:\\tese_maicon\\IA_Data_Analysis\\lifesenior-dataset-originalfiles\\dataset_split\\QD_D_11'
pasta_destino = r'D:\\tese_maicon\\IA_Data_Analysis\\lifesenior-dataset-originalfiles\\dataset_split\\test'
selecionar_e_transferir(pasta_origem, pasta_destino)

pasta_origem = r'D:\\tese_maicon\\IA_Data_Analysis\\lifesenior-dataset-originalfiles\\dataset_split\\QD_D_12'
pasta_destino = r'D:\\tese_maicon\\IA_Data_Analysis\\lifesenior-dataset-originalfiles\\dataset_split\\test'
selecionar_e_transferir(pasta_origem, pasta_destino)

pasta_origem = r'D:\\tese_maicon\\IA_Data_Analysis\\lifesenior-dataset-originalfiles\\dataset_split\\QD_G_10'
pasta_destino = r'D:\\tese_maicon\\IA_Data_Analysis\\lifesenior-dataset-originalfiles\\dataset_split\\test'
selecionar_e_transferir(pasta_origem, pasta_destino)

pasta_origem = r'D:\\tese_maicon\\IA_Data_Analysis\\lifesenior-dataset-originalfiles\\dataset_split\\QD_G_11'
pasta_destino = r'D:\\tese_maicon\\IA_Data_Analysis\\lifesenior-dataset-originalfiles\\dataset_split\\test'
selecionar_e_transferir(pasta_origem, pasta_destino)

pasta_origem = r'D:\\tese_maicon\\IA_Data_Analysis\\lifesenior-dataset-originalfiles\\dataset_split\\QD_G_12'
pasta_destino = r'D:\\tese_maicon\\IA_Data_Analysis\\lifesenior-dataset-originalfiles\\dataset_split\\test'
selecionar_e_transferir(pasta_origem, pasta_destino)