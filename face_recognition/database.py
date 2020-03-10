import mysql.connector


class Database:

    def __init__(self):
        self.con = mysql.connector.connect(host='localhost',
                                           database='rm',
                                           user='root',
                                           password='root',
                                           use_pure=True,
                                           charset='utf8')

    def addPerson(self, name: str, details: str) -> int:
        cursor = self.con.cursor()
        cursor.execute('insert into person values (0,%s,%s,%s)', (name, name, details))
        self.con.commit()
        cursor.close()

    def getPerson(self, pid: int):
        cursor = self.con.cursor()
        cursor.execute(f'select * from person where pid={pid}')
        persons=cursor.fetchall()
        cursor.close()
        return persons

    def close(self):
        self.con.close()
