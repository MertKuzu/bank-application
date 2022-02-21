from connection import connection


class RegisterFunc():

    def register(self,username, password, password2):
        self.username = username
        self.password = password
        self.password2 = password2
        #boş bırakılmaması için kontrol
        if len(self.username) == 0 or len(self.password) == 0 or len(self.password2) == 0:
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
            #var olmayan kullanıcı adı ise devam ediliyor
            if result is None:
                if self.password == self.password2:
                    if len(self.password) < 5:
                        msg = "Parola en az 5 karakter olmalıdır."
                        return msg
                    else:
                        query = "INSERT INTO information(username,password,blocked,counter) VALUES(%s,%s,0,0)"
                        values = (self.username,self.password)
                        self.mydb.execute(query,values)
                        self.connection.commit()
                        return 1
                else:
                    msg = "Parolalar aynı değil."
                    return msg
            else:
                msg = "Kullanıcı adı mevcut."
                return msg