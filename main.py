import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUi
from numpy import loadtxt
# import AOO
# good = AOO
import numpy as np

from PyQt5.QtWidgets import QLabel

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
        self.maxerror_2.setVisible(False)
        


    def loginfunction(self):
        db = open("database.txt", "r")
        username = self.username.text()
        password = self.password.text()
        
        if not len(username or password) < 1:
            user_store = []
            passw_store = []

            for i in db:
                try:
                    user,passw = i.split(",")
                    passw = passw.strip()
                    user_store.append(user)
                    passw_store.append(passw)
                    self.maxerror_2.setVisible(False)
                except:
                    self.maxerror_2.setVisible(True)
                    


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
        self.submitbutton.clicked.connect(self.validateUser)
        #self.submitbutton.clicked.connect(self.createaccfunction)
        self.returnbutton.clicked.connect(self.returnfunction)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirmpass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.matcherror.setVisible(False)
        self.usererror.setVisible(False)
        self.blankerror.setVisible(False)
        self.maxerror.setVisible(False)
        self.maxerror_2.setVisible(False)
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

            try:
                for i in db:
                    user,passw = i.split(",")
                    passw = passw.strip()
                    user_store.append(user)
                    passw_store.append(passw)

                   
            except:
                self.maxerror_2.setVisible(True)


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
    # this is to choose what characters are not valid to put. If comma is put then account wont be created. 
    def validateUser(self):
        username = self.username.text()
        password = self.password.text()

        invalid = [","]

        if any(substring in username for substring in invalid):
            print("Invalid username")
            self.maxerror_2.setVisible(True)

        else:
            db = open("database.txt")
            username = self.username.text()
            password = self.password.text()
            confirm_pass = self.confirmpass.text()

            if not len(username or password) < 1:
                user_store = []
                passw_store = []

                try:
                    for i in db:
                        user,passw = i.split(",")
                        passw = passw.strip()
                        user_store.append(user)
                        passw_store.append(passw)

                    
                except:
                    self.maxerror_2.setVisible(True)


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

