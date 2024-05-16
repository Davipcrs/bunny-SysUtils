# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AddService.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QHBoxLayout,
    QLayout, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_addServiceDialog(object):
    def setupUi(self, addServiceDialog):
        if not addServiceDialog.objectName():
            addServiceDialog.setObjectName(u"addServiceDialog")
        addServiceDialog.setWindowModality(Qt.WindowModal)
        addServiceDialog.resize(644, 452)
        palette = QPalette()
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(151, 174, 255, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(255, 255, 255, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush2)
        brush3 = QBrush(QColor(203, 214, 255, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        brush4 = QBrush(QColor(75, 87, 127, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush4)
        brush5 = QBrush(QColor(101, 116, 170, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush2)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
        brush6 = QBrush(QColor(255, 255, 220, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush6)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush)
        brush7 = QBrush(QColor(0, 0, 0, 127))
        brush7.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush7)
#endif
        palette.setBrush(QPalette.Active, QPalette.Accent, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush7)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.Accent, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush6)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush)
        brush8 = QBrush(QColor(75, 87, 127, 127))
        brush8.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush8)
#endif
        brush9 = QBrush(QColor(227, 234, 255, 255))
        brush9.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Accent, brush9)
        addServiceDialog.setPalette(palette)
        addServiceDialog.setAutoFillBackground(False)
        self.verticalLayout_2 = QVBoxLayout(addServiceDialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.nameLineEdit = QLineEdit(addServiceDialog)
        self.nameLineEdit.setObjectName(u"nameLineEdit")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nameLineEdit.sizePolicy().hasHeightForWidth())
        self.nameLineEdit.setSizePolicy(sizePolicy)
        self.nameLineEdit.setMinimumSize(QSize(0, 30))

        self.verticalLayout.addWidget(self.nameLineEdit)

        self.displayNameLineEdit = QLineEdit(addServiceDialog)
        self.displayNameLineEdit.setObjectName(u"displayNameLineEdit")
        sizePolicy.setHeightForWidth(self.displayNameLineEdit.sizePolicy().hasHeightForWidth())
        self.displayNameLineEdit.setSizePolicy(sizePolicy)
        self.displayNameLineEdit.setMinimumSize(QSize(0, 30))

        self.verticalLayout.addWidget(self.displayNameLineEdit)

        self.serviceTypeComboBox = QComboBox(addServiceDialog)
        self.serviceTypeComboBox.setObjectName(u"serviceTypeComboBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.serviceTypeComboBox.sizePolicy().hasHeightForWidth())
        self.serviceTypeComboBox.setSizePolicy(sizePolicy1)
        self.serviceTypeComboBox.setMinimumSize(QSize(0, 30))

        self.verticalLayout.addWidget(self.serviceTypeComboBox)

        self.startTypeComboBox = QComboBox(addServiceDialog)
        self.startTypeComboBox.setObjectName(u"startTypeComboBox")
        sizePolicy1.setHeightForWidth(self.startTypeComboBox.sizePolicy().hasHeightForWidth())
        self.startTypeComboBox.setSizePolicy(sizePolicy1)
        self.startTypeComboBox.setMinimumSize(QSize(0, 30))

        self.verticalLayout.addWidget(self.startTypeComboBox)

        self.errorTypeComboBox = QComboBox(addServiceDialog)
        self.errorTypeComboBox.setObjectName(u"errorTypeComboBox")
        sizePolicy1.setHeightForWidth(self.errorTypeComboBox.sizePolicy().hasHeightForWidth())
        self.errorTypeComboBox.setSizePolicy(sizePolicy1)
        self.errorTypeComboBox.setMinimumSize(QSize(0, 30))

        self.verticalLayout.addWidget(self.errorTypeComboBox)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.pathLineEdit = QLineEdit(addServiceDialog)
        self.pathLineEdit.setObjectName(u"pathLineEdit")
        sizePolicy.setHeightForWidth(self.pathLineEdit.sizePolicy().hasHeightForWidth())
        self.pathLineEdit.setSizePolicy(sizePolicy)
        self.pathLineEdit.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_2.addWidget(self.pathLineEdit)

        self.selectExe = QPushButton(addServiceDialog)
        self.selectExe.setObjectName(u"selectExe")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.selectExe.sizePolicy().hasHeightForWidth())
        self.selectExe.setSizePolicy(sizePolicy2)
        self.selectExe.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_2.addWidget(self.selectExe)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.cancelAddService = QPushButton(addServiceDialog)
        self.cancelAddService.setObjectName(u"cancelAddService")
        sizePolicy2.setHeightForWidth(self.cancelAddService.sizePolicy().hasHeightForWidth())
        self.cancelAddService.setSizePolicy(sizePolicy2)
        self.cancelAddService.setMinimumSize(QSize(0, 30))

        self.horizontalLayout.addWidget(self.cancelAddService)

        self.confirmAddService = QPushButton(addServiceDialog)
        self.confirmAddService.setObjectName(u"confirmAddService")
        sizePolicy2.setHeightForWidth(self.confirmAddService.sizePolicy().hasHeightForWidth())
        self.confirmAddService.setSizePolicy(sizePolicy2)
        self.confirmAddService.setMinimumSize(QSize(0, 30))

        self.horizontalLayout.addWidget(self.confirmAddService)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.retranslateUi(addServiceDialog)

        QMetaObject.connectSlotsByName(addServiceDialog)
    # setupUi

    def retranslateUi(self, addServiceDialog):
        addServiceDialog.setWindowTitle(QCoreApplication.translate("addServiceDialog", u"Add Service Dialog", None))
        self.selectExe.setText(QCoreApplication.translate("addServiceDialog", u"PushButton", None))
        self.cancelAddService.setText(QCoreApplication.translate("addServiceDialog", u"PushButton", None))
        self.confirmAddService.setText(QCoreApplication.translate("addServiceDialog", u"PushButton", None))
    # retranslateUi

