from connection import connection
from logs import Logs
import time

class ForgotPasswordFunc():
    
    def __init__(self, tckn, password, password2):
        self.tckn = tckn
        self.password = password
        self.password2 = password2

    def forgotPassword(self):
        self.connection = connection
        self.mydb = self.connection.cursor()
        query = "SELECT * FROM person WHERE tckn = %s"    # girilen tckn aranıyor
        value = (self.tckn,)
        self.mydb.execute(query,value)
        result = self.mydb.fetchone()

        #boş bırakılan bir alan var mı kontrol ediliyor
        if len(self.tckn) == 0 or len(self.password) == 0 or len(self.password) == 0:
            msg = "Lütfen boş alan bırakmayın."
            return msg
        
        else:

            # tckn kontrol edildikten sonra boş değer dönmediyse şifre değiştirme işlemleri
            if result is not None:
                if self.password == self.password2:
                    if len(self.password) >= 5:
                        info_id = result[6]
                        query = "UPDATE information SET password = %s WHERE id = %s"
                        values = (self.password, info_id)
                        self.mydb.execute(query, values)
                        self.connection.commit()
                        Logs(time.localtime(), "Parola değiştirildi", self.tckn).getLog()
                        return 1
                    else:
                        msg = "Parola en az 5 karakter olmalıdır."
                        return msg
                else:
                    msg = "Girilen parolalar aynı değil."
                    return msg
            else:
                msg = "Geçersiz TCKN"
                return msg
