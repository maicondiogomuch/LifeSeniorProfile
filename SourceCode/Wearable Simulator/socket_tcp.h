#ifndef SOCKET_TCP_H
#define SOCKET_TCP_H

#include <QObject>
#include <QTcpSocket>

class _SocketTCP : public QObject {

Q_OBJECT
public:
QTcpSocket  _socket;
private:


signals:

public slots:

    void SendTCP(char dado);
    void Connect(QString, unsigned int);
    int isConnected();
};

#endif // SOCKET_TCP_H
