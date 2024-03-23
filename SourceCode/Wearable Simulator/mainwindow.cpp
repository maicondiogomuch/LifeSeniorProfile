#include "mainwindow.h"
#include "ui_mainwindow.h"
#include <QDebug>
#include <QFileDialog>
#include <QtCharts/QChartView>
#include <QtCharts/QLineSeries>
#include <QtCharts/QCategoryAxis>
#include <QtCharts/QLegend>
#include <QtCore/QFile>
#include <QtCore/QTextStream>
#include <string>
#include <QtCore>
#include <QtGui>
#include <QTimer>
#include <QDateTime>
#include <Qlabel>
#include <iostream>
#include <string.h>
#include <vector>
#include <QHostAddress>

//#include <QHostAddress>
//#include <QPixmap>

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow),
    mPlot(0),
    mTag1(0),
    mTag2(0),
    mTag3(0),
    mTag4(0),
    mTag5(0),
    mTag6(0),
    mTag7(0),
    mTag8(0),
    mTag9(0)
{
    ui->setupUi(this);

    //LOG File
    fileName = "logger.txt";
    logger = new Logger(this, fileName, this->ui->plainTextEdit);
    logger->write("Hello Qt");

    //Init Protocol
    Lifes_Protocol.Init_Lifes_SIM(logger);

    timerTCP = new QTimer(this);
    connect(timerTCP, SIGNAL(timeout()), this, SLOT(SendInFreq()));

//QVBoxLayout *layout = new QVBoxLayout;
}

MainWindow::~MainWindow()
{
    delete ui;
}

QString Dpath;
QString caminho;
void MainWindow::on_loadDirectory_clicked()
{
    // Get the path of the directory that the user selected.
    QString directoryPath = QFileDialog::getExistingDirectory(this, "Select a Directory");
    Dpath = directoryPath;

    // Clear the list widget.
    this->ui->directoryBox->clear();

    // Create a list of the folders in the directory.
    QDir directory(Dpath);
    QStringList folders = directory.entryList(QDir::Dirs | QDir::NoDotAndDotDot);


    // Add the folders to the list widget.
    this->ui->directoryBox->addItems(folders);

}




void MainWindow::on_directoryBox_currentIndexChanged(int index)
{
    // Get the selected folder name.
    QString selectedFolderName =  this->ui->directoryBox->currentText();

    // Create a list of the files in the selected folder.
    QDir fileDir(Dpath + "/" + selectedFolderName);
    //Convertendo o path do diretorio em uma string
    caminho = fileDir.path();

    //Pegando a lista de arquivos dentro da atividade escolhida
    QStringList files = fileDir.entryList(QDir::Files);
    //this->logger->write(files);


    this->ui->patientBox->clear();
    this->ui->patientBox->addItems(files);


    //Identificar a atividade para mostrar na label

    if(selectedFolderName == "BSC") ui->labelAtividadeDado->setText("Back sitting chair");
    else if (selectedFolderName == "CHU") ui->labelAtividadeDado->setText("Chair Up");
    else if (selectedFolderName == "CSI") ui->labelAtividadeDado->setText("Car Stepping-In");
    else if (selectedFolderName == "CSO") ui->labelAtividadeDado->setText("Chair Stepping-Out");
    else if (selectedFolderName == "FKL") ui->labelAtividadeDado->setText("Fall Front Knees Lying");
    else if (selectedFolderName == "FOL") ui->labelAtividadeDado->setText("Fall Forward Lying");
    else if (selectedFolderName == "JOG") ui->labelAtividadeDado->setText("Jogging");
    else if (selectedFolderName == "JUM") ui->labelAtividadeDado->setText("Jumping");
    else if (selectedFolderName == "SBE") ui->labelAtividadeDado->setText("Exercising");
    else if (selectedFolderName == "SBW") ui->labelAtividadeDado->setText("Working");
    else if (selectedFolderName == "SCH") ui->labelAtividadeDado->setText("Sit Chair");
    else if (selectedFolderName == "SDL") ui->labelAtividadeDado->setText("Side Ward Lying");
    else if (selectedFolderName == "SIT") ui->labelAtividadeDado->setText("Sitting On Chair");
    else if (selectedFolderName == "SLH") ui->labelAtividadeDado->setText("Leaving Home");
    else if (selectedFolderName == "SLW") ui->labelAtividadeDado->setText("Leaving Work");
    else if (selectedFolderName == "SRH") ui->labelAtividadeDado->setText("Return Home");
    else if (selectedFolderName == "STD") ui->labelAtividadeDado->setText("Standing");
    else if (selectedFolderName == "STN") ui->labelAtividadeDado->setText("Stairs Down");
    else if (selectedFolderName == "STU") ui->labelAtividadeDado->setText("Stairs Up");
    else if (selectedFolderName == "WAL") ui->labelAtividadeDado->setText("Walking");
    else ui->labelAtividadeDado->setText("Atividade não reconhecida");



}




