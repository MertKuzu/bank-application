import sys
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QDialog, QApplication, QStackedWidget, QLineEdit
from PyQt5.QtGui import QIcon
from buyCurrencyFunc import BuyCurrencyFunc
from loginFunc import LoginFunc
from registerFunc import RegisterFunc
from personelInfoRegister import PersonInfoRegister
from forgotPasswordFunc import ForgotPasswordFunc
from mainWindowShowFunc import MainWindowShowFunc
from depositMoneyFunc import DepositMoneyFunc
from transferMoneyFunc import TransferMoneyFunc
from withdrawMoneyFunc import WithdrawMoneyFunc
from BSCurrencyShow import BSCurrencyShow
from CurrencyApi import CurrencyApi
from sellCurrencyFunc import SellCurrencyFunc
from logs import Logs
import time



class WelcomeScreen(QDialog):
    
    def __init__(self):
        super(WelcomeScreen, self).__init__()
        loadUi("UI_Welcome.ui", self)
        self.login.clicked.connect(self.gotoLogin)  #ilk sayfadaki giriş yapa tıklayınca gotoLogin fonksiyonuna yönleniyor
        self.registe.clicked.connect(self.gotoRegister)

    def gotoLogin(self):    #Login classı çağırılıp pencere değişiyor 
        login = Login()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def gotoRegister(self):    #Register classı çağırılıp pencere değişiyor
        register = Register()
        widget.addWidget(register)
        widget.setCurrentIndex(widget.currentIndex()+1)

class Login(QDialog):
    def __init__(self):     #Login penceresindeki butonlar tanımlanıyor
        super(Login, self).__init__()
        loadUi("UI_Login.ui",self)
        self.password.setEchoMode(QLineEdit.Password)
        self.login.clicked.connect(self.gotoLoginFunc)
        self.registerhere.clicked.connect(self.gotoRegister)
        self.turnback.clicked.connect(self.gotoWelcome)
        self.forgotpass.clicked.connect(self.gotoForgotPassword)

    def gotoLoginFunc(self):
        user = self.username.text()
        password = self.password.text()
        login = LoginFunc()      #butona bastıktan sonra ayrı dosyadaki arka plan işleri dönüyor
        if login.login(user,password) != 1:
            self.error.setText(login.login(user,password))
        else:
            main = MainWindow(user)
            widget.addWidget(main)
            widget.setCurrentIndex(widget.currentIndex()+1)
    
    def gotoRegister(self):
        WelcomeScreen().gotoRegister()

    def gotoWelcome(self):
        Register2().gotoWelcomeWindow()

    def gotoForgotPassword(self):
        forgotPassword = ForgotPasswordScreen()
        widget.addWidget(forgotPassword)
        widget.setCurrentIndex(widget.currentIndex()+1)


#Register penceresindeki butonlar tanımlanıyor
class Register(QDialog):
    def __init__(self):
        super(Register, self).__init__()
        loadUi("UI_Register.ui", self)
        self.password.setEchoMode(QLineEdit.Password)
        self.password_2.setEchoMode(QLineEdit.Password)
        self.continueReg.clicked.connect(self.gotoRegisterFunc)
        self.turnback.clicked.connect(self.gotoWelcome)

    def gotoRegisterFunc(self):
        global username
        username = self.username.text()
        password = self.password.text()
        password2 = self.password_2.text()
        register = RegisterFunc()      #butona bastıktan sonra ayrı dosyadaki arka plan işleri dönüyor
        if register.register(username, password, password2) != 1:
            self.error.setText(register.register(username,password,password2))
        else:
            register2 = Register2()
            widget.addWidget(register2)
            widget.setCurrentIndex(widget.currentIndex()+1)     #kullanıcı adı mevcut değilse ona göre değer returnleniyor ve kişisel bilgileri kaydetme penceresine yönlendiriyor

    def gotoWelcome(self):
        Register2().gotoWelcomeWindow()


