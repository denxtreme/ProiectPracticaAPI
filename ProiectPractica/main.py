import PrelucrareData
import form
from PyQt5 import QtCore, QtGui, QtWidgets

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Widget = QtWidgets.QWidget()
    ui = form.Ui_Widget()
    obj=PrelucrareData.APIdata("ion","https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=ead05df0fef049cd8735f1f88261624a")
    obj.CreateAllYouNeed()
    ui.setupUi(Widget)
    Widget.show()
    sys.exit(app.exec_())