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

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle('TobiPizda')
        #button0 = QPushButton('Button')
        #button1 = QPushButton('Bitton')
        layout = QVBoxLayout()
        widgets = [
            QCheckBox,
            QLCDNumber
        ]
        widgets[0].setText
        #button0 = QPushButton('Button')
        #button1 = QPushButton('Bitton')
        
        #button0.setCheckable(False)
        #button0.clicked.connect(self.button0_pressed)

        #self.setCentralWidget(button0)
        #self.setMenuWidget(button1)

        self.setFixedSize(800, 600)

        #button1.setFixedSize(200,100)
        #button0.setFixedSize(200,100)

        for w in widgets:
            layout.addWidget(w())
        
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        #text = QDialog()
        #text.setFixedSize(400, 50)
        #self.setMenuWidget(text)
    #def button0_pressed(self, ):
        #print("Hui_0") 

app = QApplication([])
window = MainWindow()
window.show()

app.exec()