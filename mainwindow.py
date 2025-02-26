# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QTextEdit,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(279, 253)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 20, 31, 16))
        self.hEdit = QTextEdit(self.centralwidget)
        self.hEdit.setObjectName(u"hEdit")
        self.hEdit.setGeometry(QRect(50, 10, 81, 31))
        self.h2Edit = QTextEdit(self.centralwidget)
        self.h2Edit.setObjectName(u"h2Edit")
        self.h2Edit.setGeometry(QRect(50, 50, 81, 31))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 60, 31, 16))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(140, 20, 41, 16))
        self.hEdit_d = QTextEdit(self.centralwidget)
        self.hEdit_d.setObjectName(u"hEdit_d")
        self.hEdit_d.setGeometry(QRect(180, 10, 81, 31))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(140, 60, 41, 16))
        self.hEdit_d2 = QTextEdit(self.centralwidget)
        self.hEdit_d2.setObjectName(u"hEdit_d2")
        self.hEdit_d2.setGeometry(QRect(180, 50, 81, 31))
        self.startBtn = QPushButton(self.centralwidget)
        self.startBtn.setObjectName(u"startBtn")
        self.startBtn.setGeometry(QRect(30, 120, 101, 41))
        self.endBtn = QPushButton(self.centralwidget)
        self.endBtn.setObjectName(u"endBtn")
        self.endBtn.setGeometry(QRect(160, 120, 101, 41))
        self.labelStat = QLabel(self.centralwidget)
        self.labelStat.setObjectName(u"labelStat")
        self.labelStat.setGeometry(QRect(40, 170, 221, 16))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 279, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\ubc84\ud2bc1", None))
        self.hEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\uc22b\uc790\ub9cc\uc785\ub825", None))
        self.h2Edit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\uc22b\uc790\ub9cc\uc785\ub825", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\ubc84\ud2bc2", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\uc9c0\uc5f0\uac12", None))
        self.hEdit_d.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\uc22b\uc790\ub9cc\uc785\ub825", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\uc9c0\uc5f0\uac12", None))
        self.hEdit_d2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\uc22b\uc790\ub9cc\uc785\ub825", None))
        self.startBtn.setText(QCoreApplication.translate("MainWindow", u"\uc801\uc6a9", None))
        self.endBtn.setText(QCoreApplication.translate("MainWindow", u"\ud574\uc81c", None))
        self.labelStat.setText(QCoreApplication.translate("MainWindow", u"\uc2dc\uc791\ub300\uae30\uc911\uc785\ub2c8\ub2e4", None))
    # retranslateUi

