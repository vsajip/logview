#from PyQt4.QtCore import SIGNAL, SLOT, Qt, QEvent
from PyQt4.QtCore import QT_VERSION_STR, PYQT_VERSION_STR
from PyQt4.QtGui import QDialog
from ui_about import Ui_AboutDialog

class AboutDialog(QDialog, Ui_AboutDialog):
    def __init__(self, parent):
        super(AboutDialog, self).__init__(parent)
        self.setupUi(self)
        self.qtversion.setText('PyQt version %s on Qt version %s' %(PYQT_VERSION_STR, QT_VERSION_STR))