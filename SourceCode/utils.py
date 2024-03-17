# -*- coding:utf-8 -*-
import os
import cv2
import pandas as pd
import numpy as np
import configparser as cp
import matplotlib.pyplot as plt
import os

RAW_DATA_PATH = 'D:\\tese_maicon\\IA_Data_Analysis\\MobiFall\\Annotated Data'
WORKING_DIRECTORY = 'D:\\tese_maicon\\IA_Data_Analysis'
#LIFESENIOR
LABEL_POSITION = 7
Label = {'NON-FALL': 0, 'FALL': 1, 'LOSS OF BALANCE': 2}
SensorTable = ['ACC_X','ACC_Y','ACC_Z','BVP','EDA','HR','TEMP']
GroundTruth = { 0: 'NON-FALL', 1: 'FALL', 2: 'LOSS OF BALANCE'}

def extract_data(data_file, sampling_frequency):
    """
    Extract data from mobileFall for experimental testing
    :param data_file: original data file
    :param sampling_frequency: raw data collection frequency
    :return:
    """
    data = pd.read_csv(data_file, index_col=0)
    #print("label ",data.label)
    data_size = len(data.label)
    #print("size ",data_size)
    for i in range(data_size):
        data.iat[i, 10] = Label[data.iloc[i, 10]]

    col_data = np.arange(0, data_size, int(sampling_frequency/50))
    extract_data = data.iloc[col_data, [1, 2, 3, 4, 5, 6, 7,8,9,10]]

    save_path = './dataset/raw/' + os.path.abspath(os.path.dirname(data_file)+os.path.sep+".").replace(RAW_DATA_PATH, '')
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    save_path = './dataset/raw/' + data_file.replace(RAW_DATA_PATH, '')
    extract_data.to_csv(save_path, index=0)
    print('output path：', save_path)

def find_all_data_and_extract(path):
    """
    Find all files recursively and convert them
    :param path:
    :return:
    """
    #print('Original dataset path：', path)
    if not os.path.exists(path):
        print('There is a problem with the path：', path)
        return None

    #print('numero: ',os.listdir(path))
    #os.listdir(path) return folders inside the path
    for i in os.listdir(path):
        if os.path.isfile(path+"/"+i):
            if 'csv' in i:
                #print('path: ',path+"/"+i)
                #each csv in folders
                extract_data(path+"/"+i, 200)
        else:
            find_all_data_and_extract(path+"/"+i)

def parser_cfg_file(cfg_file):
    """
    Read information from the configuration file
    :param cfg_file: file path
    :return:
    """
    content_params = {}

    config = cp.ConfigParser()
    config.read(cfg_file)

    for section in config.sections():
        # Get the net information in the configuration file
        if section == 'net':
            for option in config.options(section):
                content_params[option] = config.get(section,option)

        # Get the train information in the configuration file
        if section == 'train':
            for option in config.options(section):
                content_params[option] = config.get(section,option)

    return content_params

def show_data(data, name=None):
    '''
    show data
    :param data: DataFrame
    :return:
    '''
    num = data.acc_x.size

    x = np.arange(num)
    fig = plt.figure(1, figsize=(100, 60))
    #Subtable 1 plots acceleration sensor data
    plt.subplot(2, 1, 1)
    plt.title('acc')
    plt.plot(x, data.acc_x, label='x')
    plt.plot(x, data.acc_y, label='y')
    plt.plot(x, data.acc_z, label='z')

    # Add explanation icon
    plt.legend()
    x_flag = np.arange(0, num, num / 10)
    plt.xticks(x_flag)

    # Subtable 2 draws gyroscope sensor data
    plt.subplot(2, 1, 2)
    plt.title('gyro')
    plt.plot(x, data.gyro_x, label='x')
    plt.plot(x, data.gyro_y, label='y')
    plt.plot(x, data.gyro_z, label='z')

    plt.legend()
    plt.xticks(x_flag)
    #plt.show()
    if name is None:
        plt.show()
    else:
        plt.savefig(name)
    plt.close()

