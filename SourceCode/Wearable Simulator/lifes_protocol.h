#ifndef LIFES_PROTOCOL_H
#define LIFES_PROTOCOL_H


#include <QObject>
#include <QPlainTextEdit>
#include <QFile>
#include <QTextStream>
#include <QDateTime>
#include "lifes_sim_tools.h"
#include "Logger.h"
#include "protocol.h"
#include "load_data.h"

class _Lifes_Protocol : public QObject {

Q_OBJECT
public:

_lifes_sim_tools lifes_sim_tools;
private:
Logger* logger;
load_data *lData;
float teste = -1.5555555;

public slots:
void Init_Lifes_SIM(Logger*);
void Atualiza_inicial();
unsigned char TestaCRC(unsigned char crc, unsigned char data);
unsigned char lifes_SIM_comando(_command_types comando);
void Atualiza_Estrutura(_command_types comando);
_ConfigPub Configuracoes_de_Publicacao(void);
unsigned char Atualiza_Curvas(_command_types comando, unsigned short* curvas, unsigned int timestamp);
void lifes_sim_in(void);
void defineLoad(load_data *load);
load_data* obtemLData();
};


#endif // LIFES_PROTOCOL_H
