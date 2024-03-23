QT       += core gui
QT       += core gui charts
QT       += core gui network

greaterThan(QT_MAJOR_VERSION, 4): QT += widgets printsupport
QMAKE_CXXFLAGS += -Wa,-mbig-obj

CONFIG += c++17

# You can make your code fail to compile if it uses deprecated APIs.
# In order to do so, uncomment the following line.
#DEFINES += QT_DISABLE_DEPRECATED_BEFORE=0x060000    # disables all the APIs deprecated before Qt 6.0.0

SOURCES += mainwindow.cpp\
    axistag.cpp \
    lifes_protocol.cpp \
    lifes_sim_tools.cpp \
     main.cpp \
    load_data.cpp \
    logger.cpp \
    qcustomplot.cpp \
    socket_tcp.cpp


HEADERS += mainwindow.h\
    axistag.h \
    lifes_protocol.h \
    lifes_sim_tools.h \
    load_data.h \
    logger.h \
    protocol.h \
    qcustomplot.h \
    socket_tcp.h


FORMS += \
    mainwindow.ui

# Default rules for deployment.
qnx: target.path = /tmp/$${TARGET}/bin
else: unix:!android: target.path = /opt/$${TARGET}/bin
!isEmpty(target.path): INSTALLS += target

DISTFILES +=
