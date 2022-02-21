from connection import connection
from mainWindowShowFunc import MainWindowShowFunc
from logs import Logs
import time


class TransferMoneyFunc():
    def __init__(self, user, iban, money):
        self.user = user
        self.iban = iban
        self.money = money

    def transfer(self):
        result = MainWindowShowFunc(self.user).connection()
        person_id = result[0]
        self.connection = connection
        self.mydb = self.connection.cursor()
        query = "SELECT amountTL FROM accounts WHERE person_id = %s"
        value = (person_id,)
        self.mydb.execute(query, value)
        result2 = self.mydb.fetchone()
        query2 = "SELECT amountTL FROM accounts WHERE iban = %s"
        value2 = (self.iban,)
        self.mydb.execute(query2, value2)
        reciver = self.mydb.fetchone()
        #alıcı ve gönderen paraları bir değişkene aktarılıyor
        #eğer alıcı olarak değer dönmezse error dönüyor
        if len(self.money) == 0:
            msg = "Boş bırakmayın"
            return msg
        else:
            if reciver is None:
                msg = "Hatalı iban"
                return msg
            else:
                #girilen para bakiyeden düşük ise hata
                if int(result2[0]) < int(self.money):
                    msg = "Yetersiz bakiye"
                    return msg
                else:
                    #eğer her şey hatasız ise gönderenden girilen para çıkarılıyor alıcıya ekleniyor
                    amount = int(result2[0]) - int(self.money)

                    query = "UPDATE accounts SET amountTL = %s WHERE person_id = %s"
                    values = (amount, person_id)
                    self.mydb.execute(query, values)
                    self.connection.commit()

                    amount2 = int(reciver[0]) + int(self.money)

                    query2 = "UPDATE accounts SET amountTL = %s WHERE iban = %s"
                    values2 = (amount2, self.iban)
                    self.mydb.execute(query2, values2)
                    self.connection.commit()
                    Logs(time.localtime(), f"{self.iban} ibana para gönderimi", self.user).getLog()
                    return 1