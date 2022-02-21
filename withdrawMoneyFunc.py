from connection import connection 
from mainWindowShowFunc import MainWindowShowFunc
from logs import Logs
import time

class WithdrawMoneyFunc():
    def __init__(self, user, money):
        self.user = user
        self.money = money

    def withdraw(self):
        result = MainWindowShowFunc(self.user).connection()
        person_id = result[0]
        self.connection = connection
        self.mydb = self.connection.cursor()
        query = "SELECT amountTL FROM accounts WHERE person_id = %s"
        value = (person_id,)
        self.mydb.execute(query,value)
        result2 = self.mydb.fetchone()
        #çekilmek istenen para hesaptaki bakiyeden düşükse hata

        if len(self.money) == 0:
            msg = "Boş bırakmayın"
            return msg
        else:
            if int(self.money) > int(result2[0]):
                msg = "Yetersiz bakiye"
                return msg

            else:
                    # hatasız ise bakiyeden girilen para çıkartılıyor
                amount = int(result2[0]) - int(self.money)
                query2 = "UPDATE accounts SET amountTL = %s WHERE person_id = %s"
                values = (amount, person_id)
                self.mydb.execute(query2, values)
                self.connection.commit()
                Logs(time.localtime(), "Para çekimi", self.user).getLog()
                return 1