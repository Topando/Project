# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AddTaskWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AddTask(object):
    def setupUi(self, AddTask):
        AddTask.setObjectName("AddTask")
        AddTask.resize(798, 313)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        AddTask.setFont(font)
        self.centralwidget = QtWidgets.QWidget(AddTask)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 120, 301, 31))
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(300, 120, 181, 31))
        self.textEdit.setObjectName("textEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 30, 791, 91))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(60, 170, 231, 31))
        self.label_3.setObjectName("label_3")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(300, 170, 181, 31))
        self.textEdit_2.setObjectName("textEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(310, 220, 131, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(540, 0, 261, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        AddTask.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(AddTask)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 798, 25))
        self.menubar.setObjectName("menubar")
        AddTask.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(AddTask)
        self.statusbar.setObjectName("statusbar")
        AddTask.setStatusBar(self.statusbar)

        self.retranslateUi(AddTask)
        QtCore.QMetaObject.connectSlotsByName(AddTask)

    def retranslateUi(self, AddTask):
        _translate = QtCore.QCoreApplication.translate
        AddTask.setWindowTitle(_translate("AddTask", "MainWindow"))
        self.label.setText(_translate("AddTask", "Введите название файла (без расширения)"))
        self.label_2.setText(_translate("AddTask", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">Чтобы добавить новое задание вы должны добавть в папки Task и Res, соответственно, фото задания и решения. </span></p><p align=\"center\"><span style=\" font-size:11pt; color:#ff0000;\">Важно</span><span style=\" font-size:11pt;\"> чтобы файлы имели ОДИНАКОВОЕ и цифра до точки означала номер задания название, формат </span><span style=\" font-size:11pt; color:#ff0000;\">СТРОГО</span><span style=\" font-size:11pt;\"> PNG</span></p><p align=\"center\"><span style=\" font-size:11pt;\">иначе программа перестанет функционировать</span></p></body></html>"))
        self.label_3.setText(_translate("AddTask", "Введите ответ к этому заданию"))
        self.pushButton.setText(_translate("AddTask", "Записать"))
        self.pushButton_2.setText(_translate("AddTask", "Вернуться на предыдущую страницу"))
