try:
    from PySide.QtCore import __version__ as QT_VERSION_STR
    from PySide import __version__ as PYQT_VERSION_STR
    from PySide.QtGui import QDialog
    WRAPPER = 'PySide'
except ImportError:
    from PyQt4.QtCore import QT_VERSION_STR
    from PyQt4.QtCore import PYQT_VERSION_STR
    from PyQt4.QtGui import QDialog
    WRAPPER = 'PyQt'

from ui_about import Ui_AboutDialog

class AboutDialog(QDialog, Ui_AboutDialog):
    def __init__(self, parent):
        super(AboutDialog, self).__init__(parent)
        self.setupUi(self)
        args = (WRAPPER, PYQT_VERSION_STR, QT_VERSION_STR)
        self.qtversion.setText('%s version %s on Qt version %s' % args)
