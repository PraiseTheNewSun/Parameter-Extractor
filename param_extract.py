from PySide2.QtWidgets import *
import sys
import pandas as pd

class Scraper(QMainWindow): 

    style = '''
        #process1{
            background-color: #212529;
            color: #ffffff;
        }
    '''

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Parameter Extractor')
        self.setGeometry(100, 100, 400, 700)

        self.InitializeUI()

    def InitializeUI(self):
        self.file_path = QLineEdit(self)
        self.file_path.setGeometry(20, 20, 300, 30)
        self.file_path.setPlaceholderText('File path...')

        self.process1 = QPushButton(self)
        self.process1.setText('Process')
        self.process1.setObjectName('process1')
        self.process1.clicked.connect(self.Process1)
        self.process1.setGeometry(20, 70, 100, 30)

        self.available_columns = QTextEdit(self)
        self.available_columns.setGeometry(20, 120, 300, 150)
        self.available_columns.setReadOnly(True)

        self.search_term = QLineEdit(self)
        self.search_term.setGeometry(20, 290, 300, 30)
        self.search_term.setPlaceholderText('Known Info Column...')

        self.search_term2 = QLineEdit(self)
        self.search_term2.setGeometry(20, 340, 300, 30)
        self.search_term2.setPlaceholderText('Known Data Input...')

        self.process2 = QPushButton(self)
        self.process2.setText('Process')
        self.process2.setObjectName('process1')
        self.process2.setGeometry(20, 390, 100, 30)
        self.process2.clicked.connect(self.Process2)

        self.result = QTextEdit(self)
        self.result.setGeometry(20, 440, 300, 150)
        self.result.setReadOnly(True)

    def Process1(self):
        data = pd.read_excel(f'{self.file_path.text()}')
        data_head = list(data)
        self.available_columns.append(f'Available Columns:\n {data_head}')

    def Process2(self):
        data = pd.read_excel(f'{self.file_path.text()}')
        data2 = list(data[f'{self.search_term.text()}'])
        result = list(data['Phone Number'])[data2.index(f'{self.search_term2.text()}')]
        self.result.append(f'Phone No for  " {self.search_term2.text()} ":\n 0{result}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet(Scraper.style)
    window = Scraper()
    window.show()
    sys.exit(app.exec_())