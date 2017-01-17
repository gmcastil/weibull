# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(843, 736)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tableWidget = QtGui.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 10, 261, 341))
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.onsetSpinBox = QtGui.QDoubleSpinBox(self.centralwidget)
        self.onsetSpinBox.setGeometry(QtCore.QRect(10, 500, 105, 27))
        self.onsetSpinBox.setObjectName(_fromUtf8("onsetSpinBox"))
        self.widthSpinBox = QtGui.QDoubleSpinBox(self.centralwidget)
        self.widthSpinBox.setGeometry(QtCore.QRect(10, 610, 105, 27))
        self.widthSpinBox.setObjectName(_fromUtf8("widthSpinBox"))
        self.shapeSpinBox = QtGui.QDoubleSpinBox(self.centralwidget)
        self.shapeSpinBox.setGeometry(QtCore.QRect(180, 500, 105, 27))
        self.shapeSpinBox.setObjectName(_fromUtf8("shapeSpinBox"))
        self.saturationSpinBox = QtGui.QDoubleSpinBox(self.centralwidget)
        self.saturationSpinBox.setGeometry(QtCore.QRect(180, 610, 105, 27))
        self.saturationSpinBox.setObjectName(_fromUtf8("saturationSpinBox"))
        self.onsetLabel = QtGui.QLabel(self.centralwidget)
        self.onsetLabel.setGeometry(QtCore.QRect(10, 470, 161, 16))
        self.onsetLabel.setObjectName(_fromUtf8("onsetLabel"))
        self.shapeLabel = QtGui.QLabel(self.centralwidget)
        self.shapeLabel.setGeometry(QtCore.QRect(190, 470, 59, 15))
        self.shapeLabel.setObjectName(_fromUtf8("shapeLabel"))
        self.widthLabel = QtGui.QLabel(self.centralwidget)
        self.widthLabel.setGeometry(QtCore.QRect(10, 570, 141, 16))
        self.widthLabel.setObjectName(_fromUtf8("widthLabel"))
        self.saturationLabel = QtGui.QLabel(self.centralwidget)
        self.saturationLabel.setGeometry(QtCore.QRect(180, 570, 131, 16))
        self.saturationLabel.setObjectName(_fromUtf8("saturationLabel"))
        self.chiSquaredLabel = QtGui.QLabel(self.centralwidget)
        self.chiSquaredLabel.setGeometry(QtCore.QRect(320, 470, 151, 20))
        self.chiSquaredLabel.setObjectName(_fromUtf8("chiSquaredLabel"))
        self.chiSquaredLineEdit = QtGui.QLineEdit(self.centralwidget)
        self.chiSquaredLineEdit.setGeometry(QtCore.QRect(320, 500, 113, 29))
        self.chiSquaredLineEdit.setObjectName(_fromUtf8("chiSquaredLineEdit"))
        self.clearPushButton = QtGui.QPushButton(self.centralwidget)
        self.clearPushButton.setGeometry(QtCore.QRect(10, 390, 88, 27))
        self.clearPushButton.setObjectName(_fromUtf8("clearPushButton"))
        self.fitPushButton = QtGui.QPushButton(self.centralwidget)
        self.fitPushButton.setGeometry(QtCore.QRect(130, 390, 88, 27))
        self.fitPushButton.setObjectName(_fromUtf8("fitPushButton"))
        self.graphicsView = crossSectionPlotWidget(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(320, 10, 491, 421))
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 843, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menu_File = QtGui.QMenu(self.menubar)
        self.menu_File.setObjectName(_fromUtf8("menu_File"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        self.menuHelp_2 = QtGui.QMenu(self.menubar)
        self.menuHelp_2.setObjectName(_fromUtf8("menuHelp_2"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.action_Quit = QtGui.QAction(MainWindow)
        self.action_Quit.setObjectName(_fromUtf8("action_Quit"))
        self.action_Edit = QtGui.QAction(MainWindow)
        self.action_Edit.setObjectName(_fromUtf8("action_Edit"))
        self.menu_File.addAction(self.action_Quit)
        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menubar.addAction(self.menuHelp_2.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "LET (MeV-cm2/mg)", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Cross Section (cm2)", None))
        self.onsetLabel.setText(_translate("MainWindow", "Onset (MeV-cm2/mg)", None))
        self.shapeLabel.setText(_translate("MainWindow", "Shape", None))
        self.widthLabel.setText(_translate("MainWindow", "Width (MeV-cm2/mg)", None))
        self.saturationLabel.setText(_translate("MainWindow", "Saturation (cm2)", None))
        self.chiSquaredLabel.setText(_translate("MainWindow", "Chi-squared Statistic", None))
        self.clearPushButton.setText(_translate("MainWindow", "Clear", None))
        self.fitPushButton.setText(_translate("MainWindow", "Fit", None))
        self.menu_File.setTitle(_translate("MainWindow", "&File", None))
        self.menuHelp.setTitle(_translate("MainWindow", "&Edit", None))
        self.menuHelp_2.setTitle(_translate("MainWindow", "&Help", None))
        self.action_Quit.setText(_translate("MainWindow", "&Quit", None))
        self.action_Edit.setText(_translate("MainWindow", "&Edit", None))

from pyqtgraph import crossSectionPlotWidget
