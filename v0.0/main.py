import sys
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QDateEdit,
    QDateTimeEdit,
    QDial,
    QDoubleSpinBox,
    QFontComboBox,
    QLabel,
    QLCDNumber,
    QLineEdit,
    QMainWindow,
    QProgressBar,
    QPushButton,
    QRadioButton,
    QSlider,
    QSpinBox,
    QTimeEdit,
    QVBoxLayout,
    QWidget,
)
text0 = 'SukaBlyat'
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle('TobiPizda')

        layout = QVBoxLayout()

        button0 = QPushButton('Penis')
        button1 = QPushButton('pizda')
        text = QLabel(text0)

        button0.clicked.connect(self.button0_perssed)
        button1.clicked.connect(self.button1_pressed)

        text.setAlignment(Qt.AlignmentFlag.AlignCenter)

        layout.addWidget(button0)
        layout.addWidget(button1)
        layout.addWidget(text)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())