class Dash(QDialog):
    def __init__(self):
        super(Dash, self).__init__()
        loadUi("dashboard.ui", self)
        widget.setFixedWidth(1200)
        widget.setFixedHeight(600)
        self.logoutbutton.clicked.connect(self.logoutfunction)
        self.VOObutton.clicked.connect(self.gotovoo)
        self.AOObutton.clicked.connect(self.gotoaoo)
        self.AAIbutton.clicked.connect(self.gotoaai)
        self.VVIbutton.clicked.connect(self.gotovvi)
        self.AOORbutton.clicked.connect(self.gotoaoor)
        # self.VOORutton.clicked.connect(self.gotovoor)
        # self.AAIRbutton.clicked.connect(self.gotoaair)
        # self.VVIRbutton.clicked.connect(self.gotovvir)
        


    def gotovoo(self):
        voo = VOO()
        widget.addWidget(voo)
        widget.setCurrentIndex(widget.currentIndex()+1)
        # VOOLRL = self.LRL.text()
        VOOUP = voo.UPLIMIT.text()
        # VOOVPW = self.VPW.text()
       
            #voo.UPLIMIT = QLabel(self)
            # load the numbers from the textfile as an array
        try:
            datas = loadtxt('VOOLRL.txt', dtype = 'float')
            t = len(datas)
          


            # print(new_a)
            t = len(datas)
         
            a = 0
            a = datas[0]
            voo.LRL.setText(str(a))
            b = 0
            b = datas[1]
            voo.UPLIMIT.setText(str(b))
            c = 0
            c = datas[3]
            voo.VPW.setText(str(c))
            d = 0
            d = datas[2]
            voo.VA.setText(str(d))
            

        except:
            #if nothing is in the textfile give the value of 0
            voo.UPLIMIT.setText(str(0))
            voo.LRL.setText(str(0))
            voo.VPW.setText(str(0))
            voo.VA.setText(str(0))
            
    
    def gotoaoo(self):
        aoo = AOO()
        widget.addWidget(aoo)
        widget.setCurrentIndex(widget.currentIndex()+1)  
    
        try:
            datasAOO = loadtxt('AOO.txt', dtype = 'float')
           
            aAOO = 0
            aAOO = datasAOO[0]
            aoo.AOOLRL.setText(str(aAOO))
            bAOO = 0
            bAOO = datasAOO[1]
            aoo.AOOUP.setText(str(bAOO))
            cAOO = 0
            cAOO = datasAOO[2]
            aoo.AOOPW.setText(str(cAOO))
            dAOO = 0
            dAOO = datasAOO[3]
            aoo.AOOAA.setText(str(dAOO))
            

        except:
            #if nothing is in the textfile give the value of 0
            aoo.AOOUP.setText(str(0))
            aoo.AOOLRL.setText(str(0))
            aoo.AOOPW.setText(str(0))
            aoo.AOOAA.setText(str(0))  

    def gotoaai(self):
        aai = AAI()
        widget.addWidget(aai)
        widget.setCurrentIndex(widget.currentIndex()+1)   
        try:
            datasAAI = loadtxt('AAI.txt', dtype = 'float')
            aaAAI = 0
            aaAAI = datasAAI[0]
            aai.AAILRL.setText(str(aaAAI))
            aAAI = 0
            aAAI = datasAAI[1]
            aai.AAIURL.setText(str(aAAI))

            iAAI = 0
            iAAI = datasAAI[2]
            aai.AAIAA.setText(str(iAAI))

            # bAAI = 0
            # bAAI = datasAAI[3]
            # aai.AAIAW.setText(str(bAAI))
            cAAI = 0
            cAAI = datasAAI[3]
            aai.AAIAPW.setText(str(cAAI))
            dAAI = 0
            dAAI = datasAAI[4]
            aai.AAIAS.setText(str(dAAI))
            eAAI = 0
            eAAI = datasAAI[5]
            aai.AAIARP.setText(str(eAAI))
            fAAI = 0
            fAAI = datasAAI[6]
            aai.AAIPVARP.setText(str(fAAI))
            gAAI = 0
            gAAI = datasAAI[7]
            aai.AIIH.setText(str(gAAI))
            hAAI = 0
            hAAI = datasAAI[8]
            aai.AAIRS.setText(str(hAAI))
       

        except:
            #if nothing is in the textfile give the value of 0
            aai.AAILRL.setText(str(0))
            aai.AAIURL.setText(str(0))
            aai.AAIAA.setText(str(0))
            aai.AAIAPW.setText(str(0))
            aai.AAIAS.setText(str(0))
            aai.AAIARP.setText(str(0)) 
            aai.AAIPVARP.setText(str(0)) 
            aai.AIIH.setText(str(0)) 
            aai.AAIRS.setText(str(0))   

    def gotovvi(self):
        vvi = VVI()
        widget.addWidget(vvi)
        widget.setCurrentIndex(widget.currentIndex()+1)    
        
        try:
            datasVVI = loadtxt('VVI.txt', dtype = 'float')
            aaVVI = 0
            aaVVI = datasVVI[0]
            vvi.VVILRL.setText(str(aaVVI))
            aVVI = 0
            aVVI = datasVVI[1]
            vvi.VVIURL.setText(str(aVVI))

            iVVI = 0
            iVVI = datasVVI[2]
            vvi.VVIVA.setText(str(iVVI))

            cVVI = 0
            cVVI = datasVVI[3]
            vvi.VVIVPW.setText(str(cVVI))
            
            dVVI = 0
            dVVI = datasVVI[4]
            vvi.VVIVS.setText(str(dVVI))
            
            eVVI = 0
            eVVI = datasVVI[5]
            vvi.VVIVRP.setText(str(eVVI))
            fVVI = 0
            fVVI = datasVVI[6]
            vvi.VVIH.setText(str(fVVI))
            gVVI = 0
            gVVI = datasVVI[7]
            vvi.VVIRS.setText(str(gVVI))
         
            
        
        

        except:
            #if nothing is in the textfile give the value of 0
            vvi.VVILRL.setText(str(0))
            vvi.VVIURL.setText(str(0))
            vvi.VVIVA.setText(str(0))
            vvi.VVIVPW.setText(str(0))
            vvi.VVIVS.setText(str(0))
            vvi.VVIVRP.setText(str(0)) 
            vvi.VVIVRP.setText(str(0)) 
            vvi.VVIH.setText(str(0)) 
            vvi.VVIRS.setText(str(0))

    def gotoaoor(self):
        aoor = AOOR()
        widget.addWidget(aoor)
        widget.setCurrentIndex(widget.currentIndex()+1)

    
    # def gotovoor(self):
    #     voor = VOOR()
    #     widget.addWidget(voor)
    #     widget.setCurrentIndex(widget.currentIndex()+1)

    # def gotoaair(self):
    #     aair = AAIR()
    #     widget.addWidget(aair)
    #     widget.setCurrentIndex(widget.currentIndex()+1)

    # def gotovvir(self):
    #     vvir = VVIR()
    #     widget.addWidget(vvir)
    #     widget.setCurrentIndex(widget.currentIndex()+1)

           


    def logoutfunction(self):
        logout = Mainscreen()
        widget.setFixedWidth(500)
        widget.setFixedHeight(500)
        widget.addWidget(logout)
        print ("Account Logged Out") #self.message.setVisible(True)
        self.logoutbutton.clicked.connect(self.resetvalues)
        widget.setCurrentIndex(widget.currentIndex()+1) 

    # reset the file once the user logs out
        # deletefile = open("VVI.txt", 'w')
        # deletefile.close()
        # with open("VVI.txt", 'r+') as file:
        #     file.truncate(0)