QString temp;
void MainWindow::on_patientBox_currentIndexChanged(int index)
{
    //adicionar a primeira linha e jogar numa QStringList
    QString arquivoSelecionado =  this->ui->patientBox->currentText();
    QDir d(caminho + "/" + arquivoSelecionado);
    QString bloco = d.path();
    temp = bloco;
    this->logger->write(temp);
    temp = temp.replace("/", "\\");
    bloco = bloco.replace("/", "\\");
    load = new load_data(logger,bloco);
    lp = new _Lifes_Protocol();
    load->defineFileDyr(bloco);
}



QVector<double> dados;
void MainWindow::on_SET_clicked()
{
    load->data_parser();
    if(lp->obtemLData() == NULL ) {
    this->logger->write("load esta vazio!!!");
    }
    else lp->defineLoad(load);
    this->logger->write("SETADO");

}




void MainWindow::on_startbutton_clicked()
{

    //mPlot = new QCustomPlot();
    //setCentralWidget(mPlot);
    //criaGraficoAccX();
    /*criaGraficoAccY();
    criaGraficoAccZ();
    criaGraficoGyrX();
    criaGraficoGyrY();
    criaGraficoGyrZ();
    criaGraficoAzimuth();
    criaGraficoPitch();
    criaGraficoRoll();*/
    
    logger->write("Started!");
    timerTCP->start(1000);

}

void MainWindow::on_connectbutton_clicked()
{
 //socket
    Lifes_Protocol.lifes_sim_tools.socketTCP.Connect(this->ui->ipTextBox->text(), this->ui->portTextBox->text().toUInt());
    if(Lifes_Protocol.lifes_sim_tools.socketTCP.isConnected())logger->write("Connected!");
    else logger->write("Something is wrong!");
}

void MainWindow::SendInFreq()
{
        Lifes_Protocol.lifes_SIM_comando(CMD_TYPE_CRV_ACCEL);
        //Lifes_Protocol.lifes_SIM_comando(CMD_TYPE_CRV_MAG);
        //Lifes_Protocol.lifes_SIM_comando(CMD_TYPE_CRV_GYR);
        logger->write("Sent Accel Curve!");
}

void MainWindow::timerSlot()
{
    //QVector<double> vec =  load->obtemAcc_x();
    //QVector<double> t = load->obtemAcc_x;
    float ponto = load->elem1Acc_x();
    if(load->obtemAcc_x().size() != 1){
        load->acc_x_Pop();
    }
    // calculate and add a new data point to each graph:
    mGraph1->addData(mGraph1->dataCount(), ponto);
    //mGraph2->addData(mGraph2->dataCount(), qCos(mGraph2->dataCount()/50.0)+qSin(mGraph2->dataCount()/50.0/0.4364)*0.15);

    // make key axis range scroll with the data:
    ui->acc_x_widget->xAxis->rescale();
    mGraph1->rescaleValueAxis(false, true);
    //mGraph2->rescaleValueAxis(false, true);
    ui->acc_x_widget->xAxis->setRange(ui->acc_x_widget->xAxis->range().upper, 100, Qt::AlignRight);

    // update the vertical axis tag positions and texts to match the rightmost data point of the graphs:
    double graph1Value = mGraph1->dataMainValue(mGraph1->dataCount()-1);
    //double graph2Value = mGraph2->dataMainValue(mGraph2->dataCount()-1);
    mTag1->updatePosition(graph1Value);
    //mTag2->updatePosition(graph2Value);
    mTag1->setText(QString::number(graph1Value, 'f', 2));
    //mTag2->setText(QString::number(graph2Value, 'f', 2));
     //this->logger->write("timerSlot");
    ui->acc_x_widget->replot();

}


