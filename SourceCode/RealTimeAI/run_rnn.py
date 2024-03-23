# -*- coding:utf-8 -*-
import time
import numpy as np
#import tensorflow as tf
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()
from matplotlib import pyplot as plt
from build_rnn import ELDERY_RISK_RNN
from data_load import DataLoad
from utils import parser_cfg_file
from utils import Label
from utils import SensorTable
from utils import GroundTruth
import os
import logging
from sklearn import metrics

WORKING_DIRECTORY = 'D:\\tese_maicon\\IA_Data_Analysis'

class Run_ELDERY_RISK_RNN(object):

    def __init__(self, mode_dir, time_step=5, batch_size=1):
        self.batch_size = batch_size
        self.time_step = time_step
        self._run_logger_init()

        ckpt = tf.train.get_checkpoint_state(mode_dir)
        if ckpt is None:
            raise FileExistsError(str(mode_dir, 'No model can be loaded'))

        net_config = parser_cfg_file('./config/rnn_net.cfg')
        self.rnn_net = ELDERY_RISK_RNN(net_config, batch_size, time_step,training = False)
        predict = self.rnn_net.build_net_graph()
        self._predict_tensor = tf.argmax(predict, axis=2)
        saver = tf.train.Saver()
        self._sess = tf.Session()
        # Load parameters
        saver.restore(self._sess, ckpt.model_checkpoint_path)

    def run(self, data):
        data = np.reshape(data, [self.batch_size, self.time_step, self.rnn_net.senor_data_num])
        predict = self._sess.run(self._predict_tensor, feed_dict={self.rnn_net.input_tensor: data})
        return predict

    def run_stop(self):
        self._sess.close()

    def _update_show_data(self, data, step, update_data):
        for i in range(step):
            data.pop(0)
            data.append(update_data[i])
    
    def _run_logger_init(self):
        """
        Initialize log
        """
        self.run_logger = logging.getLogger('run')
        self.run_logger.setLevel(logging.DEBUG)

        #Add file output
        log_file = './run_logs/' + time.strftime('%Y%m%d%H%M', time.localtime(time.time())) + '.logs'
        file_handler = logging.FileHandler(log_file, mode='w')
        file_handler.setLevel(logging.DEBUG)
        file_formatter = logging.Formatter('%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')
        file_handler.setFormatter(file_formatter)
        self.run_logger.addHandler(file_handler)

        #Add console output
        consol_handler = logging.StreamHandler()
        consol_handler.setLevel(logging.DEBUG)
        consol_formatter = logging.Formatter('%(message)s')
        consol_handler.setFormatter(consol_formatter)
        self.run_logger.addHandler(consol_handler)

    def draw_flow(self, test_data, test_label):
        data_size = test_data.shape[0]

        x = [_ for _ in range(150)]
        ax = [0 for _ in range(150)]
        ay = [0 for _ in range(150)]
        az = [0 for _ in range(150)]
        bvp = [0 for _ in range(150)]
        eda = [0 for _ in range(150)]
        #hr = [0 for _ in range(150)]
        #temp = [0 for _ in range(150)]

        run_step = 50
        num = int(data_size / run_step)

        start_time = time.time()

        self.run_logger.info('Number of classes = %d Classes = %s',self.rnn_net.class_num,str(Label))
        self.run_logger.info('Columns = %s',net_config['sensor_columns'])
        self.run_logger.info('Sensors = %s',str(SensorTable))
        self.run_logger.info('Sample Rate = 50hz Run Step = %d', run_step)
        self.run_logger.info('datasize = %d,num = %d, passos = %d'%(data_size, num,time_step/run_step))

        fig, (ax1, ax2,ax3,ax4,ax5) = plt.subplots(5)
        plt.ion()

        predictions=0
        pred_ok = 0
        prediction_value = 0
        correct_value = 0
        pred_nok = 0
        cont_unkown = 0
        pred_correct = 0
        pred_false = 0
        a = 0
        b = 0
        c = 0
        d = 0
        totalposit = 0
        totalnegat = 0
        totaltotal = 0
        sensibilidade = 0
        especificidade = 0
        valorpredposit = 0
        valorprednegat = 0
        acuracia = 0
        rvpositiva = 0
        rvnegativa = 0
        precision = 0
        f1score=0

        for i in range(num):
            if i > int(time_step/run_step):
                predict = run.run(test_data[i * run_step - time_step: i * run_step, :])
                title = 'Real Activity: ' + GroundTruth[test_label[i * run_step]] + '     Predict: ' + GroundTruth[predict[int(time_step - 1)][0]]
                prediction_value = predict[int(time_step - 1)][0]
                correct_value = test_label[i * run_step]

                predictions = predictions + 1
                if prediction_value == correct_value:
                    pred_ok = pred_ok + 1
                else:
                    pred_nok = pred_nok + 1
            else:
                title = 'Real Activity: ' + GroundTruth[test_label[i * run_step]] + '     Predict: ' + 'unknow'
                prediction_value = test_label[i * run_step]
                correct_value = 0
                cont_unkown = cont_unkown +1



            self.run_logger.info(title)
            self.run_logger.info('i = %d, num = %d,pred_ok = %d, pred_nok = %d,a=%d, b=%d, c=%d, d=%d'%(i,num, pred_ok,pred_nok,a,b,c,d))
            self.run_logger.info('sens = %2.2f, esp = %2.2f,prec = %2.2f, acur = %2.2f,f1=%2.2f'%(sensibilidade,especificidade, precision,acuracia,f1score))

            self._update_show_data(ax, run_step, test_data[i * run_step:i * run_step + run_step, 0])
            self._update_show_data(ay, run_step, test_data[i * run_step:i * run_step + run_step, 1])
            self._update_show_data(az, run_step, test_data[i * run_step:i * run_step + run_step, 2])
            self._update_show_data(bvp, run_step, test_data[i * run_step:i * run_step + run_step, 3])
            self._update_show_data(eda, run_step, test_data[i * run_step:i * run_step + run_step, 4])
            #self._update_show_data(hr, run_step, test_data[i * run_step:i * run_step + run_step, 5])
            #self._update_show_data(temp, run_step, test_data[i * run_step:i * run_step + run_step, 6])

            if i > int(time_step/run_step):
                pred_correct = (float)(pred_ok*100)/(i+1-cont_unkown)
                if(correct_value == 1):
                    if(prediction_value == 1):
                        a = a + 1
                    else:
                        c = c + 1
                elif(correct_value == 0 or correct_value == 2 ):
                    if(prediction_value == 0 or prediction_value == 2):
                        d = d + 1
                    else:
                        b = b + 1
                
                if(a > 0 or c > 0):sensibilidade = (float)(a/(a+c))
                else: sensibilidade = 0
                if(b > 0 or d > 0):especificidade = (float)(d/(b+d))
                else: especificidade = 0
                #if(a > 0 or b > 0):valorpredposit = (float)(a/(a+b))
                #else: valorpredposit = 0
                #if(c > 0 or d > 0):valorprednegat = (float)(d/(c+d))
                #else: valorprednegat = 0
                if(a > 0 or b > 0):precision = (float)(a/(a+b))
                else:precision=0
                if(a > 0 or b > 0 or c > 0 or d > 0):acuracia = (float)((a+d)/(a+b+c+d))
                else: acuracia = 0
                if(precision> 0 or sensibilidade> 0):f1score = (float)(2*((precision*sensibilidade)/(precision+sensibilidade)))
                else:f1score=0
                #f(especificidade< 1.0):rvpositiva = (float)((sensibilidade)/(1-especificidade))
                #else: rvpositiva = 0
                #if(especificidade > 0):rvnegativa = (float)((1-sensibilidade)/(especificidade))
                #else: rvnegativa=0
                Sensivitytext = "\nSensivity: %2.2f %%" % (sensibilidade)
                acuraciatxt = "  Accuracy: %2.2f %%" % (acuracia)
                title += Sensivitytext
                title += acuraciatxt
                plt.suptitle(title, fontsize=14)

            ax1.cla()
            #ax1.set_title('Accelerometer')
            ax1.set_ylabel('ACC [g]')
            ax1.plot(x, ax)
            ax1.plot(x, ay)
            ax1.plot(x, az)

            ax2.cla()
            ax2.set_title('BVP')
            ax2.set_ylabel('BVP')
            ax2.plot(x, bvp)

            ax3.cla()
            ax3.set_ylabel('EDA [us]')
            ax3.plot(x, eda)

            #ax4.cla()
            #ax4.set_ylabel('HR [bpm]')
            #ax4.plot(x, hr)

            #ax5.cla()
            #ax5.set_ylabel('Temp [ºC]')
            #ax5.plot(x, temp)


            plt.draw()
            #plt.pause(10)
            plt.pause(0.001)

        during = str(time.time() - start_time)
        print('Detection time =', during)

        pred_correct = (float)(pred_ok*100)/(num-cont_unkown)
        pred_false = (float)(pred_nok*100)/(num-cont_unkown)
        self.run_logger.info('Total Predictions = %d,Positive = %2.2f %%, False = %2.2f %%, unknown = %d'%(num, pred_correct,pred_false,cont_unkown))
        self.run_logger.info('Sensibilidade = %2.2f %%'%(sensibilidade))
        self.run_logger.info('Especificidade = %2.2f %%'%(especificidade))
        self.run_logger.info('Precision = %2.2f %%'%(precision))
        self.run_logger.info('f1-score = %2.2f %%'%(f1score))
        self.run_logger.info('Acurácia = %2.2f %%'%(acuracia))
        #self.run_logger.info('RVpositiva = %2.2f %%'%(rvpositiva))
        #self.run_logger.info('RVnegativa = %2.2f %%'%(rvnegativa))

if __name__ == '__main__':

    #set current directory
    os.chdir(WORKING_DIRECTORY)

    # get the current working directory
    current_working_directory = os.getcwd()

    # print output to the console
    print(current_working_directory)

    net_config = parser_cfg_file('./config/rnn_net.cfg')
    time_step = int(net_config['time_step'])#50
    class_num = int(net_config['class_num'])
    sensor_columns = list(map(int,net_config['sensor_columns']))

    run = Run_ELDERY_RISK_RNN('./model/', time_step=time_step)
    data_load = DataLoad('./dataset/test/', time_step=time_step, class_num=class_num,sensor_columns = sensor_columns)

    test_data, test_label = data_load.get_test_data()
    #print('x_shape = ',test_data.shape)
    #print('x_size = ',test_data.size)
    ##print('y_shape = ',test_label.shape)
    #print('y_size = ',test_label)
    run.draw_flow(test_data, test_label)

    run.run_stop()
