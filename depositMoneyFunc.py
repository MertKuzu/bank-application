from connection import connection
from mainWindowShowFunc import MainWindowShowFunc
from logs import Logs
import time


class DepositMoneyFunc():
    def __init__(self, user, money):
        self.user = user
        self.money = money
    # girilen para dbdeki amounta ekleniyor
    def deposit(self):
        if len(self.money) == 0:
            msg = "Boş bırakmayın"
            return msg
        else:
            result = MainWindowShowFunc(self.user).connection()
            person_id = result[0]
            self.connection = connection
            self.mydb = self.connection.cursor()
            query = "SELECT amountTL FROM accounts WHERE person_id = %s"
            value = (person_id,)
            self.mydb.execute(query,value)
            result2 = self.mydb.fetchone()
            amount = int(self.money) + int(result2[0])
            query2 = "UPDATE accounts SET amountTL = %s WHERE person_id = %s"
            values = (amount, person_id)
            self.mydb.execute(query2, values)
            self.connection.commit()
            Logs(time.localtime(), "Para yatırımı", self.user).getLog()
            return 1