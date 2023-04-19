from plover.gui_qt.tool import Tool
from PyQt5 import QtCore, QtWidgets, QtGui


class Main(Tool):

    TITLE = 'Plugin Template'
    ICON  = ''
    ROLE  = 'plugin_template'

    def __init__(self, engine):
        super().__init__(engine)

        self.engine = engine
        self.engine.hook_connect('stroked', self.on_stroked)

        self.central_layout = QtWidgets.QHBoxLayout()
        self.setLayout(self.central_layout)

    def on_stroked(self, stroke):
        print(f"{stroke}")
