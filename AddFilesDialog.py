# -*- coding: utf-8 -*-

import os
from PySide.QtCore import Slot
from PySide.QtGui import QDialog, QMessageBox, QFileDialog, QTableWidgetItem
from Ui_AddFilesDialog import Ui_AddFilesDialog


class AddFilesDialog(QDialog, Ui_AddFilesDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.tags, self.files = [], []
        self.file_tag_map = {}
        self.files_count = 0
        
    def getInfomation(self):
        return self.tags, self.files, self.file_tag_map
    
    @Slot()
    def on_addTagsButton_clicked(self):
        if len(self.tagsInput.text()) == 0:
            QMessageBox.critical(self, u'错误', u'请至少输入一个类别')
        else:
            tags = set(self.tagsInput.text().split())
            self.selectedTag.addItems(list(tags-set(self.tags)))
            self.tags.extend(tags)
    
    @Slot()
    def on_addFilesButton_clicked(self):
        if len(self.tags) == 0:
            QMessageBox.critical(self, u'错误', u'请先添加至少一个类别')
        else:
            addedFiles = QFileDialog.getOpenFileNames(self, u'选择文件')[0]
            tag = self.selectedTag.currentText()
            for idx, filePath in enumerate(addedFiles):
                if filePath in self.files: continue
                fileName = os.path.split(filePath)[1]
                self.file_tag_map[fileName] = tag
                self.tags_files_table.insertRow(self.files_count+idx)
                self.tags_files_table.setItem(self.files_count+idx, 0, QTableWidgetItem(tag))
                self.tags_files_table.setItem(self.files_count+idx, 1, QTableWidgetItem(fileName))
            self.files.extend(addedFiles)
            self.files_count = len(self.files)
    
    @Slot()
    def on_clearButton_clicked(self):
        self.files = []
        self.file_tag_map = {}
        self.files_count = 0
        self.tags_files_table.clearContents()
        self.tags_files_table.setRowCount(0)
