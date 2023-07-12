import requests
from requests.auth import HTTPBasicAuth
import os, glob, zipfile

url = "https://httpbin.org/basic-auth/user/pass"

headers = {'content-type' : 'application/json', 'Authorization': 'token'}
basic = HTTPBasicAuth('user', 'pass')
response = requests.get(url, headers=headers, auth=basic)

print(response.status_code)
print(response.json())
try:
    response.raise_for_status()
    # Additional code will only run if the request is successful
except requests.exceptions.HTTPError as errh:
    print(errh)
except requests.exceptions.ConnectionError as errc:
    print(errc)
except requests.exceptions.Timeout as errt:
    print(errt)
except requests.exceptions.RequestException as err:
    print(err)

---------------------------------------------------
with zipfile.ZipExtFile(targetPath, 'r') as zip:
    zip.extractall(destination_path)

for text_file in glob.glob(destination_path+"*.txt")


--------------------------------------------
SDN = taking routing control away from individule  network elements and putting it in hands of centralized control layer. EG. Oorchestration and SDN control system.
import requests
import pytest, json

""" GET request """
api_url = "https://jsonplaceholder.typicode.com/todos/1"
headers = {'content-type' : 'application/json'}
response = requests.get(api_url)
response.json()
print(response)
#curl -o out.json https://jsonplaceholder.typicode.com/todos/1
# import pdb; pdb.set_trace()

"""POST request"""
api_url = "https://jsonplaceholder.typicode.com/todos/"
input = {
    "userId": 1,
    "title": "Buy milk",
    "completed": False
}

response = requests.post(api_url, json=input, headers=headers)
print(response)

"""PUT request """
api_url = "https://jsonplaceholder.typicode.com/todos/1"
input = {"userId": 1, "title": "Wash car", "completed": True}
response = requests.put(api_url,  json=input, headers=headers)
print(response.json())
output = response.json()

response.json()

assert output["userId"] == 1, "User id mismatch in response."

"""Delete request"""
api_url = "https://jsonplaceholder.typicode.com/todos/1"
response = requests.delete(api_url)
print(response)

from collections.abc import Sized


class Node:
  def __init__(self, data = None, next=None): 
    self.data = data
    self.next = next

class SingleLinkedList:
  def __init__(self):  
    self.head = None
  
  def insert(self, data):
    newNode = Node(data)
    if(self.head):
      current = self.head
      while(current.next):
        current = current.next
      current.next = newNode
    else:
      self.head = newNode
  
  def printLL(self):
    current = self.head
    while(current):
      print(current.data)
      current = current.next


  def remove_middle_element(self):
    head = self.head
    if (head == None):
        return None
    if (head.next == None):
        del head
        return None
    newHead = head

    tmp = self.head
    count = 0
    while (tmp):
        count += 1
        tmp = tmp.next
    mid = count // 2
    while (mid > 1):
        mid -= 1
        head = head.next
    head.next = head.next.next
    return newHead


print("\nCreating LinkedList object and inserting elements into linkedList...\n")
LL = SingleLinkedList()
LL.insert(4)
LL.insert(7)
LL.insert(23)
LL.insert(99)
LL.insert(67)
LL.insert(11)
LL.insert(54)
print("\nPrinting the node elements in linkedList...\n")
LL.printLL()
print("\nRemoving middle element from linkedlist and displaying the list:\n")
LL.remove_middle_element()
LL.printLL()



------------------------------

import os

class File:
    def __init__(self):
        path = os.path.dirname(__file__)
        self.path = path +"/testdata/"

    def write_to_file(self):

        f1=open(self.path+"input.txt", "w")
        for i in range(100):
            f1.write("MY NAME IS QAIS ")
        f1=open(self.path+"input.txt", "r")
        return f1.read()

test = File()

test.write_to_file()