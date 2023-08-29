
from helper import Helper

self = Helper
numbers = [5, 3, 9, 1, 7, 2, 7]
second_largest = self.find_second_largest(numbers)
print("The second largest number in array is: ",second_largest)

arr = [4, 6, 1, 2, 5, 7]
result = self.find_missing_number(arr)
print("The missing number is:", result)

arr1 = [2, 2, 3, 3, 4, 4, 5, 6]
self.remove_duplicates(arr1)

st = "Reversing the words in the strings now"
print(st, "\n")
self.reverse_words(st)

arr = [1, 3, 5, 7, 9, 15, 16, 19, 23, 49]
target = 7
result_in = self.b_search(self,target, arr)
print(f"Index of the target element {target} is: {result_in}")

print("The set of fabochini numbers are: ", self.fibonacci(10))

numbers = [3,4,2,21,4,5,6,776,6,55,44,23]
self.second_largest_enhanced(numbers)

numbers = [2, 3, 4, 4, 5, 6, 6, 21, 23, 44, 55, 776]
filtered_numbers = [i for i in numbers if i < 4 or i > 6]
print(filtered_numbers)

print("The linear search target is located at index: ", self.linear_search(numbers, 6))

dict1={"one": 1, "two": 2, "three": "3"}
dict2={"one": 1, "two": 2, "three": { "Three": 3}}
self.difference_dict(dict1, dict2)

word = "Racecar"
self.is_palindrome(word)

list = ["today", "Tommy", "sam", "michael", "ahmadi", "Zebra", "muzhgan", "sonny", "albert", "susan", "zilman", "zahir", "zero", "Zohaib"]
self.words_starting_with(list, "z")

self.string_digit_seperator(string="1sd4lk4kl24l5k66l")