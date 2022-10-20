import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi


class Mainscreen(QDialog):
    def __init__(self):
        super(Mainscreen,self).__init__()
        loadUi("mainscreen.ui",self)
        self.continuebutton.clicked.connect(self.gotologin)

    def gotologin(self):
        nextscreen = Login()
        widget.addWidget(nextscreen)
        widget.setCurrentIndex(widget.currentIndex()+1)        

class Login(QDialog):
    def __init__(self):
        super(Login,self). __init__()
        loadUi("login.ui",self)
        #if login button is clicked and the username and password are verified, then proceed to dash board. 
        #if the information is not verified, do not proceed to login.
        
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.loginbutton.clicked.connect(self.loginfunction)
        self.loginbutton.clicked.connect(self.gotodash)


        self.createaccbutton.clicked.connect(self.gotocreate)
        


    def loginfunction(self):
        username = self.username.text()
        password = self.password.text()
        print("Successfully logged in with username: ", username, "and password:", password)



    def gotocreate(self):
        createacc = CreateAcc()
        widget.addWidget(createacc)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def gotodash(self):
        dashboard = Dash()
        widget.addWidget(dashboard)
        widget.setCurrentIndex(widget.currentIndex()+1)        

class CreateAcc(QDialog):
    def __init__(self):
        super(CreateAcc, self).__init__()
        loadUi("createacc.ui",self)
        self.submitbutton.clicked.connect(self.createaccfunction)
        self.returnbutton.clicked.connect(self.returnfunction)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirmpass.setEchoMode(QtWidgets.QLineEdit.Password)

    def createaccfunction(self):
        username = self.username.text()

        if self.password.text() == self.confirmpass.text():
            password = self.password.text()
            print ("Successfully created account with username:", username, "and password:", password)
            login=Login()
            widget.addWidget(login)
            widget.setCurrentIndex(widget.currentIndex()+1)

        password = self.password.text()

    def returnfunction(self):
        login = Login()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex()+1)  

class Dash(QDialog):
    def __init__(self):
        super(Dash, self).__init__()
        loadUi("dashboard.ui", self)



app = QApplication(sys.argv)
mainwindow = Mainscreen()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
#widget.setFixedWidth(500)
#widget.setFixedHeight(500)
widget.show()

app.exec()