void MainWindow::timerSlotY()
{
    //QVector<double> vec =  load->obtemAcc_x();
    //QVector<double> t = load->obtemAcc_x;
    double ponto = load->elem1Acc_y();
    if(load->obtemAcc_y().size() != 1){
        load->acc_y_Pop();
    }
    // calculate and add a new data point to each graph:
    mGraph2->addData(mGraph2->dataCount(), ponto);
    //mGraph2->addData(mGraph2->dataCount(), qCos(mGraph2->dataCount()/50.0)+qSin(mGraph2->dataCount()/50.0/0.4364)*0.15);

    // make key axis range scroll with the data:
    ui->acc_y_widget->xAxis->rescale();
    mGraph2->rescaleValueAxis(false, true);
    //mGraph2->rescaleValueAxis(false, true);
    ui->acc_y_widget->xAxis->setRange(ui->acc_y_widget->xAxis->range().upper, 100, Qt::AlignRight);

    // update the vertical axis tag positions and texts to match the rightmost data point of the graphs:
    double graph2Value = mGraph2->dataMainValue(mGraph2->dataCount()-1);
    //double graph2Value = mGraph2->dataMainValue(mGraph2->dataCount()-1);
    mTag2->updatePosition(graph2Value);
    //mTag2->updatePosition(graph2Value);
    mTag2->setText(QString::number(graph2Value, 'f', 2));
    //mTag2->setText(QString::number(graph2Value, 'f', 2));

    ui->acc_y_widget->replot();
}


void MainWindow::timerSlotAccZ(){
    //QVector<double> vec =  load->obtemAcc_x();
    //QVector<double> t = load->obtemAcc_x;
    double ponto = load->elem1Acc_z();
    if(load->obtemAcc_z().size() != 1){
        load->acc_z_Pop();
    }
    // calculate and add a new data point to each graph:
    mGraph3->addData(mGraph3->dataCount(), ponto);
    //mGraph2->addData(mGraph2->dataCount(), qCos(mGraph2->dataCount()/50.0)+qSin(mGraph2->dataCount()/50.0/0.4364)*0.15);

    // make key axis range scroll with the data:
    ui->acc_z_widget->xAxis->rescale();
    mGraph3->rescaleValueAxis(false, true);
    //mGraph2->rescaleValueAxis(false, true);
    ui->acc_z_widget->xAxis->setRange(ui->acc_z_widget->xAxis->range().upper, 100, Qt::AlignRight);

    // update the vertical axis tag positions and texts to match the rightmost data point of the graphs:
    double graph2Value = mGraph3->dataMainValue(mGraph3->dataCount()-1);
    //double graph2Value = mGraph2->dataMainValue(mGraph2->dataCount()-1);
    mTag3->updatePosition(graph2Value);
    //mTag2->updatePosition(graph2Value);
    mTag3->setText(QString::number(graph2Value, 'f', 2));
    //mTag2->setText(QString::number(graph2Value, 'f', 2));

    ui->acc_z_widget->replot();

}

void MainWindow::timerSlotGyrX(){
    double ponto = load->elem1Gyr_x();
    if(load->obtemGyr_x().size() != 1){
        load->gyr_x_Pop();
    }
    // calculate and add a new data point to each graph:
    mGraph4->addData(mGraph4->dataCount(), ponto);
    //mGraph2->addData(mGraph2->dataCount(), qCos(mGraph2->dataCount()/50.0)+qSin(mGraph2->dataCount()/50.0/0.4364)*0.15);

    // make key axis range scroll with the data:
    ui->gyr_x_widget->xAxis->rescale();
    mGraph4->rescaleValueAxis(false, true);
    //mGraph2->rescaleValueAxis(false, true);
    ui->gyr_x_widget->xAxis->setRange(ui->gyr_x_widget->xAxis->range().upper, 100, Qt::AlignRight);

    // update the vertical axis tag positions and texts to match the rightmost data point of the graphs:
    double graph2Value = mGraph4->dataMainValue(mGraph4->dataCount()-1);
    //double graph2Value = mGraph2->dataMainValue(mGraph2->dataCount()-1);
    mTag4->updatePosition(graph2Value);
    mTag4->setText(QString::number(graph2Value, 'f', 2));

    ui->gyr_x_widget->replot();
}

