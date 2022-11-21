import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUi
from numpy import loadtxt
# import AOO
# good = AOO
import numpy as np
import math

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

        if any(substring in username for substring in invalid) or any(substring in password for substring in invalid):
            print("Invalid username")
            print("Invalid password")
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
        # VOOLRL = self.LRL.text()
        VOOUP = voo.UPLIMIT.text()
        # VOOVPW = self.VPW.text()
       
            #voo.UPLIMIT = QLabel(self)
            # load the numbers from the textfile as an array
        try:
            with open('VOOLRL.txt', 'r') as file:
                datasVOO = file.read()
            datasVOOvalues = datasVOO.split("\n")
          
            a = datasVOOvalues[0]
            voo.LRL.setText(str(a))
           
            b = datasVOOvalues[1]
            voo.UPLIMIT.setText(str(b))
           
            c = datasVOOvalues[3]
            voo.VPW.setText(str(c))
           
            d = datasVOOvalues[2]
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
            with open('AOO.txt', 'r') as file:
                datasAOO = file.read()
            datasAOOvalues = datasAOO.split("\n")
           
            aAOO = datasAOOvalues[0]
            aoo.AOOLRL.setText(str(aAOO))
           
            bAOO = datasAOOvalues[1]
            aoo.AOOUP.setText(str(bAOO))
            
            cAOO = datasAOOvalues[3]
            aoo.AOOPW.setText(str(cAOO))
           
            dAOO = datasAOOvalues[2]
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
            with open('AAI.txt', 'r') as file:
                 datasAAI = file.read()
            datasAAIvalues = datasAAI.split("\n")
            
            
            aaAAI = datasAAIvalues[0]
            aai.AAILRL.setText(str(aaAAI))

            
            aAAI = datasAAIvalues[1]
            aai.AAIURL.setText(str(aAAI))

            
            iAAI = datasAAIvalues[2]
            aai.AAIAA.setText(str(iAAI))

    
            cAAI = datasAAIvalues[3]
            aai.AAIAPW.setText(str(cAAI))
            
            dAAI = datasAAIvalues[4]
            aai.AAIAS.setText(str(dAAI))
           
            eAAI = datasAAIvalues[5]
            aai.AAIARP.setText(str(eAAI))
           
            fAAI = datasAAIvalues[6]
            aai.AAIPVARP.setText(str(fAAI))
           
            gAAI = datasAAIvalues[7]
            aai.AIIH.setText(str(gAAI))
           
            hAAI = datasAAIvalues[8]
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
            with open('VVI.txt', 'r') as file:
                 datasVVI = file.read()
            datasVVIvalues = datasVVI.split("\n")
         
       
            aaVVI = datasVVIvalues[0]
            vvi.VVILRL.setText(str(aaVVI))
         
            aVVI = datasVVIvalues[1]
            vvi.VVIURL.setText(str(aVVI))

            
            iVVI = datasVVIvalues[2]
            vvi.VVIVA.setText(str(iVVI))

         
            cVVI = datasVVIvalues[3]
            vvi.VVIVPW.setText(str(cVVI))
            
           
            dVVI = datasVVIvalues[4]
            vvi.VVIVS.setText(str(dVVI))
            
           
            eVVI = datasVVIvalues[5]
            vvi.VVIVRP.setText(str(eVVI))
           
            fVVI = datasVVIvalues[6]
            vvi.VVIH.setText(str(fVVI))
           
            gVVI = datasVVIvalues[7]
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
            


    def logoutfunction(self):
        logout = Mainscreen()
        widget.setFixedWidth(500)
        widget.setFixedHeight(500)
        widget.addWidget(logout)
        print ("Account Logged Out") #self.message.setVisible(True)
       
        widget.setCurrentIndex(widget.currentIndex()+1) 
        with open("VVI.txt", 'r+') as file:
            file.truncate(0)
        with open("AAI.txt", 'r+') as file:
            file.truncate(0)
        with open("AOO.txt", 'r+') as file:
            file.truncate(0)
        with open("VOOLRL.txt", 'r+') as file:
            file.truncate(0)
   


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
            if ((((int(VOOLRL)) >= 30) and ((int(VOOLRL)) <= 49) and (int(VOOLRL) % 5 == 0))) or ((((int(VOOLRL)) >= 50) and ((int(VOOLRL)) <= 89) and (int(VOOLRL) % 1 == 0))) or ((((int(VOOLRL)) >= 90) and ((int(VOOLRL)) <= 175) and (int(VOOLRL) % 5 == 0))):
                if(((int(VOOUP)) >= 50) and (int(VOOUP)) <=175) and (int(VOOUP) % 5 == 0):
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
            if ((((int(AOOLRL)) >= 30) and ((int(AOOLRL)) <= 49) and (int(AOOLRL) % 5 == 0))) or (((int((AOOLRL)) >= 50) and ((int(AOOLRL)) <= 90) and (int(AOOLRL) % 1 == 0))) or ((((int(AOOLRL)) >= 91) and ((int(AOOLRL)) <= 175) and (int(AOOLRL) % 5 == 0))):
                if(((int(AOOUP)) >= 50) and (int(AOOUP)) <=175) and (int(AOOUP) % 5 == 0):
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
            if ((((int(AAILRL)) >= 30) and ((int(AAILRL)) <= 49) and (int(AAILRL) % 5 == 0))) or ((((int(AAILRL)) >= 50) and ((int(AAILRL)) <= 90) and (int(AAILRL) % 1 == 0))) or ((((int(AAILRL)) >= 91) and ((int(AAILRL)) <= 175) and (int(AAILRL) % 5 == 0))):
                if(((int(AAIURL)) >= 50) and (int(AAIURL)) <=175) and (int(AAIURL) % 5 == 0):
                    if((((float(AAIAW)) >= 0.5) and (float(AAIAW)) <=3.2) and (10*(float(AAIAW)) % 1 == 0))  or (((float(AAIAW)) >= 3.5) and ((float(AAIAW)) <=7) and(10*(float(AAIAW)) % 5 ==0)):
                        if((((((float(AAIAPW)) >= 0.1) and (float(AAIAPW)) <=1.9) and (10*(float(AAIAPW)) % 1 == 0) or (float(AAIAPW)) == 0.5))): 
                            if(((float(AAIAS) == 0.25 or (0.50) or (0.75))) or ((float(AAIAS) >= 0.001) and ((float(AAIAS) <= 0.01) and (10*(float(AAIAS)) % 5 == 0)))):
                                if( ((int(AAIARP) >= 150) and ((int(AAIARP) <= 500) and ((int(AAIARP)) % 10 == 0)))):
                                    if( ((int(AAIPVARP) >= 150) and ((int(AAIPVARP) <= 500) and ((int(AAIPVARP)) % 10 == 0)))):
                                        if (((((int( AIIH)) >= 30) and ((int( AIIH)) <= 49) and (int( AIIH) % 5 == 0))) or ((((int( AIIH)) >= 50) and ((int( AIIH)) <= 89) and (int( AIIH) % 1 == 0))) or ((((int( AIIH)) >= 90) and ((int(AIIH)) <= 175) and (int(AIIH) % 5 == 0))) or ((int(AIIH) == 0))):   
                                            if( ((int(AAIRS) >= 0) and ((int(AAIRS) <= 21) and ((int(AAIRS)) % 3 == 0)))):  
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
            if ((((int(VVILRL)) >= 30) and (int(VVILRL)) <= 49) and (int(VVILRL) % 5 == 0)) or ((((int(VVILRL)) >= 50) and (int(VVILRL)) <= 89) and (int(VVILRL) % 1 == 0)) or (((int((VVILRL)) >= 90) and ((int(VVILRL)) <= 175) and (int(VVILRL) % 5 == 0))):
                if(((int(VVIURL)) >= 50) and (int( VVIURL)) <=175) and (int(VVIURL) % 5 == 0):
                    if((((float(VVIVA)) >= 0.5) and (float(VVIVA)) <=3.2) and (10*(float(VVIVA)) % 1 == 0))  or (((float(VVIVA)) >= 3.5) and ((float(VVIVA)) <=7) and(10*(float(VVIVA)) % 5 ==0)):
                        if(((((float(VVIVPW)) >= 0.1) and (float(VVIVPW)) <=1.9) and (10*(float(VVIVPW)) % 1 == 0)) or (float(VVIVPW)) == 0): 
                            if(((float(VVIVS) == 0.25 or (0.50) or (0.75))) or ((float(VVIVS) >= 0.001) and ((float(VVIVS) <= 0.01) and (10*(float(VVIVS)) % 5 == 0)))):
                                if( ((int(VVIVRP) >= 150) and ((int(VVIVRP) <= 500) and ((int(VVIVRP)) % 10 == 0)))):
                                    if (((((int(VVIH)) >= 30) and ((int(VVIH)) <= 49) and (int(VVIH) % 5 == 0))) or ((((int(VVIH)) >= 50) and ((int( VVIH)) <= 89) and (int(VVIH) % 1 == 0))) or ((((int(VVIH)) >= 90) and ((int(VVIH)) <= 175) and (int(VVIH) % 5 == 0))) or ((int(VVIH) == 0))):   
                                        if(((int(VVIRS) >= 0) and ((int(VVIRS) <= 21) and ((int(VVIRS)) % 3 == 0)))):  
                                          
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




app = QApplication(sys.argv)
mainwindow = Mainscreen()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.show()

app.exec()

