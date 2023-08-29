
from program_helper import Program_Helper

class Database(Program_Helper):
 
    def create_db_table(self):

        self.open_output_file()

        sql = """
        CREATE TABLE IF NOT EXISTS Books (
        Pages INT PRIMARY KEY AUTO_INCREMENT,
        Author VARCHAR(255),
        Book_title VARCHAR(255)
        )"""
    
        self.cursor.execute(sql)

    def insert_data_into_db_table(self):

        for i in range(len(self.data)):
            sql = """insert into Books (Author, Book_title, Pages) VALUES ("{}", "{}", {})""".format(
                self.data[i]["Author"], self.data[i]["Book_title"], self.data[i]["Pages"])
            self.cursor.execute(sql)
        sql = """select * from Books"""
        self.cursor.execute(sql)
        print(self.cursor.execute("""select * from Books"""))
        print ("cursor.description: ", self.cursor.description)
        print("\n", self.cursor.fetchall())
  
        self.db.commit()
        self.db.close()

    def delete_data_from_db_table(self):

        self.cursor.execute('SET SQL_SAFE_UPDATES = 0')
        sql = """delete from Books"""
        self.cursor.execute(sql)
        sql = """select * from Books"""
        self.cursor.execute(sql)
        print(self.cursor.execute("""select * from Books"""))
        print ("cursor.description: ", self.cursor.description)
        print("\n", self.cursor.fetchall())
  
        self.db.commit()
        self.db.close()

db_driver = Database()

db_driver.create_db_table()
db_driver.insert_data_into_db_table()
# db_driver.delete_data_from_db_table()