void MainWindow::timerSlotGyrY(){
    double ponto = load->elem1Gyr_y();
    if(load->obtemGyr_y().size() != 1){
        load->gyr_y_Pop();
    }
    // calculate and add a new data point to each graph:
    mGraph5->addData(mGraph5->dataCount(), ponto);
    //mGraph2->addData(mGraph2->dataCount(), qCos(mGraph2->dataCount()/50.0)+qSin(mGraph2->dataCount()/50.0/0.4364)*0.15);

    // make key axis range scroll with the data:
    ui->gyr_y_widget->xAxis->rescale();
    mGraph5->rescaleValueAxis(false, true);
    //mGraph2->rescaleValueAxis(false, true);
    ui->gyr_y_widget->xAxis->setRange(ui->gyr_y_widget->xAxis->range().upper, 100, Qt::AlignRight);

    // update the vertical axis tag positions and texts to match the rightmost data point of the graphs:
    double graph2Value = mGraph5->dataMainValue(mGraph5->dataCount()-1);
    //double graph2Value = mGraph2->dataMainValue(mGraph2->dataCount()-1);
    mTag5->updatePosition(graph2Value);
    mTag5->setText(QString::number(graph2Value, 'f', 2));

    ui->gyr_y_widget->replot();
}

void MainWindow::timerSlotGyrZ(){
    double ponto = load->elem1Gyr_z();
    if(load->obtemGyr_z().size() != 1){
        load->gyr_z_Pop();
    }
    // calculate and add a new data point to each graph:
    mGraph6->addData(mGraph6->dataCount(), ponto);
    //mGraph2->addData(mGraph2->dataCount(), qCos(mGraph2->dataCount()/50.0)+qSin(mGraph2->dataCount()/50.0/0.4364)*0.15);

    // make key axis range scroll with the data:
    ui->gyr_z_widget->xAxis->rescale();
    mGraph6->rescaleValueAxis(false, true);
    //mGraph2->rescaleValueAxis(false, true);
    ui->gyr_z_widget->xAxis->setRange(ui->gyr_z_widget->xAxis->range().upper, 100, Qt::AlignRight);

    // update the vertical axis tag positions and texts to match the rightmost data point of the graphs:
    double graph2Value = mGraph6->dataMainValue(mGraph6->dataCount()-1);
    //double graph2Value = mGraph2->dataMainValue(mGraph2->dataCount()-1);
    mTag6->updatePosition(graph2Value);
    mTag6->setText(QString::number(graph2Value, 'f', 2));
    //this->logger->write("timerSlot");
    ui->gyr_z_widget->replot();
}

void MainWindow::timerSlotAzimuth(){
    double ponto = load->elem1Azi();
    if(load->obtemAzi().size() != 1){
        load->azi_Pop();
    }
    // calculate and add a new data point to each graph:
    mGraph7->addData(mGraph7->dataCount(), ponto);
    //mGraph2->addData(mGraph2->dataCount(), qCos(mGraph2->dataCount()/50.0)+qSin(mGraph2->dataCount()/50.0/0.4364)*0.15);

    // make key axis range scroll with the data:
    ui->azimuth_widget->xAxis->rescale();
    mGraph7->rescaleValueAxis(false, true);
    //mGraph2->rescaleValueAxis(false, true);
    ui->azimuth_widget->xAxis->setRange(ui->azimuth_widget->xAxis->range().upper, 100, Qt::AlignRight);

    // update the vertical axis tag positions and texts to match the rightmost data point of the graphs:
    double graph2Value = mGraph7->dataMainValue(mGraph7->dataCount()-1);
    //double graph2Value = mGraph2->dataMainValue(mGraph2->dataCount()-1);
    mTag7->updatePosition(graph2Value);
    mTag7->setText(QString::number(graph2Value, 'f', 2));

    ui->azimuth_widget->replot();
}

void MainWindow::timerSlotPitch(){
    double ponto = load->elem1Pitch();
    if(load->obtemPitch().size() != 1){
        load->pitch_Pop();
    }
    // calculate and add a new data point to each graph:
    mGraph8->addData(mGraph8->dataCount(), ponto);
    //mGraph2->addData(mGraph2->dataCount(), qCos(mGraph2->dataCount()/50.0)+qSin(mGraph2->dataCount()/50.0/0.4364)*0.15);

    // make key axis range scroll with the data:
    ui->pitch_widget->xAxis->rescale();
    mGraph8->rescaleValueAxis(false, true);
    //mGraph2->rescaleValueAxis(false, true);
    ui->pitch_widget->xAxis->setRange(ui->pitch_widget->xAxis->range().upper, 100, Qt::AlignRight);

    // update the vertical axis tag positions and texts to match the rightmost data point of the graphs:
    double graph2Value = mGraph8->dataMainValue(mGraph8->dataCount()-1);
    //double graph2Value = mGraph2->dataMainValue(mGraph2->dataCount()-1);
    mTag8->updatePosition(graph2Value);
    mTag8->setText(QString::number(graph2Value, 'f', 2));

    ui->pitch_widget->replot();
}

