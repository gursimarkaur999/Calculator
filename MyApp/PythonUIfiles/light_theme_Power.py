

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow_Power(object):
    def setupUiPower(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(339, 565)
        MainWindow.setMinimumSize(QtCore.QSize(339, 565))
        MainWindow.setMaximumSize(QtCore.QSize(339, 565))
        MainWindow.setSizeIncrement(QtCore.QSize(0, 1))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../images/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setToolTipDuration(-1)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 341, 531))
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_buttons = QtWidgets.QFrame(self.frame)
        self.frame_buttons.setGeometry(QtCore.QRect(10, 230, 321, 311))
        self.frame_buttons.setStyleSheet("")
        self.frame_buttons.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_buttons.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_buttons.setObjectName("frame_buttons")
        self.pow_point = QtWidgets.QPushButton(self.frame_buttons)
        self.pow_point.setGeometry(QtCore.QRect(220, 240, 100, 55))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pow_point.setFont(font)
        self.pow_point.setStyleSheet("color: rgb(120, 120, 120);\n"
"background-color: rgb(193, 193, 193);\n"
"border-radius: 26px;")
        self.pow_point.setObjectName("pow_point")
        self.pow_three = QtWidgets.QPushButton(self.frame_buttons)
        self.pow_three.setGeometry(QtCore.QRect(220, 180, 100, 55))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pow_three.setFont(font)
        self.pow_three.setStyleSheet("color: rgb(120, 120, 120);\n"
"background-color: rgb(193, 193, 193);\n"
"border-radius: 26px;")
        self.pow_three.setObjectName("pow_three")
        self.pow_zero = QtWidgets.QPushButton(self.frame_buttons)
        self.pow_zero.setGeometry(QtCore.QRect(110, 240, 100, 55))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pow_zero.setFont(font)
        self.pow_zero.setStyleSheet("color: rgb(120, 120, 120);\n"
"background-color: rgb(193, 193, 193);\n"
"border-radius: 26px;")
        self.pow_zero.setObjectName("pow_zero")
        self.pow_two = QtWidgets.QPushButton(self.frame_buttons)
        self.pow_two.setGeometry(QtCore.QRect(110, 180, 100, 55))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pow_two.setFont(font)
        self.pow_two.setStyleSheet("color: rgb(120, 120, 120);\n"
"background-color: rgb(193, 193, 193);\n"
"border-radius: 26px;")
        self.pow_two.setObjectName("pow_two")
        self.pow_eight = QtWidgets.QPushButton(self.frame_buttons)
        self.pow_eight.setGeometry(QtCore.QRect(110, 60, 100, 55))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pow_eight.setFont(font)
        self.pow_eight.setStyleSheet("color: rgb(120, 120, 120);\n"
"background-color: rgb(193, 193, 193);\n"
"border-radius: 26px;")
        self.pow_eight.setObjectName("pow_eight")
        self.pow_five = QtWidgets.QPushButton(self.frame_buttons)
        self.pow_five.setGeometry(QtCore.QRect(110, 120, 100, 55))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pow_five.setFont(font)
        self.pow_five.setStyleSheet("color: rgb(120, 120, 120);\n"
"background-color: rgb(193, 193, 193);\n"
"border-radius: 26px;")
        self.pow_five.setObjectName("pow_five")
        self.pow_seven = QtWidgets.QPushButton(self.frame_buttons)
        self.pow_seven.setGeometry(QtCore.QRect(0, 60, 100, 55))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pow_seven.setFont(font)
        self.pow_seven.setStyleSheet("color: rgb(120, 120, 120);\n"
"background-color: rgb(193, 193, 193);\n"
"border-radius: 26px;")
        self.pow_seven.setObjectName("pow_seven")
        self.pow_six = QtWidgets.QPushButton(self.frame_buttons)
        self.pow_six.setGeometry(QtCore.QRect(220, 120, 100, 55))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pow_six.setFont(font)
        self.pow_six.setStyleSheet("color: rgb(120, 120, 120);\n"
"background-color: rgb(193, 193, 193);\n"
"border-radius: 26px;")
        self.pow_six.setObjectName("pow_six")
        self.pow_four = QtWidgets.QPushButton(self.frame_buttons)
        self.pow_four.setGeometry(QtCore.QRect(0, 120, 100, 55))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pow_four.setFont(font)
        self.pow_four.setStyleSheet("color: rgb(120, 120, 120);\n"
"background-color: rgb(193, 193, 193);\n"
"border-radius: 26px;")
        self.pow_four.setObjectName("pow_four")
        self.pow_nine = QtWidgets.QPushButton(self.frame_buttons)
        self.pow_nine.setGeometry(QtCore.QRect(220, 60, 100, 55))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pow_nine.setFont(font)
        self.pow_nine.setStyleSheet("color: rgb(120, 120, 120);\n"
"background-color: rgb(193, 193, 193);\n"
"border-radius: 26px;")
        self.pow_nine.setObjectName("pow_nine")
        self.pow_one = QtWidgets.QPushButton(self.frame_buttons)
        self.pow_one.setGeometry(QtCore.QRect(0, 180, 100, 55))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pow_one.setFont(font)
        self.pow_one.setStyleSheet("color: rgb(120, 120, 120);\n"
"background-color: rgb(193, 193, 193);\n"
"border-radius: 26px;")
        self.pow_one.setObjectName("pow_one")
        self.pow_ce = QtWidgets.QPushButton(self.frame_buttons)
        self.pow_ce.setGeometry(QtCore.QRect(110, 0, 100, 55))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pow_ce.setFont(font)
        self.pow_ce.setStyleSheet("color: rgb(120, 120, 120);\n"
"background-color: rgb(232, 232, 232);\n"
"border-radius: 25px;")
        self.pow_ce.setObjectName("pow_ce")
        self.pow_back = QtWidgets.QPushButton(self.frame_buttons)
        self.pow_back.setGeometry(QtCore.QRect(220, 0, 100, 55))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pow_back.setFont(font)
        self.pow_back.setStyleSheet("color: rgb(120, 120, 120);\n"
"border-radius: 25px;\n"
"background-color: rgb(255, 216, 97);\n"
"")
        self.pow_back.setObjectName("pow_back")
        self.frame_calculations_display = QtWidgets.QFrame(self.frame)
        self.frame_calculations_display.setGeometry(QtCore.QRect(10, 50, 321, 181))
        self.frame_calculations_display.setStyleSheet("")
        self.frame_calculations_display.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_calculations_display.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_calculations_display.setObjectName("frame_calculations_display")
        self.pow_label_1 = QtWidgets.QLabel(self.frame_calculations_display)
        self.pow_label_1.setGeometry(QtCore.QRect(10, 20, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pow_label_1.setFont(font)
        self.pow_label_1.setStyleSheet("color: rgb(117, 117, 117);")
        self.pow_label_1.setObjectName("pow_label_1")
        self.pow_label_2 = QtWidgets.QLabel(self.frame_calculations_display)
        self.pow_label_2.setGeometry(QtCore.QRect(10, 100, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pow_label_2.setFont(font)
        self.pow_label_2.setStyleSheet("color: rgb(117, 117, 117);")
        self.pow_label_2.setObjectName("pow_label_2")
        self.pow_comboBox_1 = QtWidgets.QComboBox(self.frame_calculations_display)
        self.pow_comboBox_1.setGeometry(QtCore.QRect(12, 60, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pow_comboBox_1.setFont(font)
        self.pow_comboBox_1.setStyleSheet("color: rgb(117, 117, 117);\n"
"border-radius: 50px;\n"
"background-color: rgb(232, 232, 232);\n"
"")
        self.pow_comboBox_1.setObjectName("pow_comboBox_1")
        self.pow_comboBox_1.addItem("")
        self.pow_comboBox_1.addItem("")
        self.pow_comboBox_1.addItem("")
        self.pow_comboBox_2 = QtWidgets.QComboBox(self.frame_calculations_display)
        self.pow_comboBox_2.setGeometry(QtCore.QRect(10, 140, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pow_comboBox_2.setFont(font)
        self.pow_comboBox_2.setStyleSheet("color: rgb(117, 117, 117);\n"
"border-radius: 50px;\n"
"background-color: rgb(232, 232, 232);\n"
"")
        self.pow_comboBox_2.setObjectName("pow_comboBox_2")
        self.pow_comboBox_2.addItem("")
        self.pow_comboBox_2.addItem("")
        self.pow_comboBox_2.addItem("")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(20, 10, 311, 41))
        font = QtGui.QFont()
        font.setPointSize(19)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(117, 117, 117);")
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 339, 26))
        self.menuBar.setObjectName("menuBar")
        self.menuOption = QtWidgets.QMenu(self.menuBar)
        self.menuOption.setStyleSheet("")
        self.menuOption.setTitle("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../images/text.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuOption.setIcon(icon1)
        self.menuOption.setObjectName("menuOption")
        self.menuCalculator = QtWidgets.QMenu(self.menuOption)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../images/calculator(3).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuCalculator.setIcon(icon2)
        self.menuCalculator.setObjectName("menuCalculator")
        self.menuConverter = QtWidgets.QMenu(self.menuOption)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../images/recycle.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuConverter.setIcon(icon3)
        self.menuConverter.setObjectName("menuConverter")
        self.menuHelp = QtWidgets.QMenu(self.menuBar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menuBar)
        self.actionDark = QtWidgets.QAction(MainWindow)
        self.actionDark.setObjectName("actionDark")
        self.actionLight = QtWidgets.QAction(MainWindow)
        self.actionLight.setObjectName("actionLight")
        self.actionSetting = QtWidgets.QAction(MainWindow)
        self.actionSetting.setObjectName("actionSetting")
        self.actionExit = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("../images/logout.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExit.setIcon(icon4)
        self.actionExit.setObjectName("actionExit")
        self.actionStandard = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("../images/calculator.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionStandard.setIcon(icon5)
        self.actionStandard.setObjectName("actionStandard")
        self.actionScientific = QtWidgets.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("../images/microscope.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionScientific.setIcon(icon6)
        self.actionScientific.setObjectName("actionScientific")
        self.actionProgrammer = QtWidgets.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("../images/code.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionProgrammer.setIcon(icon7)
        self.actionProgrammer.setObjectName("actionProgrammer")
        self.actionDate_Calculation = QtWidgets.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("../images/calendar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDate_Calculation.setIcon(icon8)
        self.actionDate_Calculation.setObjectName("actionDate_Calculation")
        self.actionCurrency = QtWidgets.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("../images/money.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCurrency.setIcon(icon9)
        self.actionCurrency.setObjectName("actionCurrency")
        self.actionVolume = QtWidgets.QAction(MainWindow)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("../images/shapes.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionVolume.setIcon(icon10)
        self.actionVolume.setObjectName("actionVolume")
        self.actionLength = QtWidgets.QAction(MainWindow)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("../images/ruler.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionLength.setIcon(icon11)
        self.actionLength.setObjectName("actionLength")
        self.actionWeight_and_Mass = QtWidgets.QAction(MainWindow)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap("../images/weighing-scale.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionWeight_and_Mass.setIcon(icon12)
        self.actionWeight_and_Mass.setObjectName("actionWeight_and_Mass")
        self.actionTemperature = QtWidgets.QAction(MainWindow)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap("../images/temperature.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionTemperature.setIcon(icon13)
        self.actionTemperature.setObjectName("actionTemperature")
        self.actionEnergy = QtWidgets.QAction(MainWindow)
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap("../images/fire.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionEnergy.setIcon(icon14)
        self.actionEnergy.setObjectName("actionEnergy")
        self.actionArea = QtWidgets.QAction(MainWindow)
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap("../images/area.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionArea.setIcon(icon15)
        self.actionArea.setObjectName("actionArea")
        self.actionSpeed = QtWidgets.QAction(MainWindow)
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap("../images/fast.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSpeed.setIcon(icon16)
        self.actionSpeed.setObjectName("actionSpeed")
        self.actionTime = QtWidgets.QAction(MainWindow)
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap("../images/clock.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionTime.setIcon(icon17)
        self.actionTime.setObjectName("actionTime")
        self.actionPower = QtWidgets.QAction(MainWindow)
        icon18 = QtGui.QIcon()
        icon18.addPixmap(QtGui.QPixmap("../images/energy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPower.setIcon(icon18)
        self.actionPower.setObjectName("actionPower")
        self.actionData = QtWidgets.QAction(MainWindow)
        icon19 = QtGui.QIcon()
        icon19.addPixmap(QtGui.QPixmap("../images/statistics.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionData.setIcon(icon19)
        self.actionData.setObjectName("actionData")
        self.actionPressure = QtWidgets.QAction(MainWindow)
        icon20 = QtGui.QIcon()
        icon20.addPixmap(QtGui.QPixmap("../images/indicator.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPressure.setIcon(icon20)
        self.actionPressure.setObjectName("actionPressure")
        self.actionAngle = QtWidgets.QAction(MainWindow)
        icon21 = QtGui.QIcon()
        icon21.addPixmap(QtGui.QPixmap("../images/angle.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAngle.setIcon(icon21)
        self.actionAngle.setObjectName("actionAngle")
        self.actionHelp = QtWidgets.QAction(MainWindow)
        self.actionHelp.setObjectName("actionHelp")
        self.actionDark_ = QtWidgets.QAction(MainWindow)
        self.actionDark_.setObjectName("actionDark_")
        self.actionLight_ = QtWidgets.QAction(MainWindow)
        self.actionLight_.setObjectName("actionLight_")
        self.menuCalculator.addAction(self.actionStandard)
        self.menuCalculator.addAction(self.actionScientific)
        self.menuCalculator.addAction(self.actionProgrammer)
        self.menuCalculator.addAction(self.actionDate_Calculation)
        self.menuConverter.addAction(self.actionVolume)
        self.menuConverter.addAction(self.actionLength)
        self.menuConverter.addAction(self.actionWeight_and_Mass)
        self.menuConverter.addAction(self.actionTemperature)
        self.menuConverter.addAction(self.actionEnergy)
        self.menuConverter.addAction(self.actionArea)
        self.menuConverter.addAction(self.actionSpeed)
        self.menuConverter.addAction(self.actionTime)
        self.menuConverter.addAction(self.actionPower)
        self.menuConverter.addAction(self.actionData)
        self.menuConverter.addAction(self.actionPressure)
        self.menuConverter.addAction(self.actionAngle)
        self.menuOption.addAction(self.menuCalculator.menuAction())
        self.menuOption.addAction(self.menuConverter.menuAction())
        self.menuOption.addSeparator()
        self.menuOption.addAction(self.actionExit)
        self.menuBar.addAction(self.menuOption.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())

        self.pow_retranslateUi(MainWindow)
        self.pow_comboBox_2.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def pow_retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculator"))
        self.pow_point.setText(_translate("MainWindow", "."))
        self.pow_three.setText(_translate("MainWindow", "3"))
        self.pow_zero.setText(_translate("MainWindow", "0"))
        self.pow_two.setText(_translate("MainWindow", "2"))
        self.pow_eight.setText(_translate("MainWindow", "8"))
        self.pow_five.setText(_translate("MainWindow", "5"))
        self.pow_seven.setText(_translate("MainWindow", "7"))
        self.pow_six.setText(_translate("MainWindow", "6"))
        self.pow_four.setText(_translate("MainWindow", "4"))
        self.pow_nine.setText(_translate("MainWindow", "9"))
        self.pow_one.setText(_translate("MainWindow", "1"))
        self.pow_ce.setToolTip(_translate("MainWindow", "Clear"))
        self.pow_ce.setText(_translate("MainWindow", "CE"))
        self.pow_back.setToolTip(_translate("MainWindow", "Remove/Back"))
        self.pow_back.setText(_translate("MainWindow", "<"))
        self.pow_label_1.setText(_translate("MainWindow", "0"))
        self.pow_label_2.setText(_translate("MainWindow", "0"))
        self.pow_comboBox_1.setItemText(0, _translate("MainWindow", "Watts"))
        self.pow_comboBox_1.setItemText(1, _translate("MainWindow", "Kilowatts"))
        self.pow_comboBox_1.setItemText(2, _translate("MainWindow", "Horsepower"))
        self.pow_comboBox_2.setItemText(0, _translate("MainWindow", "Watts"))
        self.pow_comboBox_2.setItemText(1, _translate("MainWindow", "Kilowatts"))
        self.pow_comboBox_2.setItemText(2, _translate("MainWindow", "Horsepower"))
        self.label.setText(_translate("MainWindow", "Power"))
        self.menuCalculator.setTitle(_translate("MainWindow", "Calculator"))
        self.menuConverter.setTitle(_translate("MainWindow", "Converter"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionDark.setText(_translate("MainWindow", "Dark"))
        self.actionLight.setText(_translate("MainWindow", "Light"))
        self.actionSetting.setText(_translate("MainWindow", "Setting"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionStandard.setText(_translate("MainWindow", "Standard"))
        self.actionScientific.setText(_translate("MainWindow", "Scientific"))
        self.actionProgrammer.setText(_translate("MainWindow", "Programmer"))
        self.actionDate_Calculation.setText(_translate("MainWindow", "Date Calculation"))
        self.actionCurrency.setText(_translate("MainWindow", "Currency"))
        self.actionVolume.setText(_translate("MainWindow", "Volume"))
        self.actionLength.setText(_translate("MainWindow", "Length"))
        self.actionWeight_and_Mass.setText(_translate("MainWindow", "Weight and Mass"))
        self.actionTemperature.setText(_translate("MainWindow", "Temperature"))
        self.actionEnergy.setText(_translate("MainWindow", "Energy"))
        self.actionArea.setText(_translate("MainWindow", "Area"))
        self.actionSpeed.setText(_translate("MainWindow", "Speed"))
        self.actionTime.setText(_translate("MainWindow", "Time"))
        self.actionPower.setText(_translate("MainWindow", "Power"))
        self.actionData.setText(_translate("MainWindow", "Data"))
        self.actionPressure.setText(_translate("MainWindow", "Pressure"))
        self.actionAngle.setText(_translate("MainWindow", "Angle"))
        self.actionHelp.setText(_translate("MainWindow", "Help"))
        self.actionDark_.setText(_translate("MainWindow", "Dark"))
        self.actionLight_.setText(_translate("MainWindow", "Light"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow_Power()
    ui.setupUiPower(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
