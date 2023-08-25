import json, time, pdb
from program_helper import Program_Helper

start_time = time.time()
class File(Program_Helper):

   def catagorize_library(self):
          """ Method to take raw input file, organize and catagorize neatly into a json output file """

          self.input_file(input_filename="itemslist.json")

          print("Strpping the / from the input file:\n")
          for i in range(len(self.input)):
                 self.items_list.append(self.input[i].strip("/").split("/"))

          for i in range(len(self.items_list)):
                 self.updated_list.append({"Author":self.items_list[i][0], \
                 "Book_title": self.items_list[i][1], \
                 "Pages": self.items_list[i][2]})
          self.updated_list=json.dumps(self.updated_list, indent=2)
          print(self.updated_list)
          self.write_to_file(data=self.updated_list)
   
   def sort_names(self):
       """ Take names from list and sorts them """

       self.input_file(input_filename="names_list.json")
       self.input.sort()
       print(self.input)




F = File()
F.sort_names()
F.catagorize_library()

end_time = time.time()
elapsed_time = end_time - start_time
print(f"Elapsed time: {elapsed_time} seconds") 