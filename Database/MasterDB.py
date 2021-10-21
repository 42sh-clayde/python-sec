import sqlite3
import hashlib


class MasterDB:

    def __init__(self):
        try:
            self.connect = sqlite3.connect("pwmdatabase.db")
            self.cursor = self.connect.cursor()
        except Exception as e:
            print(e)

# This will create masterTable

    def createTable(self):
    		qCreate = """
    			CREATE TABLE IF NOT EXISTS masterTable (masterPass varchar(300))
    		"""
    		self.cursor.execute(qCreate)
    		self.connect.commit()

    # This will hash the password and insert it along with email entered

    def insertIntoTable(self, mp):
    	bytesMP = bytes(mp, 'utf-8')
    	hashedMP = hashlib.sha256(bytesMP).hexdigest()
    	qInsert = """
    		INSERT INTO masterTable (masterPass)
    		VALUES (?)
    	"""
    	self.cursor.execute(qInsert, (hashedMP))
    	self.connect.commit()

    # This will update the existing password(hashed) instead of making a new row in database

    def updateIntoTable(self,mp):
        bytesMP = bytes (mp ,'utf-8')
        hashedMP = hashlib.sha256(bytesMP).hexdigest()
        qUpdate = """
            UPDATE masterTable SET masterpass = (?)
            """
        self.cursor.execute(qUpdate, (hashedMP))
        self.connect.commit()

    # This is used in loginFrame.py to check the password with database

    def loginCheck(self,mp):
        bytesMP = bytes (mp ,'utf-8')
        hashedMP = hashlib.sha256(bytesMP).hexdigest()

        qSelect = """
    			SELECT * FROM masterTable
    		"""
        self.cursor.execute(qSelect)
        data = self.cursor.fetchall()

        if hashedMP == data[0][0]:
            return True
        return False

if __name__ == '__main__':
    tutu = MasterDB
    tutu.createTable
    tutu.insertIntoTable
    tutu.loginCheck