void MainWindow::timerSlotRoll(){
    double ponto = load->elem1Roll();
    if(load->obtemRoll().size() != 1){
        load->roll_Pop();
    }
    // calculate and add a new data point to each graph:
    mGraph9->addData(mGraph9->dataCount(), ponto);
    //mGraph2->addData(mGraph2->dataCount(), qCos(mGraph2->dataCount()/50.0)+qSin(mGraph2->dataCount()/50.0/0.4364)*0.15);

    // make key axis range scroll with the data:
    ui->roll_widget->xAxis->rescale();
    mGraph9->rescaleValueAxis(false, true);
    //mGraph2->rescaleValueAxis(false, true);
    ui->roll_widget->xAxis->setRange(ui->roll_widget->xAxis->range().upper, 100, Qt::AlignRight);

    // update the vertical axis tag positions and texts to match the rightmost data point of the graphs:
    double graph2Value = mGraph9->dataMainValue(mGraph9->dataCount()-1);
    //double graph2Value = mGraph2->dataMainValue(mGraph2->dataCount()-1);
    mTag9->updatePosition(graph2Value);
    mTag9->setText(QString::number(graph2Value, 'f', 2));

    ui->roll_widget->replot();
}

void MainWindow::defineElements(double e, int index){
    elements[index] = e;
}

double MainWindow::obtemElements(int index){
    return elements[index];
}

void MainWindow::on_stopbutton_clicked()
{
    stop = true;
}

void MainWindow::criaGraficoAccX(){
    // configure plot to have two right axes:
    ui->acc_x_widget->yAxis->setTickLabels(false);
    connect(ui->acc_x_widget->yAxis2, SIGNAL(rangeChanged(QCPRange)), ui->acc_x_widget->yAxis, SLOT(setRange(QCPRange))); // left axis only mirrors inner right axis
    //ui->acc_x_widget->yAxis2->setVisible(true);
    ui->acc_x_widget->axisRect()->addAxis(QCPAxis::atRight);
    ui->acc_x_widget->axisRect()->axis(QCPAxis::atRight, 0)->setPadding(30); // add some padding to have space for tags
    ui->acc_x_widget->axisRect()->axis(QCPAxis::atRight, 1)->setPadding(30); // add some padding to have space for tags

    // create graphs:
    mGraph1 = ui->acc_x_widget->addGraph(ui->acc_x_widget->xAxis, ui->acc_x_widget->axisRect()->axis(QCPAxis::atRight, 0));
    //mGraph2 = mPlot->addGraph(mPlot->xAxis, mPlot->axisRect()->axis(QCPAxis::atRight, 1));
    mGraph1->setPen(QPen(QColor(0, 180, 60)));
    //mGraph2->setPen(QPen(QColor(0, 180, 60)));

    // create tags with newly introduced AxisTag class (see axistag.h/.cpp):
    mTag1 = new AxisTag(mGraph1->valueAxis());
    mTag1->setPen(mGraph1->pen());
    //mTag2 = new AxisTag(mGraph2->valueAxis());
    //mTag2->setPen(mGraph2->pen());

    connect(&mDataTimer, SIGNAL(timeout()), this, SLOT(timerSlot()));
    mDataTimer.start(40);
}

