import sys
import json
import os
import time
import numpy
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout,QHBoxLayout, QGraphicsOpacityEffect, QMainWindow
from PySide6.QtCore import QPropertyAnimation, Qt, QEasingCurve, QRegularExpression
from PySide6.QtGui import QRegularExpressionValidator
from decimal import Decimal, getcontext, ROUND_DOWN

import cmath
import math
from translator import Translator
from mywindow import Ui_MainWindow

class Animation(QPushButton):
    def __init__(self, text, parent=None):
        super().__init__(text, parent)
        self.opacity_effect = QGraphicsOpacityEffect(self)
        self.setGraphicsEffect(self.opacity_effect)
        self.opacity_animation = QPropertyAnimation(self.opacity_effect, b"opacity")
        self.opacity_animation.setDuration(500)
        self.opacity_animation.setEasingCurve(QEasingCurve.Type.OutQuad)
        self.opacity_effect.setOpacity(0.0)

    def fadeIn(self):
        self.opacity_animation.setStartValue(0.0)
        self.opacity_animation.setEndValue(1.0)
        self.opacity_animation.start()

    def fadeOut(self):
        self.opacity_animation.setStartValue(1.0)
        self.opacity_animation.setEndValue(0.0)
        self.opacity_animation.start()


class Root(QMainWindow):
    def __init__(self):
        super(Root, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.translator = Translator()
        self.languages = {}
        self.bts = [self.ui.b_i, self.ui.b_plus, self.ui.b_minus, self.ui.rt]
        self.reg = QRegularExpression("-?([1-9][0-9]*|0|([1-9][0-9]*).[0-9][0-9]*)[+-]?([1-9][0-9]*|0|([1-9][0-9]*).[0-9][0-9]*)?j?$")
        self.reg2 = QRegularExpression("(?:[1-9]|1[0-9]|20)$")
        getcontext().prec = 50
        self.mode = self.ui.comboBox.currentText()
        self.ui.b_0.clicked.connect(lambda: self.add_digit('0'))
        self.ui.b_1.clicked.connect(lambda: self.add_digit('1'))
        self.ui.b_2.clicked.connect(lambda: self.add_digit('2'))
        self.ui.b_3.clicked.connect(lambda: self.add_digit('3'))
        self.ui.b_4.clicked.connect(lambda: self.add_digit('4'))
        self.ui.b_5.clicked.connect(lambda: self.add_digit('5'))
        self.ui.b_6.clicked.connect(lambda: self.add_digit('6'))
        self.ui.b_7.clicked.connect(lambda: self.add_digit('7'))
        self.ui.b_8.clicked.connect(lambda: self.add_digit('8'))
        self.ui.b_9.clicked.connect(lambda: self.add_digit('9'))
        self.ui.b_i.clicked.connect(lambda: self.add_digit('j'))
        self.ui.b_plus.clicked.connect(lambda: self.add_digit('+'))
        self.ui.b_minus.clicked.connect(lambda: self.add_digit('-'))
        self.ui.b_dot.clicked.connect(lambda: self.add_dot())
        self.ui.root_8.clicked.connect(lambda: self.clear())
        self.ui.root.clicked.connect(lambda: self.root())
        self.ui.root_9.clicked.connect(lambda: self.dell())
        self.ui.root_2.clicked.connect(lambda: self.change_of_scene(self.bts))
        self.ui.root_7.clicked.connect(lambda: self.find_and_trans())
        self.ui.rt.clicked.connect(lambda: self.change_of_scene2())
        self.ui.comboBox.currentIndexChanged.connect(lambda: self.change_of_scene(self.bts))
        self.ui.comboBox_3.currentIndexChanged.connect(lambda: self.translate(self.ui.comboBox_3.currentText()))
        #validator = QRegularExpressionValidator(self.reg, self.lineEdit)
        #self.ui.lineEdit.setValidator(validator)
        validator2 = QRegularExpressionValidator(self.reg2, self.ui.comboBox_2)
        self.ui.comboBox_2.setValidator(validator2)
        self.ui.b_i.setParent(None)
        self.ui.b_plus.setParent(None)
        self.ui.b_minus.setParent(None)
        self.ui.rt.setParent(None)
        self.find_language()


    def change_of_scene(self,bts: list) -> None:
        if self.ui.comboBox.currentText()=='Complex':
            for button in range(len(bts)):
                self.ui.gridLayout.addWidget(bts[button],button,4)
                self.mode = self.ui.comboBox.currentText()
        else:
            self.ui.b_i.setParent(None)
            self.ui.b_plus.setParent(None)
            self.ui.b_minus.setParent(None)
            self.ui.rt.setParent(None)
            self.mode = self.ui.comboBox.currentText()
            self.ui.lineEdit.setText('0')

    def change_of_scene2(self) -> None:
        self.ui.b_i.setParent(None)
        self.ui.b_plus.setParent(None)
        self.ui.b_minus.setParent(None)
        self.ui.rt.setParent(None)

    def add_digit(self, btn_text: str) -> None:
        if self.ui.lineEdit.text() == '0':
            self.ui.lineEdit.setText(btn_text)
        else:
            self.ui.lineEdit.setText(self.ui.lineEdit.text() + btn_text)
    def add_dot(self) -> None:

        if self.ui.lineEdit.text() == '0':
            self.ui.lineEdit.setText('0.')
            return
        if '.' not in self.ui.lineEdit.text():

         self.ui.lineEdit.setText(self.ui.lineEdit.text() + '.')


    def clear(self)-> None:
        self.ui.lineEdit.setText('0')
        self.ui.label.clear()

    def root(self) -> None:
        self.ui.label.setText(self.ui.lineEdit.text())
        if self.ui.comboBox_2.currentText()=='':
            self.ui.comboBox_2.setCurrentText('7')
        if self.mode == 'Real':
            #self.ui.lineEdit.setText(str(round(math.sqrt(float(self.ui.lineEdit.text())),int(self.ui.comboBox_2.currentText()))))
            self.ui.lineEdit.setText(str((Decimal(numpy.sqrt(Decimal(self.ui.lineEdit.text())))).quantize(Decimal('1.'+'0'*int(self.ui.comboBox_2.currentText())), rounding=ROUND_DOWN)))
        else:
            temp = cmath.sqrt(complex(self.ui.lineEdit.text()))
            self.ui.lineEdit.setText(f'{(round(temp.real,int(self.ui.comboBox_2.currentText())))}+{(round(temp.imag,int(self.ui.comboBox_2.currentText())))}j'.replace('+-','-'))
    def dell(self) -> None:
        k = len(self.ui.lineEdit.text())
        if self.ui.lineEdit.text() == '0':
            pass
        elif k == 1:
            self.ui.lineEdit.setText('0')
        else:
            self.ui.lineEdit.setText(self.ui.lineEdit.text()[:k-1])
    def translate(self, language) -> None:
        self.translator.set_language(language)
        self.ui.label_4.setText(self.translator.translate("Language_line"))
        self.ui.label_3.setText(self.translator.translate("Accuracy_line"))
        self.ui.label_2.setText(self.translator.translate("Mode_line"))
        self.ui.comboBox.setItemText(0,self.translator.translate("Mode_real"))
        self.ui.comboBox.setItemText(1, self.translator.translate("Mode_complex"))



    def find_language(self) -> None:
        all_items = []
        for i in range(self.ui.comboBox_3.count()):
            all_items.append(self.ui.comboBox_3.itemText(i))
        for lgs in os.listdir("translations"):
            s = lgs[:len(lgs)-5]
            print(s)
            print(os.listdir("translations"))
            if s not in all_items:
                self.ui.comboBox_3.addItem(s)


    def find_and_trans(self) -> None:
        self.translate(self.ui.comboBox_3.currentText())
        self.find_language()

app = QApplication(sys.argv)

window = Root()
window.show()
sys.exit(app.exec())
