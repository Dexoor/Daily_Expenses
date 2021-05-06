from PyQt5 import QtCore, QtGui, QtWidgets

row1 = [0]
row2 = [0]


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(415, 499)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.gridFrame = QtWidgets.QFrame(self.centralwidget)
        self.gridFrame.setGeometry(QtCore.QRect(11, 1, 391, 321))
        self.gridFrame.setObjectName("gridFrame")
        self.gridLayout = QtWidgets.QGridLayout(self.gridFrame)
        self.gridLayout.setObjectName("gridLayout")
        self.name2 = QtWidgets.QLabel(self.gridFrame)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.name2.setFont(font)
        self.name2.setAlignment(QtCore.Qt.AlignCenter)
        self.name2.setObjectName("name2")
        self.gridLayout.addWidget(self.name2, 0, 5, 1, 1)
        self.name1 = QtWidgets.QLabel(self.gridFrame)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.name1.setFont(font)
        self.name1.setAlignment(QtCore.Qt.AlignCenter)
        self.name1.setObjectName("name1")
        self.gridLayout.addWidget(self.name1, 0, 2, 1, 1)
        self.col2 = QtWidgets.QTextBrowser(self.gridFrame)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(11)
        self.col2.setFont(font)
        self.col2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.col2.setStyleSheet("")
        self.col2.setObjectName("col2")
        self.gridLayout.addWidget(self.col2, 1, 5, 1, 1)
        self.col1 = QtWidgets.QTextBrowser(self.gridFrame)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(11)
        self.col1.setFont(font)
        self.col1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.col1.setObjectName("col1")
        self.gridLayout.addWidget(self.col1, 1, 2, 1, 1)
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(11, 331, 391, 163))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lcdNumber1 = QtWidgets.QLCDNumber(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(11)
        self.lcdNumber1.setFont(font)
        self.lcdNumber1.setStyleSheet("background-color: rgb(75, 142, 200);")
        self.lcdNumber1.setSmallDecimalPoint(False)
        self.lcdNumber1.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber1.setObjectName("lcdNumber1")
        self.gridLayout_2.addWidget(self.lcdNumber1, 3, 0, 1, 1)
        self.Value1 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Value1.setFont(font)
        self.Value1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Value1.setText("")
        self.Value1.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.Value1.setObjectName("Value1")
        self.Value1.returnPressed.connect(UpdateResult1)
        self.gridLayout_2.addWidget(self.Value1, 1, 0, 1, 1)
        self.ClearButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.ClearButton.pressed.connect(ClearButton)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(9)
        self.ClearButton.setFont(font)
        self.ClearButton.setObjectName("ClearButton")
        self.gridLayout_2.addWidget(self.ClearButton, 6, 1, 1, 1)
        self.LoadButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(9)
        self.LoadButton.setFont(font)
        self.LoadButton.setStyleSheet("\n"
                                      "selection-background-color: rgb(250, 216, 255);")
        self.LoadButton.setObjectName("LoadButton")
        self.gridLayout_2.addWidget(self.LoadButton, 5, 1, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(11)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.gridLayout_2.addWidget(self.comboBox, 5, 0, 2, 1)
        self.Value2 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Value2.setFont(font)
        self.Value2.setText("")
        self.Value2.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.Value2.setClearButtonEnabled(False)
        self.Value2.setObjectName("Value2")
        self.Value2.returnPressed.connect(UpdateResult2)
        self.gridLayout_2.addWidget(self.Value2, 1, 1, 1, 1)
        self.lcdNumber2 = QtWidgets.QLCDNumber(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(11)
        self.lcdNumber2.setFont(font)
        self.lcdNumber2.setStyleSheet("background-color: rgb(75, 142, 200);")
        self.lcdNumber2.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber2.setObjectName("lcdNumber2")
        self.gridLayout_2.addWidget(self.lcdNumber2, 3, 1, 1, 1)
        self.Difference = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        self.Difference.setFont(font)
        self.Difference.setText("")
        self.Difference.setAlignment(QtCore.Qt.AlignCenter)
        self.Difference.setReadOnly(True)
        self.Difference.setObjectName("Difference")
        self.gridLayout_2.addWidget(self.Difference, 4, 0, 1, 2)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 421, 505))
        self.frame.setStyleSheet("background-color: rgb(152, 144, 154);\n"
                                 "background-color: qlineargradient(spread:repeat, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(138, 106, 194, 255), stop:1 rgba(255, 255, 255, 255))\n"
                                 "\n"
                                 "")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame.raise_()
        self.gridFrame.raise_()
        self.gridLayoutWidget.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate(
            "MainWindow", "Wydatki mieszkaniowe"))
        self.name2.setText(_translate("MainWindow", "Wydatki Daniel"))
        self.name1.setText(_translate("MainWindow", "Wydatki Ola"))
        self.col2.setToolTip(_translate(
            "MainWindow", "<html><head/><body><p align=\"right\"><br/></p></body></html>"))
        self.col2.setWhatsThis(_translate(
            "MainWindow", "<html><head/><body><p align=\"right\"><br/></p></body></html>"))
        self.col2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                     "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                     "p, li { white-space: pre-wrap; }\n"
                                     "</style></head><body style=\" font-family:\'Comic Sans MS\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
                                     "<p align=\"right\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.col1.setWhatsThis(_translate(
            "MainWindow", "<html><head/><body><p align=\"right\"><br/></p></body></html>"))
        self.col1.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                     "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                     "p, li { white-space: pre-wrap; }\n"
                                     "</style></head><body style=\" font-family:\'Comic Sans MS\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
                                     "<p align=\"right\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.Value1.setToolTip(_translate(
            "MainWindow", "<html><head/><body><p align=\"right\"><br/></p></body></html>"))
        self.Value1.setWhatsThis(_translate(
            "MainWindow", "<html><head/><body><p align=\"right\"><br/></p></body></html>"))
        self.ClearButton.setText(_translate("MainWindow", "Clear"))
        self.LoadButton.setText(_translate("MainWindow", "Load"))
        self.comboBox.setToolTip(_translate(
            "MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.comboBox.setWhatsThis(_translate(
            "MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.Value2.setToolTip(_translate(
            "MainWindow", "<html><head/><body><p align=\"right\"><br/></p></body></html>"))
        self.Value2.setWhatsThis(_translate(
            "MainWindow", "<html><head/><body><p align=\"right\"><br/></p></body></html>"))


