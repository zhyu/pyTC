# -*- coding: utf-8 -*-

class StopWords:
    def __init__(self, files=[]):
        self.content = []
        for filePath in files:
            self.content.extend(open(filePath).read().decode('GB18030').split())
    
    def getStopWords(self):
        return self.content
        