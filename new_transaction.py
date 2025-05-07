# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_transaction.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QComboBox, QDateEdit,
    QDialog, QFrame, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)
import res-new-window-rc_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(348, 347)
        Dialog.setStyleSheet(u"background-color: qlineargradient(\n"
"    spread:pad,\n"
"    x1:1, y1:1,\n"
"    x2:0, y2:0,\n"
"    stop:0 rgba(178, 255, 218, 255),\n"
"    stop:0.5 rgba(102, 217, 192, 235),\n"
"    stop:1 rgba(38, 166, 154, 255)\n"
");\n"
"font-family: Noto Sans SC;")
        self.verticalLayout_2 = QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgba(255, 255, 255, 60);\n"
"border: 1px solid rgba(0, 100, 100, 60);\n"
"border-radius: 7px;\n"
"color: #004d4d;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lbl_new_transaction = QLabel(self.frame)
        self.lbl_new_transaction.setObjectName(u"lbl_new_transaction")
        self.lbl_new_transaction.setMaximumSize(QSize(16777215, 16777215))
        self.lbl_new_transaction.setStyleSheet(u"font-weight: bold;\n"
"font-size: 20pt;\n"
"background-color: none;\n"
"border: none;")
        self.lbl_new_transaction.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.lbl_new_transaction)

        self.cb_category = QComboBox(self.frame)
        self.cb_category.addItem("")
        self.cb_category.addItem("")
        self.cb_category.addItem("")
        self.cb_category.addItem("")
        self.cb_category.addItem("")
        self.cb_category.setObjectName(u"cb_category")
        self.cb_category.setStyleSheet(u"QComboBox{\n"
"font-size: 16pt;\n"
"}\n"
"\n"
"QComboBox:item {\n"
"color: white\n"
"}")

        self.verticalLayout.addWidget(self.cb_category)

        self.data = QDateEdit(self.frame)
        self.data.setObjectName(u"data")
        self.data.setStyleSheet(u"font-size: 16pt;\n"
"padding-left: 10px;")
        self.data.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.data.setDate(QDate(2025, 1, 1))

        self.verticalLayout.addWidget(self.data)

        self.le_description = QLineEdit(self.frame)
        self.le_description.setObjectName(u"le_description")
        self.le_description.setStyleSheet(u"font-size: 16pt;\n"
"padding-left: 10px")

        self.verticalLayout.addWidget(self.le_description)

        self.le_balance = QLineEdit(self.frame)
        self.le_balance.setObjectName(u"le_balance")
        self.le_balance.setStyleSheet(u"font-size: 16pt;\n"
"padding-left: 10px")

        self.verticalLayout.addWidget(self.le_balance)

        self.comboBox_2 = QComboBox(self.frame)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setStyleSheet(u"QComboBox{\n"
"font-size: 16pt;\n"
"}\n"
"\n"
"QComboBox:item {\n"
"color: white\n"
"}")

        self.verticalLayout.addWidget(self.comboBox_2)

        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"QPushButton{\n"
"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;\n"
"width: 230px;\n"
"height: 50px\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgba(255,255,255,40);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgba(255,255,255,70);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icon/icons/post_add_white_24dp.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(24, 24))

        self.verticalLayout.addWidget(self.pushButton)


        self.verticalLayout_2.addWidget(self.frame)


        self.retranslateUi(Dialog)

        self.cb_category.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.lbl_new_transaction.setText(QCoreApplication.translate("Dialog", u"New Transaction", None))
        self.cb_category.setItemText(0, QCoreApplication.translate("Dialog", u"Groceries", None))
        self.cb_category.setItemText(1, QCoreApplication.translate("Dialog", u"Entertaiment", None))
        self.cb_category.setItemText(2, QCoreApplication.translate("Dialog", u"Auto", None))
        self.cb_category.setItemText(3, QCoreApplication.translate("Dialog", u"Other", None))
        self.cb_category.setItemText(4, QCoreApplication.translate("Dialog", u"Work", None))

        self.cb_category.setPlaceholderText(QCoreApplication.translate("Dialog", u"Choose category", None))
        self.le_description.setPlaceholderText(QCoreApplication.translate("Dialog", u"Description", None))
        self.le_balance.setPlaceholderText(QCoreApplication.translate("Dialog", u"Balance", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("Dialog", u"income", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("Dialog", u"outcome", None))

        self.pushButton.setText(QCoreApplication.translate("Dialog", u"Save new Transaction", None))
    # retranslateUi

