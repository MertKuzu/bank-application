from connection import connection
import random


class createIban():
    #iban yaratma
    def createIban(self):
        self.connection = connection
        self.mydb = self.connection.cursor()

        iban = random.randint(1000001,9999999)

        query = "SELECT * FROM accounts WHERE iban = %s"
        value = (iban,)
        self.mydb.execute(query, value)
        result = self.mydb.fetchone()

        while True:
            if result is None:
                return iban
            else:
                iban = iban = random.randint(1000001,9999999)
            