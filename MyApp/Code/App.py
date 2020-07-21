import sys

from PyQt5 import QtWidgets, QtGui, QtCore
from MyApp.PythonUIfiles.light_theme import Ui_MainWindow2
from MyApp.PythonUIfiles.light_theme_scientific import Ui_MainWindow_Scientific
from MyApp.PythonUIfiles.light_theme_Programmer import Ui_MainWindow_Programmer
from MyApp.PythonUIfiles.light_theme_date_cal import Ui_MainWindow_Date
from MyApp.PythonUIfiles.light_theme_Volume import Ui_MainWindow_Volume
from MyApp.PythonUIfiles.light_theme_Length import Ui_MainWindow_Length
from MyApp.PythonUIfiles.light_theme_WeightandMass import Ui_MainWindow_WeightMass
from MyApp.PythonUIfiles.light_theme_Temperature import Ui_MainWindow_Temperature
from MyApp.PythonUIfiles.light_theme_Energy import Ui_MainWindow_Energy
from MyApp.PythonUIfiles.light_theme_Area import Ui_MainWindow_Area
from MyApp.PythonUIfiles.light_theme_Speed import Ui_MainWindow_Speed
from MyApp.PythonUIfiles.light_theme_Time import Ui_MainWindow_Time
from MyApp.PythonUIfiles.light_theme_Power import Ui_MainWindow_Power
from MyApp.PythonUIfiles.light_theme_Data import Ui_MainWindow_Data
from MyApp.PythonUIfiles.light_theme_Pressure import Ui_MainWindow_Pressure
from MyApp.PythonUIfiles.light_theme_Angle import Ui_MainWindow_Angle

import math
from decimal import Decimal


