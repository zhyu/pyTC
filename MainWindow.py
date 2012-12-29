# -*- coding: utf-8 -*-

import os
import StopWords, TrainingSet, TestSet
from collections import defaultdict
from PySide.QtCore import Slot
from PySide.QtGui import QMainWindow, QDesktopWidget, QFileDialog, QMessageBox, QTableWidgetItem
from Ui_MainWindow import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.center()
        self.stopWords, self.files, self.tags = [], [], []
        self.file_tagged, self.file_tag_map = {}, {}
        #self.precision, self.recall = {}, {}
    
    def center(self, parent=None):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width()-size.width())/2, (screen.height()-size.height())/2)
        
    @Slot()
    def on_selectTrainingSetButton_clicked(self):
        self.trainingSet = TrainingSet.TrainingSet()
        self.trainingSet.selectFiles()
    
    @Slot()
    def on_selectTestSetButton_clicked(self):
        self.testSet = TestSet.TestSet()
        self.testSet.selectFiles()
    
    @Slot()
    def on_selectStopWordsButton_clicked(self):
        files = QFileDialog.getOpenFileNames(self, u'选择停词文件')[0]
        self.stopWords = StopWords.StopWords(files).getStopWords()
    
    @Slot()
    def on_startTrainingButton_clicked(self):
        try:
            self.trainingSet.startTraining(self.stopWords)
        except AttributeError:
            QMessageBox.critical(self, u'错误', u'请先选择训练集')
            
    
    @Slot()
    def on_startCategorizationButton_clicked(self):
        try:
            self.resultTable.clearContents()
            self.testSet.startCategorization(self.trainingSet.getProb())
            self.files, self.tags, self.file_tagged, self.file_tag_map = self.testSet.getResult()
            self.resultTable.setRowCount(len(self.files))
            right = defaultdict(int)
            tagged = defaultdict(int)
            origin = defaultdict(int)
            for idx, filePath in enumerate(self.files):
                fileName = os.path.split(filePath)[1]
                taggedName = self.file_tagged[fileName]
                originName = self.file_tag_map[fileName]
                if taggedName == originName: right[taggedName] += 1
                tagged[taggedName] += 1
                origin[originName] += 1
                self.resultTable.setItem(idx, 0, QTableWidgetItem(fileName))
                self.resultTable.setItem(idx, 1, QTableWidgetItem(taggedName))
                self.resultTable.setItem(idx, 2, QTableWidgetItem(originName))
                
            self.informationTable.setRowCount(len(self.tags))
            for idx, tag in enumerate(self.tags):
                self.informationTable.setItem(idx, 0, QTableWidgetItem(tag))
                self.informationTable.setItem(idx, 1, QTableWidgetItem(unicode(1.0*right[tag]/tagged[tag])))
                self.informationTable.setItem(idx, 2, QTableWidgetItem(unicode(1.0*right[tag]/origin[tag])))
                
        except AttributeError:
            QMessageBox.critical(self, u'错误', u'请先选择测试集')
