#ifndef PROTOCOL_H
#define PROTOCOL_H

//comandos simples Gateway para LIFES_SIM
#define GATEWAY_INFORMA_LINK_ON 			254
#define GATEWAY_INFORMA_LINK_OFF 			253

//comandos compostos Gateway para LIFES_SIM
#define GATEWAY_INFORMA_IP                  219
#define GAEWAY_SERVER_CLOCK                 218

//comandos
typedef enum {
    CMD_TYPE_SYNC_CLOCK = 1,

    CMD_TYPE_CRV_ACCEL,
    CMD_TYPE_CRV_MAG,
    CMD_TYPE_CRV_GYR,

    CMD_TYPE_PARAM_ACCEL,
    CMD_TYPE_PARAM_GYR,
    CMD_TYPE_PARAM_MAG,

    CMD_TYPE_CFG_ACCEL,
    CMD_TYPE_CFG_GYR,
    CMD_TYPE_CFG_MAG,
    CMD_TYPE_CFG_PUB,

    CMD_TYPE_END

} _command_types;

///////////////////////////////////////////////////////////////////////////////
//curvas

#define CURVAS_DEFAULT_SIZE                 3   // X, Y e Z

//_Curva de Acelerometria
typedef struct
{
    //unsigned short cnt;
    //unsigned short curvas[CURVAS_DEFAULT_SIZE];
    //unsigned int timestamp;
    float curvas[CURVAS_DEFAULT_SIZE];
} _CurvaAccel;

//_Curva de Magnetômetro
typedef struct
{
    //unsigned short cnt;
    //unsigned int timestamp;
    unsigned short curvas[CURVAS_DEFAULT_SIZE];
} _CurvaMag;

//_Curva de Giroscopio
typedef struct
{
    //unsigned short cnt;
    //unsigned int timestamp;
    unsigned short curvas[CURVAS_DEFAULT_SIZE];
} _CurvaGyro;

///////////////////////////////////////////////////////////////////////////////
//parametros

//_Parametros Accelerometria
typedef struct
{
    //valores de referencia
    unsigned short example_value;
} _ParametrosAccel;

//_Parametros Magnetometro
typedef struct
{
    //valores de referencia
    unsigned short example_value;
} _ParametrosMag;

//_Parametros Giroscopio
typedef struct
{
    //valores de referencia
    unsigned short example_value;
} _ParametrosGyro;

///////////////////////////////////////////////////////////////////////////////
//configurações

typedef enum
{
    CONFIG_ENABLED_ACCEL    = 0b00000001,
    CONFIG_ENABLED_GYR      = 0b00000010,
    CONFIG_ENABLED_MAG      = 0b00000100,
    CONFIG_ENABLED_EDA      = 0b00001000,
    CONFIG_ENABLED_IBI      = 0b00010000,
} _ConfigEnabledSensors;

//_Config Accel
typedef struct
{
    unsigned char example_value;
} _ConfigAccel;

//_Config Magnetrometro
typedef struct
{
    unsigned char example_value;
} _ConfigMag;

//_Config Giroscopio
typedef struct
{
    unsigned char example_value;
} _ConfigGyro;

//_Configuracoes de publicacao (intervalo e dados)
typedef struct
{
    unsigned char bitarray_enabled_sensors;
    unsigned short interval_ms;
} _ConfigPub;

/* composição estruturas protocolo */

//_curvas
typedef struct
{
    _CurvaAccel acelerometer;
    _CurvaGyro  gyroscope;
    _CurvaMag   magnetometer;
} _curvas;

//_parametros
typedef struct
{
    _ParametrosMag    magnetometer;
    _ParametrosGyro   gyroscope;
    _ParametrosAccel  accelerometer;
} _parametros;

//_configuracoes
typedef struct
{
    _ConfigAccel accelerometer;
    _ConfigGyro  gyroscope;
    _ConfigMag   magnetometer;
    _ConfigPub   publisher;
} _configuracoes;


//_Relogio
typedef struct
{
    unsigned char Segundo;
    unsigned char Minuto;
    unsigned char Hora;
    unsigned char Dia;
    unsigned char Mes;
    unsigned char Ano;
} _Relogio;

//Time_Sync
typedef struct
{
    unsigned char comando;
    unsigned char tamanho;
    unsigned char Hora;
    unsigned char Minuto;
    unsigned char Segundo;
    unsigned char Dia;
    unsigned char Mes;
    unsigned char Ano[2];
    unsigned char crc;
} Time_Sync;


//_dados
typedef struct
{
    _Relogio relogio;
    _curvas curvas;
    _parametros parametros;
    _configuracoes config;
    Time_Sync rel;
} _dados;

//LIFE SIM protocol
typedef struct
{
    enum
    {
        DESL, INI, ACTIVE
    } st;
    _dados dados;
    unsigned short size[CMD_TYPE_END]; //último comando mais 1
    void *address[CMD_TYPE_END];
} _lifes_sim;

///////////////////////////////////////////////////////////////////////////////
//csv structure

#define LIFE_SIM_CSV_DATASET_SIZE   15


typedef union
{
    unsigned short raw[LIFE_SIM_CSV_DATASET_SIZE];
    struct // should match csv_headers
    {
        unsigned int timestamp;
        unsigned short miliseconds;
        unsigned short acc_curvas[CURVAS_DEFAULT_SIZE];
        unsigned short gyro_curvas[CURVAS_DEFAULT_SIZE];
        unsigned short mag_curvas[CURVAS_DEFAULT_SIZE];
        unsigned short eda;
        unsigned short ibi;
        unsigned short temperature;
    } data;
} _life_sim_csv_dataset;

#endif // PROTOCOL_H
