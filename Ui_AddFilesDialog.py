# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/zhyu/workspace/pyTC/AddFilesDialog.ui'
#
# Created: Sat Dec 29 16:13:44 2012
#      by: pyside-uic 0.2.13 running on PySide 1.1.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_AddFilesDialog(object):
    def setupUi(self, AddFilesDialog):
        AddFilesDialog.setObjectName("AddFilesDialog")
        AddFilesDialog.resize(400, 320)
        self.tags_files_table = QtGui.QTableWidget(AddFilesDialog)
        self.tags_files_table.setGeometry(QtCore.QRect(20, 20, 351, 201))
        self.tags_files_table.setSelectionMode(QtGui.QAbstractItemView.NoSelection)
        self.tags_files_table.setObjectName("tags_files_table")
        self.tags_files_table.setColumnCount(2)
        self.tags_files_table.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tags_files_table.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tags_files_table.setHorizontalHeaderItem(1, item)
        self.tags_files_table.horizontalHeader().setStretchLastSection(True)
        self.addTagsButton = QtGui.QPushButton(AddFilesDialog)
        self.addTagsButton.setGeometry(QtCore.QRect(280, 250, 91, 23))
        self.addTagsButton.setObjectName("addTagsButton")
        self.addFilesButton = QtGui.QPushButton(AddFilesDialog)
        self.addFilesButton.setGeometry(QtCore.QRect(180, 280, 91, 23))
        self.addFilesButton.setObjectName("addFilesButton")
        self.clearButton = QtGui.QPushButton(AddFilesDialog)
        self.clearButton.setGeometry(QtCore.QRect(280, 280, 91, 23))
        self.clearButton.setObjectName("clearButton")
        self.tagsInput = QtGui.QLineEdit(AddFilesDialog)
        self.tagsInput.setGeometry(QtCore.QRect(20, 250, 251, 22))
        self.tagsInput.setObjectName("tagsInput")
        self.label = QtGui.QLabel(AddFilesDialog)
        self.label.setGeometry(QtCore.QRect(20, 230, 151, 21))
        self.label.setObjectName("label")
        self.selectedTag = QtGui.QComboBox(AddFilesDialog)
        self.selectedTag.setGeometry(QtCore.QRect(90, 280, 78, 23))
        self.selectedTag.setObjectName("selectedTag")
        self.label_2 = QtGui.QLabel(AddFilesDialog)
        self.label_2.setGeometry(QtCore.QRect(20, 280, 71, 21))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(AddFilesDialog)
        QtCore.QMetaObject.connectSlotsByName(AddFilesDialog)

    def retranslateUi(self, AddFilesDialog):
        AddFilesDialog.setWindowTitle(QtGui.QApplication.translate("AddFilesDialog", "添加文件", None, QtGui.QApplication.UnicodeUTF8))
        self.tags_files_table.setSortingEnabled(True)
        self.tags_files_table.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("AddFilesDialog", "所属类别", None, QtGui.QApplication.UnicodeUTF8))
        self.tags_files_table.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("AddFilesDialog", "文件名", None, QtGui.QApplication.UnicodeUTF8))
        self.addTagsButton.setText(QtGui.QApplication.translate("AddFilesDialog", "添加类别", None, QtGui.QApplication.UnicodeUTF8))
        self.addFilesButton.setText(QtGui.QApplication.translate("AddFilesDialog", "添加文件", None, QtGui.QApplication.UnicodeUTF8))
        self.clearButton.setText(QtGui.QApplication.translate("AddFilesDialog", "清空列表", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("AddFilesDialog", "要添加的类别(用空格分隔):", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("AddFilesDialog", "所属的类别:", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    AddFilesDialog = QtGui.QDialog()
    ui = Ui_AddFilesDialog()
    ui.setupUi(AddFilesDialog)
    AddFilesDialog.show()
    sys.exit(app.exec_())

