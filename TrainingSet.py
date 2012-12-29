# -*- coding: utf-8 -*-

import os
import AddFilesDialog
from collections import defaultdict
from operator import itemgetter
from PySide.QtGui import QDialog, QMessageBox

class TrainingSet:
    def __init__(self):
        self.tags, self.files = [], []
        self.file_tag_map, self.feature = {}, {}
        self.tag_count = defaultdict(int)
        self.df = defaultdict(lambda:defaultdict(int))
        self.prob = defaultdict(lambda:defaultdict(float))
    
    def selectFiles(self):
        self.dialog = AddFilesDialog.AddFilesDialog()
        if self.dialog.exec_() == QDialog.Rejected:
            self.tags, self.files, self.file_tag_map = self.dialog.getInfomation()
        
    def startTraining(self, stopWords):
        count_term_tag = defaultdict(lambda:defaultdict(list))
        
        for filePath in self.files:
            fileName = os.path.split(filePath)[1]
            data = open(filePath).read().decode('GB18030').split()
            tag = self.file_tag_map[fileName]
            self.tag_count[tag] += 1
            for term in data:
                if term in stopWords or term[0] < u'\u4e00' or term[0] > u'\u9fa5': continue
                if fileName not in count_term_tag[term][tag]:
                    count_term_tag[term][tag].append(fileName)
                    
        for tag in self.tags:
            for term in count_term_tag.keys():
                self.df[tag][term] = len(count_term_tag[term][tag])
        
        for tag in self.tags:
            self.feature[tag] = map(itemgetter(0), sorted(self.df[tag].iteritems(), key=itemgetter(1), reverse=True)[:100])
            for term in self.feature[tag]:
                self.prob[term][tag] = 1.0 * (self.df[tag][term] + 1) / (self.tag_count[tag] + 2)
                
        QMessageBox.information(None, u'训练完成', u'训练完成，可以开始分类了')
        
    def getProb(self):
        return self.prob
                    