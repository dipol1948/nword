# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'testtest1.ui'
##
## Created by: Qt User Interface Compiler version 6.9.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 617)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QWidget {\n"
"	color: white;\n"
"	background-color: #121212;\n"
"	\n"
"}\n"
"\n"
"\n"
"QPushButton{\n"
"	background-color: rgba(0,0,0,100);\n"
"	border: 2px solid rgba(255,33,100,230);\n"
"	border-radius: 10px;\n"
"	font-size: 20pt;\n"
"	color: rgba(255,255,255,200);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgba(255,33,100,100)\n"
"\n"
"}\n"
"\n"
"QComboBox{\n"
"background-color: rgba(0,0,0,100);\n"
"	border: 2px solid rgba(255,33,100,230);\n"
"	border-radius: 10px;\n"
"	font-size: 10pt;\n"
"}\n"
"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_4)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_3)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.comboBox_3 = QComboBox(self.centralwidget)
        self.comboBox_3.setObjectName(u"comboBox_3")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.comboBox_3.sizePolicy().hasHeightForWidth())
        self.comboBox_3.setSizePolicy(sizePolicy1)
        self.comboBox_3.setEditable(False)

        self.horizontalLayout.addWidget(self.comboBox_3)

        self.comboBox_2 = QComboBox(self.centralwidget)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        sizePolicy1.setHeightForWidth(self.comboBox_2.sizePolicy().hasHeightForWidth())
        self.comboBox_2.setSizePolicy(sizePolicy1)
        self.comboBox_2.setEditable(True)
        self.comboBox_2.setCurrentText(u"7")

        self.horizontalLayout.addWidget(self.comboBox_2)

        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        sizePolicy1.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy1)
        self.comboBox.setEditable(False)
        self.comboBox.setCurrentText(u"Real")

        self.horizontalLayout.addWidget(self.comboBox)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy2)
        self.label.setStyleSheet(u"color: rgba(255,33,100,100)\n"
"")

        self.verticalLayout.addWidget(self.label)

        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy3)
        self.lineEdit.setStyleSheet(u"font-size: 40pt;\n"
"border: none;")
        self.lineEdit.setMaxLength(50)
        self.lineEdit.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.lineEdit.setReadOnly(True)

        self.verticalLayout.addWidget(self.lineEdit)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.b_i = QPushButton(self.centralwidget)
        self.b_i.setObjectName(u"b_i")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.b_i.sizePolicy().hasHeightForWidth())
        self.b_i.setSizePolicy(sizePolicy4)

        self.gridLayout.addWidget(self.b_i, 0, 4, 1, 1)

        self.b_4 = QPushButton(self.centralwidget)
        self.b_4.setObjectName(u"b_4")
        sizePolicy4.setHeightForWidth(self.b_4.sizePolicy().hasHeightForWidth())
        self.b_4.setSizePolicy(sizePolicy4)

        self.gridLayout.addWidget(self.b_4, 1, 0, 1, 1)

        self.root_7 = QPushButton(self.centralwidget)
        self.root_7.setObjectName(u"root_7")
        sizePolicy4.setHeightForWidth(self.root_7.sizePolicy().hasHeightForWidth())
        self.root_7.setSizePolicy(sizePolicy4)

        self.gridLayout.addWidget(self.root_7, 2, 3, 1, 1)

        self.b_7 = QPushButton(self.centralwidget)
        self.b_7.setObjectName(u"b_7")
        sizePolicy4.setHeightForWidth(self.b_7.sizePolicy().hasHeightForWidth())
        self.b_7.setSizePolicy(sizePolicy4)

        self.gridLayout.addWidget(self.b_7, 0, 0, 1, 1)

        self.root_8 = QPushButton(self.centralwidget)
        self.root_8.setObjectName(u"root_8")
        sizePolicy4.setHeightForWidth(self.root_8.sizePolicy().hasHeightForWidth())
        self.root_8.setSizePolicy(sizePolicy4)

        self.gridLayout.addWidget(self.root_8, 1, 3, 1, 1)

        self.rt = QPushButton(self.centralwidget)
        self.rt.setObjectName(u"rt")
        sizePolicy4.setHeightForWidth(self.rt.sizePolicy().hasHeightForWidth())
        self.rt.setSizePolicy(sizePolicy4)

        self.gridLayout.addWidget(self.rt, 3, 4, 1, 1)

        self.root_9 = QPushButton(self.centralwidget)
        self.root_9.setObjectName(u"root_9")
        self.root_9.setEnabled(True)
        sizePolicy4.setHeightForWidth(self.root_9.sizePolicy().hasHeightForWidth())
        self.root_9.setSizePolicy(sizePolicy4)

        self.gridLayout.addWidget(self.root_9, 0, 3, 1, 1)

        self.b_0 = QPushButton(self.centralwidget)
        self.b_0.setObjectName(u"b_0")
        sizePolicy4.setHeightForWidth(self.b_0.sizePolicy().hasHeightForWidth())
        self.b_0.setSizePolicy(sizePolicy4)
        self.b_0.setStyleSheet(u"QPushButton{\n"
"	background-color: rgba(0,0,0,100);\n"
"	border: 2px solid rgba(255,33,100,230);\n"
"	border-radius: 10px;\n"
"	font-size: 20pt;\n"
"	color: rgba(255,255,255,200);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgba(255,33,100,100)\n"
"\n"
"}\n"
"")

        self.gridLayout.addWidget(self.b_0, 3, 1, 1, 1)

        self.b_2 = QPushButton(self.centralwidget)
        self.b_2.setObjectName(u"b_2")
        sizePolicy4.setHeightForWidth(self.b_2.sizePolicy().hasHeightForWidth())
        self.b_2.setSizePolicy(sizePolicy4)

        self.gridLayout.addWidget(self.b_2, 2, 1, 1, 1)

        self.b_8 = QPushButton(self.centralwidget)
        self.b_8.setObjectName(u"b_8")
        sizePolicy4.setHeightForWidth(self.b_8.sizePolicy().hasHeightForWidth())
        self.b_8.setSizePolicy(sizePolicy4)

        self.gridLayout.addWidget(self.b_8, 0, 1, 1, 1)

        self.b_minus = QPushButton(self.centralwidget)
        self.b_minus.setObjectName(u"b_minus")
        sizePolicy4.setHeightForWidth(self.b_minus.sizePolicy().hasHeightForWidth())
        self.b_minus.setSizePolicy(sizePolicy4)

        self.gridLayout.addWidget(self.b_minus, 2, 4, 1, 1)

        self.b_9 = QPushButton(self.centralwidget)
        self.b_9.setObjectName(u"b_9")
        sizePolicy4.setHeightForWidth(self.b_9.sizePolicy().hasHeightForWidth())
        self.b_9.setSizePolicy(sizePolicy4)

        self.gridLayout.addWidget(self.b_9, 0, 2, 1, 1)

        self.root_2 = QPushButton(self.centralwidget)
        self.root_2.setObjectName(u"root_2")
        sizePolicy4.setHeightForWidth(self.root_2.sizePolicy().hasHeightForWidth())
        self.root_2.setSizePolicy(sizePolicy4)

        self.gridLayout.addWidget(self.root_2, 3, 3, 1, 1)

        self.b_dot = QPushButton(self.centralwidget)
        self.b_dot.setObjectName(u"b_dot")
        sizePolicy4.setHeightForWidth(self.b_dot.sizePolicy().hasHeightForWidth())
        self.b_dot.setSizePolicy(sizePolicy4)

        self.gridLayout.addWidget(self.b_dot, 3, 0, 1, 1)

        self.b_3 = QPushButton(self.centralwidget)
        self.b_3.setObjectName(u"b_3")
        sizePolicy4.setHeightForWidth(self.b_3.sizePolicy().hasHeightForWidth())
        self.b_3.setSizePolicy(sizePolicy4)

        self.gridLayout.addWidget(self.b_3, 2, 2, 1, 1)

        self.root = QPushButton(self.centralwidget)
        self.root.setObjectName(u"root")
        sizePolicy4.setHeightForWidth(self.root.sizePolicy().hasHeightForWidth())
        self.root.setSizePolicy(sizePolicy4)

        self.gridLayout.addWidget(self.root, 3, 2, 1, 1)

        self.b_1 = QPushButton(self.centralwidget)
        self.b_1.setObjectName(u"b_1")
        sizePolicy4.setHeightForWidth(self.b_1.sizePolicy().hasHeightForWidth())
        self.b_1.setSizePolicy(sizePolicy4)

        self.gridLayout.addWidget(self.b_1, 2, 0, 1, 1)

        self.b_6 = QPushButton(self.centralwidget)
        self.b_6.setObjectName(u"b_6")
        sizePolicy4.setHeightForWidth(self.b_6.sizePolicy().hasHeightForWidth())
        self.b_6.setSizePolicy(sizePolicy4)

        self.gridLayout.addWidget(self.b_6, 1, 2, 1, 1)

        self.b_5 = QPushButton(self.centralwidget)
        self.b_5.setObjectName(u"b_5")
        sizePolicy4.setHeightForWidth(self.b_5.sizePolicy().hasHeightForWidth())
        self.b_5.setSizePolicy(sizePolicy4)

        self.gridLayout.addWidget(self.b_5, 1, 1, 1, 1)

        self.b_plus = QPushButton(self.centralwidget)
        self.b_plus.setObjectName(u"b_plus")
        sizePolicy4.setHeightForWidth(self.b_plus.sizePolicy().hasHeightForWidth())
        self.b_plus.setSizePolicy(sizePolicy4)

        self.gridLayout.addWidget(self.b_plus, 1, 4, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"bimbo", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Language", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Accuracy", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Mode", None))
        self.comboBox_3.setCurrentText("")
        self.comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"7", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("MainWindow", u"8", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("MainWindow", u"9", None))
        self.comboBox_2.setItemText(3, QCoreApplication.translate("MainWindow", u"10", None))
        self.comboBox_2.setItemText(4, QCoreApplication.translate("MainWindow", u"15", None))

        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Real", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Complex", None))

        self.label.setText("")
        self.lineEdit.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.b_i.setText(QCoreApplication.translate("MainWindow", u"j", None))