class VOO(QDialog):
    def __init__(self):
        super(VOO, self).__init__()
        loadUi("VOO.ui", self)
        self.submitbutton.clicked.connect(self.inputfunction)
        self.backbutton.clicked.connect(self.backfunction)
        
        
        self.INVALID.setVisible(False)
        widget.setFixedWidth(900)
        widget.setFixedHeight(600)

 

    #function to handel the ranges for modes                      
    def inputfunction(self):
        VOOLRL = self.LRL.text()
        VOOUP = self.UPLIMIT.text()
        VOOVPW = self.VPW.text()
        VA = self.VA.text()

        try:
            # ranges for the voo. If range is not met then show invalid error
            if ((((float(VOOLRL)) >= 30) and ((float(VOOLRL)) <= 49) and (float(VOOLRL) % 5 == 0))) or ((((float(VOOLRL)) >= 50) and ((float(VOOLRL)) <= 89) and (float(VOOLRL) % 1 == 0))) or ((((float(VOOLRL)) >= 90) and ((float(VOOLRL)) <= 175) and (float(VOOLRL) % 5 == 0))):
                if(((float(VOOUP)) >= 50) and (float(VOOUP)) <=175) and (float(VOOUP) % 5 == 0):
                    if((((float(VA)) >= 0.5) and (float(VA)) <=3.2) and (10*(float(VA)) % 1 == 0))  or (((float(VA)) >= 3.5) and ((float(VA)) <=7) and(10*(float(VA)) % 5 ==0)):
                        if((((float(VOOVPW)) >= 0.1) and (float(VOOVPW)) <=1.9) and (10*(float(VOOVPW)) % 1 == 0)): 
                            # open to the file and write the inputed numbers              
                            db = open("VOOLRL.txt", "w")
                            db.write(VOOLRL + "\n" + VOOUP + "\n" +  VA + "\n"+ VOOVPW)
                            print("Success")
                            db.close()
                        else:
                          self.INVALID.setVisible(True)  
                        
                    else: 
                        self.INVALID.setVisible(True)
                else: 
                    self.INVALID.setVisible(True)
            else: 
                self.INVALID.setVisible(True)
        except: 
            self.INVALID.setVisible(True)
                
             
    
    def backfunction(self):
        back = Dash()
        widget.addWidget(back)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
