from PySide6.QtWidgets import QApplication, QMainWindow
from ui_main import Ui_MainWindow
import sys

class BudgetBuddy(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BudgetBuddy()
    window.show()
    sys.exit(app.exec())
