from connection import connection
from createIban import createIban

class CreateAccount():

    def __init__(self, person_id, account_type):
        self.person_id = person_id
        self.account_type = account_type
        

    def createAccount(self):
        self.connection = connection
        self.mydb = self.connection.cursor()
        self.iban = createIban().createIban()

        # hesap açımı için gerkli bilgileri db ye gönderip kaydediyor
        query = "INSERT INTO accounts(person_id, iban, account_type, amountTL, amountUSD, amountEUR) VALUES(%s,%s,%s,%s,%s,%s)"
        values = (self.person_id, self.iban, self.account_type, 0, 0, 0)
        self.mydb.execute(query,values)
        self.connection.commit()
