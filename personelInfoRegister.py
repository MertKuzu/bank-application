from connection import connection
from createAccount import CreateAccount
import mysql.connector
from logs import Logs
import time

class PersonInfoRegister():

    def personInfoRegister(self, name, surname, tckn, adress, birthdate, gender, username):
        self.name = name
        self.surname = surname
        self.tckn = tckn
        self.adress = adress
        self.birthdate = birthdate
        self.gender = gender
        self.username = username
        #global varriable olan username ile infoid alınıyor dbden person tablosuna kayıt etmek için
        self.connection = connection
        self.mydb = self.connection.cursor()

        query = "SELECT * FROM information WHERE username = %s"
        value = (self.username,)
        self.mydb.execute(query, value)
        result = self.mydb.fetchone()
        self.infoid = result[0]
        #boş bırakılmış mı kontrolü 
        if len(self.name) == 0 or len(self.surname) == 0 or len(self.tckn) == 0 or len(self.adress) == 0:
            msg = "Lütfen boş alan bırakmayın."
            return msg

        else:
            try:
                query = "INSERT INTO person(tckn, name, surname, birthday, adress, info_id, gender) VALUES(%s,%s,%s,%s,%s,%s,%s)"
                values = (self.tckn, self.name, self.surname, self.birthdate, self.adress, self.infoid, self.gender)
                self.mydb.execute(query,values)
                self.connection.commit()
                query2 = "SELECT * FROM person WHERE info_id = %s"
                value2 = (self.infoid,)
                self.mydb.execute(query2,value2)
                result2 = self.mydb.fetchone()
                person_id = result2[0]   #account kime ait olduğunu belirtmek için person_id ye ihtiyacımız var buradan alıyoruz
                CreateAccount(person_id, "Vadesiz").createAccount()    #default hesap açılımı 
                Logs(time.localtime(), "Yeni üyelik", self.username).getLog()
                return 1
            except mysql.connector.Error:
                #var olan bir tckn girildiyse uyarı
                msg = "Var olan bir kimlik bilgisi"
                return msg                 