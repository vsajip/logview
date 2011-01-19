from PyQt4.QtCore import Qt, SIGNAL
from PyQt4.QtGui import QDialog
from ui_textinfo import Ui_TextInfoDialog

class TextInfoDialog(QDialog, Ui_TextInfoDialog):
    def __init__(self, parent, info):
        super(TextInfoDialog, self).__init__(parent)
        self.info = info
        self.setupUi(self)

    def setupUi(self, w):
        super(TextInfoDialog, self).setupUi(w)
        self.text.setPlainText(self.info)
        self.connect(self.selectAll, SIGNAL('clicked(bool)'), self.on_select_all)
        self.connect(self.copy, SIGNAL('clicked(bool)'), self.on_copy)

    def on_select_all(self, checked=False):
        self.text.selectAll()

    def on_copy(self, checked=False):
        self.text.copy()