#kişisel verilerin alındığı class buttonlar tanımlanıyor
class Register2(QDialog):
    def __init__(self):
        super(Register2, self).__init__()
        loadUi("UI_Register_2.ui",self)
        self.reg.clicked.connect(self.register)

    def register(self):
        name = self.name.text()
        surname = self.surname.text()
        tckn = self.tckn.text()
        adress = self.adress.text()
        birthdate = self.birthdate.text()
        gender = self.gender.currentText()
        personalInfoRegister = PersonInfoRegister()    #bu verilerin kaydedilme işlemi bu class ile
        if personalInfoRegister.personInfoRegister(name, surname, tckn, adress, birthdate, gender, username) != 1:
            self.error.setText(personalInfoRegister.personInfoRegister(name, surname, tckn, adress, birthdate, gender, username))
        else:
            self.gotoWelcomeWindow()
    #üyelik başarılı şekilde gerçekleşince welcome ekranına geri yolluyor
    def gotoWelcomeWindow(self):
        win = WelcomeScreen()
        widget.addWidget(win)
        widget.setCurrentIndex(widget.currentIndex()+1)

class ForgotPasswordScreen(QDialog):
    def __init__(self):
        # gui ve butonların tanımı
        super(ForgotPasswordScreen, self).__init__()
        loadUi("UI_ForgotPassword.ui", self)
        self.turnback.clicked.connect(self.gotoLogin)
        self.change.clicked.connect(self.gotoChange)
        self.password.setEchoMode(QLineEdit.Password)
        self.password_2.setEchoMode(QLineEdit.Password)

    def gotoChange(self):
        # labellardan alınan bilgiler gerekli classa gönderilip işleme sokuluyor
        tckn = self.tckn.text()
        password = self.password.text()
        password2 = self.password_2.text()
        if ForgotPasswordFunc(tckn, password, password2).forgotPassword() != 1:
            self.error.setText(ForgotPasswordFunc(tckn, password, password2).forgotPassword())
        else:
            self.gotoLogin()
            self.error.setText("Parola değiştirildi.")

    def gotoLogin(self):
        WelcomeScreen().gotoLogin()

class MainWindow(QDialog):
    # butonların tanımlanması 
    def __init__(self, user):
        super(MainWindow, self).__init__()
        loadUi("UI_Main.ui",self)
        self.user = user
        self.showname.setText(MainWindowShowFunc(self.user).showname())
        self.showmoney.setText(MainWindowShowFunc(self.user).showmoney())
        self.iban.setText(MainWindowShowFunc(self.user).showiban())
        self.showmoneyusd.setText(BSCurrencyShow(self.user).showUSD())
        self.showmoneyeur.setText(BSCurrencyShow(self.user).showEUR())
        self.exit.clicked.connect(self.gotoWelcome)
        self.depositmoney.clicked.connect(self.gotoDepositMoney)
        self.withdrawmoney.clicked.connect(self.gotoWithdrawMoney)
        self.sendmoney.clicked.connect(self.gotoTransferMoney)
        self.currencybs.clicked.connect(self.gotoCurrencyBS)
        self.sellcur.clicked.connect(self.gotoSellCur)

    def gotoWelcome(self):
        Logs(time.localtime(), "Çıkış yapıldı", self.user).getLog()
        Register2().gotoWelcomeWindow()

    def gotoDepositMoney(self):
        depositmoney = DepositMoney(self.user)
        widget.addWidget(depositmoney)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def gotoWithdrawMoney(self):
        withdrawmoney = WithdrawMoney(self.user)
        widget.addWidget(withdrawmoney)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def gotoTransferMoney(self):
        transfermoney = TransferMoney(self.user)
        widget.addWidget(transfermoney)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def gotoCurrencyBS(self):
        currencybs = BSCurrency(self.user)
        widget.addWidget(currencybs)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def gotoSellCur(self):
        sellcurrency = SellCurrency(self.user)
        widget.addWidget(sellcurrency)
        widget.setCurrentIndex(widget.currentIndex()+1)


class DepositMoney(QDialog):
    def __init__(self, user):
        #butonların tanımlanması
        super(DepositMoney, self).__init__()
        loadUi("UI_DepositMoney.ui",self)
        self.user = user
        self.deposit.clicked.connect(self.gotoDeposit)
        self.turnback.clicked.connect(self.gotoMain)
        self.showmoney.setText(MainWindowShowFunc(self.user).showmoney())

    def gotoDeposit(self):
        depositmoney = self.entermoney.text()
        if DepositMoneyFunc(self.user, depositmoney).deposit() != 1:
            self.error.setText(DepositMoneyFunc(self.user, depositmoney).deposit())
        else:
            self.gotoMain()

    def gotoMain(self):
        main = MainWindow(self.user)
        widget.addWidget(main)
        widget.setCurrentIndex(widget.currentIndex()+1)

