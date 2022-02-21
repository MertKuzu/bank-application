from connection import connection
import time
from logs import Logs

class LoginFunc():
    
    def login(self, username, password):
        self.username = username
        self.password = password
        #eğer alanlar boş bırakıldıysa uyarı
        if len(self.username) == 0 or len(self.password) == 0:
            msg = "Lütfen boş alan bırakmayın."
            return msg
        else:
            #db bağlantısı
            self.connection = connection
            self.mydb = self.connection.cursor()
            query = "SELECT * FROM information WHERE username = %s"
            value = (self.username,)
            self.mydb.execute(query,value)
            result = self.mydb.fetchone()
            #kullanıcı var mı kontrolü
            if result is None:
                msg = "Var olmayan kullanıcı."
                return msg
            #eğer hesap bloklu değilse parola kontrolü
            elif result[3] == 0:
                if result[2] == self.password:
                    query = "UPDATE information SET counter = 0 WHERE username=%s"
                    self.mydb.execute(query,value)
                    self.connection.commit()
                    Logs(time.localtime(), "Hesaba girildi", self.username).getLog()
                    return 1
                else:
                    #yanlış parola girildiğinde counter 1 artıyor 3 olduğunda hesap bloklanıyor
                    msg = "Hatalı parola."
                    counter = int(result[4])
                    counter +=1
                    query = "UPDATE information SET counter=%s WHERE username=%s"
                    values = (counter,self.username)
                    self.mydb.execute(query,values)
                    self.connection.commit()
                    Logs(time.localtime(), "Hatalı parola girildi", self.username).getLog()
                    if result[4] == 6:
                        query = "UPDATE information SET blocked = 1 WHERE username = %s"
                        self.mydb.execute(query,value)
                        self.connection.commit()
                        Logs(time.localtime(), "Hesap bloklandı", self.username).getLog()
                    else:
                        return msg
            else:
                msg = "Bloklanmış hesap."
                Logs(time.localtime(), "Bloklanmış hesaba giriş denemesi", self.username).getLog()
                return msg

