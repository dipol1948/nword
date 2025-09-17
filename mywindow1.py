# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'testtest.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
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
"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setStyleSheet(u"color: rgba(255,33,100,100)\n"
"")

        self.verticalLayout.addWidget(self.label)

        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy1)
        self.lineEdit.setStyleSheet(u"font-size: 40pt;\n"
"border: none;")
        self.lineEdit.setMaxLength(20)
        self.lineEdit.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.lineEdit.setReadOnly(True)

        self.verticalLayout.addWidget(self.lineEdit)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.b_dot = QPushButton(self.centralwidget)
        self.b_dot.setObjectName(u"b_dot")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.b_dot.sizePolicy().hasHeightForWidth())
        self.b_dot.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.b_dot, 3, 0, 1, 1)

        self.root = QPushButton(self.centralwidget)
        self.root.setObjectName(u"root")
        sizePolicy2.setHeightForWidth(self.root.sizePolicy().hasHeightForWidth())
        self.root.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.root, 3, 2, 1, 1)

        self.b_0 = QPushButton(self.centralwidget)
        self.b_0.setObjectName(u"b_0")
        sizePolicy2.setHeightForWidth(self.b_0.sizePolicy().hasHeightForWidth())
        self.b_0.setSizePolicy(sizePolicy2)
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

        self.b_5 = QPushButton(self.centralwidget)
        self.b_5.setObjectName(u"b_5")
        sizePolicy2.setHeightForWidth(self.b_5.sizePolicy().hasHeightForWidth())
        self.b_5.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.b_5, 1, 1, 1, 1)

        self.b_6 = QPushButton(self.centralwidget)
        self.b_6.setObjectName(u"b_6")
        sizePolicy2.setHeightForWidth(self.b_6.sizePolicy().hasHeightForWidth())
        self.b_6.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.b_6, 1, 2, 1, 1)

        self.b_4 = QPushButton(self.centralwidget)
        self.b_4.setObjectName(u"b_4")
        sizePolicy2.setHeightForWidth(self.b_4.sizePolicy().hasHeightForWidth())
        self.b_4.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.b_4, 1, 0, 1, 1)

        self.root_2 = QPushButton(self.centralwidget)
        self.root_2.setObjectName(u"root_2")
        sizePolicy2.setHeightForWidth(self.root_2.sizePolicy().hasHeightForWidth())
        self.root_2.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.root_2, 3, 3, 1, 1)

        self.root_8 = QPushButton(self.centralwidget)
        self.root_8.setObjectName(u"root_8")
        sizePolicy2.setHeightForWidth(self.root_8.sizePolicy().hasHeightForWidth())
        self.root_8.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.root_8, 1, 3, 1, 1)

        self.root_9 = QPushButton(self.centralwidget)
        self.root_9.setObjectName(u"root_9")
        sizePolicy2.setHeightForWidth(self.root_9.sizePolicy().hasHeightForWidth())
        self.root_9.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.root_9, 0, 3, 1, 1)

        self.b_1 = QPushButton(self.centralwidget)
        self.b_1.setObjectName(u"b_1")
        sizePolicy2.setHeightForWidth(self.b_1.sizePolicy().hasHeightForWidth())
        self.b_1.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.b_1, 2, 0, 1, 1)

        self.b_9 = QPushButton(self.centralwidget)
        self.b_9.setObjectName(u"b_9")
        sizePolicy2.setHeightForWidth(self.b_9.sizePolicy().hasHeightForWidth())
        self.b_9.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.b_9, 0, 2, 1, 1)

        self.b_7 = QPushButton(self.centralwidget)
        self.b_7.setObjectName(u"b_7")
        sizePolicy2.setHeightForWidth(self.b_7.sizePolicy().hasHeightForWidth())
        self.b_7.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.b_7, 0, 0, 1, 1)

        self.root_7 = QPushButton(self.centralwidget)
        self.root_7.setObjectName(u"root_7")
        sizePolicy2.setHeightForWidth(self.root_7.sizePolicy().hasHeightForWidth())
        self.root_7.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.root_7, 2, 3, 1, 1)

        self.b_8 = QPushButton(self.centralwidget)
        self.b_8.setObjectName(u"b_8")
        sizePolicy2.setHeightForWidth(self.b_8.sizePolicy().hasHeightForWidth())
        self.b_8.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.b_8, 0, 1, 1, 1)

        self.b_3 = QPushButton(self.centralwidget)
        self.b_3.setObjectName(u"b_3")
        sizePolicy2.setHeightForWidth(self.b_3.sizePolicy().hasHeightForWidth())
        self.b_3.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.b_3, 2, 2, 1, 1)

        self.b_2 = QPushButton(self.centralwidget)
        self.b_2.setObjectName(u"b_2")
        sizePolicy2.setHeightForWidth(self.b_2.sizePolicy().hasHeightForWidth())
        self.b_2.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.b_2, 2, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"bimbo", None))
        self.label.setText("")
        self.lineEdit.setText(QCoreApplication.translate("MainWindow", u"Zero", None))
        self.b_dot.setText(QCoreApplication.translate("MainWindow", u".", None))
