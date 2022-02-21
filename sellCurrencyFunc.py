from connection import connection
from mainWindowShowFunc import MainWindowShowFunc
from CurrencyApi import CurrencyApi
from logs import Logs
import time


class SellCurrencyFunc():
    def __init__(self, user, amount, currency):
        self.user = user
        self.amount = amount
        self.currency = currency
        self.connection = connection
        self.mydb = self.connection.cursor()


    def sellCurrency(self):
        result = MainWindowShowFunc(self.user).connection()
        person_id = result[0]

        query = "SELECT * FROM accounts WHERE person_id = %s"
        value = (person_id,)
        self.mydb.execute(query, value)
        result2 = self.mydb.fetchone()

        if len(self.amount) == 0:
            msg = "Boş bırakmayın"
            return msg
        else:

            if self.currency == "usd":
                if int(result2[5]) < int(self.amount):
                    msg = "Yetersiz bakiye"
                    return msg
                else:
                    #girilen miktarla anlık kur çarpılıyor ve döviz satımı gerçekleşiyor gerekli değerler güncelleniyor
                    price = CurrencyApi(self.currency).callCurrencySelling()
                    total = float(price) * float(self.amount)
                    result3 = float(result2[5]) - float(self.amount)
                    newmoney = float(total) + float(result2[4])
                    query = "UPDATE accounts SET amountTL = %s, amountUSD = %s WHERE person_id = %s"
                    values = (newmoney, result3, person_id)
                    self.mydb.execute(query,values)
                    self.connection.commit()
                    Logs(time.localtime(), "Döviz satımı", self.user).getLog()
                    return 1
            else:
                if int(result2[6]) < int(self.amount):
                    msg = "Yetersiz bakiye"
                    return msg
                else:
                    price = CurrencyApi(self.currency).callCurrencySelling()
                    total = float(price) * float(self.amount)
                    result3 = float(result2[6]) - float(self.amount)
                    newmoney = float(total) + float(result2[4])
                    query = "UPDATE accounts SET amountTL = %s, amountEUR = %s WHERE person_id = %s"
                    values = (newmoney, result3, person_id)
                    self.mydb.execute(query,values)
                    self.connection.commit()
                    Logs(time.localtime(), "Döviz satımı", self.user).getLog()
                    return 1