def kalman_filter(data):
    kalman = cv2.KalmanFilter(6, 6)
    kalman.measurementMatrix = np.array([[1, 0, 0, 0, 0, 0],
                                         [0, 1, 0, 0, 0, 0],
                                         [0, 0, 1, 0, 0, 0],
                                         [0, 0, 0, 1, 0, 0],
                                         [0, 0, 0, 0, 1, 0],
                                         [0, 0, 0, 0, 0, 1]], np.float32)
    kalman.transitionMatrix = np.array([[1, 0, 0, 0, 0, 0],
                                         [0, 1, 0, 0, 0, 0],
                                         [0, 0, 1, 0, 0, 0],
                                         [0, 0, 0, 1, 0, 0],
                                         [0, 0, 0, 0, 1, 0],
                                         [0, 0, 0, 0, 0, 1]], np.float32)
    kalman.processNoiseCov = np.array([[1, 0, 0, 0, 0, 0],
                                       [0, 1, 0, 0, 0, 0],
                                       [0, 0, 1, 0, 0, 0],
                                       [0, 0, 0, 1, 0, 0],
                                       [0, 0, 0, 0, 1, 0],
                                       [0, 0, 0, 0, 0, 1]], np.float32) * 0.20
    kalman.measurementNoiseCov = np.array([[1, 0, 0, 0, 0, 0],
                                          [0, 1, 0, 0, 0, 0],
                                          [0, 0, 1, 0, 0, 0],
                                          [0, 0, 0, 1, 0, 0],
                                          [0, 0, 0, 0, 1, 0],
                                          [0, 0, 0, 0, 0, 1]], np.float32) * 1

    row_num = data.acc_x.size

    for i in range(row_num):
        correct = np.array(data.iloc[i, 0:6].values, np.float32).reshape([6, 1])
        kalman.correct(correct)
        predict = kalman.predict()
        data.iloc[i, 0] = predict[0]
        data.iloc[i, 1] = predict[1]
        data.iloc[i, 2] = predict[2]
        data.iloc[i, 3] = predict[3]
        data.iloc[i, 4] = predict[4]
        data.iloc[i, 5] = predict[5]

    return data

def find_all_data_and_filtrate(path):
    """
    Recursively search all files and perform kalman filtering
    :param path:
    :return:
    """

    print('path filtrate：', path)

    if not os.path.exists(path):
        print('There is a problem with the path：', path)
        return None

    for i in os.listdir(path):
        if os.path.isfile(path+"/"+i):
            if 'csv' in i:
                data = pd.read_csv(path+"/"+i)
                data = kalman_filter(data)
                data.to_csv(path+"/"+i, index=False)
                #print('path filtrate：', path+"/"+i)
        else:
            find_all_data_and_filtrate(path+"/"+i)

def main():
    #set current directory
    os.chdir(WORKING_DIRECTORY)

    # get the current working directory
    current_working_directory = os.getcwd()

    # print output to the console
    print(current_working_directory)

    #find_all_data_and_extract(RAW_DATA_PATH)
    find_all_data_and_filtrate('./dataset/kalman/')

if __name__ == '__main__':
    main()
    #if os.path.exists('./dataset/train/BSC_1_1_annotated.csv') == False:
    #    print('./dataset/train/BSC_1_1_annotated.csv', 'file does not exist！')
    #data = pd.read_csv('./dataset/train/BSC_1_1_annotated.csv')
    
    #show_data(data)
    #data = kalman_filter(data)
    #data.to_csv('./dataset/train/BSC_1_1_annotated.csv', index=False)
    #show_data(data)
    #a = data.iloc[4:5,0]
    #print(a)
    #data = pd.read_csv('./dataset/train/STU_1_1_annotated.csv')
    
    #show_data(data)

