import os
from PySide2.QtWidgets import QVBoxLayout
from PySide2.QtWidgets import QWidget
from PySide2.QtCore import QFile
from PySide2.QtUiTools import QUiLoader
from pymxs import runtime as rt

import webbrowser
import os
import PySide2
from PySide2 import QtGui, QtCore
from PySide2.QtGui import QIcon, QColor
from PySide2.QtWidgets import QMainWindow, QGridLayout, QWidget, QDesktopWidget, QFileDialog, QMessageBox
from PySide2.QtCore import QFile
from PySide2.QtUiTools import QUiLoader
from pymxs import runtime as mxs
import json
from qtmax import GetQMaxMainWindow
import uuid
import time
import pymxs

class TestDialog(QtWidgets.QDialog):
    def __init__(self, parent=QWidget.find(rt.windows.getMAXHWND())):
        QtWidgets.QDialog.__init__(self, parent)
        loader = QUiLoader()
        # ui_file_path = os.path.join(  os.path.dirname(os.path.realpath(__file__)), 'test_ui.ui')
        ui_file = QFile('C:\Users\CGcenter\Desktop\user-interface.ui')
        ui_file.open(QFile.ReadOnly)
        self.ui = loader.load(ui_file, self)
        ui_file.close()
        layout = QVBoxLayout()
        layout.addWidget(self.ui)
        layout.setMargin(0)
        self.setLayout(layout)
        
    def makeTeapot(self):
        rt.teapot()
        rt.redrawViews()

def main():
    dlg = TestDialog()
    dlg.show()


if __name__ == '__main__':
    main()