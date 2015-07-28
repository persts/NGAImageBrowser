# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_NGABrowser.ui'
#
# Created: Tue Jul 28 09:55:09 2015
#      by: PyQt4 UI code generator 4.10.4
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

class Ui_NGABrowserWidget(object):
    def setupUi(self, NGABrowserWidget):
        NGABrowserWidget.setObjectName(_fromUtf8("NGABrowserWidget"))
        NGABrowserWidget.resize(321, 617)
        self.verticalLayout = QtGui.QVBoxLayout(NGABrowserWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tabWidget = QtGui.QTabWidget(NGABrowserWidget)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.verticalLayout.addWidget(self.tabWidget)

        self.retranslateUi(NGABrowserWidget)
        self.tabWidget.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(NGABrowserWidget)

    def retranslateUi(self, NGABrowserWidget):
        NGABrowserWidget.setWindowTitle(_translate("NGABrowserWidget", "NGABrowser", None))

