from connection import connection

class MainWindowShowFunc():
    def __init__(self, user):
        self.user = user
    #user adından info id alınıyor 
    def connection(self):
        self.connection = connection
        self.mydb = self.connection.cursor()
        query = "SELECT * FROM information WHERE username = %s"
        value = (self.user,)
        self.mydb.execute(query,value)
        result = self.mydb.fetchone()
        info_id = result[0]
        query2 = "SELECT * FROM person WHERE info_id = %s"
        value2 = (info_id,)
        self.mydb.execute(query2, value2)
        return self.mydb.fetchone()
    # info id den kullanıcı adı soy adı
    def showname(self):
        result2 = self.connection()
        nameSurname = result2[2] + " " + result2[3]
        return nameSurname
    #info idden person idsi person idden de acount amount alınıyor
    def showmoney(self):
        result = self.connection()
        person_id = result[0]
        query = "SELECT * FROM accounts WHERE person_id = %s"
        value = (person_id,)
        self.mydb.execute(query,value)
        result2 = self.mydb.fetchone()
        showMoney = str(result2[4]) + " TL"
        return showMoney

    def showiban(self):
        result = self.connection()
        person_id = result[0]
        query = "SELECT iban FROM accounts WHERE  person_id = %s"
        value = (person_id,)
        self.mydb.execute(query,value)
        result2 = self.mydb.fetchone()
        return str(result2[0])