void MainWindow::criaGraficoAccY(){
    ui->acc_y_widget->yAxis->setTickLabels(false);
    connect(ui->acc_y_widget->yAxis2, SIGNAL(rangeChanged(QCPRange)), ui->acc_y_widget->yAxis, SLOT(setRange(QCPRange))); // left axis only mirrors inner right axis
    //ui->acc_x_widget->yAxis2->setVisible(true);
    ui->acc_y_widget->axisRect()->addAxis(QCPAxis::atRight);
    ui->acc_y_widget->axisRect()->axis(QCPAxis::atRight, 0)->setPadding(30); // add some padding to have space for tags
    ui->acc_y_widget->axisRect()->axis(QCPAxis::atRight, 1)->setPadding(30); // add some padding to have space for tags

    // create graphs:
    mGraph2 = ui->acc_y_widget->addGraph(ui->acc_y_widget->xAxis, ui->acc_y_widget->axisRect()->axis(QCPAxis::atRight, 0));
    //mGraph2 = mPlot->addGraph(mPlot->xAxis, mPlot->axisRect()->axis(QCPAxis::atRight, 1));
    mGraph2->setPen(QPen(QColor(0, 0, 255)));
    //mGraph2->setPen(QPen(QColor(0, 180, 60)));

    // create tags with newly introduced AxisTag class (see axistag.h/.cpp):
    mTag2 = new AxisTag(mGraph2->valueAxis());
    mTag2->setPen(mGraph2->pen());
    //mTag2 = new AxisTag(mGraph2->valueAxis());
    //mTag2->setPen(mGraph2->pen());

    connect(&mDataTimer2, SIGNAL(timeout()), this, SLOT(timerSlotY()));
    mDataTimer2.start(40);
}

void MainWindow::criaGraficoAccZ(){
    ui->acc_z_widget->yAxis->setTickLabels(false);
    connect(ui->acc_z_widget->yAxis2, SIGNAL(rangeChanged(QCPRange)), ui->acc_z_widget->yAxis, SLOT(setRange(QCPRange))); // left axis only mirrors inner right axis
    //ui->acc_x_widget->yAxis2->setVisible(true);
    ui->acc_z_widget->axisRect()->addAxis(QCPAxis::atRight);
    ui->acc_z_widget->axisRect()->axis(QCPAxis::atRight, 0)->setPadding(30); // add some padding to have space for tags
    ui->acc_z_widget->axisRect()->axis(QCPAxis::atRight, 1)->setPadding(30); // add some padding to have space for tags

    // create graphs:
    mGraph3 = ui->acc_z_widget->addGraph(ui->acc_z_widget->xAxis, ui->acc_z_widget->axisRect()->axis(QCPAxis::atRight, 0));
    //mGraph2 = mPlot->addGraph(mPlot->xAxis, mPlot->axisRect()->axis(QCPAxis::atRight, 1));
    mGraph3->setPen(QPen(QColor(0, 0, 255)));
    //mGraph2->setPen(QPen(QColor(0, 180, 60)));

    // create tags with newly introduced AxisTag class (see axistag.h/.cpp):
    mTag3 = new AxisTag(mGraph3->valueAxis());
    mTag3->setPen(mGraph3->pen());
    //mTag2 = new AxisTag(mGraph2->valueAxis());
    //mTag2->setPen(mGraph2->pen());

    connect(&mDataTimer3, SIGNAL(timeout()), this, SLOT(timerSlotAccZ()));
    mDataTimer3.start(40);
}

void MainWindow::criaGraficoGyrX(){
    ui->gyr_x_widget->yAxis->setTickLabels(false);
    connect(ui->gyr_x_widget->yAxis2, SIGNAL(rangeChanged(QCPRange)), ui->gyr_x_widget->yAxis, SLOT(setRange(QCPRange))); // left axis only mirrors inner right axis
    //ui->acc_x_widget->yAxis2->setVisible(true);
    ui->gyr_x_widget->axisRect()->addAxis(QCPAxis::atRight);
    ui->gyr_x_widget->axisRect()->axis(QCPAxis::atRight, 0)->setPadding(30); // add some padding to have space for tags
    ui->gyr_x_widget->axisRect()->axis(QCPAxis::atRight, 1)->setPadding(30); // add some padding to have space for tags

    // create graphs:
    mGraph4 = ui->gyr_x_widget->addGraph(ui->gyr_x_widget->xAxis, ui->gyr_x_widget->axisRect()->axis(QCPAxis::atRight, 0));
    //mGraph2 = mPlot->addGraph(mPlot->xAxis, mPlot->axisRect()->axis(QCPAxis::atRight, 1));
    mGraph4->setPen(QPen(QColor(0, 0, 255)));
    //mGraph2->setPen(QPen(QColor(0, 180, 60)));

    // create tags with newly introduced AxisTag class (see axistag.h/.cpp):
    mTag4 = new AxisTag(mGraph4->valueAxis());
    mTag4->setPen(mGraph4->pen());
    //mTag2 = new AxisTag(mGraph2->valueAxis());
    //mTag2->setPen(mGraph2->pen());

    connect(&mDataTimer4, SIGNAL(timeout()), this, SLOT(timerSlotGyrX()));
    mDataTimer4.start(40);
}

