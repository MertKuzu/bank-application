from connection import connection
from mainWindowShowFunc import MainWindowShowFunc
from CurrencyApi import CurrencyApi
from logs import Logs
import time

class BuyCurrencyFunc():
    def __init__(self, user, amount, currency):
        self.user = user
        self.amount = amount
        self.currency = currency
        self.connection = connection
        self.mydb = self.connection.cursor()

    def buyCurrency(self):
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

            if int(result2[4]) < int(self.amount):
                msg = "Yetersiz bakiye"
                return msg
            else:
                    #kur alınıyor alınan kurla girilen miktar çarpılıyor döviz alımı gerçekleşiyor
                price = CurrencyApi(self.currency).callCurrencyBuying()
                total = float(price) * float(self.amount)
                result3 = float(result2[4]) - float(self.amount)
                if self.currency == "usd":
                    query = "UPDATE accounts SET amountTL = %s, amountUSD = %s WHERE person_id = %s"
                    newmoney = float(total)+float(result2[5])
                else:
                    query = "UPDATE accounts SET amountTL = %s, amountEUR = %s WHERE person_id = %s"
                    newmoney = float(total) + float(result2[6])
                values = (result3, newmoney, person_id)
                self.mydb.execute(query,values)
                self.connection.commit()
                Logs(time.localtime(), "Döviz alımı", self.user).getLog()
                return 1
