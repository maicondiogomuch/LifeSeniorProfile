#include "Socket_TCP.h"


void _SocketTCP::Connect(QString ip, unsigned int port)
{
    if (ip.isEmpty() || port == 0)
        _socket.connectToHost(QHostAddress("127.0.0.1"), 23);
    else
        _socket.connectToHost(QHostAddress(ip), port);
}

void _SocketTCP::SendTCP(char dado)
{
    QByteArray buf;
    buf.append(dado);

    _socket.write(buf);
}

int _SocketTCP::isConnected()
{

    if(_socket.state() == QAbstractSocket::SocketState::ConnectedState)return 1;
    else return 0;
}