void MainWindow::criaGraficoGyrY(){
    ui->gyr_y_widget->yAxis->setTickLabels(false);
    connect(ui->gyr_y_widget->yAxis2, SIGNAL(rangeChanged(QCPRange)), ui->gyr_y_widget->yAxis, SLOT(setRange(QCPRange))); // left axis only mirrors inner right axis
    //ui->acc_x_widget->yAxis2->setVisible(true);
    ui->gyr_y_widget->axisRect()->addAxis(QCPAxis::atRight);
    ui->gyr_y_widget->axisRect()->axis(QCPAxis::atRight, 0)->setPadding(30); // add some padding to have space for tags
    ui->gyr_y_widget->axisRect()->axis(QCPAxis::atRight, 1)->setPadding(30); // add some padding to have space for tags

    // create graphs:
    mGraph5 = ui->gyr_y_widget->addGraph(ui->gyr_y_widget->xAxis, ui->gyr_y_widget->axisRect()->axis(QCPAxis::atRight, 0));
    //mGraph2 = mPlot->addGraph(mPlot->xAxis, mPlot->axisRect()->axis(QCPAxis::atRight, 1));
    mGraph5->setPen(QPen(QColor(0, 0, 255)));
    //mGraph2->setPen(QPen(QColor(0, 180, 60)));

    // create tags with newly introduced AxisTag class (see axistag.h/.cpp):
    mTag5 = new AxisTag(mGraph5->valueAxis());
    mTag5->setPen(mGraph5->pen());
    //mTag2 = new AxisTag(mGraph2->valueAxis());
    //mTag2->setPen(mGraph2->pen());

    connect(&mDataTimer5, SIGNAL(timeout()), this, SLOT(timerSlotGyrY()));
    mDataTimer5.start(40);
}

void MainWindow::criaGraficoGyrZ(){
    ui->gyr_z_widget->yAxis->setTickLabels(false);
    connect(ui->gyr_z_widget->yAxis2, SIGNAL(rangeChanged(QCPRange)), ui->gyr_z_widget->yAxis, SLOT(setRange(QCPRange))); // left axis only mirrors inner right axis
    //ui->acc_x_widget->yAxis2->setVisible(true);
    ui->gyr_z_widget->axisRect()->addAxis(QCPAxis::atRight);
    ui->gyr_z_widget->axisRect()->axis(QCPAxis::atRight, 0)->setPadding(30); // add some padding to have space for tags
    ui->gyr_z_widget->axisRect()->axis(QCPAxis::atRight, 1)->setPadding(30); // add some padding to have space for tags

    // create graphs:
    mGraph6 = ui->gyr_z_widget->addGraph(ui->gyr_z_widget->xAxis, ui->gyr_z_widget->axisRect()->axis(QCPAxis::atRight, 0));
    //mGraph2 = mPlot->addGraph(mPlot->xAxis, mPlot->axisRect()->axis(QCPAxis::atRight, 1));
    mGraph6->setPen(QPen(QColor(0, 0, 255)));
    //mGraph2->setPen(QPen(QColor(0, 180, 60)));

    // create tags with newly introduced AxisTag class (see axistag.h/.cpp):
    mTag6 = new AxisTag(mGraph6->valueAxis());
    mTag6->setPen(mGraph6->pen());
    //mTag2 = new AxisTag(mGraph2->valueAxis());
    //mTag2->setPen(mGraph2->pen());

    connect(&mDataTimer6, SIGNAL(timeout()), this, SLOT(timerSlotGyrZ()));
    mDataTimer6.start(40);
}

