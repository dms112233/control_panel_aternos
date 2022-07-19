from ast import Try
from getpass import getpass
from http import server
from python_aternos import Client, atserver
from PyQt5 import QtCore, QtGui, QtWidgets
import json
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(421, 194)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.servers_box = QtWidgets.QComboBox(self.centralwidget)
        self.servers_box.setGeometry(QtCore.QRect(10, 10, 151, 22))
        self.servers_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.servers_box.setObjectName("servers_box")
        self.start_button = QtWidgets.QPushButton(self.centralwidget)
        self.start_button.setGeometry(QtCore.QRect(10, 40, 151, 23))
        self.start_button.setStyleSheet("background-color: rgb(0, 200, 23);")
        self.start_button.setObjectName("start_button")
        self.restart_button = QtWidgets.QPushButton(self.centralwidget)
        self.restart_button.setGeometry(QtCore.QRect(10, 100, 151, 23))
        self.restart_button.setStyleSheet("background-color: rgb(225, 225, 0);")
        self.restart_button.setObjectName("restart_button")
        self.stop_button = QtWidgets.QPushButton(self.centralwidget)
        self.stop_button.setGeometry(QtCore.QRect(10, 70, 151, 23))
        self.stop_button.setStyleSheet("background-color: rgb(222, 0, 0);")
        self.stop_button.setObjectName("stop_button")
        self.status_button = QtWidgets.QPushButton(self.centralwidget)
        self.status_button.setGeometry(QtCore.QRect(10, 130, 151, 51))
        self.status_button.setStyleSheet("background-color: rgb(85, 0, 255);")
        self.status_button.setObjectName("status_button")
        self.resylt_area = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.resylt_area.setGeometry(QtCore.QRect(170, 40, 250, 141))
        self.resylt_area.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.resylt_area.setReadOnly(True)
        self.resylt_area.setObjectName("resylt_area")
        self.update_button = QtWidgets.QPushButton(self.centralwidget)
        self.update_button.setGeometry(QtCore.QRect(170, 10, 250, 23))
        self.update_button.setStyleSheet("background-color: rgb(255, 85, 255)")
        self.update_button.setObjectName("start_button_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        self.update_list()
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.start_button.setText(_translate("MainWindow", "start"))
        self.restart_button.setText(_translate("MainWindow", "restart"))
        self.stop_button.setText(_translate("MainWindow", "stop"))
        self.status_button.setText(_translate("MainWindow", "status"))
        self.update_button.setText(_translate("MainWindow", "update"))
        self.update_button.clicked.connect(self.update_list)
        self.start_button.clicked.connect(self.start_server)
        self.stop_button.clicked.connect(self.stop_server)
        self.status_button.clicked.connect(self.status)
        self.restart_button.clicked.connect(self.restart)


    def update_list(self):
        data = self.read_config()
        self.servers_box.addItems(data)

    def start_server(self): 
        data = self.read_config()
        servers = self.servers_box.currentText()
        aternos = Client.from_credentials(data[servers][0]["login"], data[servers][0]["password"])
        srvs = aternos.list_servers()
        s = srvs[0]
        s.start()

    def stop_server(self):
        data = self.read_config()
        servers = self.servers_box.currentText()
        aternos = Client.from_credentials(data[servers][0]["login"], data[servers][0]["password"])
        srvs = aternos.list_servers()
        s = srvs[0]
        s.stop()

    def restart(self):
        data = self.read_config()
        servers = self.servers_box.currentText()
        aternos = Client.from_credentials(data[servers][0]["login"], data[servers][0]["password"])
        srvs = aternos.list_servers()
        s = srvs[0]
        s.restart()

    def status(self):
        data = self.read_config()
        servers = self.servers_box.currentText()
        aternos = Client.from_credentials(data[servers][0]["login"], data[servers][0]["password"])
        srvs = aternos.list_servers()
        for srv in srvs:
            self.resylt_area.setPlainText(f"*** {srv.domain} *** \n {srv.motd} \n ***Status:{srv.status} \n ***Full address:{srv.address} \n ***Port:{srv.port} \n ***Name: {srv.subdomain} \n ***Minecraft{srv.software}{srv.version} \n ***IsBedrock: {srv.edition == atserver.Edition.bedrock} \n ***IsJava: {srv.edition == atserver.Edition.java}")
        
    def read_config(self):
        with open("servers.json", "r") as read_file:
            data = json.load(read_file)
        return data

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


"""
{
    'server1': 
        [
            {
            'login': 'aaa',
            'password': '123'
             }
        ],
"""