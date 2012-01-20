# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Sun Feb  6 14:39:53 2011
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from qt import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 545)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.cSplit = Splitter(self.centralwidget)
        self.cSplit.setOrientation(QtCore.Qt.Horizontal)
        self.cSplit.setObjectName("cSplit")
        self.layoutWidget = QtGui.QWidget(self.cSplit)
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tbtree = QtGui.QWidget(self.layoutWidget)
        self.tbtree.setObjectName("tbtree")
        self.horizontalLayout = QtGui.QHBoxLayout(self.tbtree)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.toolButton = QtGui.QToolButton(self.tbtree)
        self.toolButton.setObjectName("toolButton")
        self.horizontalLayout.addWidget(self.toolButton)
        self.toolButton_2 = QtGui.QToolButton(self.tbtree)
        self.toolButton_2.setObjectName("toolButton_2")
        self.horizontalLayout.addWidget(self.toolButton_2)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addWidget(self.tbtree)
        self.tree = LoggerTree(self.layoutWidget)
        self.tree.setObjectName("tree")
        self.verticalLayout.addWidget(self.tree)
        self.mSplit = Splitter(self.cSplit)
        self.mSplit.setOrientation(QtCore.Qt.Vertical)
        self.mSplit.setObjectName("mSplit")
        self.layoutWidget1 = QtGui.QWidget(self.mSplit)
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tbmaster = QtGui.QWidget(self.layoutWidget1)
        self.tbmaster.setEnabled(True)
        self.tbmaster.setObjectName("tbmaster")
        self.gridLayout = QtGui.QGridLayout(self.tbmaster)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName("gridLayout")
        self.wantDebug = QtGui.QCheckBox(self.tbmaster)
        self.wantDebug.setChecked(True)
        self.wantDebug.setObjectName("wantDebug")
        self.gridLayout.addWidget(self.wantDebug, 0, 0, 1, 1)
        self.wantInfo = QtGui.QCheckBox(self.tbmaster)
        self.wantInfo.setChecked(True)
        self.wantInfo.setObjectName("wantInfo")
        self.gridLayout.addWidget(self.wantInfo, 1, 0, 1, 1)
        self.clearAll = QtGui.QToolButton(self.tbmaster)
        self.clearAll.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clearAll.sizePolicy().hasHeightForWidth())
        self.clearAll.setSizePolicy(sizePolicy)
        self.clearAll.setObjectName("clearAll")
        self.gridLayout.addWidget(self.clearAll, 0, 3, 1, 1)
        self.colprefs = QtGui.QToolButton(self.tbmaster)
        self.colprefs.setObjectName("colprefs")
        self.gridLayout.addWidget(self.colprefs, 1, 3, 1, 1)
        self.wantCritical = QtGui.QCheckBox(self.tbmaster)
        self.wantCritical.setChecked(True)
        self.wantCritical.setObjectName("wantCritical")
        self.gridLayout.addWidget(self.wantCritical, 0, 2, 1, 1)
        self.wantAll = QtGui.QCheckBox(self.tbmaster)
        self.wantAll.setChecked(True)
        self.wantAll.setObjectName("wantAll")
        self.gridLayout.addWidget(self.wantAll, 1, 2, 1, 1)
        self.wantError = QtGui.QCheckBox(self.tbmaster)
        self.wantError.setChecked(True)
        self.wantError.setObjectName("wantError")
        self.gridLayout.addWidget(self.wantError, 1, 1, 1, 1)
        self.wantWarning = QtGui.QCheckBox(self.tbmaster)
        self.wantWarning.setChecked(True)
        self.wantWarning.setObjectName("wantWarning")
        self.gridLayout.addWidget(self.wantWarning, 0, 1, 1, 1)
        self.search = QtGui.QToolButton(self.tbmaster)
        self.search.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.search.sizePolicy().hasHeightForWidth())
        self.search.setSizePolicy(sizePolicy)
        self.search.setObjectName("search")
        self.gridLayout.addWidget(self.search, 4, 3, 1, 1)
        self.match = QtGui.QLineEdit(self.tbmaster)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.match.sizePolicy().hasHeightForWidth())
        self.match.setSizePolicy(sizePolicy)
        self.match.setObjectName("match")
        self.gridLayout.addWidget(self.match, 4, 1, 1, 1)
        self.matchlabel = QtGui.QLabel(self.tbmaster)
        self.matchlabel.setObjectName("matchlabel")
        self.gridLayout.addWidget(self.matchlabel, 4, 0, 1, 1)
        self.useRegexp = QtGui.QCheckBox(self.tbmaster)
        self.useRegexp.setObjectName("useRegexp")
        self.gridLayout.addWidget(self.useRegexp, 4, 2, 1, 1)
        self.line = QtGui.QFrame(self.tbmaster)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 3, 0, 1, 4)
        self.verticalLayout_2.addWidget(self.tbmaster)
        self.master = MasterTable(self.layoutWidget1)
        self.master.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.master.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.master.setObjectName("master")
        self.verticalLayout_2.addWidget(self.master)
        self.verticalLayout_2.setStretch(1, 1)
        self.detail = DetailTable(self.mSplit)
        self.detail.setSelectionMode(QtGui.QAbstractItemView.NoSelection)
        self.detail.setObjectName("detail")
        self.verticalLayout_3.addWidget(self.cSplit)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName("menubar")
        self.menu_Help = QtGui.QMenu(self.menubar)
        self.menu_Help.setObjectName("menu_Help")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_About = QtGui.QAction(MainWindow)
        self.action_About.setObjectName("action_About")
        self.menu_Help.addAction(self.action_About)
        self.menubar.addAction(self.menu_Help.menuAction())
        self.matchlabel.setBuddy(self.match)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.toolButton, self.toolButton_2)
        MainWindow.setTabOrder(self.toolButton_2, self.tree)
        MainWindow.setTabOrder(self.tree, self.wantDebug)
        MainWindow.setTabOrder(self.wantDebug, self.wantWarning)
        MainWindow.setTabOrder(self.wantWarning, self.wantCritical)
        MainWindow.setTabOrder(self.wantCritical, self.wantInfo)
        MainWindow.setTabOrder(self.wantInfo, self.wantError)
        MainWindow.setTabOrder(self.wantError, self.wantAll)
        MainWindow.setTabOrder(self.wantAll, self.clearAll)
        MainWindow.setTabOrder(self.clearAll, self.colprefs)
        MainWindow.setTabOrder(self.colprefs, self.match)
        MainWindow.setTabOrder(self.match, self.useRegexp)
        MainWindow.setTabOrder(self.useRegexp, self.search)
        MainWindow.setTabOrder(self.search, self.master)
        MainWindow.setTabOrder(self.master, self.detail)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Python Log Viewer", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton.setText(QtGui.QApplication.translate("MainWindow", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton_2.setText(QtGui.QApplication.translate("MainWindow", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.wantDebug.setText(QtGui.QApplication.translate("MainWindow", "&DEBUG", None, QtGui.QApplication.UnicodeUTF8))
        self.wantInfo.setText(QtGui.QApplication.translate("MainWindow", "&INFO", None, QtGui.QApplication.UnicodeUTF8))
        self.clearAll.setToolTip(QtGui.QApplication.translate("MainWindow", "Clear all records", None, QtGui.QApplication.UnicodeUTF8))
        self.clearAll.setText(QtGui.QApplication.translate("MainWindow", "&Clear", None, QtGui.QApplication.UnicodeUTF8))
        self.colprefs.setText(QtGui.QApplication.translate("MainWindow", "C&olumns ...", None, QtGui.QApplication.UnicodeUTF8))
        self.wantCritical.setText(QtGui.QApplication.translate("MainWindow", "C&RITICAL", None, QtGui.QApplication.UnicodeUTF8))
        self.wantAll.setText(QtGui.QApplication.translate("MainWindow", "&All", None, QtGui.QApplication.UnicodeUTF8))
        self.wantError.setText(QtGui.QApplication.translate("MainWindow", "&ERROR", None, QtGui.QApplication.UnicodeUTF8))
        self.wantWarning.setText(QtGui.QApplication.translate("MainWindow", "&WARNING", None, QtGui.QApplication.UnicodeUTF8))
        self.search.setText(QtGui.QApplication.translate("MainWindow", "&Search", None, QtGui.QApplication.UnicodeUTF8))
        self.matchlabel.setText(QtGui.QApplication.translate("MainWindow", "&Match in message:", None, QtGui.QApplication.UnicodeUTF8))
        self.useRegexp.setText(QtGui.QApplication.translate("MainWindow", "Regex", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_Help.setTitle(QtGui.QApplication.translate("MainWindow", "&Help", None, QtGui.QApplication.UnicodeUTF8))
        self.action_About.setText(QtGui.QApplication.translate("MainWindow", "&About", None, QtGui.QApplication.UnicodeUTF8))

from splitters import Splitter
from tables import DetailTable, MasterTable, LoggerTree
