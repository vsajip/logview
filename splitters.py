try:
    from PySide.QtCore import SIGNAL
    from PySide.QtGui import QSplitter, QSplitterHandle
except ImportError:
    from PyQt4.QtCore import SIGNAL
    from PyQt4.QtGui import QSplitter, QSplitterHandle

class SplitterHandle(QSplitterHandle):
    def mouseDoubleClickEvent(self, event):
        super(SplitterHandle, self).mouseDoubleClickEvent(event)
        splitter = self.splitter()
        index = splitter.indexOf(self)
        splitter.emit(SIGNAL('doubleClicked'), index, int(event.buttons()))

class Splitter(QSplitter):
    def createHandle(self):
        return SplitterHandle(self.orientation(), self)
