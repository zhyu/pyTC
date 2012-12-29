# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/zhyu/workspace/pyTC/MainWindow.ui'
#
# Created: Sat Dec 29 16:13:43 2012
#      by: pyside-uic 0.2.13 running on PySide 1.1.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 510)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.resultTable = QtGui.QTableWidget(self.centralWidget)
        self.resultTable.setGeometry(QtCore.QRect(20, 20, 351, 271))
        self.resultTable.setObjectName("resultTable")
        self.resultTable.setColumnCount(3)
        self.resultTable.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.resultTable.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.resultTable.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.resultTable.setHorizontalHeaderItem(2, item)
        self.resultTable.horizontalHeader().setStretchLastSection(True)
        self.selectTrainingSetButton = QtGui.QPushButton(self.centralWidget)
        self.selectTrainingSetButton.setGeometry(QtCore.QRect(20, 440, 91, 23))
        self.selectTrainingSetButton.setObjectName("selectTrainingSetButton")
        self.selectTestSetButton = QtGui.QPushButton(self.centralWidget)
        self.selectTestSetButton.setGeometry(QtCore.QRect(150, 440, 91, 23))
        self.selectTestSetButton.setObjectName("selectTestSetButton")
        self.selectStopWordsButton = QtGui.QPushButton(self.centralWidget)
        self.selectStopWordsButton.setGeometry(QtCore.QRect(280, 440, 91, 23))
        self.selectStopWordsButton.setObjectName("selectStopWordsButton")
        self.startTrainingButton = QtGui.QPushButton(self.centralWidget)
        self.startTrainingButton.setGeometry(QtCore.QRect(80, 470, 91, 23))
        self.startTrainingButton.setObjectName("startTrainingButton")
        self.startCategorizationButton = QtGui.QPushButton(self.centralWidget)
        self.startCategorizationButton.setGeometry(QtCore.QRect(220, 470, 91, 23))
        self.startCategorizationButton.setObjectName("startCategorizationButton")
        self.informationTable = QtGui.QTableWidget(self.centralWidget)
        self.informationTable.setGeometry(QtCore.QRect(20, 300, 351, 131))
        self.informationTable.setSelectionMode(QtGui.QAbstractItemView.NoSelection)
        self.informationTable.setObjectName("informationTable")
        self.informationTable.setColumnCount(3)
        self.informationTable.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.informationTable.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.informationTable.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.informationTable.setHorizontalHeaderItem(2, item)
        self.informationTable.horizontalHeader().setStretchLastSection(True)
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "pyTC", None, QtGui.QApplication.UnicodeUTF8))
        self.resultTable.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("MainWindow", "文件名", None, QtGui.QApplication.UnicodeUTF8))
        self.resultTable.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("MainWindow", "预测所属类别", None, QtGui.QApplication.UnicodeUTF8))
        self.resultTable.horizontalHeaderItem(2).setText(QtGui.QApplication.translate("MainWindow", "实际所属类别", None, QtGui.QApplication.UnicodeUTF8))
        self.selectTrainingSetButton.setText(QtGui.QApplication.translate("MainWindow", "选择训练集", None, QtGui.QApplication.UnicodeUTF8))
        self.selectTestSetButton.setText(QtGui.QApplication.translate("MainWindow", "选择测试集", None, QtGui.QApplication.UnicodeUTF8))
        self.selectStopWordsButton.setText(QtGui.QApplication.translate("MainWindow", "选择停用词", None, QtGui.QApplication.UnicodeUTF8))
        self.startTrainingButton.setText(QtGui.QApplication.translate("MainWindow", "开始训练", None, QtGui.QApplication.UnicodeUTF8))
        self.startCategorizationButton.setText(QtGui.QApplication.translate("MainWindow", "开始分类", None, QtGui.QApplication.UnicodeUTF8))
        self.informationTable.setSortingEnabled(True)
        self.informationTable.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("MainWindow", "类别", None, QtGui.QApplication.UnicodeUTF8))
        self.informationTable.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("MainWindow", "准确率", None, QtGui.QApplication.UnicodeUTF8))
        self.informationTable.horizontalHeaderItem(2).setText(QtGui.QApplication.translate("MainWindow", "召回率", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

