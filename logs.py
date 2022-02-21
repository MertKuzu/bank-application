from connection import connection

class Logs():
    def __init__(self, time, process, user):
        self.time = time
        self.process = process
        self.user = user
        self.connection = connection
        self.mydb = self.connection.cursor()

    def getLog(self):
        #yapılan işlemler db ye kaydediliyor
        query = "INSERT INTO logs(process_time, process, username) VALUES(%s,%s,%s)"
        values = (self.time, self.process, self.user)

        self.mydb.execute(query,values)
        self.connection.commit()     