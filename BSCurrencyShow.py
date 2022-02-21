from connection import connection
from mainWindowShowFunc import MainWindowShowFunc

class BSCurrencyShow():
    def __init__(self, user):
        self.user = user
        self.connection = connection
        self.mydb = self.connection.cursor()
    #db den dolar ve euro miktarını yazdırıyor
    def showUSD(self):
        result = MainWindowShowFunc(self.user).connection()
        person_id = result[0]
        query = "SELECT * FROM accounts WHERE person_id = %s"
        value = (person_id,)
        self.mydb.execute(query,value)
        result2 = self.mydb.fetchone()
        showMoney = str(result2[5]) + " $"
        return showMoney

    def showEUR(self):
        result = MainWindowShowFunc(self.user).connection()
        person_id = result[0]
        query = "SELECT * FROM accounts WHERE person_id = %s"
        value = (person_id,)
        self.mydb.execute(query,value)
        result2 = self.mydb.fetchone()
        showMoney = str(result2[6]) + " €"
        return showMoney
    