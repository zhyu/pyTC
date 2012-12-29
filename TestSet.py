# -*- coding: utf-8 -*-

import os
import AddFilesDialog
from collections import defaultdict
from math import log
from operator import itemgetter
from PySide.QtGui import QDialog

class TestSet:
    def __init__(self):
        self.tags, self.files = [], []
        self.file_tag_map, self.file_tagged = {}, {}
        self.file_count = 0
        self.tag_count = defaultdict(int)
        self.prob_tag = {}
    
    def selectFiles(self):
        self.dialog = AddFilesDialog.AddFilesDialog()
        if self.dialog.exec_() == QDialog.Rejected:
            self.tags, self.files, self.file_tag_map = self.dialog.getInfomation()
        self.file_count = len(self.files)
        for filePath in self.files:
            fileName = os.path.split(filePath)[1]
            self.tag_count[self.file_tag_map[fileName]] += 1
        for tag in self.tags:
            self.prob_tag[tag] = 1.0 * self.tag_count[tag] / self.file_count
        
    def startCategorization(self, preProb):
        wrong = 0
        file_tag_prob = defaultdict(lambda:defaultdict(float))
        for filePath in self.files:
            fileName = os.path.split(filePath)[1]
            data = open(filePath).read().decode('GB18030').split()
            for term in data:
                for tag in self.tags:
                    file_tag_prob[fileName][tag] += log(preProb[term][tag]*self.prob_tag[tag]+1)
            self.file_tagged[fileName] = sorted(file_tag_prob[fileName].iteritems(), key=itemgetter(1), reverse=True)[0][0]
                                                
    def getResult(self):
        return self.files, self.tags, self.file_tagged, self.file_tag_map
            