#if QT_CONFIG(shortcut)
        self.b_dot.setShortcut(QCoreApplication.translate("MainWindow", u",", None))
#endif // QT_CONFIG(shortcut)
        self.root.setText(QCoreApplication.translate("MainWindow", u"\u221a ", None))
#if QT_CONFIG(shortcut)
        self.root.setShortcut(QCoreApplication.translate("MainWindow", u"=", None))
#endif // QT_CONFIG(shortcut)
        self.b_0.setText(QCoreApplication.translate("MainWindow", u"0", None))
#if QT_CONFIG(shortcut)
        self.b_0.setShortcut(QCoreApplication.translate("MainWindow", u"0", None))
#endif // QT_CONFIG(shortcut)
        self.b_5.setText(QCoreApplication.translate("MainWindow", u"5", None))
#if QT_CONFIG(shortcut)
        self.b_5.setShortcut(QCoreApplication.translate("MainWindow", u"5", None))
#endif // QT_CONFIG(shortcut)
        self.b_6.setText(QCoreApplication.translate("MainWindow", u"6", None))
#if QT_CONFIG(shortcut)
        self.b_6.setShortcut(QCoreApplication.translate("MainWindow", u"6", None))
#endif // QT_CONFIG(shortcut)
        self.b_4.setText(QCoreApplication.translate("MainWindow", u"4", None))
#if QT_CONFIG(shortcut)
        self.b_4.setShortcut(QCoreApplication.translate("MainWindow", u"4", None))
#endif // QT_CONFIG(shortcut)
        self.root_2.setText(QCoreApplication.translate("MainWindow", u"DEL Sys32", None))
#if QT_CONFIG(shortcut)
        self.root_2.setShortcut(QCoreApplication.translate("MainWindow", u"=", None))
#endif // QT_CONFIG(shortcut)
        self.root_8.setText(QCoreApplication.translate("MainWindow", u"C", None))
#if QT_CONFIG(shortcut)
        self.root_8.setShortcut(QCoreApplication.translate("MainWindow", u"=", None))
#endif // QT_CONFIG(shortcut)
        self.root_9.setText(QCoreApplication.translate("MainWindow", u"DEL", None))
#if QT_CONFIG(shortcut)
        self.root_9.setShortcut(QCoreApplication.translate("MainWindow", u"=", None))
#endif // QT_CONFIG(shortcut)
        self.b_1.setText(QCoreApplication.translate("MainWindow", u"1", None))
#if QT_CONFIG(shortcut)
        self.b_1.setShortcut(QCoreApplication.translate("MainWindow", u"1", None))
#endif // QT_CONFIG(shortcut)
        self.b_9.setText(QCoreApplication.translate("MainWindow", u"9", None))
#if QT_CONFIG(shortcut)
        self.b_9.setShortcut(QCoreApplication.translate("MainWindow", u"9", None))
#endif // QT_CONFIG(shortcut)
        self.b_7.setText(QCoreApplication.translate("MainWindow", u"7", None))
#if QT_CONFIG(shortcut)
        self.b_7.setShortcut(QCoreApplication.translate("MainWindow", u"7", None))
#endif // QT_CONFIG(shortcut)
        self.root_7.setText(QCoreApplication.translate("MainWindow", u"CE", None))
#if QT_CONFIG(shortcut)
        self.root_7.setShortcut(QCoreApplication.translate("MainWindow", u"=", None))
#endif // QT_CONFIG(shortcut)
        self.b_8.setText(QCoreApplication.translate("MainWindow", u"8", None))
#if QT_CONFIG(shortcut)
        self.b_8.setShortcut(QCoreApplication.translate("MainWindow", u"8", None))
#endif // QT_CONFIG(shortcut)
        self.b_3.setText(QCoreApplication.translate("MainWindow", u"3", None))
#if QT_CONFIG(shortcut)
        self.b_3.setShortcut(QCoreApplication.translate("MainWindow", u"3", None))
#endif // QT_CONFIG(shortcut)
        self.b_2.setText(QCoreApplication.translate("MainWindow", u"2", None))
#if QT_CONFIG(shortcut)
        self.b_2.setShortcut(QCoreApplication.translate("MainWindow", u"2", None))
#endif // QT_CONFIG(shortcut)
    # retranslateUi

