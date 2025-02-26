from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from mainwindow import Ui_MainWindow
import keyEvent, keyboard

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.startBtn.clicked.connect(self.logicStart)
        self.endBtn.clicked.connect(self.logicEnd)
    
    def logicStart(self):
        if (
            self.hEdit.toPlainText() == ""
            or self.h2Edit.toPlainText() == ""
            or self.hEdit_d.toPlainText() == ""
            or self.hEdit_d2.toPlainText() == ""
        ):
            QMessageBox.warning(
                self,
                "알림",
                "빈곳에 텍스트를 입력해주세요",
                QMessageBox.Ok,
                QMessageBox.Ok,
            )
        else:

            keyEvent.healKeys = int(self.hEdit.toPlainText())
            keyEvent.honKeys = int(self.h2Edit.toPlainText())
            keyEvent.healDelay = int(self.hEdit_d.toPlainText())
            keyEvent.honDelay = int(self.hEdit_d2.toPlainText())

            self.hEdit.setEnabled(False)
            self.h2Edit.setEnabled(False)
            self.hEdit_d.setEnabled(False)
            self.hEdit_d2.setEnabled(False)

            self.labelStat.setText("시작키 입력준비중입니다")
            keyboard.hook(keyEvent.eventListener)

    def logicEnd(self):
        self.hEdit.setEnabled(True)
        self.h2Edit.setEnabled(True)
        self.hEdit_d.setEnabled(True)
        self.hEdit_d2.setEnabled(True)
        self.labelStat.setText("시작대기중입니다")
        keyboard.unhook_all()
    
app = QApplication()
window = MainWindow()
window.show()
app.exec()