class AOO(QDialog):
    def __init__(self):
        super(AOO, self).__init__()
        loadUi("AOO.ui", self)
        self.INVALID.setVisible(False)
        self.AOOsubmitbutton.clicked.connect(self.AOOinputfunction)
        self.backbutton.clicked.connect(self.backfunction)
 
    def AOOinputfunction (self):
        AOOLRL = self.AOOLRL.text()
        AOOUP = self.AOOUP.text()
        AOOPW = self.AOOPW.text()
        AOOAA = self.AOOAA.text()
        try:
            # ranges for the voo. If range is not met then show invalid error
            if ((((float(AOOLRL)) >= 30) and ((float(AOOLRL)) <= 49) and (float(AOOLRL) % 5 == 0))) or ((((float(AOOLRL)) >= 50) and ((float(AOOLRL)) <= 90) and (float(AOOLRL) % 1 == 0))) or ((((float(AOOLRL)) >= 91) and ((float(AOOLRL)) <= 175) and (float(AOOLRL) % 5 == 0))):
                if(((float(AOOUP)) >= 50) and (float(AOOUP)) <=175) and (float(AOOUP) % 5 == 0):
                    if((((float(AOOAA)) >= 0.5) and (float(AOOAA)) <=3.2) and (10*(float(AOOAA)) % 1 == 0))  or (((float(AOOAA)) >= 3.5) and ((float(AOOAA)) <=7) and(10*(float(AOOAA)) % 5 ==0)):
                        if((((float(AOOPW)) >= 0.5) and (float(AOOPW)) <=3.2) and (10*(float(AOOPW)) % 1 == 0)): 
                            self.INVALID.setVisible(False)
                            # open to the file and write the inputed numbers              
                            db = open("AOO.txt", "w")
                            db.write(AOOLRL + "\n" + AOOUP  + "\n" +AOOAA + "\n" + AOOPW)
                            print("Success")
                            db.close()
                        else:
                            self.INVALID.setVisible(True)  
                            
                    else: 
                        self.INVALID.setVisible(True)
                else: 
                    self.INVALID.setVisible(True)
            else: 
                self.INVALID.setVisible(True)
        except: 
            self.INVALID.setVisible(True)  

    def backfunction(self):
        back = Dash()
        widget.addWidget(back)
        widget.setCurrentIndex(widget.currentIndex()+1)