#if QT_CONFIG(shortcut)
        self.b_i.setShortcut(QCoreApplication.translate("MainWindow", u"I", None))
#endif // QT_CONFIG(shortcut)
        self.b_4.setText(QCoreApplication.translate("MainWindow", u"4", None))
#if QT_CONFIG(shortcut)
        self.b_4.setShortcut(QCoreApplication.translate("MainWindow", u"4", None))
#endif // QT_CONFIG(shortcut)
        self.root_7.setText(QCoreApplication.translate("MainWindow", u"CE", None))
#if QT_CONFIG(shortcut)
        self.root_7.setShortcut(QCoreApplication.translate("MainWindow", u"=", None))
#endif // QT_CONFIG(shortcut)
        self.b_7.setText(QCoreApplication.translate("MainWindow", u"7", None))
#if QT_CONFIG(shortcut)
        self.b_7.setShortcut(QCoreApplication.translate("MainWindow", u"7", None))
#endif // QT_CONFIG(shortcut)
        self.root_8.setText(QCoreApplication.translate("MainWindow", u"C", None))
#if QT_CONFIG(shortcut)
        self.root_8.setShortcut(QCoreApplication.translate("MainWindow", u"=", None))
#endif // QT_CONFIG(shortcut)
        self.rt.setText(QCoreApplication.translate("MainWindow", u"DEL Sys32", None))