class MyMainWindow(QtWidgets.QMainWindow, Ui_MainWindow2, Ui_MainWindow_Scientific, Ui_MainWindow_Programmer,
                   Ui_MainWindow_Date, Ui_MainWindow_Volume, Ui_MainWindow_Length, Ui_MainWindow_WeightMass,
                   Ui_MainWindow_Temperature, Ui_MainWindow_Energy, Ui_MainWindow_Area, Ui_MainWindow_Speed,
                   Ui_MainWindow_Time, Ui_MainWindow_Power, Ui_MainWindow_Data, Ui_MainWindow_Pressure,
                   Ui_MainWindow_Angle):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.change_to_standard()
        MyMainWindow.winFlag = ''

    def link_menu_fnc(self):
        # linking Menu bar function
        self.actionStandard.triggered.connect(self.change_to_standard)
        self.actionScientific.triggered.connect(self.change_to_scientific)
        self.actionProgrammer.triggered.connect(self.change_to_programmer)

        self.actionDate_Calculation.triggered.connect(self.change_to_date)
        self.actionVolume.triggered.connect(self.change_to_volume)
        self.actionLength.triggered.connect(self.change_to_length)
        self.actionWeight_and_Mass.triggered.connect(self.change_to_weightmass)
        self.actionTemperature.triggered.connect(self.change_to_temperature)
        self.actionEnergy.triggered.connect(self.change_to_energy)
        self.actionArea.triggered.connect(self.change_to_area)
        self.actionSpeed.triggered.connect(self.change_to_speed)
        self.actionTime.triggered.connect(self.change_to_time)
        self.actionPower.triggered.connect(self.change_to_power)
        self.actionData.triggered.connect(self.change_to_data)
        self.actionPressure.triggered.connect(self.change_to_pressure)
        self.actionAngle.triggered.connect(self.change_to_angle)

    def change_to_standard(self):
        MyMainWindow.winFlag = 'n' #normal
        self.setupUi2(self)  # here we setup ui file of light mode (Initially)

        self.zero.clicked.connect(lambda: self.get('0'))
        self.one.clicked.connect(lambda: self.get('1'))
        self.two.clicked.connect(lambda: self.get('2'))
        self.three.clicked.connect(lambda: self.get('3'))
        self.four.clicked.connect(lambda: self.get('4'))
        self.five.clicked.connect(lambda: self.get('5'))
        self.six.clicked.connect(lambda: self.get('6'))
        self.seven.clicked.connect(lambda: self.get('7'))
        self.eight.clicked.connect(lambda: self.get('8'))
        self.nine.clicked.connect(lambda: self.get('9'))
        self.plus.clicked.connect(lambda: self.get('+'))
        self.minus.clicked.connect(lambda: self.get('-'))
        self.multiply.clicked.connect(lambda: self.get('*'))
        self.divide.clicked.connect(lambda: self.get('/'))
        self.plus_minus.clicked.connect(lambda: self.get('+_-'))
        self.per.clicked.connect(lambda: self.get('%'))
        self.one_by_x.clicked.connect(lambda: self.get('1/x'))
        self.x_square.clicked.connect(lambda: self.get('x_square'))
        self.root.clicked.connect(lambda: self.get('SquareRoot'))
        self.back.clicked.connect(lambda: self.get('<'))
        self.ce.clicked.connect(lambda: self.get('CE'))
        self.clear.clicked.connect(lambda: self.get('C'))
        self.equal.clicked.connect(lambda: self.get('='))
        self.point.clicked.connect(lambda: self.get('.'))



        # linking Menu bar function
        self.link_menu_fnc()

    def change_to_scientific(self):
        try:
            MyMainWindow.winFlag = 's' #scientific
            self.setupUiScientific(self)
            self.s_zero.clicked.connect(lambda: self.get_scientific('0'))
            self.s_one.clicked.connect(lambda: self.get_scientific('1'))
            self.s_two.clicked.connect(lambda: self.get_scientific('2'))
            self.s_three.clicked.connect(lambda: self.get_scientific('3'))
            self.s_four.clicked.connect(lambda: self.get_scientific('4'))
            self.s_five.clicked.connect(lambda: self.get_scientific('5'))
            self.s_six.clicked.connect(lambda: self.get_scientific('6'))
            self.s_seven.clicked.connect(lambda: self.get_scientific('7'))
            self.s_eight.clicked.connect(lambda: self.get_scientific('8'))
            self.s_nine.clicked.connect(lambda: self.get_scientific('9'))
            self.s_plus.clicked.connect(lambda: self.get_scientific('+'))
            self.s_minus.clicked.connect(lambda: self.get_scientific('-'))
            self.s_multiply.clicked.connect(lambda: self.get_scientific('*'))
            self.s_divide.clicked.connect(lambda: self.get_scientific('/'))
            self.s_plus_minus.clicked.connect(lambda: self.get_scientific('+_-'))
            self.s_per.clicked.connect(lambda: self.get_scientific('per'))
            self.s_one_by_x.clicked.connect(lambda: self.get_scientific('1/x'))
            self.s_x_square.clicked.connect(lambda: self.get_scientific('x_square'))
            self.s_root.clicked.connect(lambda: self.get_scientific('SquareRoot'))
            self.s_back.clicked.connect(lambda: self.get_scientific('<'))
            self.s_ce.clicked.connect(lambda: self.get_scientific('CE'))
            self.s_equal.clicked.connect(lambda: self.get_scientific('='))
            self.s_point.clicked.connect(lambda: self.get_scientific('.'))
            self.s_pie.clicked.connect(lambda: self.get_scientific('pie'))
            self.s_e.clicked.connect(lambda: self.get_scientific('e'))
            self.s_absolute_x.clicked.connect(lambda: self.get_scientific('absolute_x'))
            self.s_exp.clicked.connect(lambda: self.get_scientific('exp'))
            self.s_mod.clicked.connect(lambda: self.get_scientific('%'))
            self.s_open_bracket.clicked.connect(lambda: self.get_scientific('('))
            self.s_close_bracket.clicked.connect(lambda: self.get_scientific(')'))
            self.s_n_factorial.clicked.connect(lambda: self.get_scientific('n_factorial'))
            self.s_xy.clicked.connect(lambda: self.get_scientific('**'))
            self.s_ten_x.clicked.connect(lambda: self.get_scientific('ten_x'))
            self.s_log.clicked.connect(lambda: self.get_scientific('log'))
            self.s_ln.clicked.connect(lambda: self.get_scientific('ln'))

            # linking Menu bar function
            self.link_menu_fnc()


        except Exception as e:
            print(e)

    def change_to_programmer(self):
        try:
            MyMainWindow.winflag = 'p' #programmer
            self.setupUiProgrammer(self)
            self.p_zero.clicked.connect(lambda: self.get_programmer('0'))
            self.p_one.clicked.connect(lambda: self.get_programmer('1'))
            self.p_two.clicked.connect(lambda: self.get_programmer('2'))
            self.p_three.clicked.connect(lambda: self.get_programmer('3'))
            self.p_four.clicked.connect(lambda: self.get_programmer('4'))
            self.p_five.clicked.connect(lambda: self.get_programmer('5'))
            self.p_six.clicked.connect(lambda: self.get_programmer('6'))
            self.p_seven.clicked.connect(lambda: self.get_programmer('7'))
            self.p_eight.clicked.connect(lambda: self.get_programmer('8'))
            self.p_nine.clicked.connect(lambda: self.get_programmer('9'))
            self.p_plus.clicked.connect(lambda: self.get_programmer('+'))
            self.p_minus.clicked.connect(lambda: self.get_programmer('-'))
            self.p_multiply.clicked.connect(lambda: self.get_programmer('*'))
            self.p_divide.clicked.connect(lambda: self.get_programmer('/'))
            self.p_plus_minus.clicked.connect(lambda: self.get_programmer('+_-'))
            self.p_per.clicked.connect(lambda: self.get_programmer('%'))
            self.p_back.clicked.connect(lambda: self.get_programmer('<'))
            self.p_ce.clicked.connect(lambda: self.get_programmer('CE'))
            self.p_equal.clicked.connect(lambda: self.get_programmer('='))
            self.p_open_bracket.clicked.connect(lambda: self.get_programmer('('))
            self.p_close_bracket.clicked.connect(lambda: self.get_programmer(')'))
            self.p_lsh.clicked.connect(lambda: self.get_programmer('<<'))
            self.p_rsh.clicked.connect(lambda: self.get_programmer('>>'))
            self.p_a.clicked.connect(lambda: self.get_programmer('A'))
            self.p_b.clicked.connect(lambda: self.get_programmer('B'))
            self.p_c.clicked.connect(lambda: self.get_programmer('C'))
            self.p_d.clicked.connect(lambda: self.get_programmer('D'))
            self.p_e.clicked.connect(lambda: self.get_programmer('E'))
            self.p_f.clicked.connect(lambda: self.get_programmer('F'))
            # print('0')
            # self.p_label_hex.mousePressEvent = self.change_value_hex
            # print('1')
            # self.p_label_hex_val.mousePressEvent = self.change_value_hex
            # print('2')
            # self.p_label_dec.mousePressEvent = self.change_value_dec
            # print('3')
            # self.p_label_dec_val.mousePressEvent = self.change_value_dec
            # print('4')
            # self.p_label_oct.mousePressEvent = self.change_value_oct
            # print('5')
            # self.p_label_oct_val.mousePressEvent = self.change_value_oct
            # print('6')
            # self.p_label_bin.mousePressEvent = self.change_value_bin
            # print('7')
            # self.p_label_bin_val.mousePressEvent = self.change_value_bin
            # print('8')
            # Disabling all button according to decimal conversion
            self.p_a.setStyleSheet("color: rgb(120, 120, 120, 90);\n"
                                       "background-color: rgba(193, 193, 193, 70);\n"
                                       "border-radius: 22px;")
            self.p_a.setEnabled(False)
            self.p_b.setStyleSheet("color: rgb(120, 120, 120, 90);\n"
                                       "background-color: rgba(193, 193, 193, 70);\n"
                                       "border-radius: 22px;")
            self.p_b.setEnabled(False)
            self.p_c.setStyleSheet("color: rgb(120, 120, 120, 90);\n"
                                       "background-color: rgba(193, 193, 193, 70);\n"
                                       "border-radius: 22px;")
            self.p_c.setEnabled(False)
            self.p_d.setStyleSheet("color: rgb(120, 120, 120, 90);\n"
                                       "background-color: rgba(193, 193, 193, 70);\n"
                                       "border-radius: 22px;")
            self.p_d.setEnabled(False)
            self.p_e.setStyleSheet("color: rgb(120, 120, 120, 90);\n"
                                       "background-color: rgba(193, 193, 193, 70);\n"
                                       "border-radius: 22px;")
            self.p_e.setEnabled(False)
            self.p_f.setStyleSheet("color: rgb(120, 120, 120, 90);\n"
                                       "background-color: rgba(193, 193, 193, 70);\n"
                                       "border-radius: 22px;")
            self.p_f.setEnabled(False)
            self.p_point.setStyleSheet("color: rgb(120, 120, 120, 90);\n"
                                       "background-color: rgba(193, 193, 193, 70);\n"
                                       "border-radius: 22px;")
            self.p_point.setEnabled(False)

            # linking Menu bar function
            self.link_menu_fnc()
        except Exception as e:
            print(e)

    def change_to_date(self):
        MyMainWindow.winflag = 'dc'  # date cal
        self.setupUiDate(self)

        # linking Menu bar function
        self.link_menu_fnc()

    def change_to_volume(self):
        MyMainWindow.winflag = 'vol'  # volume
        self.setupUiVolume(self)
        # binding function
        self.vol_zero.clicked.connect(lambda: self.get_volume('0'))
        self.vol_one.clicked.connect(lambda: self.get_volume('1'))
        self.vol_two.clicked.connect(lambda: self.get_volume('2'))
        self.vol_three.clicked.connect(lambda: self.get_volume('3'))
        self.vol_four.clicked.connect(lambda: self.get_volume('4'))
        self.vol_five.clicked.connect(lambda: self.get_volume('5'))
        self.vol_six.clicked.connect(lambda: self.get_volume('6'))
        self.vol_seven.clicked.connect(lambda: self.get_volume('7'))
        self.vol_eight.clicked.connect(lambda: self.get_volume('8'))
        self.vol_nine.clicked.connect(lambda: self.get_volume('9'))
        self.vol_back.clicked.connect(lambda: self.get_volume('<'))
        self.vol_ce.clicked.connect(lambda: self.get_volume('CE'))
        self.vol_point.clicked.connect(lambda: self.get_volume('.'))
        self.vol_comboBox_1.activated[str].connect(lambda: self.vol_calculations(float(self.vol_label_1.text())))
        self.vol_comboBox_2.activated[str].connect(lambda: self.vol_calculations(float(self.vol_label_1.text())))


        # linking Menu bar function
        self.link_menu_fnc()


    def change_to_length(self):
        MyMainWindow.winflag = 'len'  # length
        self.setupUiLength(self)
        self.len_zero.clicked.connect(lambda: self.get_length('0'))
        self.len_one.clicked.connect(lambda: self.get_length('1'))
        self.len_two.clicked.connect(lambda: self.get_length('2'))
        self.len_three.clicked.connect(lambda: self.get_length('3'))
        self.len_four.clicked.connect(lambda: self.get_length('4'))
        self.len_five.clicked.connect(lambda: self.get_length('5'))
        self.len_six.clicked.connect(lambda: self.get_length('6'))
        self.len_seven.clicked.connect(lambda: self.get_length('7'))
        self.len_eight.clicked.connect(lambda: self.get_length('8'))
        self.len_nine.clicked.connect(lambda: self.get_length('9'))
        self.len_back.clicked.connect(lambda: self.get_length('<'))
        self.len_ce.clicked.connect(lambda: self.get_length('CE'))
        self.len_point.clicked.connect(lambda: self.get_length('.'))
        self.len_comboBox_1.activated[str].connect(lambda: self.len_calculations(float(self.len_label_1.text())))
        self.len_comboBox_2.activated[str].connect(lambda: self.len_calculations(float(self.len_label_1.text())))

        # linking Menu bar function
        self.link_menu_fnc()

    def change_to_weightmass(self):
        MyMainWindow.winflag = 'wm'  # weight and mass
        self.setupUiWeightMass(self)
        self.wm_zero.clicked.connect(lambda: self.get_weightmass('0'))
        self.wm_one.clicked.connect(lambda: self.get_weightmass('1'))
        self.wm_two.clicked.connect(lambda: self.get_weightmass('2'))
        self.wm_three.clicked.connect(lambda: self.get_weightmass('3'))
        self.wm_four.clicked.connect(lambda: self.get_weightmass('4'))
        self.wm_five.clicked.connect(lambda: self.get_weightmass('5'))
        self.wm_six.clicked.connect(lambda: self.get_weightmass('6'))
        self.wm_seven.clicked.connect(lambda: self.get_weightmass('7'))
        self.wm_eight.clicked.connect(lambda: self.get_weightmass('8'))
        self.wm_nine.clicked.connect(lambda: self.get_weightmass('9'))
        self.wm_back.clicked.connect(lambda: self.get_weightmass('<'))
        self.wm_ce.clicked.connect(lambda: self.get_weightmass('CE'))
        self.wm_point.clicked.connect(lambda: self.get_weightmass('.'))
        self.wm_comboBox_1.activated[str].connect(lambda: self.wm_calculations(float(self.wm_label_1.text())))
        self.wm_comboBox_2.activated[str].connect(lambda: self.wm_calculations(float(self.wm_label_1.text())))
        # linking Menu bar function
        self.link_menu_fnc()

    def change_to_temperature(self):
        MyMainWindow.winflag = 'temp'  # temperature
        self.setupUiTemperature(self)
        self.temp_zero.clicked.connect(lambda: self.get_temperature('0'))
        self.temp_one.clicked.connect(lambda: self.get_temperature('1'))
        self.temp_two.clicked.connect(lambda: self.get_temperature('2'))
        self.temp_three.clicked.connect(lambda: self.get_temperature('3'))
        self.temp_four.clicked.connect(lambda: self.get_temperature('4'))
        self.temp_five.clicked.connect(lambda: self.get_temperature('5'))
        self.temp_six.clicked.connect(lambda: self.get_temperature('6'))
        self.temp_seven.clicked.connect(lambda: self.get_temperature('7'))
        self.temp_eight.clicked.connect(lambda: self.get_temperature('8'))
        self.temp_nine.clicked.connect(lambda: self.get_temperature('9'))
        self.temp_back.clicked.connect(lambda: self.get_temperature('<'))
        self.temp_ce.clicked.connect(lambda: self.get_temperature('CE'))
        self.temp_point.clicked.connect(lambda: self.get_temperature('.'))
        self.temp_comboBox_1.activated[str].connect(lambda: self.temp_calculations(float(self.temp_label_1.text())))
        self.temp_comboBox_2.activated[str].connect(lambda: self.temp_calculations(float(self.temp_label_1.text())))
        # linking Menu bar function
        self.link_menu_fnc()

    def change_to_energy(self):
        MyMainWindow.winflag = 'ener'  # energy
        self.setupUiEnergy(self)
        self.ener_zero.clicked.connect(lambda: self.get_energy('0'))
        self.ener_one.clicked.connect(lambda: self.get_energy('1'))
        self.ener_two.clicked.connect(lambda: self.get_energy('2'))
        self.ener_three.clicked.connect(lambda: self.get_energy('3'))
        self.ener_four.clicked.connect(lambda: self.get_energy('4'))
        self.ener_five.clicked.connect(lambda: self.get_energy('5'))
        self.ener_six.clicked.connect(lambda: self.get_energy('6'))
        self.ener_seven.clicked.connect(lambda: self.get_energy('7'))
        self.ener_eight.clicked.connect(lambda: self.get_energy('8'))
        self.ener_nine.clicked.connect(lambda: self.get_energy('9'))
        self.ener_back.clicked.connect(lambda: self.get_energy('<'))
        self.ener_ce.clicked.connect(lambda: self.get_energy('CE'))
        self.ener_point.clicked.connect(lambda: self.get_energy('.'))
        self.ener_comboBox_1.activated[str].connect(lambda: self.ener_calculations(float(self.ener_label_1.text())))
        self.ener_comboBox_2.activated[str].connect(lambda: self.ener_calculations(float(self.ener_label_1.text())))
        # linking Menu bar function
        self.link_menu_fnc()

    def change_to_area(self):
        MyMainWindow.winflag = 'area'  # area
        self.setupUiArea(self)
        self.area_zero.clicked.connect(lambda: self.get_area('0'))
        self.area_one.clicked.connect(lambda: self.get_area('1'))
        self.area_two.clicked.connect(lambda: self.get_area('2'))
        self.area_three.clicked.connect(lambda: self.get_area('3'))
        self.area_four.clicked.connect(lambda: self.get_area('4'))
        self.area_five.clicked.connect(lambda: self.get_area('5'))
        self.area_six.clicked.connect(lambda: self.get_area('6'))
        self.area_seven.clicked.connect(lambda: self.get_area('7'))
        self.area_eight.clicked.connect(lambda: self.get_area('8'))
        self.area_nine.clicked.connect(lambda: self.get_area('9'))
        self.area_back.clicked.connect(lambda: self.get_area('<'))
        self.area_ce.clicked.connect(lambda: self.get_area('CE'))
        self.area_point.clicked.connect(lambda: self.get_area('.'))
        self.area_comboBox_1.activated[str].connect(lambda: self.area_calculations(float(self.area_label_1.text())))
        self.area_comboBox_2.activated[str].connect(lambda: self.area_calculations(float(self.area_label_1.text())))
        # linking Menu bar function
        self.link_menu_fnc()

    def change_to_speed(self):
        MyMainWindow.winflag = 'sp'  # speed
        self.setupUiSpeed(self)

        # linking Menu bar function
        self.link_menu_fnc()

    def change_to_time(self):
        MyMainWindow.winflag = 't'  # programmer
        self.setupUiTime(self)

        # linking Menu bar function
        self.link_menu_fnc()

    def change_to_power(self):
        MyMainWindow.winflag = 'pow'  # power
        self.setupUiPower(self)

        # linking Menu bar function
        self.link_menu_fnc()

    def change_to_data(self):
        MyMainWindow.winflag = 'da'  # data
        self.setupUiData(self)

        # linking Menu bar function
        self.link_menu_fnc()

    def change_to_pressure(self):
        MyMainWindow.winflag = 'pr'  # pressure
        self.setupUiPressure(self)

        # linking Menu bar function
        self.link_menu_fnc()

    def change_to_angle(self):
        MyMainWindow.winflag = 'a'  # angle
        self.setupUiAngle(self)

        # linking Menu bar function
        self.link_menu_fnc()

    def change_value_hex(self):
        try:
            print('hex')
            self.p_a.setEnabled(True)
            self.p_b.setEnabled(True)
            self.p_c.setEnabled(True)
            self.p_d.setEnabled(True)
            self.p_e.setEnabled(True)
            self.p_f.setEnabled(True)
            self.p_a.setStyleSheet("color: rgb(120, 120, 120);\n"
                                   "background-color: rgb(232, 232, 232);\n"
                                   "border-radius: 22px;")
            self.p_b.setStyleSheet("color: rgb(120, 120, 120);\n"
                                   "background-color: rgb(232, 232, 232);\n"
                                   "border-radius: 22px;")
            self.p_c.setStyleSheet("color: rgb(120, 120, 120);\n"
                                   "background-color: rgb(232, 232, 232);\n"
                                   "border-radius: 22px;")
            self.p_d.setStyleSheet("color: rgb(120, 120, 120);\n"
                                   "background-color: rgb(232, 232, 232);\n"
                                   "border-radius: 22px;")
            self.p_e.setStyleSheet("color: rgb(120, 120, 120);\n"
                                   "background-color: rgb(232, 232, 232);\n"
                                   "border-radius: 22px;")
            self.p_f.setStyleSheet("color: rgb(120, 120, 120);\n"
                                   "background-color: rgb(232, 232, 232);\n"
                                   "border-radius: 22px;")
        except Exception as e:
            print(e)

    def change_value_dec(self):
        try:
            print('dec')

            self.p_a.setEnabled(False)
            self.p_b.setEnabled(False)
            self.p_c.setEnabled(False)
            self.p_d.setEnabled(False)
            self.p_e.setEnabled(False)
            self.p_f.setEnabled(False)
            self.p_a.setStyleSheet("color: rgb(120, 120, 120, 27);\n"
                                   "background-color: rgba(193, 193, 193, 27);\n"
                                   "border-radius: 22px;")
            self.p_b.setStyleSheet("color: rgb(120, 120, 120, 27);\n"
                                   "background-color: rgba(193, 193, 193, 27);\n"
                                   "border-radius: 22px;")
            self.p_c.setStyleSheet("color: rgb(120, 120, 120, 27);\n"
                                   "background-color: rgba(193, 193, 193, 27);\n"
                                   "border-radius: 22px;")
            self.p_d.setStyleSheet("color: rgb(120, 120, 120, 27);\n"
                                   "background-color: rgba(193, 193, 193, 27);\n"
                                   "border-radius: 22px;")
            self.p_e.setStyleSheet("color: rgb(120, 120, 120, 27);\n"
                                   "background-color: rgba(193, 193, 193, 27);\n"
                                   "border-radius: 22px;")
            self.p_f.setStyleSheet("color: rgb(120, 120, 120, 27);\n"
                                   "background-color: rgba(193, 193, 193, 27);\n"
                                   "border-radius: 22px;")
        except Exception as e:
            print(e)

    def change_value_oct(self):
        try:
            print('oct')
            self.p_a.setEnabled(False)
            self.p_b.setEnabled(False)
            self.p_c.setEnabled(False)
            self.p_d.setEnabled(False)
            self.p_e.setEnabled(False)
            self.p_f.setEnabled(False)
            self.p_eight.setEnabled(False)
            self.p_nine.setEnabled(False)
            self.p_a.setStyleSheet("color: rgb(120, 120, 120, 27);\n"
                                   "background-color: rgba(193, 193, 193, 27);\n"
                                   "border-radius: 22px;")
            self.p_b.setStyleSheet("color: rgb(120, 120, 120, 27);\n"
                                   "background-color: rgba(193, 193, 193, 27);\n"
                                   "border-radius: 22px;")
            self.p_c.setStyleSheet("color: rgb(120, 120, 120, 27);\n"
                                   "background-color: rgba(193, 193, 193, 27);\n"
                                   "border-radius: 22px;")
            self.p_d.setStyleSheet("color: rgb(120, 120, 120, 27);\n"
                                   "background-color: rgba(193, 193, 193, 27);\n"
                                   "border-radius: 22px;")
            self.p_e.setStyleSheet("color: rgb(120, 120, 120, 27);\n"
                                   "background-color: rgba(193, 193, 193, 27);\n"
                                   "border-radius: 22px;")
            self.p_f.setStyleSheet("color: rgb(120, 120, 120, 27);\n"
                                   "background-color: rgba(193, 193, 193, 27);\n"
                                   "border-radius: 22px;")
            self.p_eight.setStyleSheet("color: rgb(120, 120, 120, 27);\n"
                                       "background-color: rgba(193, 193, 193, 27);\n"
                                       "border-radius: 22px;")
            self.p_nine.setStyleSheet("color: rgb(120, 120, 120, 27);\n"
                                      "background-color: rgba(193, 193, 193, 27);\n"
                                      "border-radius: 22px;")
        except Exception as e:
            print(e)

    def change_value_bin(self):
        try:
            print('bin')
            self.p_a.setEnabled(False)
            self.p_b.setEnabled(False)
            self.p_c.setEnabled(False)
            self.p_d.setEnabled(False)
            self.p_e.setEnabled(False)
            self.p_f.setEnabled(False)
            self.p_nine.setEnabled(False)
            self.p_eight.setEnabled(False)
            self.p_seven.setEnabled(False)
            self.p_six.setEnabled(False)
            self.p_five.setEnabled(False)
            self.p_four.setEnabled(False)
            self.p_three.setEnabled(False)
            self.p_two.setEnabled(False)
            self.p_a.setStyleSheet("color: rgb(120, 120, 120, 27);\n"
                                   "background-color: rgba(193, 193, 193, 27);\n"
                                   "border-radius: 22px;")
            self.p_b.setStyleSheet("color: rgb(120, 120, 120, 27);\n"
                                   "background-color: rgba(193, 193, 193, 27);\n"
                                   "border-radius: 22px;")
            self.p_c.setStyleSheet("color: rgb(120, 120, 120, 27);\n"
                                   "background-color: rgba(193, 193, 193, 27);\n"
                                   "border-radius: 22px;")
            self.p_d.setStyleSheet("color: rgb(120, 120, 120, 27);\n"
                                   "background-color: rgba(193, 193, 193, 27);\n"
                                   "border-radius: 22px;")
            self.p_e.setStyleSheet("color: rgb(120, 120, 120, 27);\n"
                                   "background-color: rgba(193, 193, 193, 27);\n"
                                   "border-radius: 22px;")
            self.p_f.setStyleSheet("color: rgb(120, 120, 120, 27);\n"
                                   "background-color: rgba(193, 193, 193, 27);\n"
                                   "border-radius: 22px;")
            self.p_eight.setStyleSheet("color: rgb(120, 120, 120, 27);\n"
                                       "background-color: rgba(193, 193, 193, 27);\n"
                                       "border-radius: 22px;")
            self.p_nine.setStyleSheet("color: rgb(120, 120, 120, 27);\n"
                                      "background-color: rgba(193, 193, 193, 27);\n"
                                      "border-radius: 22px;")
            self.p_seven.setStyleSheet("color: rgb(120, 120, 120, 27);\n"
                                       "background-color: rgba(193, 193, 193, 27);\n"
                                       "border-radius: 22px;")
            self.p_six.setStyleSheet("color: rgb(120, 120, 120, 27);\n"
                                     "background-color: rgba(193, 193, 193, 27);\n"
                                     "border-radius: 22px;")
            self.p_five.setStyleSheet("color: rgb(120, 120, 120, 27);\n"
                                      "background-color: rgba(193, 193, 193, 27);\n"
                                      "border-radius: 22px;")
            self.p_four.setStyleSheet("color: rgb(120, 120, 120, 27);\n"
                                      "background-color: rgba(193, 193, 193, 27);\n"
                                      "border-radius: 22px;")
            self.p_three.setStyleSheet("color: rgb(120, 120, 120, 27);\n"
                                       "background-color: rgba(193, 193, 193, 27);\n"
                                       "border-radius: 22px;")
            self.p_two.setStyleSheet("color: rgb(120, 120, 120, 27);\n"
                                     "background-color: rgba(193, 193, 193, 27);\n"
                                     "border-radius: 22px;")
        except Exception as e:
            print(e)

    # area
    def get_area(self, data):
        try:
            if self.area_label_1.text() == '0':
                self.area_label_1.setText(data)
            elif data in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                if self.area_label_1.text() == 'Error':
                    self.area_label_1.clear()
                    self.area_label_1.setText(self.area_label_1.text() + data)
                elif len(self.area_label_1.text()) == 30:
                    pass
                else:
                    self.area_label_1.setText(self.area_label_1.text() + data)
            elif data == '<':
                if self.area_label_1.text() == '0':
                    self.area_enable()
                elif len(self.area_label_1.text()) == 1:
                    self.area_label_1.setText('0')
                elif len(self.area_label_1.text()) > 0:
                    changed_data = list(self.area_label_1.text())
                    changed_data.pop()
                    sums = ''
                    for i in changed_data:
                        sums += i
                    self.area_label_1.setText(sums)
                else:
                    pass

            elif data == '.':
                if '.' in self.area_label_1.text():
                    pass
                elif self.area_label_1.text() == '0' or self.area_label_1.text() == '':
                    self.area_label_1.setText('0' + data)
                else:
                    self.area_label_1.setText(self.area_label_1.text() + data)

            elif data == 'CE':
                self.area_label_1.clear()
                self.area_label_2.clear()
            self.area_calculations(float(self.area_label_1.text()))
            self.reduce_font_converter(self.area_label_1, len(self.area_label_1.text()))
            self.reduce_font_converter(self.area_label_2, len(self.area_label_2.text()))

        except Exception as e:
            print(e)

    def area_enable(self):
        self.area_point.setEnabled(True)

    def area_disable(self):
        self.area_point.setEnabled(False)

    def area_calculations(self, value):
        try:
            self.combo_option1 = self.area_comboBox_1.currentText()
            self.combo_option2 = self.area_comboBox_2.currentText()
            get = 0
            if self.combo_option1 == 'Square millimeters':
                if self.combo_option2 == 'Square millimeters':
                    get = value
                elif self.combo_option2 == 'Square centimeters':
                    get = value / 100
                elif self.combo_option2 == 'Square meters':
                    get = value / 1000000
                elif self.combo_option2 == 'Square Kilometers':
                    get = value / 1000000000000
            elif self.combo_option1 == 'Square centimeters':
                if self.combo_option2 == 'Square millimeters':
                    get = value * 100
                elif self.combo_option2 == 'Square centimeters':
                    get = value
                elif self.combo_option2 == 'Square meters':
                    get = value / 10000
                elif self.combo_option2 == 'Square Kilometers':
                    get = value / 10000000000
            elif self.combo_option1 == 'Square meters':
                if self.combo_option2 == 'Square millimeters':
                    get = value * 1000000
                elif self.combo_option2 == 'Square centimeters':
                    get = value * 10000
                elif self.combo_option2 == 'Square meters':
                    get = value
                elif self.combo_option2 == 'Square Kilometers':
                    get = value / 1000000

            self.area_label_2.setText(str(get))
        except Exception as e:
            self.area_label_2.setText("Error")

    # Energy
    def get_energy(self, data):
        try:
            if self.ener_label_1.text() == '0':
                self.ener_label_1.setText(data)
            elif data in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                if self.ener_label_1.text() == 'Error':
                    self.ener_label_1.clear()
                    self.ener_label_1.setText(self.ener_label_1.text() + data)
                elif len(self.ener_label_1.text()) == 30:
                    pass
                else:
                    self.ener_label_1.setText(self.ener_label_1.text() + data)
            elif data == '<':
                if self.ener_label_1.text() == '0':
                    self.ener_enable()
                elif len(self.ener_label_1.text()) == 1:
                    self.ener_label_1.setText('0')
                elif len(self.ener_label_1.text()) > 0:
                    changed_data = list(self.ener_label_1.text())
                    changed_data.pop()
                    sums = ''
                    for i in changed_data:
                        sums += i
                    self.ener_label_1.setText(sums)
                else:
                    pass

            elif data == '.':
                if '.' in self.ener_label_1.text():
                    pass
                elif self.ener_label_1.text() == '0' or self.ener_label_1.text() == '':
                    self.ener_label_1.setText('0' + data)
                else:
                    self.ener_label_1.setText(self.ener_label_1.text() + data)

            elif data == 'CE':
                self.ener_label_1.clear()
                self.ener_label_2.clear()
            self.ener_calculations(float(self.ener_label_1.text()))
            self.reduce_font_converter(self.ener_label_1, len(self.ener_label_1.text()))
            self.reduce_font_converter(self.ener_label_2, len(self.ener_label_2.text()))

        except Exception as e:
            print(e)

    def ener_enable(self):
        self.ener_point.setEnabled(True)

    def ener_disable(self):
        self.ener_point.setEnabled(False)

    def ener_calculations(self, value):
        try:
            self.combo_option1 = self.ener_comboBox_1.currentText()
            self.combo_option2 = self.ener_comboBox_2.currentText()
            get = 0
            if self.combo_option1 == 'Electron volts':
                if self.combo_option2 == 'Electron volts':
                    get = value
                elif self.combo_option2 == 'Joules':
                    get = eval(str(value) + '* 1.602177e-19')
                elif self.combo_option2 == 'Kilojoules':
                    get = eval(str(value) + '* 1.602177e-22')
            elif self.combo_option1 == 'Joules':
                if self.combo_option2 == 'Electron volts':
                    get = eval(str(value) + '* 6.241509e+18')
                elif self.combo_option2 == 'Joules':
                    get = value
                elif self.combo_option2 == 'Kilojoules':
                    get = value / 1000
            elif self.combo_option1 == 'Kilojoules':
                if self.combo_option2 == 'Electron volts':
                    get = eval(str(value) + '* 6.241509e+21')
                elif self.combo_option2 == 'Joules':
                    get = value * 1000
                elif self.combo_option2 == 'Kilojoules':
                    get = value

            self.ener_label_2.setText(str(get))
        except Exception as e:
            self.ener_label_2.setText("Error")

    # temperature
    def get_temperature(self, data):
        try:
            if self.temp_label_1.text() == '0':
                self.temp_label_1.setText(data)
            elif data in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                if self.temp_label_1.text() == 'Error':
                    self.temp_label_1.clear()
                    self.temp_label_1.setText(self.temp_label_1.text() + data)
                elif len(self.temp_label_1.text()) == 30:
                    pass
                else:
                    self.temp_label_1.setText(self.temp_label_1.text() + data)
            elif data == '<':
                if self.temp_label_1.text() == '0':
                    self.temp_enable()
                elif len(self.temp_label_1.text()) == 1:
                    self.temp_label_1.setText('0')
                elif len(self.temp_label_1.text()) > 0:
                    changed_data = list(self.temp_label_1.text())
                    changed_data.pop()
                    sums = ''
                    for i in changed_data:
                        sums += i
                    self.temp_label_1.setText(sums)
                else:
                    pass

            elif data == '.':
                if '.' in self.temp_label_1.text():
                    pass
                elif self.temp_label_1.text() == '0' or self.temp_label_1.text() == '':
                    self.temp_label_1.setText('0' + data)
                else:
                    self.temp_label_1.setText(self.temp_label_1.text() + data)

            elif data == 'CE':
                self.temp_label_1.clear()
                self.temp_label_2.clear()
            self.temp_calculations(float(self.temp_label_1.text()))
            self.reduce_font_converter(self.temp_label_1, len(self.temp_label_1.text()))
            self.reduce_font_converter(self.temp_label_2, len(self.temp_label_2.text()))

        except Exception as e:
            print(e)

    def temp_enable(self):
        self.temp_point.setEnabled(True)

    def temp_disable(self):
        self.temp_point.setEnabled(False)

    def temp_calculations(self, value):
        try:
            self.combo_option1 = self.temp_comboBox_1.currentText()
            self.combo_option2 = self.temp_comboBox_2.currentText()
            get = 0
            if self.combo_option1 == 'Celsius':
                if self.combo_option2 == 'Celsius':
                    get = value
                elif self.combo_option2 == 'Fahrenheit':
                    get = value * 1.8 + 32
                elif self.combo_option2 == 'Kelvin':
                    get = value + 273.15
            elif self.combo_option1 == 'Fahrenheit':
                if self.combo_option2 == 'Celsius':
                    get = (value - 32) /1.8
                elif self.combo_option2 == 'Fahrenheit':
                    get = value
                elif self.combo_option2 == 'Kelvin':
                    get = (value + 459.67) * 5/9
            elif self.combo_option1 == 'Kelvin':
                if self.combo_option2 == 'Celsius':
                    get = value - 273.15
                elif self.combo_option2 == 'Fahrenheit':
                    get = value * 9/5 - 459.67
                elif self.combo_option2 == 'Kelvin':
                    get = value
            if type(1.1) == type(get):
                count = 0
                for i in list(str(get)):
                    count += 1
                    if i == '.':
                        count = 0
                if count > 10:
                    return round(get, 10)
                else:
                    self.temp_label_2.setText(str(get))
            else:
                self.temp_label_2.setText(str(get))
        except Exception as e:
            self.temp_label_2.setText("Error")

    # weight and mass
    def get_weightmass(self, data):
        try:
            if self.wm_label_1.text() == '0':
                self.wm_label_1.setText(data)
            elif data in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                if self.wm_label_1.text() == 'Error':
                    self.wm_label_1.clear()
                    self.wm_label_1.setText(self.wm_label_1.text() + data)
                elif len(self.wm_label_1.text()) == 30:
                    pass
                else:
                    self.wm_label_1.setText(self.wm_label_1.text() + data)
            elif data == '<':
                if self.wm_label_1.text() == '0':
                    self.wm_enable()
                elif len(self.wm_label_1.text()) == 1:
                    self.wm_label_1.setText('0')
                elif len(self.wm_label_1.text()) > 0:
                    changed_data = list(self.wm_label_1.text())
                    changed_data.pop()
                    sums = ''
                    for i in changed_data:
                        sums += i
                    self.wm_label_1.setText(sums)
                else:
                    pass

            elif data == '.':
                if '.' in self.wm_label_1.text():
                    pass
                elif self.wm_label_1.text() == '0' or self.wm_label_1.text() == '':
                    self.wm_label_1.setText('0' + data)
                else:
                    self.wm_label_1.setText(self.wm_label_1.text() + data)

            elif data == 'CE':
                self.wm_label_1.clear()
                self.wm_label_2.clear()
            self.wm_calculations(float(self.wm_label_1.text()))
            self.reduce_font_converter(self.wm_label_1, len(self.wm_label_1.text()))
            self.reduce_font_converter(self.wm_label_2, len(self.wm_label_2.text()))

        except Exception as e:
            print(e)

    def wm_enable(self):
        self.wm_point.setEnabled(True)

    def wm_disable(self):
        self.wm_point.setEnabled(False)

    def wm_calculations(self, value):
        try:
            self.combo_option1 = self.wm_comboBox_1.currentText()
            self.combo_option2 = self.wm_comboBox_2.currentText()
            get = 0
            if self.combo_option1 == 'Grams':
                if self.combo_option2 == 'Grams':
                    get = value
                elif self.combo_option2 == 'Kilograms':
                    get = value / 1000
                elif self.combo_option2 == 'Pounds':
                    get = value * 0.0022046226
            elif self.combo_option1 == 'Kilograms':
                if self.combo_option2 == 'Grams':
                    get = value * 1000
                elif self.combo_option2 == 'Kilograms':
                    get = value
                elif self.combo_option2 == 'Pounds':
                    get = value * 2.2046226218
            elif self.combo_option1 == 'Pounds':
                if self.combo_option2 == 'Grams':
                    get = value * 453.59237
                elif self.combo_option2 == 'Kilograms':
                    get = value * 0.45359237
                elif self.combo_option2 == 'Pounds':
                    get = value
            if type(1.1) == type(get):
                count = 0
                for i in list(str(get)):
                    count += 1
                    if i == '.':
                        count = 0
                if count > 10:
                    return round(get, 10)
                else:
                    self.wm_label_2.setText(str(get))
            else:
                self.wm_label_2.setText(str(get))
        except Exception as e:
            self.wm_label_2.setText("Error")

    # volume
    def get_length(self, data):
        try:
            if self.len_label_1.text() == '0':
                self.len_label_1.setText(data)
            elif data in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                if self.len_label_1.text() == 'Error':
                    self.len_label_1.clear()
                    self.len_label_1.setText(self.len_label_1.text() + data)
                elif len(self.len_label_1.text()) == 30:
                    pass
                else:
                    self.len_label_1.setText(self.len_label_1.text() + data)
            elif data == '<':
                if self.len_label_1.text() == '0':
                    self.len_enable()
                elif len(self.len_label_1.text()) == 1:
                    self.len_label_1.setText('0')
                elif len(self.len_label_1.text()) > 0:
                    changed_data = list(self.len_label_1.text())
                    changed_data.pop()
                    sums = ''
                    for i in changed_data:
                        sums += i
                    self.len_label_1.setText(sums)
                else:
                    pass

            elif data == '.':
                if '.' in self.len_label_1.text():
                    pass
                elif self.len_label_1.text() == '0' or self.len_label_1.text() == '':
                    self.len_label_1.setText('0' + data)
                else:
                    self.len_label_1.setText(self.len_label_1.text() + data)

            elif data == 'CE':
                self.len_label_1.clear()
                self.len_label_2.clear()
            self.len_calculations(float(self.len_label_1.text()))
            self.reduce_font_converter(self.len_label_1, len(self.len_label_1.text()))
            self.reduce_font_converter(self.len_label_2, len(self.len_label_2.text()))

        except Exception as e:
            print(e)

    def len_enable(self):
        self.len_point.setEnabled(True)

    def len_disable(self):
        self.len_point.setEnabled(False)

    def len_calculations(self, value):
        try:
            self.combo_option1 = self.len_comboBox_1.currentText()
            self.combo_option2 = self.len_comboBox_2.currentText()
            get = 0
            if self.combo_option1 == 'Nanometers':
                if self.combo_option2 == 'Nanometers':
                    get = value
                elif self.combo_option2 == 'Millimeters':
                    get = value / 1000000
                elif self.combo_option2 == 'Centimeters':
                    get = value / 10000000
                elif self.combo_option2 == 'Meters':
                    get = value / 1000000000
                elif self.combo_option2 == 'Kilometers':
                    get = value / 1000000000000

            elif self.combo_option1 == 'Millimeters':
                if self.combo_option2 == 'Nanometers':
                    get = value * 1000000
                elif self.combo_option2 == 'Millimeters':
                    get = value
                elif self.combo_option2 == 'Centimeters':
                    get = value / 10
                elif self.combo_option2 == 'Meters':
                    get = value / 1000
                elif self.combo_option2 == 'Kilometers':
                    get = value / 1000000
            elif self.combo_option1 == 'Centimeters':
                if self.combo_option2 == 'Nanometers':
                    get = value * 10000000
                elif self.combo_option2 == 'Millimeters':
                    get = value * 10
                elif self.combo_option2 == 'Centimeters':
                    get = value
                elif self.combo_option2 == 'Meters':
                    get = value / 100
                elif self.combo_option2 == 'Kilometers':
                    get = value / 100000
            elif self.combo_option1 == 'Meters':
                if self.combo_option2 == 'Nanometers':
                    get = value * 1000000000
                elif self.combo_option2 == 'Millimeters':
                    get = value * 1000
                elif self.combo_option2 == 'Centimeters':
                    get = value * 100
                elif self.combo_option2 == 'Meters':
                    get = value
                elif self.combo_option2 == 'Kilometers':
                    get = value / 1000
            elif self.combo_option1 == 'Kilometers':
                if self.combo_option2 == 'Nanometers':
                    get = value * 1000000000000
                elif self.combo_option2 == 'Millimeters':
                    get = value * 1000000
                elif self.combo_option2 == 'Centimeters':
                    get = value * 100000
                elif self.combo_option2 == 'Meters':
                    get = value * 1000
                elif self.combo_option2 == 'Kilometers':
                    get = value

            if type(1.1) == type(get):
                count = 0
                for i in list(str(get)):
                    count += 1
                    if i == '.':
                        count = 0
                if count > 15:
                    return round(get, 10)
                else:
                    self.len_label_2.setText(str(get))
            else:
                self.len_label_2.setText(str(get))
        except Exception as e:
            self.len_label_2.setText("Error")

    def get_volume(self, data):
        try:
            if self.vol_label_1.text() == '0':
                self.vol_label_1.setText(data)
            elif data in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                if self.vol_label_1.text() == 'Error':
                    self.vol_label_1.clear()
                    self.vol_label_1.setText(self.vol_label_1.text() + data)
                elif len(self.vol_label_1.text()) == 30:
                    pass
                else:
                    self.vol_label_1.setText(self.vol_label_1.text() + data)
            elif data == '<':
                if self.vol_label_1.text() == '0':
                    self.vol_enable()
                elif len(self.vol_label_1.text()) == 1:
                    self.vol_label_1.setText('0')
                elif len(self.vol_label_1.text()) > 0:
                    changed_data = list(self.vol_label_1.text())
                    changed_data.pop()
                    sums = ''
                    for i in changed_data:
                        sums += i
                    self.vol_label_1.setText(sums)
                else:
                    pass

            elif data == '.':
                if '.' in self.vol_label_1.text():
                    pass
                elif self.vol_label_1.text() == '0' or self.vol_label_1.text() == '':
                    self.vol_label_1.setText('0' + data)
                else:
                    self.vol_label_1.setText(self.vol_label_1.text() + data)

            elif data == 'CE':
                self.vol_label_1.clear()
                self.vol_label_2.clear()
            self.vol_calculations(float(self.vol_label_1.text()))
            self.reduce_font_converter(self.vol_label_1, len(self.vol_label_1.text()))
            self.reduce_font_converter(self.vol_label_2, len(self.vol_label_2.text()))

        except Exception as e:
            print(e)

    def vol_enable(self):
        self.vol_point.setEnabled(True)


    def vol_disable(self):
        self.vol_point.setEnabled(False)

    def vol_calculations(self, value):
        try:
            self.combo_option1 = self.vol_comboBox_1.currentText()
            self.combo_option2 = self.vol_comboBox_2.currentText()
            get = 0
            if self.combo_option1 == 'Mililiters':
                if self.combo_option2 == 'Mililiters':
                    get = value
                elif self.combo_option2 == 'Liters':
                    get = value / 1000
                elif self.combo_option2 == 'Cubic meters':
                    get = value / 1000000
            elif self.combo_option1 == 'Liters':
                if self.combo_option2 == 'Mililiters':
                    get = value * 1000
                elif self.combo_option2 == 'Liters':
                    get = value
                elif self.combo_option2 == 'Cubic meters':
                    get = value / 1000
            elif self.combo_option1 == 'Cubic meters':
                if self.combo_option2 == 'Mililiters':
                    get = value * 1000000
                elif self.combo_option2 == 'Liters':
                    get = value * 1000
                elif self.combo_option2 == 'Cubic meters':
                    get = value
            if type(1.1) == type(get):
                count = 0
                for i in list(str(get)):
                    count += 1
                    if i == '.':
                        count = 0
                if count > 10:
                    return round(get, 10)
                else:
                    self.vol_label_2.setText(str(get))
            else:
                self.vol_label_2.setText(str(get))
        except Exception as e:
            self.vol_label_2.setText("Error")

    # programmer
    def get_programmer(self, data):
        try:
            if self.p_label_2.text() != 'Error':
                self.p_enable()
            if self.p_label_2.text() == '0' and data not in ['+', '-', '*', '/', '=', '<', 'CE', '%', '+_-', '<<','>>', '(', ')']:
                self.p_label_2.setText(data)
                # converting value into hex, decimal, oct and bin
                self.p_label_hex_val.setText(str(hex(int(self.p_label_2.text()))))
                self.p_label_dec_val.setText(str(self.p_label_2.text()))
                self.p_label_oct_val.setText(str(oct(int(self.p_label_2.text()))))
                self.p_label_bin_val.setText(str(bin(int(self.p_label_2.text()))))
            elif data in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                if self.p_label_2.text() == 'Error':
                    self.p_label_2.clear()
                    self.p_label_2.setText(self.p_label_2.text() + data)
                elif len(self.p_label_2.text()) == 30:
                    pass
                else:
                    self.p_label_2.setText(self.p_label_2.text() + data)
                #converting value into hex, decimal, oct and bin
                self.p_label_hex_val.setText(str(hex(int(self.p_label_2.text()))))
                self.p_label_dec_val.setText(str(self.p_label_2.text()))
                self.p_label_oct_val.setText(str(oct(int(self.p_label_2.text()))))
                self.p_label_bin_val.setText(str(bin(int(self.p_label_2.text()))))
            elif data in ['+', '-', '*', '/', '<<','>>', '%']:
                if self.p_label_3.text() == '':
                    self.p_label_3.setText(self.p_label_2.text() + data)
                    self.p_label_2.clear()
                elif self.p_label_2.text() != '' and list(self.p_label_3.text()).pop() not in ['+', '-', '*', '/', '<<','>>', '(', ')', '%']:
                    self.p_label_3.setText(self.p_label_2.text() + data)
                else:
                    check_operator2 = list(self.p_label_3.text()).pop()
                    if self.p_label_2.text() != '' and check_operator2 not in ['0', '1', '2', '3', '4', '5', '6', '7', '8',
                                                                             '9']:
                        self.p_label_3.setText(self.p_label_3.text() + self.p_label_2.text() + data)
                    elif check_operator2 != data and check_operator2 not in ['0', '1', '2', '3', '4', '5', '6', '7', '8',
                                                                             '9', '(', ')']:
                        self.p_label_3.setText(self.p_label_3.text()[:-1] + data)  # change operator
                    elif check_operator2 in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ')']:
                        self.p_label_3.setText(self.p_label_3.text() + data + self.p_label_2.text())
                self.p_label_2.clear()
            elif data == '<':
                if self.p_label_2.text() == 'E':
                    self.p_enable()
                if self.p_label_2.text() == '0':
                    self.p_enable()
                elif self.p_label_2.text() in ['-0', '-1', '-2', '-3', '-4', '-5', '-6', '-7', '-8', '-9']:
                    self.p_label_2.setText('0')
                elif len(self.p_label_2.text()) == 1:
                    self.p_label_2.setText('0')
                elif len(self.p_label_2.text()) > 0:
                    changed_data = list(self.p_label_2.text())
                    changed_data.pop()
                    sums = ''
                    for i in changed_data:
                        sums += i
                    self.p_label_2.setText(sums)
                else:
                    pass
            elif data == '=':
                if len([x for x in list(self.p_label_3.text()) if x == '(']) > 0 and (
                        len([x for x in list(self.p_label_3.text()) if x == '(']) > len(
                    [x for x in list(self.p_label_3.text()) if x == ')'])):
                    difference = len([x for x in list(self.p_label_3.text()) if x == '(']) - len(
                        [x for x in list(self.p_label_3.text()) if x == ')'])
                    self.p_label_3.setText(self.p_label_3.text() + self.p_label_2.text())
                    print("hbjsbjds")
                    try:
                        for i in range(difference):
                            self.p_label_3.setText(self.p_label_3.text() + ')')
                        self.p_label_2.clear()

                    except Exception as e:
                        print(e)
                if self.p_label_3.text() == '':
                    print('shjfs')
                    self.p_label_2.setText(self.p_label_2.text())
                elif self.p_label_3.text() != '':
                    print('fsd')
                    if list(self.p_label_3.text()).pop() in ['+', '-', '*', '/', '<','>', '%'] and self.p_label_2.text() == '':
                        print("yess")
                        string_without_sign = list(self.p_label_3.text())
                        string_without_sign.pop()
                        string_sum = ''
                        for i in string_without_sign:
                            string_sum += i
                        result = self.p_calculations(string_sum)
                        self.p_label_2.setText(str(result))
                    elif list(self.p_label_3.text()).pop() in ['+', '-', '*', '/', '<','>', '%']:
                        print("new_str")
                        new_str = self.p_label_3.text() + self.p_label_2.text()
                        self.p_label_3.setText(new_str)
                        result = self.p_calculations(new_str)
                        self.p_label_2.setText(str(result))
                    elif self.p_label_3.text() != '' and self.p_label_2.text() == '':
                        print("no")
                        result = self.p_calculations(self.p_label_3.text())
                        self.p_label_2.setText(str(result))
                self.p_label_3.clear()
                #     converting value into hex, decimal, oct and bin
                self.p_label_hex_val.setText(str(hex(int(self.p_label_2.text()))))
                self.p_label_dec_val.setText(str(self.p_label_2.text()))
                self.p_label_oct_val.setText(str(oct(int(self.p_label_2.text()))))
                self.p_label_bin_val.setText(str(bin(int(self.p_label_2.text()))))


            elif data == '+_-':
                if self.p_label_2.text() != '':
                    if self.p_label_2.text() not in ['0', '0.0']:
                        first_letter = list(self.p_label_2.text())[0]
                        minus = '-'
                        if first_letter != minus:
                            self.p_label_2.setText(minus + self.p_label_2.text())
                        elif first_letter == minus:
                            self.p_label_2.setText(self.p_label_2.text()[1:])
                    else:
                        pass

            elif data == 'CE':

                if self.p_label_2.text() != '0':
                    self.p_label_2.clear()
                    self.p_label_2.setText('0')
                    self.p_enable()
                else:
                    self.p_label_3.clear()
            elif data == '(':
                try:
                    if self.p_label_3.text() == '':
                        self.p_label_3.setText(data)
                    else:
                        if list(self.p_label_3.text()).pop() == ')':
                            self.p_label_3.setText(data)
                        if list(self.p_label_3.text()).pop() in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ')']:
                            self.p_label_3.setText(self.p_label_3.text() + '*' + '(')
                        else:
                            self.p_label_3.setText(self.p_label_3.text() + data)

                except Exception as e:
                    print(e)

            elif data == ')':
                try:
                    if self.p_label_3.text() != '':
                        if len([x for x in list(self.p_label_3.text()) if x == '(']) != len(
                                [x for x in list(self.p_label_3.text()) if x == ')']):
                            self.p_label_3.setText(self.p_label_3.text() + self.p_label_2.text() + data)
                            self.p_label_2.clear()

                except Exception as e:
                    print(e)
            self.reduce_font(self.p_label_2, len(self.p_label_2.text()))


        except Exception as e:
            print(e)

    def p_enable(self):
        self.p_plus.setEnabled(True)
        self.p_minus.setEnabled(True)
        self.p_multiply.setEnabled(True)
        self.p_divide.setEnabled(True)
        self.p_point.setEnabled(True)
        self.p_plus_minus.setEnabled(True)
        self.p_per.setEnabled(True)
        self.p_back.setEnabled(True)

    def p_disable(self):
        self.p_plus.setEnabled(False)
        self.p_minus.setEnabled(False)
        self.p_multiply.setEnabled(False)
        self.p_divide.setEnabled(False)
        self.p_point.setEnabled(False)
        self.p_plus_minus.setEnabled(False)
        self.p_per.setEnabled(False)
        self.p_back.setEnabled(False)

    def p_calculations(self, value):
        try:
            get = eval(value)
            if type(1.1) == type(get):
                return math.trunc(get)
            else:
                return get
        except ZeroDivisionError as e:
            self.p_label_3.clear()
            self.disable()
            return 'Error'
        except Exception as e:
            return 'Error'
    # Scientific window functions
    def get_scientific(self, data):
        if self.s_label_2.text() != 'Error':
            self.s_enable()
        if self.s_label_2.text() == '0' and data not in ['+', '-', '*', '/', '=', '<', '.', 'CE', '%', '1/x',
                                                       'SquareRoot', 'x_square', '+_-', 'pie', 'e', 'absolute_x', 'exp',
                                                       'per', '(', ')', 'n_factorial', '**', 'ten_x', 'log', 'ln']:
            self.s_label_2.setText(data)
        elif data in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            if self.s_label_2.text() == 'Error':
                self.s_label_2.clear()
                self.s_label_2.setText(data)
            elif len(self.s_label_2.text()) == 30:
                pass
            else:
                self.s_label_2.setText(self.s_label_2.text() + data)
        elif data in ['+', '-', '*', '/', '%', '**']:
            if self.s_label_3.text() == '':
                self.s_label_3.setText(self.s_label_2.text() + data)
                self.s_label_2.clear()
            elif self.s_label_2.text() != '' and list(self.s_label_3.text()).pop() not in ['+', '-', '*', '/', '%', '**', '(', ')']:

                self.s_label_3.setText(self.s_label_2.text() + data)
            else:
                check_operator2 = list(self.s_label_3.text()).pop()
                if self.s_label_2.text() != '' and check_operator2 not in ['0', '1', '2', '3', '4', '5', '6', '7', '8',
                                                                         '9']:
                    self.s_label_3.setText(self.s_label_3.text() + self.s_label_2.text() + data)
                elif check_operator2 != data and check_operator2 not in ['0', '1', '2', '3', '4', '5', '6', '7', '8',
                                                                         '9', '(', ')']:
                    self.s_label_3.setText(self.s_label_3.text()[:-1] + data)  # change operator
                elif check_operator2 in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ')']:
                    self.s_label_3.setText(self.s_label_3.text() + data + self.s_label_2.text())
            self.s_label_2.clear()
        elif data == '<':
            if self.s_label_2.text() == 'E':
                self.s_enable()
            if self.s_label_2.text() == '0':
                self.s_enable()
            elif self.s_label_2.text() in ['-0', '-1', '-2', '-3', '-4', '-5', '-6', '-7', '-8', '-9']:
                self.s_label_2.setText('0')
            elif len(self.s_label_2.text()) == 1:
                self.s_label_2.setText('0')
            elif len(self.s_label_2.text()) > 0:
                changed_data = list(self.s_label_2.text())
                changed_data.pop()
                sums = ''
                for i in changed_data:
                    sums += i
                self.s_label_2.setText(sums)
            else:
                pass
        elif data == '=':
            if len([x for x in list(self.s_label_3.text()) if x == '(']) > 0 and (
                    len([x for x in list(self.s_label_3.text()) if x == '(']) > len(
                    [x for x in list(self.s_label_3.text()) if x == ')'])):
                difference = len([x for x in list(self.s_label_3.text()) if x == '(']) - len(
                    [x for x in list(self.s_label_3.text()) if x == ')'])
                self.s_label_3.setText(self.s_label_3.text() + self.s_label_2.text())
                print("hbjsbjds")
                try:
                    for i in range(difference):
                        self.s_label_3.setText(self.s_label_3.text() + ')')
                    self.s_label_2.clear()

                except Exception as e:
                    print(e)
            try:
                if self.s_label_3.text() == '':
                    self.s_label_2.setText(self.s_label_2.text())
                elif self.s_label_3.text() != '':

                    if list(self.s_label_3.text()).pop() in ['+', '-', '*', '/', '%', '**'] and self.s_label_2.text() == '':
                        string_without_sign = list(self.s_label_3.text())

                        string_without_sign.pop()
                        string_sum = ''
                        for i in string_without_sign:
                            string_sum += i
                        result = self.s_calculations(string_sum)
                        self.s_label_2.setText(str(result))
                    elif list(self.s_label_3.text()).pop() in ['+', '-', '*', '/', '%', '**']:
                        new_str = self.s_label_3.text() + self.s_label_2.text()
                        self.s_label_3.setText(new_str)
                        result = self.s_calculations(new_str)
                        self.s_label_2.setText(str(result))
                    elif list(self.s_label_3.text()).pop() == ')':
                        result = self.s_calculations(self.s_label_3.text())
                        self.s_label_2.setText(str(result))
                    elif self.s_label_3.text() != '' and self.label_2.text() == '':
                        result = self.s_calculations(self.s_label_3.text())
                        self.s_label_2.setText(str(result))


                # self.s_label_3.clear()
            except Exception as e:
                print(e)
        elif data == '.':
            if '.' in self.s_label_2.text():
                pass
            elif self.s_label_2.text() == '0' or self.s_label_2.text() == '':
                self.s_label_2.setText('0' + data)
            else:
                self.s_label_2.setText(self.s_label_2.text() + data)
        elif data == 'per':
            if self.s_label_2.text() != '':
                new_str = self.s_label_2.text() + '/' + '100'
                result = self.s_calculations(new_str)
                self.s_label_2.setText(str(result))
        elif data == '1/x':
            if self.s_label_2.text() != '':
                new_str = '1' + '/' + self.s_label_2.text()
                result = self.s_calculations(new_str)
                self.s_label_2.setText(str(result))
        elif data == 'x_square':
            if self.s_label_2.text() != '':
                new_str = self.s_label_2.text() + '**' + '2'
                result = self.s_calculations(new_str)
                self.s_label_2.setText(str(result))
        elif data == 'SquareRoot':
            if self.s_label_2.text() == '':
                pass
            else:
                try:
                    self.s_label_2.setText(str(round(math.sqrt(eval(self.s_label_2.text())), 4)))
                except ValueError as e:
                    self.s_label_3.clear()
                    self.s_disable()
                    self.s_label_2.setText('Error')
        elif data == '+_-':
            if self.s_label_2.text() != '':
                if self.s_label_2.text() not in ['0', '0.0']:
                    first_letter = list(self.s_label_2.text())[0]
                    minus = '-'
                    if first_letter != minus:
                        self.s_label_2.setText(minus + self.s_label_2.text())
                    elif first_letter == minus:
                        self.s_label_2.setText(self.s_label_2.text()[1:])
                else:
                    pass
        elif data == 'CE':
            if self.s_label_2.text() != '0':
                self.s_label_2.clear()
                self.s_label_2.setText('0')
                self.s_enable()
            else:
                self.s_label_3.clear()
        elif data == 'pie':
            self.s_label_2.clear()
            self.s_label_2.setText(str(math.pi))
        elif data == 'e':
            self.s_label_2.clear()
            self.s_label_2.setText(str(math.e))
        elif data == 'ln':
            try:
                if self.s_label_2.text() != '':
                    new_str = str(math.log(float(self.s_label_2.text())))
                    self.s_label_2.setText(str(new_str))
            except ValueError:
                self.s_label_2.clear()
                self.s_label_2.setText('Error')

        elif data == 'absolute_x':
            result = float(self.s_label_2.text())
            self.s_label_2.clear()
            self.s_label_2.setText(str(abs(result)))
        elif data == 'n_factorial':
            try:
                result = float(self.s_label_2.text())
                if len(self.s_label_2.text())>3:
                    self.s_label_2.clear()
                    self.s_label_2.setText('Overflow')
                else:
                    self.s_label_2.clear()
                    self.s_label_2.setText(str(math.factorial(result)))
            except Exception:
                self.s_label_2.clear()
                self.s_label_2.setText('Error')
        elif data == 'exp':
            try:
                result = self.s_label_2.text()
                result = '%.2E' % Decimal(result)
                self.s_label_2.clear()
                self.s_label_2.setText(result)
            except Exception:
                self.s_label_2.clear()
                self.s_label_2.setText('Error')
        elif data == 'log':
            try:
                result = float(self.s_label_2.text())
                self.s_label_2.clear()
                self.s_label_2.setText(str(math.log10(result)))
            except Exception:
                self.s_label_2.clear()
                self.s_label_2.setText('Error')
        elif data == 'ten_x':
            try:
                result = float(self.s_label_2.text())
                self.s_label_2.clear()
                self.s_label_2.setText(str(pow(10, result)))
            except Exception:
                self.s_label_2.clear()
                self.s_label_2.setText('Error')
        elif data == '(':
            try:
                if self.s_label_3.text() == '':
                    self.s_label_3.setText(data)
                else:
                    if list(self.s_label_3.text()).pop() == ')':
                        self.s_label_3.setText(data)
                    if list(self.s_label_3.text()).pop() in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ')']:
                        self.s_label_3.setText(self.s_label_3.text() + '*' + '(')
                    else:
                        self.s_label_3.setText(self.s_label_3.text() + data)

            except Exception as e:
                print(e)

        elif data == ')':
            try:
                if self.s_label_3.text() != '':
                    if len([x for x in list(self.s_label_3.text()) if x =='(']) != len([x for x in list(self.s_label_3.text()) if x ==')']):
                        self.s_label_3.setText(self.s_label_3.text() + self.s_label_2.text() + data)
                        self.s_label_2.clear()

            except Exception as e:
                print(e)



        self.reduce_font(self.s_label_2, len(self.s_label_2.text()))

    # font changing functions
    def reduce_font_converter(self, obj, label_length):
        font = QtGui.QFont()
        if label_length < 9:
            font.setPointSize(15)
            obj.setFont(font)
        elif label_length>21 and label_length<=35:
            font.setPointSize(10)
            obj.setFont(font)
        elif label_length>35:
            result = obj.text()
            result = '%.2E' % Decimal(result)
            obj.clear()
            obj.setText(result)

    def reduce_font(self, obj, label_length):
        font = QtGui.QFont()
        if label_length < 9:
            font.setPointSize(28)
            obj.setFont(font)
        elif label_length > 10 and label_length <= 14:
            font.setPointSize(22)
            obj.setFont(font)
        elif label_length > 14 and label_length<=21:
            font.setPointSize(16)
            obj.setFont(font)
        elif label_length>21 and label_length<=35:
            font.setPointSize(10)
            obj.setFont(font)
        elif label_length>35:
            result = obj.text()
            result = '%.2E' % Decimal(result)
            obj.clear()
            obj.setText(result)


    def s_enable(self):
        self.s_plus.setEnabled(True)
        self.s_minus.setEnabled(True)
        self.s_multiply.setEnabled(True)
        self.s_divide.setEnabled(True)
        self.s_point.setEnabled(True)
        self.s_plus_minus.setEnabled(True)
        self.s_per.setEnabled(True)
        self.s_back.setEnabled(True)
        self.s_one_by_x.setEnabled(True)
        self.s_x_square.setEnabled(True)
        self.s_root.setEnabled(True)

    def s_disable(self):
        self.s_plus.setEnabled(False)
        self.s_minus.setEnabled(False)
        self.s_multiply.setEnabled(False)
        self.s_divide.setEnabled(False)
        self.s_point.setEnabled(False)
        self.s_plus_minus.setEnabled(False)
        self.s_per.setEnabled(False)
        self.s_back.setEnabled(False)
        self.s_one_by_x.setEnabled(False)
        self.s_x_square.setEnabled(False)
        self.s_root.setEnabled(False)

    def s_calculations(self, value):
        try:
            get = eval(value)
            if type(1.1) == type(get):
                count = 0
                for i in list(str(get)):
                    count += 1
                    if i == '.':
                        count = 0
                if count > 4:
                    return round(get, 4)
                else:
                    return get
            else:
                return get
        except ZeroDivisionError as e:
            self.s_label_3.clear()
            self.s_disable()
            return 'Error'
        except Exception as e:
            return 'Error'

    def get(self, data):
        try:

            if self.label_2.text() != 'Error':
                self.enable()
            if self.label_2.text() == '0' and data not in ['+', '-', '*', '/', '=', '<', '.', 'C', 'CE', '%', '1/x',
                                                           'SquareRoot', 'x_square', '+_-']:
                self.label_2.setText(data)
            elif data in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                if self.label_2.text() == 'Error':
                    self.label_2.clear()
                    self.label_2.setText(self.label_2.text() + data)
                elif len(self.label_2.text()) == 30:
                    pass
                else:
                    self.label_2.setText(self.label_2.text() + data)
            elif data in ['+', '-', '*', '/']:
                if self.label_3.text() == '':
                    self.label_3.setText(self.label_2.text() + data)
                    self.label_2.clear()
                elif self.label_2.text() != '' and list(self.label_3.text()).pop() not in ['+', '-', '*', '/']:
                    self.label_3.setText(self.label_2.text() + data)
                else:
                    check_operator2 = list(self.label_3.text()).pop()
                    if self.label_2.text() != '' and check_operator2 not in ['0', '1', '2', '3', '4', '5', '6', '7', '8',
                                                                             '9']:
                        self.label_3.setText(self.label_3.text() + self.label_2.text() + data)
                    elif check_operator2 != data and check_operator2 not in ['0', '1', '2', '3', '4', '5', '6', '7', '8',
                                                                             '9']:
                        self.label_3.setText(self.label_3.text()[:-1] + data)  # change operator
                    elif check_operator2 in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                        self.label_3.setText(self.label_3.text() + data + self.label_2.text())
                self.label_2.clear()
            elif data == '<':
                if self.label_2.text() == 'E':
                    self.enable()
                if self.label_2.text() == '0':
                    self.enable()
                elif self.label_2.text() in ['-0', '-1', '-2', '-3', '-4', '-5', '-6', '-7', '-8', '-9']:
                    self.label_2.setText('0')
                elif len(self.label_2.text()) == 1:
                    self.label_2.setText('0')
                elif len(self.label_2.text()) > 0:
                    changed_data = list(self.label_2.text())
                    changed_data.pop()
                    sums = ''
                    for i in changed_data:
                        sums += i
                    self.label_2.setText(sums)
                else:
                    pass
            elif data == '=':
                if self.label_3.text() == '':
                    self.label_2.setText(self.label_2.text())
                elif self.label_3.text() != '':
                    if list(self.label_3.text()).pop() in ['+', '-', '*', '/'] and self.label_2.text() == '':
                        string_without_sign = list(self.label_3.text())
                        string_without_sign.pop()
                        string_sum = ''
                        for i in string_without_sign:
                            string_sum += i
                        result = self.calculations(string_sum)
                        self.label_2.setText(str(result))
                    elif list(self.label_3.text()).pop() in ['+', '-', '*', '/']:
                        new_str = self.label_3.text() + self.label_2.text()
                        self.label_3.setText(new_str)
                        result = self.calculations(new_str)
                        self.label_2.setText(str(result))
                    elif self.label_3.text() != '' and self.label_2.text() == '':
                        result = self.calculations(self.label_3.text())
                        self.label_2.setText(str(result))
                self.label_3.clear()
            elif data == '.':
                if '.' in self.label_2.text():
                    pass
                elif self.label_2.text() == '0' or self.label_2.text() == '':
                    self.label_2.setText('0' + data)
                else:
                    self.label_2.setText(self.label_2.text() + data)
            elif data == '%':
                if self.label_2.text() != '':
                    new_str = self.label_2.text() + '/' + '100'
                    result = self.calculations(new_str)
                    self.label_2.setText(str(result))
            elif data == '1/x':
                if self.label_2.text() != '':
                    new_str = '1' + '/' + self.label_2.text()
                    result = self.calculations(new_str)
                    self.label_2.setText(str(result))
            elif data == 'x_square':
                if self.label_2.text() != '':
                    new_str = self.label_2.text() + '**' + '2'
                    result = self.calculations(new_str)
                    self.label_2.setText(str(result))
            elif data == 'SquareRoot':
                if self.label_2.text() == '':
                    pass
                else:
                    try:
                        self.label_2.setText(str(round(math.sqrt(eval(self.label_2.text())), 4)))
                    except ValueError as e:
                        self.label_3.clear()
                        self.disable()
                        self.label_2.setText('Error')
            elif data == '+_-':
                if self.label_2.text() != '':
                    if self.label_2.text() not in ['0', '0.0']:
                        first_letter = list(self.label_2.text())[0]
                        minus = '-'
                        if first_letter != minus:
                            self.label_2.setText(minus + self.label_2.text())
                        elif first_letter == minus:
                            self.label_2.setText(self.label_2.text()[1:])
                    else:
                        pass
            elif data == 'C':
                self.label_2.clear()
                self.label_3.clear()
                self.label_2.setText('0')
                self.enable()
            elif data == 'CE':
                self.label_2.clear()
                self.label_2.setText('0')
                self.enable()
            self.reduce_font(self.label_2, len(self.label_2.text()))

        except Exception as e:
            print(e)

    def enable(self):
        self.plus.setEnabled(True)
        self.minus.setEnabled(True)
        self.multiply.setEnabled(True)
        self.divide.setEnabled(True)
        self.point.setEnabled(True)
        self.plus_minus.setEnabled(True)
        self.per.setEnabled(True)
        self.back.setEnabled(True)
        self.one_by_x.setEnabled(True)
        self.x_square.setEnabled(True)
        self.root.setEnabled(True)

    def disable(self):
        self.plus.setEnabled(False)
        self.minus.setEnabled(False)
        self.multiply.setEnabled(False)
        self.divide.setEnabled(False)
        self.point.setEnabled(False)
        self.plus_minus.setEnabled(False)
        self.per.setEnabled(False)
        self.back.setEnabled(False)
        self.one_by_x.setEnabled(False)
        self.x_square.setEnabled(False)
        self.root.setEnabled(False)

    def calculations(self, value):
        try:
            get = eval(value)
            if type(1.1) == type(get):
                count = 0
                for i in list(str(get)):
                    count += 1
                    if i == '.':
                        count = 0
                if count > 4:
                    return round(get, 4)
                else:
                    return get
            else:
                return get
        except ZeroDivisionError as e:
            self.label_3.clear()
            self.disable()
            return 'Error'
        except Exception as e:
            return 'Error'

    def keyPressEvent(self, event):
        if event.key() == 48:  # 0
            if MyMainWindow.winFlag == 'n':
                self.get('0')
            elif MyMainWindow.winFlag == 's':
                self.get_scientific('0')
        elif event.key() == 49:  # 1
            if MyMainWindow.winFlag == 'n':
                self.get('1')
            elif MyMainWindow.winFlag == 's':
                self.get_scientific('1')
        elif event.key() == 50:  # 2
            if MyMainWindow.winFlag == 'n':
                self.get('2')
            elif MyMainWindow.winFlag == 's':
                self.get_scientific('2')
        elif event.key() == 51:  # 3
            if MyMainWindow.winFlag == 'n':
                self.get('3')
            elif MyMainWindow.winFlag == 's':
                self.get_scientific('3')
        elif event.key() == 52:  # 4
            if MyMainWindow.winFlag == 'n':
                self.get('4')
            elif MyMainWindow.winFlag == 's':
                self.get_scientific('4')
        elif event.key() == 53:  # 5
            if MyMainWindow.winFlag == 'n':
                self.get('5')
            elif MyMainWindow.winFlag == 's':
                self.get_scientific('5')
        elif event.key() == 54:  # 6
            if MyMainWindow.winFlag == 'n':
                self.get('6')
            elif MyMainWindow.winFlag == 's':
                self.get_scientific('6')
        elif event.key() == 55:  # 7
            if MyMainWindow.winFlag == 'n':
                self.get('7')
            elif MyMainWindow.winFlag == 's':
                self.get_scientific('7')
        elif event.key() == 56:  # 8
            if MyMainWindow.winFlag == 'n':
                self.get('8')
            elif MyMainWindow.winFlag == 's':
                self.get_scientific('8')
        elif event.key() == 57:  # 9
            if MyMainWindow.winFlag == 'n':
                self.get('9')
            elif MyMainWindow.winFlag == 's':
                self.get_scientific('9')
        elif event.key() == 43:  # +
            if MyMainWindow.winFlag == 'n':
                self.get('+')
            elif MyMainWindow.winFlag == 's':
                self.get_scientific('+')
        elif event.key() == 45:  # -
            if MyMainWindow.winFlag == 'n':
                self.get('-')
            elif MyMainWindow.winFlag == 's':
                self.get_scientific('-')
        elif event.key() == 42:  # *
            if MyMainWindow.winFlag == 'n':
                self.get('*')
            elif MyMainWindow.winFlag == 's':
                self.get_scientific('*')
        elif event.key() == 47:  # /
            if MyMainWindow.winFlag == 'n':
                self.get('/')
            elif MyMainWindow.winFlag == 's':
                self.get_scientific('/')
        elif event.key() == 37:  # %
            if MyMainWindow.winFlag == 'n':
                self.get('%')
            elif MyMainWindow.winFlag == 's':
                self.get_scientific('%')
        elif event.key() == 16777219:  # Backspace
            if MyMainWindow.winFlag == 'n':
                self.get('<')
            elif MyMainWindow.winFlag == 's':
                self.get_scientific('<')
        elif event.key() == QtCore.Qt.Key_Enter:  # enter (=)
            if MyMainWindow.winFlag == 'n':
                self.get('=')
            elif MyMainWindow.winFlag == 's':
                self.get_scientific('=')
        elif event.key() == 61:
            if MyMainWindow.winFlag == 'n':
                self.get('=')
            elif MyMainWindow.winFlag == 's':
                self.get_scientific('=')
        elif event.key() == 46:  # . (point)
            if MyMainWindow.winFlag == 'n':
                self.get('.')
            elif MyMainWindow.winFlag == 's':
                self.get_scientific('.')


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    win = MyMainWindow()
    win.show()

    sys.exit(app.exec_())


