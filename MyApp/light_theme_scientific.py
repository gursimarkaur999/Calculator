# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Designing/light_theme_scientific.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow_Scientific(object):
    def setupUiScientific(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(339, 565)
        MainWindow.setMinimumSize(QtCore.QSize(339, 565))
        MainWindow.setMaximumSize(QtCore.QSize(339, 565))
        MainWindow.setSizeIncrement(QtCore.QSize(0, 1))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
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
        self.frame_buttons.setGeometry(QtCore.QRect(10, 120, 321, 421))
        self.frame_buttons.setStyleSheet("")
        self.frame_buttons.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_buttons.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_buttons.setObjectName("frame_buttons")
        self.s_point = QtWidgets.QPushButton(self.frame_buttons)
        self.s_point.setGeometry(QtCore.QRect(180, 360, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.s_point.setFont(font)
        self.s_point.setStyleSheet("color: rgb(120, 120, 120);\n"
"background-color: rgb(193, 193, 193);\n"
"border-radius: 25px;")
        self.s_point.setObjectName("s_point")
        self.s_three = QtWidgets.QPushButton(self.frame_buttons)
        self.s_three.setGeometry(QtCore.QRect(180, 300, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.s_three.setFont(font)
        self.s_three.setStyleSheet("color: rgb(120, 120, 120);\n"
"background-color: rgb(193, 193, 193);\n"
"border-radius: 25px;")
        self.s_three.setObjectName("s_three")
        self.s_zero = QtWidgets.QPushButton(self.frame_buttons)
        self.s_zero.setGeometry(QtCore.QRect(120, 360, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.s_zero.setFont(font)
        self.s_zero.setStyleSheet("color: rgb(120, 120, 120);\n"
"background-color: rgb(193, 193, 193);\n"
"border-radius: 25px;")
        self.s_zero.setObjectName("s_zero")
        self.s_two = QtWidgets.QPushButton(self.frame_buttons)
        self.s_two.setGeometry(QtCore.QRect(120, 300, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.s_two.setFont(font)
        self.s_two.setStyleSheet("color: rgb(120, 120, 120);\n"
"background-color: rgb(193, 193, 193);\n"
"border-radius: 25px;")
        self.s_two.setObjectName("s_two")
        self.s_eight = QtWidgets.QPushButton(self.frame_buttons)
        self.s_eight.setGeometry(QtCore.QRect(120, 180, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.s_eight.setFont(font)
        self.s_eight.setStyleSheet("color: rgb(120, 120, 120);\n"
"background-color: rgb(193, 193, 193);\n"
"border-radius: 25px;")
        self.s_eight.setObjectName("s_eight")
        self.s_five = QtWidgets.QPushButton(self.frame_buttons)
        self.s_five.setGeometry(QtCore.QRect(120, 240, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.s_five.setFont(font)
        self.s_five.setStyleSheet("color: rgb(120, 120, 120);\n"
"background-color: rgb(193, 193, 193);\n"
"border-radius: 25px;")
        self.s_five.setObjectName("s_five")
        self.s_seven = QtWidgets.QPushButton(self.frame_buttons)
        self.s_seven.setGeometry(QtCore.QRect(60, 180, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.s_seven.setFont(font)
        self.s_seven.setStyleSheet("color: rgb(120, 120, 120);\n"
"background-color: rgb(193, 193, 193);\n"
"border-radius: 25px;")
        self.s_seven.setObjectName("s_seven")
        self.s_plus_minus = QtWidgets.QPushButton(self.frame_buttons)
        self.s_plus_minus.setGeometry(QtCore.QRect(60, 360, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.s_plus_minus.setFont(font)
        self.s_plus_minus.setStyleSheet("color: rgb(120, 120, 120);\n"
"background-color: rgb(193, 193, 193);\n"
"border-radius: 25px;")
        self.s_plus_minus.setObjectName("s_plus_minus")
        self.s_multiply = QtWidgets.QPushButton(self.frame_buttons)
        self.s_multiply.setGeometry(QtCore.QRect(240, 180, 81, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.s_multiply.setFont(font)
        self.s_multiply.setStyleSheet("color: rgb(120, 120, 120);\n"
"border-radius: 25px;\n"
"background-color: rgb(255, 216, 97);\n"
"")
        self.s_multiply.setObjectName("s_multiply")
        self.s_divide = QtWidgets.QPushButton(self.frame_buttons)
        self.s_divide.setGeometry(QtCore.QRect(240, 120, 81, 51))
        self.s_divide.setMinimumSize(QtCore.QSize(51, 51))
        self.s_divide.setMaximumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.s_divide.setFont(font)
        self.s_divide.setStyleSheet("color: rgb(120, 120, 120);\n"
"border-radius: 25px;\n"
"background-color: rgb(255, 216, 97);\n"
"")
        self.s_divide.setObjectName("s_divide")
        self.s_six = QtWidgets.QPushButton(self.frame_buttons)
        self.s_six.setGeometry(QtCore.QRect(180, 240, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.s_six.setFont(font)
        self.s_six.setStyleSheet("color: rgb(120, 120, 120);\n"
"background-color: rgb(193, 193, 193);\n"
"border-radius: 25px;")
        self.s_six.setObjectName("s_six")
        self.s_four = QtWidgets.QPushButton(self.frame_buttons)
        self.s_four.setGeometry(QtCore.QRect(60, 240, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.s_four.setFont(font)
        self.s_four.setStyleSheet("color: rgb(120, 120, 120);\n"
"background-color: rgb(193, 193, 193);\n"
"border-radius: 25px;")
        self.s_four.setObjectName("s_four")
        self.s_plus = QtWidgets.QPushButton(self.frame_buttons)
        self.s_plus.setGeometry(QtCore.QRect(240, 300, 81, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.s_plus.setFont(font)
        self.s_plus.setStyleSheet("color: rgb(120, 120, 120);\n"
"border-radius: 25px;\n"
"background-color: rgb(255, 216, 97);\n"
"")
        self.s_plus.setObjectName("s_plus")
        self.s_equal = QtWidgets.QPushButton(self.frame_buttons)
        self.s_equal.setGeometry(QtCore.QRect(240, 360, 81, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.s_equal.setFont(font)
        self.s_equal.setStyleSheet("color: rgb(120, 120, 120);\n"
"border-radius: 25px;\n"
"background-color: rgb(255, 216, 97);\n"
"")
        self.s_equal.setObjectName("s_equal")
        self.s_nine = QtWidgets.QPushButton(self.frame_buttons)
        self.s_nine.setGeometry(QtCore.QRect(180, 180, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.s_nine.setFont(font)
        self.s_nine.setStyleSheet("color: rgb(120, 120, 120);\n"
"background-color: rgb(193, 193, 193);\n"
"border-radius: 25px;")
        self.s_nine.setObjectName("s_nine")
        self.s_minus = QtWidgets.QPushButton(self.frame_buttons)
        self.s_minus.setGeometry(QtCore.QRect(240, 240, 81, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.s_minus.setFont(font)
        self.s_minus.setStyleSheet("color: rgb(120, 120, 120);\n"
"border-radius: 25px;\n"
"background-color: rgb(255, 216, 97);\n"
"")
        self.s_minus.setObjectName("s_minus")
        self.s_one = QtWidgets.QPushButton(self.frame_buttons)
        self.s_one.setGeometry(QtCore.QRect(60, 300, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.s_one.setFont(font)
        self.s_one.setStyleSheet("color: rgb(120, 120, 120);\n"
"background-color: rgb(193, 193, 193);\n"
"border-radius: 25px;")
        self.s_one.setObjectName("s_one")
        self.s_ce = QtWidgets.QPushButton(self.frame_buttons)
        self.s_ce.setGeometry(QtCore.QRect(180, 0, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.s_ce.setFont(font)
        self.s_ce.setStyleSheet("color: rgb(120, 120, 120);\n"
"background-color: rgb(232, 232, 232);\n"
"border-radius: 25px;")
        self.s_ce.setObjectName("s_ce")
        self.s_e = QtWidgets.QPushButton(self.frame_buttons)
        self.s_e.setGeometry(QtCore.QRect(120, 0, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.s_e.setFont(font)
        self.s_e.setStyleSheet("color: rgb(120, 120, 120);\n"
"background-color: rgb(232, 232, 232);\n"
"border-radius: 25px;")
        self.s_e.setObjectName("s_e")
        self.s_pie = QtWidgets.QPushButton(self.frame_buttons)
        self.s_pie.setGeometry(QtCore.QRect(60, 0, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.s_pie.setFont(font)
        self.s_pie.setStyleSheet("color: rgb(120, 120, 120);\n"
"background-color: rgb(232, 232, 232);\n"
"border-radius: 25px;")
        self.s_pie.setObjectName("s_pie")
        self.s_mod = QtWidgets.QPushButton(self.frame_buttons)
        self.s_mod.setGeometry(QtCore.QRect(240, 60, 81, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.s_mod.setFont(font)
        self.s_mod.setStyleSheet("color: rgb(120, 120, 120);\n"
"border-radius: 25px;\n"
"background-color: rgb(255, 216, 97);\n"
"")
        self.s_mod.setObjectName("s_mod")
        self.s_absolute_x = QtWidgets.QPushButton(self.frame_buttons)
        self.s_absolute_x.setGeometry(QtCore.QRect(120, 60, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.s_absolute_x.setFont(font)
        self.s_absolute_x.setStyleSheet("color: rgb(120, 120, 120);\n"
"background-color: rgb(232, 232, 232);\n"
"border-radius: 25px;")
        self.s_absolute_x.setObjectName("s_absolute_x")
        self.s_exp = QtWidgets.QPushButton(self.frame_buttons)
        self.s_exp.setGeometry(QtCore.QRect(180, 60, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.s_exp.setFont(font)
        self.s_exp.setStyleSheet("color: rgb(120, 120, 120);\n"
"background-color: rgb(232, 232, 232);\n"
"border-radius: 25px;")
        self.s_exp.setObjectName("s_exp")
        self.s_back = QtWidgets.QPushButton(self.frame_buttons)
        self.s_back.setGeometry(QtCore.QRect(240, 0, 81, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.s_back.setFont(font)
        self.s_back.setStyleSheet("color: rgb(120, 120, 120);\n"
"border-radius: 25px;\n"
"background-color: rgb(255, 216, 97);\n"
"")
        self.s_back.setObjectName("s_back")
        self.s_n_factorial = QtWidgets.QPushButton(self.frame_buttons)
        self.s_n_factorial.setGeometry(QtCore.QRect(180, 120, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.s_n_factorial.setFont(font)
        self.s_n_factorial.setStyleSheet("color: rgb(120, 120, 120);\n"
"background-color: rgb(232, 232, 232);\n"
"border-radius: 25px;")
        self.s_n_factorial.setObjectName("s_n_factorial")
        self.s_close_bracket = QtWidgets.QPushButton(self.frame_buttons)
        self.s_close_bracket.setGeometry(QtCore.QRect(120, 120, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.s_close_bracket.setFont(font)
        self.s_close_bracket.setStyleSheet("color: rgb(120, 120, 120);\n"
"background-color: rgb(232, 232, 232);\n"
"border-radius: 25px;")
        self.s_close_bracket.setObjectName("s_close_bracket")
        self.s_open_bracket = QtWidgets.QPushButton(self.frame_buttons)
        self.s_open_bracket.setGeometry(QtCore.QRect(60, 120, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.s_open_bracket.setFont(font)
        self.s_open_bracket.setStyleSheet("color: rgb(120, 120, 120);\n"
"background-color: rgb(232, 232, 232);\n"
"border-radius: 25px;")
        self.s_open_bracket.setObjectName("s_open_bracket")
        self.s_ten_x = QtWidgets.QPushButton(self.frame_buttons)
        self.s_ten_x.setGeometry(QtCore.QRect(0, 240, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.s_ten_x.setFont(font)
        self.s_ten_x.setStyleSheet("color: rgb(120, 120, 120);\n"
"background-color: rgb(232, 232, 232);\n"
"border-radius: 25px;")
        self.s_ten_x.setObjectName("s_ten_x")
        self.s_xy = QtWidgets.QPushButton(self.frame_buttons)
        self.s_xy.setGeometry(QtCore.QRect(0, 180, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.s_xy.setFont(font)
        self.s_xy.setStyleSheet("color: rgb(120, 120, 120);\n"
"background-color: rgb(232, 232, 232);\n"
"border-radius: 25px;")
        self.s_xy.setObjectName("s_xy")
        self.s_ln = QtWidgets.QPushButton(self.frame_buttons)
        self.s_ln.setGeometry(QtCore.QRect(0, 360, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.s_ln.setFont(font)
        self.s_ln.setStyleSheet("color: rgb(120, 120, 120);\n"
"background-color: rgb(232, 232, 232);\n"
"border-radius: 25px;")
        self.s_ln.setObjectName("s_ln")
        self.s_log = QtWidgets.QPushButton(self.frame_buttons)
        self.s_log.setGeometry(QtCore.QRect(0, 300, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.s_log.setFont(font)
        self.s_log.setStyleSheet("color: rgb(120, 120, 120);\n"
"background-color: rgb(232, 232, 232);\n"
"border-radius: 25px;")
        self.s_log.setObjectName("s_log")
        self.s_x_square = QtWidgets.QPushButton(self.frame_buttons)
        self.s_x_square.setGeometry(QtCore.QRect(0, 60, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.s_x_square.setFont(font)
        self.s_x_square.setStyleSheet("color: rgb(120, 120, 120);\n"
"background-color: rgb(232, 232, 232);\n"
"border-radius: 25px;")
        self.s_x_square.setObjectName("s_x_square")
        self.s_one_by_x = QtWidgets.QPushButton(self.frame_buttons)
        self.s_one_by_x.setGeometry(QtCore.QRect(60, 60, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.s_one_by_x.setFont(font)
        self.s_one_by_x.setStyleSheet("color: rgb(120, 120, 120);\n"
"background-color: rgb(232, 232, 232);\n"
"border-radius: 25px;")
        self.s_one_by_x.setObjectName("s_one_by_x")
        self.s_root = QtWidgets.QPushButton(self.frame_buttons)
        self.s_root.setGeometry(QtCore.QRect(0, 120, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.s_root.setFont(font)
        self.s_root.setStyleSheet("color: rgb(120, 120, 120);\n"
"background-color: rgb(232, 232, 232);\n"
"border-radius: 25px;")
        self.s_root.setObjectName("s_root")
        self.s_per = QtWidgets.QPushButton(self.frame_buttons)
        self.s_per.setGeometry(QtCore.QRect(0, 0, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.s_per.setFont(font)
        self.s_per.setStyleSheet("color: rgb(120, 120, 120);\n"
"background-color: rgb(232, 232, 232);\n"
"border-radius: 25px;")
        self.s_per.setObjectName("s_per")
        self.frame_calculations_display = QtWidgets.QFrame(self.frame)
        self.frame_calculations_display.setGeometry(QtCore.QRect(10, 40, 321, 71))
        self.frame_calculations_display.setStyleSheet("")
        self.frame_calculations_display.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_calculations_display.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_calculations_display.setObjectName("frame_calculations_display")
        self.s_label_2 = QtWidgets.QLabel(self.frame_calculations_display)
        self.s_label_2.setGeometry(QtCore.QRect(0, 30, 321, 41))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.s_label_2.setFont(font)
        self.s_label_2.setStyleSheet("color: rgb(0, 0, 0);")
        self.s_label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.s_label_2.setObjectName("s_label_2")
        self.s_label_3 = QtWidgets.QLabel(self.frame_calculations_display)
        self.s_label_3.setGeometry(QtCore.QRect(0, 0, 321, 20))
        self.s_label_3.setMaximumSize(QtCore.QSize(100000, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.s_label_3.setFont(font)
        self.s_label_3.setStyleSheet("color: rgb(0, 0, 0);")
        self.s_label_3.setText("")
        self.s_label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.s_label_3.setObjectName("s_label_3")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(20, 10, 311, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
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
        icon1.addPixmap(QtGui.QPixmap("images/text.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuOption.setIcon(icon1)
        self.menuOption.setObjectName("menuOption")
        self.menuCalculator = QtWidgets.QMenu(self.menuOption)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images/calculator(3).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuCalculator.setIcon(icon2)
        self.menuCalculator.setObjectName("menuCalculator")
        self.menuConverter = QtWidgets.QMenu(self.menuOption)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("images/recycle.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
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
        icon4.addPixmap(QtGui.QPixmap("images/logout.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExit.setIcon(icon4)
        self.actionExit.setObjectName("actionExit")
        self.actionStandard = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("images/calculator.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionStandard.setIcon(icon5)
        self.actionStandard.setObjectName("actionStandard")
        self.actionScientific = QtWidgets.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("images/microscope.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionScientific.setIcon(icon6)
        self.actionScientific.setObjectName("actionScientific")
        self.actionProgrammer = QtWidgets.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("images/code.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionProgrammer.setIcon(icon7)
        self.actionProgrammer.setObjectName("actionProgrammer")
        self.actionDate_Calculation = QtWidgets.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("images/calendar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDate_Calculation.setIcon(icon8)
        self.actionDate_Calculation.setObjectName("actionDate_Calculation")

        self.actionVolume = QtWidgets.QAction(MainWindow)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("images/shapes.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionVolume.setIcon(icon10)
        self.actionVolume.setObjectName("actionVolume")
        self.actionLength = QtWidgets.QAction(MainWindow)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("images/ruler.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionLength.setIcon(icon11)
        self.actionLength.setObjectName("actionLength")
        self.actionWeight_and_Mass = QtWidgets.QAction(MainWindow)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap("images/weighing-scale.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionWeight_and_Mass.setIcon(icon12)
        self.actionWeight_and_Mass.setObjectName("actionWeight_and_Mass")
        self.actionTemperature = QtWidgets.QAction(MainWindow)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap("images/temperature.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionTemperature.setIcon(icon13)
        self.actionTemperature.setObjectName("actionTemperature")
        self.actionEnergy = QtWidgets.QAction(MainWindow)
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap("images/fire.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionEnergy.setIcon(icon14)
        self.actionEnergy.setObjectName("actionEnergy")
        self.actionArea = QtWidgets.QAction(MainWindow)
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap("images/area.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionArea.setIcon(icon15)
        self.actionArea.setObjectName("actionArea")
        self.actionSpeed = QtWidgets.QAction(MainWindow)
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap("images/fast.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSpeed.setIcon(icon16)
        self.actionSpeed.setObjectName("actionSpeed")
        self.actionTime = QtWidgets.QAction(MainWindow)
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap("images/clock.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionTime.setIcon(icon17)
        self.actionTime.setObjectName("actionTime")
        self.actionPower = QtWidgets.QAction(MainWindow)
        icon18 = QtGui.QIcon()
        icon18.addPixmap(QtGui.QPixmap("images/energy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPower.setIcon(icon18)
        self.actionPower.setObjectName("actionPower")
        self.actionData = QtWidgets.QAction(MainWindow)
        icon19 = QtGui.QIcon()
        icon19.addPixmap(QtGui.QPixmap("images/statistics.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionData.setIcon(icon19)
        self.actionData.setObjectName("actionData")
        self.actionPressure = QtWidgets.QAction(MainWindow)
        icon20 = QtGui.QIcon()
        icon20.addPixmap(QtGui.QPixmap("images/indicator.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPressure.setIcon(icon20)
        self.actionPressure.setObjectName("actionPressure")
        self.actionAngle = QtWidgets.QAction(MainWindow)
        icon21 = QtGui.QIcon()
        icon21.addPixmap(QtGui.QPixmap("images/angle.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
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

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculator"))
        self.s_point.setText(_translate("MainWindow", "."))
        self.s_three.setText(_translate("MainWindow", "3"))
        self.s_zero.setText(_translate("MainWindow", "0"))
        self.s_two.setText(_translate("MainWindow", "2"))
        self.s_eight.setText(_translate("MainWindow", "8"))
        self.s_five.setText(_translate("MainWindow", "5"))
        self.s_seven.setText(_translate("MainWindow", "7"))
        self.s_plus_minus.setText(_translate("MainWindow", "+/-"))
        self.s_multiply.setToolTip(_translate("MainWindow", "Multiply"))
        self.s_multiply.setText(_translate("MainWindow", "X"))
        self.s_divide.setToolTip(_translate("MainWindow", "Divide"))
        self.s_divide.setText(_translate("MainWindow", "/"))
        self.s_six.setText(_translate("MainWindow", "6"))
        self.s_four.setText(_translate("MainWindow", "4"))
        self.s_plus.setToolTip(_translate("MainWindow", "Plus"))
        self.s_plus.setText(_translate("MainWindow", "+"))
        self.s_equal.setText(_translate("MainWindow", "="))
        self.s_nine.setText(_translate("MainWindow", "9"))
        self.s_minus.setToolTip(_translate("MainWindow", "Subtract"))
        self.s_minus.setText(_translate("MainWindow", "-"))
        self.s_one.setText(_translate("MainWindow", "1"))
        self.s_ce.setToolTip(_translate("MainWindow", "Clear"))
        self.s_ce.setText(_translate("MainWindow", "CE"))
        self.s_e.setToolTip(_translate("MainWindow", "Clear recent calculation"))
        self.s_e.setText(_translate("MainWindow", "e"))
        self.s_pie.setText(_translate("MainWindow", u'\u03C0'))
        self.s_mod.setToolTip(_translate("MainWindow", "Clear"))
        self.s_mod.setText(_translate("MainWindow", "mod"))
        self.s_absolute_x.setText(_translate("MainWindow", "|x|"))
        self.s_exp.setToolTip(_translate("MainWindow", "Clear recent calculation"))
        self.s_exp.setText(_translate("MainWindow", "exp"))
        self.s_back.setToolTip(_translate("MainWindow", "Remove/Back"))
        self.s_back.setText(_translate("MainWindow", "<"))
        self.s_n_factorial.setText(_translate("MainWindow", "n!"))
        self.s_close_bracket.setText(_translate("MainWindow", ")"))
        self.s_open_bracket.setText(_translate("MainWindow", "("))
        self.s_ten_x.setText(_translate("MainWindow", u'10\u207F'))
        self.s_xy.setText(_translate("MainWindow", u'x\u207F'))
        self.s_ln.setText(_translate("MainWindow", "ln"))
        self.s_log.setText(_translate("MainWindow", "log"))
        self.s_x_square.setToolTip(_translate("MainWindow", "Square"))
        self.s_x_square.setText(_translate("MainWindow", "x²"))
        self.s_one_by_x.setToolTip(_translate("MainWindow", "one by x"))
        self.s_one_by_x.setText(_translate("MainWindow", "1/x"))
        self.s_root.setToolTip(_translate("MainWindow", "Square root"))
        self.s_root.setText(_translate("MainWindow", "²√x"))
        self.s_per.setText(_translate("MainWindow", "%"))
        self.s_label_2.setText(_translate("MainWindow", "0"))
        self.label.setText(_translate("MainWindow", "Scientific"))
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
    ui = Ui_MainWindow_Scientific()
    ui.setupUiScientific(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
