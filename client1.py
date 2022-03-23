from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QMainWindow,
    QPushButton,
    QLineEdit,
    QLabel,
    QMessageBox,
)
from PyQt5.Qt import QUrl, QDesktopServices
import requests
import sys
import webbrowser


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Client")
        self.setFixedSize(400, 400)
        self.label1 = QLabel("Enter your IP:", self)
        self.text1 = QLineEdit(self)
        self.text1.move(10, 30)
        self.label2 = QLabel("Enter your api_key:", self)
        self.text2 = QLineEdit(self)
        self.label2.move(0,70)
        self.text2.move(10, 100)  
        self.label3 = QLabel("Enter your hostname:", self)
        self.text3 = QLineEdit(self)
        self.label3.move(0,130)  
        self.text3.move(10, 150)      
        self.label4 = QLabel("Answer:", self)
        self.label4.move(0, 180)
        self.button = QPushButton("Send", self)
        self.button.move(10, 200)

        self.button.clicked.connect(self.on_click)
        self.button.pressed.connect(self.on_click)

        self.show()

    def on_click(self):
        hostname = self.text3.text()
        ip = self.text1.text()
        apikey = self.text2.text()

        if (hostname == "") and (ip == "") and (apikey == ""):
            QMessageBox.about(self, "Error", "Please fill the field")
        else:
            res = self.__query(hostname,ip,apikey)
            if res:
                #self.label4.setText("\n Longitude:%s\n Latitude:%s\n" % (res["Longitude"],res["Latitude"]))
                #self.label4.setText("Answer%s" % (res["Hello"]))
                # Avec l'aide de Sylvain de la classe 32 pour la question 5
                #self.label4.adjustSize()
                self.show()
                url2 = "https://www.openstreetmap.org/?mlat=%s&mlon=%s#map=12" % (res["Latitude"], res["Longitude"])
                webbrowser.open_new_tab(url2)

    def __query(self, hostname,ip,apikey):
        url = "http://%s/ip/%s?key=%s" % (hostname,ip,apikey)
        r = requests.get(url)
        if r.status_code == requests.codes.NOT_FOUND:
            QMessageBox.about(self, "Error", "IP not found")
        if r.status_code == requests.codes.OK:
            return r.json()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MainWindow()
    app.exec_()