class AAI(QDialog):
    def __init__(self):
        super(AAI, self).__init__()
        loadUi("AAI.ui", self)
        self.AAIsubmit.clicked.connect(self.AAIinputfunction)
        self.INVALID.setVisible(False)
        self.backbutton.clicked.connect(self.backfunction)
        widget.setFixedWidth(900)
        widget.setFixedHeight(670)

    def AAIinputfunction (self):
        AAILRL = self.AAILRL.text()
        AAIURL = self.AAIURL.text()
        AAIAW = self.AAIAA.text()
        AAIAPW = self.AAIAPW.text()
        AAIAS = self.AAIAS.text()
        AAIARP = self.AAIARP.text()
        AAIPVARP = self.AAIPVARP.text()
        AIIH = self.AIIH.text()
        AAIRS = self.AAIRS.text()
        try:
            # ranges for the voo. If range is not met then show invalid error
            if ((((float(AAILRL)) >= 30) and ((float(AAILRL)) <= 49) and (float(AAILRL) % 5 == 0))) or ((((float(AAILRL)) >= 50) and ((float(AAILRL)) <= 90) and (float(AAILRL) % 1 == 0))) or ((((float(AAILRL)) >= 91) and ((float(AAILRL)) <= 175) and (float(AAILRL) % 5 == 0))):
                if(((float(AAIURL)) >= 50) and (float(AAIURL)) <=175) and (float(AAIURL) % 5 == 0):
                    if((((float(AAIAW)) >= 0.5) and (float(AAIAW)) <=3.2) and (10*(float(AAIAW)) % 1 == 0))  or (((float(AAIAW)) >= 3.5) and ((float(AAIAW)) <=7) and(10*(float(AAIAW)) % 5 ==0)):
                        if((((((float(AAIAPW)) >= 0.1) and (float(AAIAPW)) <=1.9) and (10*(float(AAIAPW)) % 1 == 0) or (float(AAIAPW)) == 0.5))): 
                            if(((float(AAIAS) == 0.25 or (0.50) or (0.75))) or ((float(AAIAS) >= 0.001) and ((float(AAIAS) <= 0.01) and (10*(float(AAIAS)) % 5 == 0)))):
                                if( ((float(AAIARP) >= 150) and ((float(AAIARP) <= 500) and ((float(AAIARP)) % 10 == 0)))):
                                    if( ((float(AAIPVARP) >= 150) and ((float(AAIPVARP) <= 500) and ((float(AAIPVARP)) % 10 == 0)))):
                                        if (((((float( AIIH)) >= 30) and ((float( AIIH)) <= 49) and (float( AIIH) % 5 == 0))) or ((((float( AIIH)) >= 50) and ((float( AIIH)) <= 90) and (float( AIIH) % 1 == 0))) or ((((float( AIIH)) >= 91) and ((float(AIIH)) <= 175) and (float(AIIH) % 5 == 0))) or ((float(AIIH) == 0))):   
                                            if( ((float(AAIRS) >= 0) and ((float(AAIRS) <= 21) and ((float(AAIRS)) % 3 == 0)))):  
                                                self.INVALID.setVisible(False)
                                                 # open to the file and write the inputed numbers              
                                                db = open("AAI.txt", "w")
                                                db.write(AAILRL + "\n" + AAIURL + "\n" + AAIAW + "\n" + AAIAPW + "\n" + AAIAS + "\n" + AAIARP + "\n" + AAIPVARP + "\n" + AIIH + "\n" + AAIRS)
                                        
                                                print("Success")
                                                db.close()
                        
                                            else:
                                                self.INVALID.setVisible(True)
                                        
                                        else:
                                            self.INVALID.setVisible(True)
                                    else:
                                        self.INVALID.setVisible(True)
                                
                                else: 
                                    self.INVALID.setVisible(True)        
                            else:
                                self.INVALID.setVisible(True)
                        
                        else:
                             self.INVALID.setVisible(True)  
                                
                    else: 
                        self.INVALID.setVisible(True)
                else: 
                    self.INVALID.setVisible(True)
            else: 
                self.INVALID.setVisible(True)
        except: 
            self.INVALID.setVisible(True)  

    def backfunction(self):
        back = Dash()
        widget.addWidget(back)
        widget.setCurrentIndex(widget.currentIndex()+1)

