import sqlite3
from Backend.manager import Encryption

class appDb:
    def __init__(self):
        try:
            self.connect = sqlite3.connect("pwmdatabase.db")
            self.cursor = self.connect.cursor()
        except Exception as e:
            print(e)
    
    def createDataTable (self):
        sCreate = """
			CREATE TABLE IF NOT EXISTS appData (siteName varchar(300),siteUrl varchar(300),sitePassword text)
		"""
        self.cursor.execute(sCreate)
        self.connect.commit()

    def insertDataTable(self,sn,su,sp):
        enc = Encryption()
        enc_ps = enc.encrypt(sp)
        sInsert = """
            INSERT INTO appData (siteName,siteUrl,sitePassword) 
            VALUES (%s %s %s)
        """
        self.cursor.execute(sInsert, (sn, su, enc_ps))
        self.connect.commit()

    def searchPasswd (self, sname):
        en = Encryption
        resultsiteName = "SELECT * FROM data WHERE siteName LIKE '%{}%'".format(sname)
        self.cursor.execute(resultsiteName)
        c = self.cursor.fetchall()
        self.connect.commit()
        if not c:
            return ("")

        dec_ps = en.decrypt(c[0][2]).decode('utf-8')
        return (c[0],dec_ps)

    def deleteDataTable(self,sn):
        sDelete =("DELETE FROM data WHERE siteName LIKE '%{}%'").format(sn)
        try:
            self.cursor.execute(sDelete)
            self.connect.commit()
        except Exception as e:
            print(e)

    def printData (self):
        sPrint = """
            SELECT siteName, siteUsername FROM data
        """
        self.cursor.execute(sPrint)
        self.connect.commit()
        alldata = self.cursor.fetchall()
        print (alldata)


#main 

mydb = appDb
mydb.createDataTable
Encryption.gen_key
#mydb.insertDataTable('','toto','www.toto.com','password')
mydb.printData