def UpdateResult1():  # po wpisaniu kwoty i wcisnieciu enter kolumna 1
    text1 = str(ui.Value1.text())
    ui.col1.append(text1 + " PLN")
    row1.append(int(text1))
    ui.Value1.clear()
    sum1 = sum(row1, 0)
    ui.lcdNumber1.display(sum1)
    DifferenceUpdate()
    # SaveDataTxt1()


def UpdateResult2():  # po wpisaniu kwoty i wcisnieciu enter kolumna 2
    text2 = str(ui.Value2.text())
    ui.col2.append(text2 + " PLN")
    row2.append(int(text2))
    ui.Value2.clear()
    sum2 = sum(row2, 0)
    ui.lcdNumber2.display(sum2)
    DifferenceUpdate()
    # SaveDataTxt1()


def DifferenceUpdate():  # roznica miedzy kolumnami
    substraction = ((sum(row1, 0)) - (sum(row2, 0)))
    if substraction == 0:
        ui.Difference.setText("Jesteśmy kwita")
    elif substraction > 0:
        ui.Difference.setText("Daniel jest winny:  " + str(substraction))
    elif substraction < 0:
        ui.Difference.setText("Ola jest winna:  " + str(-substraction))


def ClearButton():
    ui.col1.clear()
    ui.col1.setAlignment(QtCore.Qt.AlignRight)
    ui.col2.clear()
    ui.col2.setAlignment(QtCore.Qt.AlignRight)
    row1.clear()
    row2.clear()
    ui.Difference.clear()
    ui.lcdNumber1.display(0)
    ui.lcdNumber2.display(0)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