void MainWindow::criaGraficoAzimuth(){
    ui->azimuth_widget->yAxis->setTickLabels(false);
    connect(ui->azimuth_widget->yAxis2, SIGNAL(rangeChanged(QCPRange)), ui->azimuth_widget->yAxis, SLOT(setRange(QCPRange))); // left axis only mirrors inner right axis
    //ui->acc_x_widget->yAxis2->setVisible(true);
    ui->azimuth_widget->axisRect()->addAxis(QCPAxis::atRight);
    ui->azimuth_widget->axisRect()->axis(QCPAxis::atRight, 0)->setPadding(30); // add some padding to have space for tags
    ui->azimuth_widget->axisRect()->axis(QCPAxis::atRight, 1)->setPadding(30); // add some padding to have space for tags

    // create graphs:
    mGraph7 = ui->azimuth_widget->addGraph(ui->azimuth_widget->xAxis, ui->azimuth_widget->axisRect()->axis(QCPAxis::atRight, 0));
    //mGraph2 = mPlot->addGraph(mPlot->xAxis, mPlot->axisRect()->axis(QCPAxis::atRight, 1));
    mGraph7->setPen(QPen(QColor(0, 0, 255)));
    //mGraph2->setPen(QPen(QColor(0, 180, 60)));

    // create tags with newly introduced AxisTag class (see axistag.h/.cpp):
    mTag7 = new AxisTag(mGraph7->valueAxis());
    mTag7->setPen(mGraph7->pen());
    //mTag2 = new AxisTag(mGraph2->valueAxis());
    //mTag2->setPen(mGraph2->pen());

    connect(&mDataTimer7, SIGNAL(timeout()), this, SLOT(timerSlotAzimuth()));
    mDataTimer7.start(40);
}

void MainWindow::criaGraficoPitch(){
    ui->pitch_widget->yAxis->setTickLabels(false);
    connect(ui->pitch_widget->yAxis2, SIGNAL(rangeChanged(QCPRange)), ui->pitch_widget->yAxis, SLOT(setRange(QCPRange))); // left axis only mirrors inner right axis
    //ui->acc_x_widget->yAxis2->setVisible(true);
    ui->pitch_widget->axisRect()->addAxis(QCPAxis::atRight);
    ui->pitch_widget->axisRect()->axis(QCPAxis::atRight, 0)->setPadding(30); // add some padding to have space for tags
    ui->pitch_widget->axisRect()->axis(QCPAxis::atRight, 1)->setPadding(30); // add some padding to have space for tags

    // create graphs:
    mGraph8 = ui->pitch_widget->addGraph(ui->pitch_widget->xAxis, ui->pitch_widget->axisRect()->axis(QCPAxis::atRight, 0));
    //mGraph2 = mPlot->addGraph(mPlot->xAxis, mPlot->axisRect()->axis(QCPAxis::atRight, 1));
    mGraph8->setPen(QPen(QColor(0, 0, 255)));
    //mGraph2->setPen(QPen(QColor(0, 180, 60)));

    // create tags with newly introduced AxisTag class (see axistag.h/.cpp):
    mTag8 = new AxisTag(mGraph8->valueAxis());
    mTag8->setPen(mGraph8->pen());
    //mTag2 = new AxisTag(mGraph2->valueAxis());
    //mTag2->setPen(mGraph2->pen());

    connect(&mDataTimer8, SIGNAL(timeout()), this, SLOT(timerSlotPitch()));
    mDataTimer8.start(40);
}

void MainWindow::criaGraficoRoll(){
    ui->roll_widget->yAxis->setTickLabels(false);
    connect(ui->roll_widget->yAxis2, SIGNAL(rangeChanged(QCPRange)), ui->roll_widget->yAxis, SLOT(setRange(QCPRange))); // left axis only mirrors inner right axis
    //ui->acc_x_widget->yAxis2->setVisible(true);
    ui->roll_widget->axisRect()->addAxis(QCPAxis::atRight);
    ui->roll_widget->axisRect()->axis(QCPAxis::atRight, 0)->setPadding(30); // add some padding to have space for tags
    ui->roll_widget->axisRect()->axis(QCPAxis::atRight, 1)->setPadding(30); // add some padding to have space for tags

    // create graphs:
    mGraph9 = ui->roll_widget->addGraph(ui->roll_widget->xAxis, ui->roll_widget->axisRect()->axis(QCPAxis::atRight, 0));
    //mGraph2 = mPlot->addGraph(mPlot->xAxis, mPlot->axisRect()->axis(QCPAxis::atRight, 1));
    mGraph9->setPen(QPen(QColor(0, 0, 255)));
    //mGraph2->setPen(QPen(QColor(0, 180, 60)));

    // create tags with newly introduced AxisTag class (see axistag.h/.cpp):
    mTag9 = new AxisTag(mGraph9->valueAxis());
    mTag9->setPen(mGraph9->pen());
    //mTag2 = new AxisTag(mGraph2->valueAxis());
    //mTag2->setPen(mGraph2->pen());

    connect(&mDataTimer9, SIGNAL(timeout()), this, SLOT(timerSlotRoll()));
    mDataTimer9.start(40);
}





