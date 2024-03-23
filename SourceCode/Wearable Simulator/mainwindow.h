#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include <QTimer>
#include <QTime>
#include <QtCore>
#include <QDir>
#include "Logger.h"
#include "load_data.h"
#include "qcustomplot.h"
#include "axistag.h"
#include "Lifes_Protocol.h"
#include "protocol.h"
#include "Socket_TCP.h"

QT_BEGIN_NAMESPACE
namespace Ui { class MainWindow; }
QT_END_NAMESPACE

class QTimer;

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    MainWindow(QWidget *parent = nullptr);
    ~MainWindow();

    QString fileName;
    Logger *logger;
    QTimer *timerTCP;
    _Lifes_Protocol Lifes_Protocol;

private slots:

    void SendInFreq();

    void on_loadDirectory_clicked();

    void on_directoryBox_currentIndexChanged(int index);

    void on_patientBox_currentIndexChanged(int index);

    void on_startbutton_clicked();

    void defineElements(double e, int index);

    double obtemElements(int index);

    void criaGraficoAccX();

    void criaGraficoAccY();

    void criaGraficoAccZ();

    void criaGraficoGyrX();

    void criaGraficoGyrY();

    void criaGraficoGyrZ();

    void criaGraficoAzimuth();

    void criaGraficoPitch();

    void criaGraficoRoll();

    void on_stopbutton_clicked();

    void on_SET_clicked();

    void timerSlot();

    void timerSlotY();

    void timerSlotAccZ();

    void timerSlotGyrX();

    void timerSlotGyrY();

    void timerSlotGyrZ();

    void timerSlotAzimuth();

    void timerSlotPitch();

    void timerSlotRoll();

    void on_connectbutton_clicked();

private:
    Ui::MainWindow *ui;
    QTimer *timer;
    QTimer *timer2;
    double elements[12] = {0.0};
    bool stop = false;
    QCustomPlot *mPlot;

    QPointer<QCPGraph> mGraph1;
    AxisTag *mTag1;

    QPointer<QCPGraph> mGraph2;
    AxisTag *mTag2;
    
    QPointer<QCPGraph> mGraph3;
    AxisTag *mTag3;
    
    QPointer<QCPGraph> mGraph4;
    AxisTag *mTag4;

    QPointer<QCPGraph> mGraph5;
    AxisTag *mTag5;

    QPointer<QCPGraph> mGraph6;
    AxisTag *mTag6;

    QPointer<QCPGraph> mGraph7;
    AxisTag *mTag7;

    QPointer<QCPGraph> mGraph8;
    AxisTag *mTag8;

    QPointer<QCPGraph> mGraph9;
    AxisTag *mTag9;

    QTimer mDataTimer;
    QTimer mDataTimer2;
    QTimer mDataTimer3;
    QTimer mDataTimer4;
    QTimer mDataTimer5;
    QTimer mDataTimer6;
    QTimer mDataTimer7;
    QTimer mDataTimer8;
    QTimer mDataTimer9;
    
    _Lifes_Protocol *lp;
    load_data *load;

};
#endif // MAINWINDOW_H
