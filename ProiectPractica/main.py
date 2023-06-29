import PrelucrareData
import form
import test
from PyQt5 import QtCore, QtGui, QtWidgets


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Widget = QtWidgets.QWidget()
    ui = form.Ui_Widget()

    ui.setupUi(Widget)
    Widget.show()
    sys.exit(app.exec_())
   