#if QT_CONFIG(shortcut)
        self.rt.setShortcut(QCoreApplication.translate("MainWindow", u"=", None))
#endif // QT_CONFIG(shortcut)
        self.root_9.setText(QCoreApplication.translate("MainWindow", u"DEL", None))
#if QT_CONFIG(shortcut)
        self.root_9.setShortcut(QCoreApplication.translate("MainWindow", u"=", None))
#endif // QT_CONFIG(shortcut)
        self.b_0.setText(QCoreApplication.translate("MainWindow", u"0", None))
#if QT_CONFIG(shortcut)
        self.b_0.setShortcut(QCoreApplication.translate("MainWindow", u"0", None))
#endif // QT_CONFIG(shortcut)
        self.b_2.setText(QCoreApplication.translate("MainWindow", u"2", None))
#if QT_CONFIG(shortcut)
        self.b_2.setShortcut(QCoreApplication.translate("MainWindow", u"2", None))
#endif // QT_CONFIG(shortcut)
        self.b_8.setText(QCoreApplication.translate("MainWindow", u"8", None))
#if QT_CONFIG(shortcut)
        self.b_8.setShortcut(QCoreApplication.translate("MainWindow", u"8", None))
#endif // QT_CONFIG(shortcut)
        self.b_minus.setText(QCoreApplication.translate("MainWindow", u"-", None))
