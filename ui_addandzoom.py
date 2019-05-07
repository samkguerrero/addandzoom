# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addandzoom_dialog_base.ui'
#
# Created: Wed Jan 27 23:02:19 2016
#      by: PyQt4 UI code generator 4.10.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_addandzoomDialogBase(object):
    def setupUi(self, addandzoomDialogBase):
        addandzoomDialogBase.setObjectName(_fromUtf8("addandzoomDialogBase"))
        addandzoomDialogBase.resize(174, 96)
        self.verticalLayout = QtGui.QVBoxLayout(addandzoomDialogBase)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.coordinateslabel = QtGui.QLabel(addandzoomDialogBase)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.coordinateslabel.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gill Sans MT"))
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.coordinateslabel.setFont(font)
        self.coordinateslabel.setObjectName(_fromUtf8("coordinateslabel"))
        self.verticalLayout.addWidget(self.coordinateslabel)
        self.coordinatestxt = QtGui.QLineEdit(addandzoomDialogBase)
        self.coordinatestxt.setObjectName(_fromUtf8("coordinatestxt"))
        self.verticalLayout.addWidget(self.coordinatestxt)
        self.button_box = QtGui.QDialogButtonBox(addandzoomDialogBase)
        self.button_box.setOrientation(QtCore.Qt.Horizontal)
        self.button_box.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.button_box.setObjectName(_fromUtf8("button_box"))
        self.verticalLayout.addWidget(self.button_box)

        self.retranslateUi(addandzoomDialogBase)
        QtCore.QObject.connect(self.button_box, QtCore.SIGNAL(_fromUtf8("accepted()")), addandzoomDialogBase.accept)
        QtCore.QObject.connect(self.button_box, QtCore.SIGNAL(_fromUtf8("rejected()")), addandzoomDialogBase.reject)
        QtCore.QMetaObject.connectSlotsByName(addandzoomDialogBase)

    def retranslateUi(self, addandzoomDialogBase):
        addandzoomDialogBase.setWindowTitle(_translate("addandzoomDialogBase", "addandzoom", None))
        self.coordinateslabel.setText(_translate("addandzoomDialogBase", "Coordinates", None))