class WithdrawMoney(QDialog):
    #butonların tanımlanması
    def __init__(self, user):
        super(WithdrawMoney, self).__init__()
        loadUi("UI_WithdrawMoney.ui",self)
        self.user = user
        self.turnback.clicked.connect(self.gotoMain)
        self.withdraw.clicked.connect(self.gotoWithdraw)
        self.showmoney.setText(MainWindowShowFunc(self.user).showmoney())

    def gotoMain(self):
        DepositMoney(self.user).gotoMain()

    def gotoWithdraw(self):
        withdrawmoney = self.entermoney.text()
        if WithdrawMoneyFunc(self.user, withdrawmoney).withdraw() != 1:
            self.error.setText(WithdrawMoneyFunc(self.user, withdrawmoney).withdraw())
        else:
            self.gotoMain()

class TransferMoney(QDialog):
    #butonların tanımlanması
    def __init__(self, user):
        super(TransferMoney, self).__init__()
        loadUi("UI_SendMoney.ui",self)
        self.user = user
        self.showmoney.setText(MainWindowShowFunc(self.user).showmoney())
        self.turnback.clicked.connect(self.gotoMain)
        self.send.clicked.connect(self.gotoTransfer)

    def gotoMain(self):
        DepositMoney(self.user).gotoMain()

    def gotoTransfer(self):
        transfermoney = self.entermoney.text()
        iban = self.enteriban.text()
        if TransferMoneyFunc(self.user, iban, transfermoney).transfer() != 1:
            self.error.setText(TransferMoneyFunc(self.user, iban, transfermoney).transfer())
        else:
            self.gotoMain()

class BSCurrency(QDialog):
    def __init__(self, user):
        super(BSCurrency, self).__init__()
        loadUi("UI_BSCurrency.ui", self)
        self.user = user
        self.turnback.clicked.connect(self.gotoMain)
        self.showmoneytl.setText(MainWindowShowFunc(self.user).showmoney())
        self.showmoneyusd.setText(BSCurrencyShow(self.user).showUSD())
        self.showmoneyeur.setText(BSCurrencyShow(self.user).showEUR())
        self.showusdcur.setText("USD: "+str(CurrencyApi("usd").callCurrencySelling())+" TL")
        self.showeurcur.setText("EUR: "+str(CurrencyApi("eur").callCurrencySelling())+" TL")
        self.buy.clicked.connect(self.gotoBuy)

    def gotoMain(self):
        DepositMoney(self.user).gotoMain()

    def gotoBuy(self):
        amount = self.entermoney.text()
        currency = self.selectcur.currentText()

        if BuyCurrencyFunc(self.user, amount, currency).buyCurrency() != 1:
            self.error.setText(str(BuyCurrencyFunc(self.user, amount, currency).buyCurrency()))
        else:
            self.gotoMain()

class SellCurrency(QDialog):
    def __init__(self, user):
        super(SellCurrency, self).__init__()
        loadUi("UI_SellCurrency.ui", self)
        self.user = user
        self.turnback.clicked.connect(self.gotoMain)
        self.showmoneytl.setText(MainWindowShowFunc(self.user).showmoney())
        self.showmoneyusd.setText(BSCurrencyShow(self.user).showUSD())
        self.showmoneyeur.setText(BSCurrencyShow(self.user).showEUR())
        self.showusdcur.setText("USD: "+str(CurrencyApi("usd").callCurrencySelling())+" TL")
        self.showeurcur.setText("EUR: "+str(CurrencyApi("eur").callCurrencySelling())+" TL")
        self.sell.clicked.connect(self.gotoSell)

    def gotoMain(self):
        DepositMoney(self.user).gotoMain()

    def gotoSell(self):
        amount = self.entermoney.text()
        currency = self.selectcur.currentText()

        if SellCurrencyFunc(self.user, amount, currency).sellCurrency() != 1:
            self.error.setText(str(SellCurrencyFunc(self.user, amount, currency).sellCurrency()))
        else:
            self.gotoMain()


        
#main

def app():
    global widget
    app = QApplication(sys.argv)
    win = WelcomeScreen()
    widget = QStackedWidget()
    widget.addWidget(win)
    widget.setFixedHeight(800)
    widget.setFixedWidth(1200)
    widget.setWindowTitle("Kuzu Bank")
    widget.setWindowIcon(QIcon("logo.png"))
    widget.show()
    sys.exit(app.exec_())

app()