#if QT_CONFIG(shortcut)
        self.b_minus.setShortcut(QCoreApplication.translate("MainWindow", u"-", None))
#endif // QT_CONFIG(shortcut)
        self.b_9.setText(QCoreApplication.translate("MainWindow", u"9", None))
#if QT_CONFIG(shortcut)
        self.b_9.setShortcut(QCoreApplication.translate("MainWindow", u"9", None))
#endif // QT_CONFIG(shortcut)
        self.root_2.setText(QCoreApplication.translate("MainWindow", u"DEL Sys32", None))
#if QT_CONFIG(shortcut)
        self.root_2.setShortcut(QCoreApplication.translate("MainWindow", u"=", None))
#endif // QT_CONFIG(shortcut)
        self.b_dot.setText(QCoreApplication.translate("MainWindow", u".", None))
#if QT_CONFIG(shortcut)
        self.b_dot.setShortcut(QCoreApplication.translate("MainWindow", u",", None))
#endif // QT_CONFIG(shortcut)
        self.b_3.setText(QCoreApplication.translate("MainWindow", u"3", None))
#if QT_CONFIG(shortcut)
        self.b_3.setShortcut(QCoreApplication.translate("MainWindow", u"3", None))
#endif // QT_CONFIG(shortcut)
        self.root.setText(QCoreApplication.translate("MainWindow", u"\u221a ", None))
#if QT_CONFIG(shortcut)
        self.root.setShortcut(QCoreApplication.translate("MainWindow", u"=", None))
#endif // QT_CONFIG(shortcut)
        self.b_1.setText(QCoreApplication.translate("MainWindow", u"1", None))
#if QT_CONFIG(shortcut)
        self.b_1.setShortcut(QCoreApplication.translate("MainWindow", u"1", None))
#endif // QT_CONFIG(shortcut)
        self.b_6.setText(QCoreApplication.translate("MainWindow", u"6", None))
#if QT_CONFIG(shortcut)
        self.b_6.setShortcut(QCoreApplication.translate("MainWindow", u"6", None))
#endif // QT_CONFIG(shortcut)
        self.b_5.setText(QCoreApplication.translate("MainWindow", u"5", None))
#if QT_CONFIG(shortcut)
        self.b_5.setShortcut(QCoreApplication.translate("MainWindow", u"5", None))
#endif // QT_CONFIG(shortcut)
        self.b_plus.setText(QCoreApplication.translate("MainWindow", u"+", None))
#if QT_CONFIG(shortcut)
        self.b_plus.setShortcut(QCoreApplication.translate("MainWindow", u"+", None))
#endif // QT_CONFIG(shortcut)
    # retranslateUi

