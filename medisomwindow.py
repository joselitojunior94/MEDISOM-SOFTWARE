# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'medisomwindow.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainPage(object):
    def setupUi(self, MainPage):
        MainPage.setObjectName(_fromUtf8("MainPage"))
        MainPage.resize(736, 611)
        MainPage.setMouseTracking(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../Imagens/imagens-letra-m-1.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainPage.setWindowIcon(icon)
        MainPage.setAccessibleName(_fromUtf8(""))
        MainPage.setAccessibleDescription(_fromUtf8(""))
        self.centralwidget = QtGui.QWidget(MainPage)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.GerarButton = QtGui.QPushButton(self.centralwidget)
        self.GerarButton.setGeometry(QtCore.QRect(520, 390, 141, 61))
        self.GerarButton.setObjectName(_fromUtf8("GerarButton"))
        self.SalvarButton_2 = QtGui.QPushButton(self.centralwidget)
        self.SalvarButton_2.setGeometry(QtCore.QRect(330, 490, 111, 27))
        self.SalvarButton_2.setObjectName(_fromUtf8("SalvarButton_2"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(460, 150, 141, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.DiametroBox = QtGui.QLineEdit(self.centralwidget)
        self.DiametroBox.setGeometry(QtCore.QRect(610, 150, 113, 27))
        self.DiametroBox.setText(_fromUtf8(""))
        self.DiametroBox.setObjectName(_fromUtf8("DiametroBox"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(460, 220, 131, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.PontosBox = QtGui.QLineEdit(self.centralwidget)
        self.PontosBox.setGeometry(QtCore.QRect(610, 220, 113, 27))
        self.PontosBox.setObjectName(_fromUtf8("PontosBox"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(490, 290, 201, 17))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(450, 310, 161, 17))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.EscalaBox = QtGui.QLineEdit(self.centralwidget)
        self.EscalaBox.setGeometry(QtCore.QRect(610, 290, 113, 27))
        self.EscalaBox.setText(_fromUtf8(""))
        self.EscalaBox.setObjectName(_fromUtf8("EscalaBox"))
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(590, 570, 141, 17))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.MapdeclarativeView = QtDeclarative.QDeclarativeView(self.centralwidget)
        self.MapdeclarativeView.setGeometry(QtCore.QRect(10, 90, 431, 391))
        self.MapdeclarativeView.setObjectName(_fromUtf8("MapdeclarativeView"))
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(20, 20, 701, 61))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Purisa"))
        font.setPointSize(22)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        MainPage.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainPage)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainPage.setStatusBar(self.statusbar)
        self.actionAbrir_mapa = QtGui.QAction(MainPage)
        self.actionAbrir_mapa.setObjectName(_fromUtf8("actionAbrir_mapa"))
        self.actionSalvar_mapa = QtGui.QAction(MainPage)
        self.actionSalvar_mapa.setObjectName(_fromUtf8("actionSalvar_mapa"))
        self.actionFechar = QtGui.QAction(MainPage)
        self.actionFechar.setObjectName(_fromUtf8("actionFechar"))

        self.retranslateUi(MainPage)
        QtCore.QMetaObject.connectSlotsByName(MainPage)

    def retranslateUi(self, MainPage):
        MainPage.setWindowTitle(_translate("MainPage", "MGV 1.0", None))
        self.GerarButton.setText(_translate("MainPage", "GERAR!", None))
        self.SalvarButton_2.setText(_translate("MainPage", "Salvar como...", None))
        self.label.setText(_translate("MainPage", "Diâmetro do Tubo:", None))
        self.label_2.setText(_translate("MainPage", "Número de pontos: ", None))
        self.label_3.setText(_translate("MainPage", "Escala: ", None))
        self.label_4.setText(_translate("MainPage", "(Distância das linhas)", None))
        self.label_5.setText(_translate("MainPage", "Medisom UFBA 2016", None))
        self.label_6.setText(_translate("MainPage", "MEDISOM Graphics Viewer V1.0 Beta", None))
        self.actionAbrir_mapa.setText(_translate("MainPage", "Abrir mapa...", None))
        self.actionSalvar_mapa.setText(_translate("MainPage", "Salvar mapa...", None))
        self.actionFechar.setText(_translate("MainPage", "Fechar", None))

from PyQt4 import QtDeclarative