class VVI(QDialog):
    def __init__(self):
        super(VVI, self).__init__()
        loadUi("VVI.ui", self)
        self.INVALID.setVisible(False)
        self.VVIsubmitbutton.clicked.connect(self.VVIinputfunction)
        self.backbutton.clicked.connect(self.backfunction)
        widget.setFixedWidth(900)
        widget.setFixedHeight(830)
       
    def VVIinputfunction(self):
        VVILRL = self.VVILRL.text()
        VVIURL = self.VVIURL.text()
        VVIVA = self.VVIVA.text()
        VVIVPW = self.VVIVPW.text()
        VVIVS = self.VVIVS.text()
        VVIVRP = self.VVIVRP.text()
        VVIH = self.VVIH.text()
        VVIRS = self.VVIRS.text()
        try:
            # ranges for the voo. If range is not met then show invalid error
            if ((((float(VVILRL)) >= 30) and ((float( VVILRL)) <= 49) and (float(VVILRL) % 5 == 0))) or ((((float(VVILRL)) >= 50) and ((float(VVILRL)) <= 90) and (float(VVILRL) % 1 == 0))) or ((((float(VVILRL)) >= 91) and ((float(VVILRL)) <= 175) and (float(VVILRL) % 5 == 0))):
                if(((float(VVIURL)) >= 50) and (float( VVIURL)) <=175) and (float(VVIURL) % 5 == 0):
                    if((((float(VVIVA)) >= 0.5) and (float(VVIVA)) <=3.2) and (10*(float(VVIVA)) % 1 == 0))  or (((float(VVIVA)) >= 3.5) and ((float(VVIVA)) <=7) and(10*(float(VVIVA)) % 5 ==0)):
                        if(((((float(VVIVPW)) >= 0.1) and (float(VVIVPW)) <=1.9) and (10*(float(VVIVPW)) % 1 == 0)) or (float(VVIVPW)) == 0): 
                            if(((float(VVIVS) == 0.25 or (0.50) or (0.75))) or ((float(VVIVS) >= 0.001) and ((float(VVIVS) <= 0.01) and (10*(float(VVIVS)) % 5 == 0)))):
                                if( ((float(VVIVRP) >= 150) and ((float(VVIVRP) <= 500) and ((float(VVIVRP)) % 10 == 0)))):
                                    if (((((float(VVIH)) >= 30) and ((float(VVIH)) <= 49) and (float(VVIH) % 5 == 0))) or ((((float(VVIH)) >= 50) and ((float( VVIH)) <= 90) and (float(VVIH) % 1 == 0))) or ((((float(VVIH)) >= 91) and ((float(VVIH)) <= 175) and (float(VVIH) % 5 == 0))) or ((float(VVIH) == 0))):   
                                        if(((float(VVIRS) >= 0) and ((float(VVIRS) <= 21) and ((float(VVIRS)) % 3 == 0)))):  
                                          
                                                self.INVALID.setVisible(False)
                                                 # open to the file and write the inputed numbers              
                                                db = open("VVI.txt", "w")
                                                db.write(VVILRL + "\n" + VVIURL + "\n" + VVIVA + "\n" + VVIVPW + "\n" + VVIVS + "\n" + VVIVRP + "\n" + VVIH + "\n" + VVIRS )
                                                print("Success")
                                                db.close()
                        
                                           
                                        
                                        else:
                                            self.INVALID.setVisible(True)
                                    else:
                                        self.INVALID.setVisible(True)
                                
                                else: 
                                    self.INVALID.setVisible(True)        
                            else:
                                self.INVALID.setVisible(True)
                        
                        else:
                             self.INVALID.setVisible(True)  
                                
                    else: 
                        self.INVALID.setVisible(True)
                else: 
                    self.INVALID.setVisible(True)
            else: 
                self.INVALID.setVisible(True)
        except: 
            self.INVALID.setVisible(True)  
        
    def backfunction(self):
        back = Dash()
        widget.addWidget(back)
        widget.setCurrentIndex(widget.currentIndex()+1)

class AOOR(QDialog):
    def __init__(self):
        super(AOOR, self).__init__()
        loadUi("AOOR.ui", self)
        self.INVALID.setVisible(False)
        # self.AOORsubmitbutton.clicked.connect(self.AOORinputfunction)
        # self.backbutton.clicked.connect(self.backfunction)
        widget.setFixedWidth(900)
        widget.setFixedHeight(700)

    # def backfunction(self):
    # back = Dash()
    # widget.addWidget(back)
    # widget.setCurrentIndex(widget.currentIndex()+1)

# class VOOR(QDialog):
#     def __init__(self):
#         super(VOOR, self).__init__()
#         loadUi("VOOR.ui", self)
#         self.INVALID.setVisible(False)
#         self.VVIsubmitbutton.clicked.connect(self.AOORinputfunction) FIX SUBMIT BUTTON NAME FOR ALL AND INPUT FUNCTION NAME
#         self.backbutton.clicked.connect(self.backfunction)
#         widget.setFixedWidth(900)
#         widget.setFixedHeight(830)

# class AAIR(QDialog):
#     def __init__(self):
#         super(AAIR, self).__init__()
#         loadUi("AAIR.ui", self)
#         self.INVALID.setVisible(False)
#         self.VVIsubmitbutton.clicked.connect(self.AOORinputfunction)
#         self.backbutton.clicked.connect(self.backfunction)
#         widget.setFixedWidth(900)
#         widget.setFixedHeight(830)

class VVIR(QDialog):
    def __init__(self):
        super(VVIR, self).__init__()
        loadUi("VVIR.ui", self)
        # self.INVALID.setVisible(False)
        # self.VVIsubmitbutton.clicked.connect(self.AOORinputfunction)
        # self.backbutton.clicked.connect(self.backfunction)
        # widget.setFixedWidth(900)
        # widget.setFixedHeight(830)




app = QApplication(sys.argv)
mainwindow = Mainscreen()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.show()

app.exec()
