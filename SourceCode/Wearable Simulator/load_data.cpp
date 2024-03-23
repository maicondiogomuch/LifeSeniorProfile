#include "load_data.h"

load_data::load_data(Logger *logger, QString filename)
    //: QObject{parent}
{
    this->logger = logger;
    fileDyr = filename;
}
load_data::~load_data(){}


void load_data::printParser(){
    for (int i = 0; i < obtemAcc_x().size(); i++){
         std::cout << "printParser:"<< std::endl;
        std::cout <<  obtemAcc_x()[i] << std::endl;
    }
}


void load_data::data_parser(){
     /* Open file */
    QString arq = obtemFile();
    QFile file(arq);
    if (!file.open(QIODevice::ReadOnly)) {
    std::cerr << "Failed to open file" << std::endl;
    }

    QTextStream in(&file);

    // Read the first line of the file and ignore it.
    in.readLine();
    
    while (!in.atEnd()) {
        QString linha = in.readLine();
        QStringList elements = linha.split(",");
        double valor = elements[2].toDouble();
        defineAcc_x(valor);
        double valor1 = elements[3].toDouble();
        defineAcc_y(valor1);
        double valor2 = elements[4].toDouble();
        defineAcc_z(valor2);
        double valor3 = elements[5].toDouble();
        defineGyr_x(valor3);
        double valor4 = elements[6].toDouble();
        defineGyr_y(valor4);
        double valor5 = elements[7].toDouble();
        defineGyr_z(valor5);
        double valor6 = elements[8].toDouble();
        defineAzi(valor6);
        double valor7 = elements[9].toDouble();
        definePitch(valor7);
        double valor8 = elements[10].toDouble();
        defineRoll(valor8);
    }
      file.close();
}

QStringList load_data::get_activity_list(void)
{
    return activity_list;
}
void load_data::defineFileDyr(QString f){
    fileDyr = f;
}
void load_data::defineRel_time(double rt){
    rel_time.push_back(rt);
}
void load_data::defineAcc_x(double accx){
        acc_x.push_back(accx);
}
void load_data::defineAcc_y(double accy){
        acc_y.push_back(accy);
}
void load_data::defineAcc_z(double accz){
         acc_z.push_back(accz);
}
void load_data::defineGyr_x(double gyrx){
         gyr_x.push_back(gyrx);
}
void load_data::defineGyr_y(double gyry){
         gyr_y.push_back(gyry);
}
void load_data::defineGyr_z(double gyrz){
         gyr_z.push_back(gyrz);
}
void load_data::defineAzi(double a){
        azi.push_back(a);
}
void load_data::definePitch(double p){
        pitch.push_back(p);
}
void load_data::defineRoll(double r){
        roll.push_back(r);
}

QString load_data::obtemFile(){
    return fileDyr;
}
QVector<double> load_data::obtemRel_time(){
    return rel_time;
}
QVector<double> load_data::obtemAcc_x(){
    return acc_x;
}
QVector<double> load_data::obtemAcc_y(){
    return acc_y;
}
QVector<double> load_data::obtemAcc_z(){
    return acc_z;
}
QVector<double> load_data::obtemGyr_x(){
    return gyr_x;
}
QVector<double> load_data::obtemGyr_y(){
    return gyr_y;
}
QVector<double> load_data::obtemGyr_z(){
    return gyr_z;
}
QVector<double> load_data::obtemAzi(){
    return azi;
}
QVector<double> load_data::obtemPitch(){
    return pitch;
}
QVector<double> load_data::obtemRoll(){
    return roll;
}

double load_data::elem1Acc_x(){
    return acc_x[0];
}
double load_data::elem1Acc_y(){
    return acc_y[0];
}
double load_data::elem1Acc_z(){
    return acc_z[0];
}
double load_data::elem1Gyr_x(){
    return gyr_x[0];
}
double load_data::elem1Gyr_y(){
    return gyr_y[0];
}
double load_data::elem1Gyr_z(){
    return gyr_z[0];
}
double load_data::elem1Azi(){
    return azi[0];
}
double load_data::elem1Pitch(){
    return pitch[0];
}
double load_data::elem1Roll(){
    return roll[0];
}

void load_data::acc_x_Pop(){
    acc_x.pop_front();
}
void load_data::acc_y_Pop(){
    acc_y.pop_front();
}
void load_data::acc_z_Pop(){
    acc_z.pop_front();
}
void load_data::gyr_x_Pop(){
    gyr_x.pop_front();
}
void load_data::gyr_y_Pop(){
    gyr_y.pop_front();
}
void load_data::gyr_z_Pop(){
    gyr_z.pop_front();
}
void load_data::azi_Pop(){
    azi.pop_front();
}
void load_data::pitch_Pop(){
    pitch.pop_front();
}
void load_data::roll_Pop(){
   roll.pop_front();
}
