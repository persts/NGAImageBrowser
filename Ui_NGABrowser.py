# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_NGABrowser.ui'
#
# Created: Tue Aug 11 12:15:16 2015
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
        NGABrowserWidget.resize(853, 727)
        self.gridLayout = QtGui.QGridLayout(NGABrowserWidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.frame = QtGui.QFrame(NGABrowserWidget)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.verticalLayout = QtGui.QVBoxLayout(self.frame)
        self.verticalLayout.setSpacing(1)
        self.verticalLayout.setMargin(1)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.splitter = QtGui.QSplitter(self.frame)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.metadata = QtGui.QTableWidget(self.splitter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.metadata.sizePolicy().hasHeightForWidth())
        self.metadata.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.metadata.setFont(font)
        self.metadata.setObjectName(_fromUtf8("metadata"))
        self.metadata.setColumnCount(2)
        self.metadata.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.metadata.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.metadata.setHorizontalHeaderItem(1, item)
        self.metadata.horizontalHeader().setStretchLastSection(True)
        self.metadata.verticalHeader().setDefaultSectionSize(20)
        self.metadata.verticalHeader().setMinimumSectionSize(20)
        self.tabWidget = QtGui.QTabWidget(self.splitter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMinimumSize(QtCore.QSize(0, 400))
        self.tabWidget.setTabPosition(QtGui.QTabWidget.West)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.verticalLayout.addWidget(self.splitter)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 2)
        self.pButtonCatalog = QtGui.QPushButton(NGABrowserWidget)
        self.pButtonCatalog.setObjectName(_fromUtf8("pButtonCatalog"))
        self.gridLayout.addWidget(self.pButtonCatalog, 1, 0, 1, 1)
        self.frameUsable = QtGui.QFrame(NGABrowserWidget)
        self.frameUsable.setMaximumSize(QtCore.QSize(16777215, 100))
        self.frameUsable.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frameUsable.setFrameShadow(QtGui.QFrame.Raised)
        self.frameUsable.setObjectName(_fromUtf8("frameUsable"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.frameUsable)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label = QtGui.QLabel(self.frameUsable)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.rButtonNo = QtGui.QRadioButton(self.frameUsable)
        self.rButtonNo.setObjectName(_fromUtf8("rButtonNo"))
        self.horizontalLayout.addWidget(self.rButtonNo)
        self.rButtonMaybe = QtGui.QRadioButton(self.frameUsable)
        self.rButtonMaybe.setObjectName(_fromUtf8("rButtonMaybe"))
        self.horizontalLayout.addWidget(self.rButtonMaybe)
        self.rButtonYes = QtGui.QRadioButton(self.frameUsable)
        self.rButtonYes.setObjectName(_fromUtf8("rButtonYes"))
        self.horizontalLayout.addWidget(self.rButtonYes)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.gridLayout.addWidget(self.frameUsable, 1, 1, 1, 1)

        self.retranslateUi(NGABrowserWidget)
        self.tabWidget.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(NGABrowserWidget)

    def retranslateUi(self, NGABrowserWidget):
        NGABrowserWidget.setWindowTitle(_translate("NGABrowserWidget", "NGABrowser", None))
        item = self.metadata.horizontalHeaderItem(0)
        item.setText(_translate("NGABrowserWidget", "Attribute", None))
        item = self.metadata.horizontalHeaderItem(1)
        item.setText(_translate("NGABrowserWidget", "Value", None))
        self.pButtonCatalog.setText(_translate("NGABrowserWidget", "Catalog", None))
        self.label.setText(_translate("NGABrowserWidget", "Usable?", None))
        self.rButtonNo.setText(_translate("NGABrowserWidget", "No", None))
        self.rButtonMaybe.setText(_translate("NGABrowserWidget", "Maybe", None))
        self.rButtonYes.setText(_translate("NGABrowserWidget", "Yes", None))

