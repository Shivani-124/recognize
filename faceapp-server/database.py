# %%
import MySQLdb
from person import Person
from faceencoding import Faceencoding

# %%


class Database:

    def __init__(self):
        print('Connecting to MySQL')
        self.con = MySQLdb.connect(
            user='root', password='root', database='rm', host='localhost')
        print('Connected', self.con)

    def close(self):
        self.con.commit()
        self.con.close()

    def addperson(self, p):
        print(p)
        cursor=self.con.cursor()
        cursor.execute("insert into person values (0,%s,%s,%s)",(p.name,p.phoneticname,p.details))
        cursor.execute("select last_insert_id()")
        data=cursor.fetchall()
        print('data',data)
        return data[0][0]

    def addfaceencoding(self, fe):
        cursor=self.con.cursor()
        cursor.execute("insert into faceencoding values (0,%s,%s)",(str(fe.pid),fe.encoding))
        
    def getfaceencoding(self):
        cursor=self.con.cursor()
        cursor.execute("select * from faceencoding")
        data=cursor.fetchall()
        return data

    def getstudent(self,studentid):
        cursor=self.con.cursor()
        cursor.execute("select * from person where pid="+str(studentid))
        data=cursor.fetchall()
        return data
    
    def addGatepass(self,date,issuedby,pid):
        cursor=self.con.cursor()
        cursor.execute("insert into gatepass values (%s,%s,0)")
        data=cursor.fetchall()
        return data
    
    def getGatepass(self):
        cursor=self.con.cursor()
        cursor.execute("select * from gatepass")
        data=cursor.fetchall()
        return data
# %%
# if __name__ == "__main__":
# d = Database()
# p=Person()
# p.name='123'
# p.phoneticname='234'
# p.details='456'
# d.addperson(p)

# fe=Faceencoding()
# fe.pid=11
# fe.encoding='123xyzpc34'
# d.addfaceencoding(fe)
# d.close()


# %%
