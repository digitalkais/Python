class Helper:

    def find_second_largest(self, numbers):
        """
        This function takes a list of numbers as input and returns the second largest number in the list.
        """
        largest = None
        second_largest = None

        for num in numbers:
            if largest is None:
                largest = num
            elif num > largest:
                second_largest = largest
                largest = num
            elif second_largest is None or num > second_largest:
                second_largest = num

        return second_largest

    def second_largest_enhanced(self, numbers):
        numbers.sort()
        print("2nd largest number using the enhanced method: ", numbers[-2])

    def find_missing_number(self, arr):
        n = len(arr) + 1  # Length of the original array including the missing number
        total_sum = (n * (n + 1)) / 2  # Sum of all numbers from 1 to n
        print("Sum of all numbers from 1 to n is: ", total_sum)
        array_sum = sum(arr)  # Sum of numbers in the array
        missing_number = total_sum - array_sum

        return missing_number

    def remove_duplicates(self, arr1):
        res = [*set(arr1)]
        print(res)

    def reverse_words(self, st):
        st = st.split()
        st = st[::-1]
        st = ' '.join(st)
        print(st)

    def binary_search(self, arr, target):
        #using Devide and Conquer
        # Base case: If the array is empty or target is not present, return -1
        if not arr:
            return -1

        # Find the middle index of the array
        mid = len(arr) // 2

        # Check if the middle element is the target
        if arr[mid] == target:
            return mid
        # If the target is smaller than the middle element, search the left half
        elif target < arr[mid]:
            return self.binary_search(arr[:mid], target)
        # If the target is larger than the middle element, search the right half
        else:
            result = self.binary_search(arr[mid + 1:], target)
            # If the target is found in the right half, adjust the index accordingly
            if result != -1:
                return mid + 1 + result
            else:
                return -1

    def b_search(self, target, arr):

        if arr == []:
            return -1
        mid = len(arr) // 2 #middle element index

        if target == arr[mid]: #check if target is middle element
            return mid

        elif target < arr[mid]: # if target is less then middle, search left side
            return self.b_search(self, target, arr[:mid])

        else:
            result = self.b_search(self, target, arr[mid +1:])
            return result + mid +1

    def linear_search(self, numbers, target):
        for num in range(len(numbers)):
            if numbers[num] == target:
                return numbers.index(numbers[num])

    def fibonacci(self, n):

        fib = [0,1]
        next_number = list()
        while len(fib) < n:
            next_number = (fib[-1] + fib[-2])
            fib.append(next_number)
        return fib

    def difference_dict(self, dict1, dict2):

        differing_keys = []
        for key in dict1:
            if key in dict1 and dict1[key] != dict2[key]:
                differing_keys.append(key)

        for key in differing_keys:
            print(f"Key: {key}, Dict1 Value: {dict1[key]}, Dict2 Value: {dict2[key]}")

    def is_palindrome(self, word):
        word = word.lower()
        if word == word[::-1]:
            print(word, " is a palindrome word.")
        else:
            print(word, " is not a palindrome word.")