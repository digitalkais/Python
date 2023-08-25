import os, json, pymysql


class Program_Helper:
    
    def __init__(self):
        """ Initialize the objects """
        self.items_list = list()
        self.updated_list = list()

        self.db = pymysql.connect(
           host='database-2.chntjmvgtb6f.us-west-1.rds.amazonaws.com',
           user='admin',
           password='Maglev12',
           db='',
           port=3306,
           charset='utf8mb4',
           cursorclass=pymysql.cursors.DictCursor
           )
        self.cursor = self.db.cursor()
        table_name = 'QaisDatabase1' #database to be used
        self.cursor.execute('use {}'.format(table_name))
        self.path = os.path.join("/Users/qaisahmadi/Documents/Python/testdata/")

    def input_file(self,input_filename):
        """ Setup input file path in testdata location """

        input = open(self.path + input_filename, "r")
        input = input.read()
        self.input = json.loads(input)

    def write_to_file(self, data):
       
       self.data=data
       inA = open(self.path +"output.json", "a")
       inA.write(self.data)

    def open_output_file(self):

        with open(self.path +"output.json", "r") as file:
            content = file.read()
        self.data = json.loads(content)

