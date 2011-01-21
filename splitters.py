from PyQt4.QtCore import SIGNAL
from PyQt4.QtGui import QSplitter, QSplitterHandle

class SplitterHandle(QSplitterHandle):
    def mouseDoubleClickEvent(self, event):
        super(SplitterHandle, self).mouseDoubleClickEvent(event)
        splitter = self.splitter()
        index = splitter.indexOf(self)
        splitter.emit(SIGNAL('doubleClicked'), index)

class Splitter(QSplitter):
    def createHandle(self):
        return SplitterHandle(self.orientation(), self)


