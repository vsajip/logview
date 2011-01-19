from PyQt4.QtCore import Qt, QVariant, SIGNAL
from PyQt4.QtGui import QDialog, QAbstractItemView, QListWidgetItem
from ui_colprefs import Ui_ColPrefsDialog
import copy

class ColumnItem(QListWidgetItem):
    def __init__(self, parent, column):
        super(ColumnItem, self).__init__(parent, QListWidgetItem.UserType)
        self.column = column

    def data(self, role):
        result = QVariant()
        if role == Qt.DisplayRole:
            result = self.column.title
        elif role == Qt.CheckStateRole:
            if self.column.visible:
                result = Qt.Checked
            else:
                result = Qt.Unchecked
        if not isinstance(result, QVariant):
            result = QVariant(result)
        return result

    def setData(self, role, value):
        if role == Qt.CheckStateRole:
            self.column.visible = value.toBool()

class ColPrefsDialog(QDialog, Ui_ColPrefsDialog):
    def __init__(self, parent, columns):
        super(ColPrefsDialog, self).__init__(parent)
        self.columns = [copy.copy(c) for c in columns]
        self.setupUi(self)
        self.connect(self, SIGNAL('accepted()'), self.on_accept)

    def setupUi(self, w):
        super(ColPrefsDialog, self).setupUi(w)
        thelist = self.list
        thelist.setDragDropMode(QAbstractItemView.InternalMove)

        for col in self.columns:
            item = ColumnItem(thelist, col)

    def on_accept(self):
        thelist = self.list
        n = thelist.count()
        columns = []
        for i in range(n):
            item = thelist.item(i)
            columns.append(item.column)
        self.columns = columns
