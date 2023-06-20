import os, json


class Program_Helper:
    def __init__(self):
        """ Initialize the objects """
        self.items_list = list()
        self.updated_list = list()

    def input_file(self,input_filename):
        """ Setup input file path in testdata location """
        self.path = os.path.join("/Users/qaisahmadi/Documents/Python/testdata/")
        input = open(self.path + input_filename, "r")
        input = input.read()
        self.input = json.loads(input)

 
    def write_to_file(self, data):
       inA = open(self.path +"output.json", "a")
       inA.write(data)
