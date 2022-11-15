import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi
 




class Mainscreen(QDialog):
    def __init__(self):
        super(Mainscreen,self).__init__()
        loadUi("mainscreen.ui",self)
        self.continuebutton.clicked.connect(self.gotologin)
        widget = QtWidgets.QStackedWidget()
        widget.setFixedWidth(500)
        widget.setFixedHeight(500)

    def gotologin(self):
        nextscreen = Login()
        widget.addWidget(nextscreen)
        widget.setCurrentIndex(widget.currentIndex()+1)        

class Login(QDialog):
    def __init__(self):
        super(Login,self). __init__()
        loadUi("login.ui",self)      
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.loginbutton.clicked.connect(self.loginfunction)
        widget.setFixedWidth(500)
        widget.setFixedHeight(500)
        self.createaccbutton.clicked.connect(self.gotocreate)
        self.invalid_error.setVisible(False)
        

        

        


    def loginfunction(self):
        db = open("database.txt", "r")
        username = self.username.text()
        password = self.password.text()

        if not len(username or password) < 1:
            user_store = []
            passw_store = []

            for i in db:
                user,passw = i.split(",")
                passw = passw.strip()
                user_store.append(user)
                passw_store.append(passw)

            data = dict(zip(user_store,passw_store))

            try:
                if data[username]:
                    try:
                        if password == data[username]:
                            print("Login sucsess") 
                            print("Hi", username)
                            self.gotodash()
                        else:
                            print("Invalid credentials") 
                            self.invalid_error.setVisible(True)

                    except:
                        print("Invalid credentials") 
                        self.invalid_error.setVisible(True)
                
                else:
                    print("User does not exist") 
                    self.invalid_error.setVisible(True)

            except:
                print("login error") 
                self.invalid_error.setVisible(True)


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
        self.matcherror.setVisible(False)
        self.usererror.setVisible(False)
        self.blankerror.setVisible(False)
        self.maxerror.setVisible(False)

        widget.setFixedWidth(500)
        widget.setFixedHeight(500)
        

    def createaccfunction(self):
       
        db = open("database.txt")
        username = self.username.text()
        password = self.password.text()
        confirm_pass = self.confirmpass.text()

        if not len(username or password) < 1:
            user_store = []
            passw_store = []

            for i in db:
                user,passw = i.split(",")
                passw = passw.strip()
                user_store.append(user)
                passw_store.append(passw)

            data = dict(zip(user_store,passw_store))

            if password != confirm_pass:
                print("Passwords do not match")
                self.confirmpass.clear()
                self.matcherror.setVisible(True)
                return
                
            elif username in user_store:
                print("User already exists, choose another")
                self.username.clear()
                self.usererror.setVisible(True)
                return
            
            elif username == "" or password =="" or confirm_pass == "":
                print("Cannot leave blank fields")
                self.username.clear()
                self.password.clear()
                self.confirmpass.clear()
                self.blankerror.setVisible(True)
                return

            
            else:
                db = open("database.txt", "r")
                read_db = db.readlines()
                db.close()
                if len(read_db) < 10:
                    db = open("database.txt", "a")
                    db.write(username+", "+ password+"\n")
                    print("Success")
                    db.close()
                else:
                    print("User Limit Reached")
                    self.username.clear()
                    self.password.clear()
                    self.confirmpass.clear()
                    self.maxerror.setVisible(True)
                    return


            login=Login()
            widget.addWidget(login)
            widget.setCurrentIndex(widget.currentIndex()+1)
                    
    def returnfunction(self):
        login = Login()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex()+1)
          
        

class Dash(QDialog):
    def __init__(self):
        super(Dash, self).__init__()
        loadUi("dashboard.ui", self)
        widget.setFixedWidth(900)
        widget.setFixedHeight(600)
        self.logoutbutton.clicked.connect(self.logoutfunction)
        self.VOObutton.clicked.connect(self.gotovoo)
        self.AOObutton.clicked.connect(self.gotoaoo)
        self.AAIbutton.clicked.connect(self.gotoaai)
        self.VVIbutton.clicked.connect(self.gotovvi)
        


    def gotovoo(self):
        voo = VOO()
        widget.addWidget(voo)
        widget.setCurrentIndex(widget.currentIndex()+1)    

    def gotoaoo(self):
        aoo = AOO()
        widget.addWidget(aoo)
        widget.setCurrentIndex(widget.currentIndex()+1)    

    def gotoaai(self):
        aai = AAI()
        widget.addWidget(aai)
        widget.setCurrentIndex(widget.currentIndex()+1)    

    def gotovvi(self):
        vvi = VVI()
        widget.addWidget(vvi)
        widget.setCurrentIndex(widget.currentIndex()+1)    


    def logoutfunction(self):
        logout = Mainscreen()
        widget.setFixedWidth(500)
        widget.setFixedHeight(500)
        widget.addWidget(logout)
        print ("Account Logged Out") #self.message.setVisible(True)
        widget.setCurrentIndex(widget.currentIndex()+1) 

class VOO(QDialog):
    def __init__(self):
        super(VOO, self).__init__()
        loadUi("VOO.ui", self)
        self.submitbutton.clicked.connect(self.inputfunction)
        self.backbutton.clicked.connect(self.backfunction)
        self.INVALID.setVisible(False)
        widget.setFixedWidth(900)
        widget.setFixedHeight(600)

        
    def inputfunction(self):
        VOOLRL = self.LRL.text()
        if ((float(VOOLRL)) > 0):
            self.INVALID.setVisible(False)
            db = open("VOOLRL.txt", "a")
            db.write(VOOLRL)
            print("Success")
            db.close()

        else: 
            self.INVALID.setVisible(True)    
            

    def backfunction(self):
        back = Dash()
        widget.addWidget(back)
        widget.setCurrentIndex(widget.currentIndex()+1)

class AOO(QDialog):
    def __init__(self):
        super(AOO, self).__init__()
        loadUi("AOO.ui", self)
        self.backbutton.clicked.connect(self.backfunction)
        widget.setFixedWidth(900)
        widget.setFixedHeight(600)

    def backfunction(self):
        back = Dash()
        widget.addWidget(back)
        widget.setCurrentIndex(widget.currentIndex()+1)

class AAI(QDialog):
    def __init__(self):
        super(AAI, self).__init__()
        loadUi("AAI.ui", self)
        self.backbutton.clicked.connect(self.backfunction)
        widget.setFixedWidth(900)
        widget.setFixedHeight(670)

    def backfunction(self):
        back = Dash()
        widget.addWidget(back)
        widget.setCurrentIndex(widget.currentIndex()+1)

class VVI(QDialog):
    def __init__(self):
        super(VVI, self).__init__()
        loadUi("VVI.ui", self)
        self.backbutton.clicked.connect(self.backfunction)
        widget.setFixedWidth(900)
        widget.setFixedHeight(830)
        
    def backfunction(self):
        back = Dash()
        widget.addWidget(back)
        widget.setCurrentIndex(widget.currentIndex()+1)




app = QApplication(sys.argv)
mainwindow = Mainscreen()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.show()

app.exec()

