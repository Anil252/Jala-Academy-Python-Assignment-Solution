#!/usr/bin/env python
# coding: utf-8

# ## Basic Python
# 

# In[ ]:


'''1.Python Basics
1. Write a program to print your name.
2. Write a program for a Single line comment and multi-line comments
3. Define variables for different Data Types int, Boolean, char, float, double and print on the 
Console.
4. Define the local and Global variables with the same name and print both variables and 
understand the scope of the variable
'''


# In[ ]:


# 1. Write a program to print your name.


# In[ ]:


print("Anil Yadav")


# In[ ]:


# 2.Write a program for a Single line comment and multi-line comments


# In[ ]:


#single line comment


# In[ ]:


# This is a single line comment

'''
This is a multi-line comment.
You can also use triple double quotes for multi-line comments.
For example:
"""
This is another way to write
a multi-line comment.
"""
'''
print("Comments have been added in the code")


# In[ ]:


# 3. Define variables for different Data Types int, Boolean, char, float, double and print on the console.


# In[ ]:


# Defining variables of different data types
integer_var = 10
boolean_var = True
char_var = 'A'  # In Python, char is a string of length 1
float_var = 10.5
double_var = 20.123456789  # In Python, float can be used as double

# Printing variables on the console
print("Integer:", integer_var)
print("Boolean:", boolean_var)
print("Character:", char_var)
print("Float:", float_var)
print("Double:", double_var)


# In[ ]:


#4. Define the local and Global variables with the same name and print both variables and understand the scope of the variable



# In[ ]:


# Defining a global variable
global_var = "I am a global variable"

def my_function():
    # Defining a local variable with the same name
    global_var = "I am a local variable"
    print("Inside function:", global_var)

# Calling the function
my_function()

# Printing the global variable
print("Outside function:", global_var)


# ## Operators

# In[ ]:


'''1. Write a function for arithmetic operators(+,-,*,/)
2. Write a method for increment and decrement operators(++, --)
3. Write a program to find the two numbers equal or not.
4. Program for relational operators (<,<==, >, >==)
5. Print the smaller and larger numbe'''


# In[ ]:


# 1.


# In[ ]:


def arithmetic_operations(a, b):
    addition = a + b
    subtraction = a - b
    multiplication = a * b
    division = a / b if b != 0 else "undefined (division by zero)"
    return addition, subtraction, multiplication, division

# Example :
a = 10
b = 5
add, sub, mul, div = arithmetic_operations(a, b)
print("Addition:", add)
print("Subtraction:", sub)
print("Multiplication:", mul)
print("Division:", div)


# In[ ]:


# 2.


# In[ ]:


def increment_decrement(value):
    # Increment
    incremented_value = value + 1
    # Decrement
    decremented_value = value - 1
    return incremented_value, decremented_value

# Example usage:
value = 10
inc_value, dec_value = increment_decrement(value)
print("Original Value:", value)
print("Incremented Value:", inc_value)
print("Decremented Value:", dec_value)


# In[ ]:


#3.


# In[ ]:


def check_equality(num1, num2):
    return num1 == num2

# Example usage:
num1 = 10
num2 = 10
are_equal = check_equality(num1, num2)
print("Are the two numbers equal?", are_equal)


# In[ ]:


#4.


# In[ ]:


def relational_operators(a, b):
    less_than = a < b
    less_than_or_equal = a <= b
    greater_than = a > b
    greater_than_or_equal = a >= b
    return less_than, less_than_or_equal, greater_than, greater_than_or_equal

# Example usage:
a = 10
b = 5
lt, lte, gt, gte = relational_operators(a, b)
print("a < b:", lt)
print("a <= b:", lte)
print("a > b:", gt)
print("a >= b:", gte)


# In[ ]:


# 5.


# In[ ]:


def find_smaller_and_larger(a, b):
    if a < b:
        smaller = a
        larger = b
    else:
        smaller = b
        larger = a
    return smaller, larger

# Example usage:
a = 10
b = 5
smaller, larger = find_smaller_and_larger(a, b)
print("Smaller number:", smaller)
print("Larger number:", larger)


# ## Loops

# In[ ]:


'''1. Write a program to print “Bright IT Career” ten times using for loop
2. Write a java program to print 1 to 20 numbers using the while loop.
3. Program to equal operator and not equal operators
4. Write a program to print the odd and even numbers.
5. Write a program to print largest number among three numbers.
6. Write a program to print even number between 10 and 20 using while
7. Write a program to print 1 to 10 using the do-while loop statement.
8. Write a program to find Armstrong number or not
9. Write a program to find the prime or not.
10. Write a program to palindrome or not.
11. Program to check whether a number is EVEN or ODD using switch
12. Print gender (Male/Female) program according to given M/F using switch'''


# In[ ]:


#1.


# In[ ]:


for _ in range(10):
    print("Bright IT Career")


# In[ ]:


#2.


# In[ ]:


i = 1
while i <= 20:
    print(i)
    i += 1


# In[ ]:


#3.


# In[ ]:


def check_equality(num1, num2):
    is_equal = num1 == num2
    is_not_equal = num1 != num2
    return is_equal, is_not_equal

# Example usage:
num1 = 10
num2 = 5
equal, not_equal = check_equality(num1, num2)
print("Equal:", equal)
print("Not Equal:", not_equal)


# In[ ]:


#4.


# In[ ]:


def print_odd_and_even(start, end):
    print("Even numbers:")
    for num in range(start, end + 1):
        if num % 2 == 0:
            print(num)
    
    print("Odd numbers:")
    for num in range(start, end + 1):
        if num % 2 != 0:
            print(num)

# Example usage:
print_odd_and_even(1, 10)


# In[ ]:


#5.


# In[ ]:


def find_largest(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

# Example usage:
num1 = 10
num2 = 20
num3 = 15
largest = find_largest(num1, num2, num3)
print("Largest number:", largest)


# In[ ]:


#6.


# In[ ]:


num = 10
while num <= 20:
    if num % 2 == 0:
        print(num)
    num += 1


# In[ ]:


#7.


# In[ ]:


num = 1
while True:
    print(num)
    num += 1
    if num > 10:
        break


# In[ ]:


#8.


# In[ ]:


def is_armstrong(number):
    num_str = str(number)
    num_len = len(num_str)
    sum_of_powers = sum(int(digit) ** num_len for digit in num_str)
    return sum_of_powers == number

# Example usage:
number = 153
print(f"Is {number} an Armstrong number?", is_armstrong(number))


# In[ ]:


#9.


# In[ ]:


def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

# Example usage:
number = 29
print(f"Is {number} a prime number?", is_prime(number))


# In[ ]:


#10.


# In[ ]:


def is_palindrome(number):
    num_str = str(number)
    return num_str == num_str[::-1]

# Example usage:
number = 121
print(f"Is {number} a palindrome?", is_palindrome(number))


# In[ ]:


#11.


# In[ ]:


def check_even_odd(number):
    switch = {
        0: "Even",
        1: "Odd"
    }
    return switch.get(number % 2)

# Example usage:
number = 10
print(f"The number {number} is {check_even_odd(number)}")


# In[ ]:


#12.


# In[ ]:


def print_gender(gender):
    switch = {
        'M': "Male",
        'F': "Female"
    }
    return switch.get(gender.upper(), "Invalid input")

# Example usage:
gender = 'M'
print(f"Gender: {print_gender(gender)}")


# ## Arrays

# In[ ]:


'''1. Write a function to add integer values of an array
2. Write a function to calculate the average value of an array of integers
3. Write a program to find the index of an array element
4. Write a function to test if array contains a specific value
5. Write a function to remove a specific element from an array
6. Write a function to copy an array to another array
7. Write a function to insert an element at a specific position in the array
8. Write a function to find the minimum and maximum value of an array
9. Write a function to reverse an array of integer values
10. Write a function to find the duplicate values of an array
11. Write a program to find the common values between two arrays
12. Write a method to remove duplicate elements from an array
13. Write a method to find the second largest number in an array
14. Write a method to find the second largest number in an array
15. Write a method to find number of even number and odd numbers in an array
16. Write a function to get the difference of largest and smallest value
17. Write a method to verify if the array contains two specified elements(12,23)
18. Write a program to remove the duplicate elements and return the new array'''


# In[ ]:


#1.


# In[ ]:


def sum_of_array(arr):
    return sum(arr)

# Example usage:
array = [1, 2, 3, 4, 5]
print("Sum of array:", sum_of_array(array))


# In[ ]:


#2.


# In[ ]:


def average_of_array(arr):
    return sum(arr) / len(arr) if arr else 0

# Example usage:
array = [1, 2, 3, 4, 5]
print("Average of array:", average_of_array(array))


# In[ ]:


#3.


# In[ ]:


def find_index(arr, element):
    try:
        return arr.index(element)
    except ValueError:
        return -1

# Example usage:
array = [1, 2, 3, 4, 5]
element = 3
print(f"Index of {element}:", find_index(array, element))


# In[ ]:


#4.


# In[ ]:


def contains_value(arr, value):
    return value in arr

# Example usage:
array = [1, 2, 3, 4, 5]
value = 3
print(f"Array contains {value}:", contains_value(array, value))


# In[ ]:


#5.


# In[ ]:


def remove_element(arr, value):
    return [x for x in arr if x != value]

# Example usage:
array = [1, 2, 3, 4, 5]
value = 3
print("Array after removing element:", remove_element(array, value))



# In[ ]:


#6.


# In[ ]:


def copy_array(arr):
    return arr.copy()

# Example usage:
array = [1, 2, 3, 4, 5]
copied_array = copy_array(array)
print("Copied array:", copied_array)


# In[ ]:


#7.


# In[ ]:


def insert_element(arr, index, value):
    return arr[:index] + [value] + arr[index:]

# Example usage:
array = [1, 2, 3, 4, 5]
index = 2
value = 10
print("Array after insertion:", insert_element(array, index, value))


# In[ ]:


#8.


# In[ ]:


def min_and_max(arr):
    return min(arr), max(arr)

# Example usage:
array = [1, 2, 3, 4, 5]
print("Minimum and Maximum value:", min_and_max(array))


# In[ ]:


#9.


# In[ ]:


def reverse_array(arr):
    return arr[::-1]

# Example usage:
array = [1, 2, 3, 4, 5]
print("Reversed array:", reverse_array(array))


# In[ ]:


#10.


# In[ ]:


def find_duplicates(arr):
    seen = set()
    duplicates = set()
    for value in arr:
        if value in seen:
            duplicates.add(value)
        seen.add(value)
    return list(duplicates)

# Example usage:
array = [1, 2, 3, 4, 5, 3, 2]
print("Duplicate values:", find_duplicates(array))


# In[ ]:


#11.


# In[ ]:


def common_values(arr1, arr2):
    return list(set(arr1) & set(arr2))

# Example usage:
array1 = [1, 2, 3, 4, 5]
array2 = [3, 4, 5, 6, 7]
print("Common values:", common_values(array1, array2))


# In[ ]:


#12.


# In[ ]:


def remove_duplicates(arr):
    return list(set(arr))

# Example usage:
array = [1, 2, 3, 4, 5, 3, 2]
print("Array after removing duplicates:", remove_duplicates(array))


# In[ ]:


#13.


# In[ ]:


def second_largest(arr):
    unique_arr = list(set(arr))
    unique_arr.sort()
    return unique_arr[-2] if len(unique_arr) >= 2 else None

# Example usage:
array = [1, 2, 3, 4, 5]
print("Second largest number:", second_largest(array))


# In[ ]:


#14.


# In[ ]:


def second_smallest(arr):
    unique_arr = list(set(arr))
    unique_arr.sort()
    return unique_arr[1] if len(unique_arr) >= 2 else None

# Example usage:
array = [1, 2, 3, 4, 5]
print("Second smallest number:", second_smallest(array))


# In[ ]:


#15.


# In[ ]:


def count_even_odd(arr):
    even_count = sum(1 for x in arr if x % 2 == 0)
    odd_count = len(arr) - even_count
    return even_count, odd_count

# Example usage:
array = [1, 2, 3, 4, 5]
even_count, odd_count = count_even_odd(array)
print("Even numbers count:", even_count)
print("Odd numbers count:", odd_count)


# In[ ]:


#16.


# In[ ]:


def difference_max_min(arr):
    return max(arr) - min(arr)

# Example usage:
array = [1, 2, 3, 4, 5]
print("Difference between largest and smallest value:", difference_max_min(array))


# In[ ]:


#17.


# In[ ]:


def contains_elements(arr, elem1, elem2):
    return elem1 in arr and elem2 in arr

# Example usage:
array = [1, 2, 12, 23, 5]
elem1 = 12
elem2 = 23
print(f"Array contains {elem1} and {elem2}:", contains_elements(array, elem1, elem2))


# In[ ]:


#18.


# In[ ]:


def remove_duplicates_new_array(arr):
    return list(set(arr))

# Example usage:
array = [1, 2, 3, 4, 5, 3, 2]
print("New array after removing duplicates:", remove_duplicates_new_array(array))


# ## Static

# In[ ]:


'''1. Define a static variable and access that through a class 
2. Define a static variable and access that through a instance
3. Define a static variable and change within the instance
4. Define a static variable and change within the class'''


# In[ ]:


#1.


# In[ ]:


class MyClass:
    static_var = "I am a static variable"

# Accessing the static variable through the class
print(MyClass.static_var)


# In[ ]:


#2.


# In[ ]:


class MyClass:
    static_var = "I am a static variable"

# Creating an instance of the class
instance = MyClass()

# Accessing the static variable through the instance
print(instance.static_var)


# In[ ]:


#3.


# In[ ]:


class MyClass:
    static_var = "I am a static variable"

# Creating an instance of the class
instance = MyClass()

# Changing the static variable within the instance
instance.static_var = "Changed within instance"

# This changes the variable only for this instance
print("Instance variable:", instance.static_var)
print("Class variable:", MyClass.static_var)


# In[ ]:


#4.


# In[ ]:


class MyClass:
    static_var = "I am a static variable"

# Changing the static variable within the class
MyClass.static_var = "Changed within class"

# Creating an instance of the class
instance = MyClass()

# Accessing the static variable through the instance and class
print("Instance variable:", instance.static_var)
print("Class variable:", MyClass.static_var)


# ## Strings

# In[ ]:


'''1. Different ways creating a string
2. Concatenating two strings using + operator
3. Finding the length of the string
4. Extract a string using Substring
5. Searching in strings using index()
6. Matching a String Against a Regular Expression With matches()
7. Comparing strings
8. startsWith(), endsWith() and compareTo()
9. Trimming strings with strip()
10. Replacing characters in strings with replace()
11. Splitting strings with split()
12. Converting integer objects to Strings
13. Converting to uppercase and lowercase'''


# In[ ]:


#1.


# In[ ]:


# Creating strings using different methods
str1 = "Hello, World!"  # Double quotes
str2 = 'Hello, World!'  # Single quotes
str3 = """Hello, World!"""  # Triple double quotes (also for multi-line strings)
str4 = '''Hello, World!'''  # Triple single quotes (also for multi-line strings)

print(str1)
print(str2)
print(str3)
print(str4)


# In[ ]:


#2.


# In[ ]:


str1 = "Hello"
str2 = "World"
concatenated = str1 + " " + str2
print(concatenated)


# In[ ]:


#3.


# In[ ]:


str1 = "Hello, World!"
length = len(str1)
print("Length of the string:", length)


# In[ ]:


#4.


# In[ ]:


str1 = "Hello, World!"
substring = str1[7:12]  # Extracting 'World'
print("Substring:", substring)


# In[ ]:


#5.


# In[ ]:


str1 = "Hello, World!"
index = str1.index("World")
print("Index of 'World':", index)


# In[ ]:


#6.


# In[ ]:


import re

pattern = r'^Hello'
string = "Hello, World!"
match = re.match(pattern, string)

if match:
    print("The string matches the pattern")
else:
    print("The string does not match the pattern")


# In[ ]:


#7.


# In[ ]:


str1 = "Hello"
str2 = "World"
str3 = "Hello"

print("str1 == str2:", str1 == str2)  # False
print("str1 == str3:", str1 == str3)  # True


# In[ ]:


#8.


# In[ ]:


str1 = "Hello, World!"

print("Starts with 'Hello':", str1.startswith("Hello"))
print("Ends with 'World!':", str1.endswith("World!"))

# CompareTo equivalent in Python
def compare_to(str1, str2):
    if str1 < str2:
        return -1
    elif str1 > str2:
        return 1
    else:
        return 0

str2 = "Hello"
str3 = "World"
print("compare_to(str2, str3):", compare_to(str2, str3))  # -1
print("compare_to(str3, str2):", compare_to(str3, str2))  # 1
print("compare_to(str2, str2):", compare_to(str2, str2))  # 0


# In[ ]:


#9.


# In[ ]:


str1 = "   Hello, World!   "
trimmed = str1.strip()
print("Trimmed string:", trimmed)


# In[ ]:


#10.


# In[ ]:


str1 = "Hello, World!"
replaced = str1.replace("World", "Python")
print("Replaced string:", replaced)


# In[ ]:


#11.


# In[ ]:


str1 = "Hello, World!"
split_str = str1.split(", ")
print("Split string:", split_str)


# In[ ]:


#12.


# In[ ]:


number = 123
str_number = str(number)
print("String representation of number:", str_number)


# In[ ]:


#13.


# In[ ]:


str1 = "Hello, World!"

uppercase = str1.upper()
lowercase = str1.lower()

print("Uppercase:", uppercase)
print("Lowercase:", lowercase)



# ## Inheritance

# In[ ]:


'''A, B and C are classes
A is a super class. B is a sub class of A. C is a sub class of B. 
Create three methods in each class, 2 methods are specific to each class and third 
method (override method) should be in all three Classes A, B and C
Create a class with main method. Create an object for each class A, B and C in main 
method and call every method of each class using its own object/instance.
Call an overridden method with super class reference to B and C class’s objects
Runtime Polymorphism with Data Members/Instance variables, Repeat the above 
process only for data member'''


# In[ ]:


class A:
    def __init__(self):
        self.data = "Data in A"

    def method1(self):
        print("Method1 of Class A")

    def method2(self):
        print("Method2 of Class A")

    def common_method(self):
        print("Common Method of Class A")

class B(A):
    def __init__(self):
        super().__init__()
        self.data = "Data in B"

    def method1(self):
        print("Method1 of Class B")

    def method2(self):
        print("Method2 of Class B")

    def common_method(self):
        print("Common Method of Class B")

class C(B):
    def __init__(self):
        super().__init__()
        self.data = "Data in C"

    def method1(self):
        print("Method1 of Class C")

    def method2(self):
        print("Method2 of Class C")

    def common_method(self):
        print("Common Method of Class C")


# In[ ]:


def main():
    # Creating objects for each class
    objA = A()
    objB = B()
    objC = C()

    # Calling methods of Class A
    print("Class A Methods:")
    objA.method1()
    objA.method2()
    objA.common_method()

    # Calling methods of Class B
    print("\nClass B Methods:")
    objB.method1()
    objB.method2()
    objB.common_method()

    # Calling methods of Class C
    print("\nClass C Methods:")
    objC.method1()
    objC.method2()
    objC.common_method()

    # Runtime polymorphism with super class reference
    print("\nCalling overridden method with superclass reference:")
    super_ref = A()
    super_ref = objB
    super_ref.common_method()

    super_ref = objC
    super_ref.common_method()

    # Runtime Polymorphism with Data Members/Instance variables
    print("\nRuntime Polymorphism with Data Members:")
    print("Data in objA:", objA.data)
    print("Data in objB:", objB.data)
    print("Data in objC:", objC.data)

    # Using superclass reference to access data members
    super_ref = A()
    super_ref = objB
    print("Data in super_ref (B):", super_ref.data)

    super_ref = objC
    print("Data in super_ref (C):", super_ref.data)

if __name__ == "__main__":
    main()


# ## Access Modifiers

# In[ ]:


'''1. Create a class with PRIVATE fields, private method and a main method. Print the fields 
in main method. Call the private method in main method.
Create a sub class and try to access the private fields and methods from sub class.
2. Create a class with PROTECTED fields and methods. Access these fields and methods 
from any other class in the same package. 
Also, Access the PROTECTED fields and methods from child class located in a different 
package
Access the PROTECTED fields and methods from any class in different package
3. Create a class with PUBLIC fields and methods. 
Access the public methods and fields from any class in the same package or different 
package'''


# In[ ]:


#1 ,2,3


# In[ ]:


class A:
    def __init__(self):
        self.__private_field = "I am a private field"

    def __private_method(self):
        print("This is a private method")

    def main_method(self):
        # Accessing private field and method within the class
        print("Accessing private field in main method:", self.__private_field)
        self.__private_method()


class B(A):
    def __init__(self):
        super().__init__()

    def try_access_private(self):
        # Attempt to access private fields and methods from the subclass (will raise AttributeError)
        try:
            print(self.__private_field)
        except AttributeError as e:
            print("Cannot access private field from subclass:", e)

        try:
            self.__private_method()
        except AttributeError as e:
            print("Cannot access private method from subclass:", e)


def main_private():
    # Creating an object of class A
    a = A()
    a.main_method()

    # Creating an object of class B
    b = B()
    b.try_access_private()


### 2. Protected Fields and Methods

class C:
    def __init__(self):
        self._protected_field = "I am a protected field"

    def _protected_method(self):
        print("This is a protected method")


class D(C):
    def __init__(self):
        super().__init__()

    def access_protected(self):
        print("Accessing protected field from subclass:", self._protected_field)
        self._protected_method()


def main_protected():
    # Creating an object of class C
    c = C()
    print("Accessing protected field within same script:", c._protected_field)
    c._protected_method()

    # Creating an object of class D
    d = D()
    d.access_protected()


### 3. Public Fields and Methods

class E:
    def __init__(self):
        self.public_field = "I am a public field"

    def public_method(self):
        print("This is a public method")


class F(E):
    def __init__(self):
        super().__init__()

    def access_public(self):
        print("Accessing public field from subclass:", self.public_field)
        self.public_method()


def main_public():
    # Creating an object of class E
    e = E()
    print("Accessing public field within same script:", e.public_field)
    e.public_method()

    # Creating an object of class F
    f = F()
    f.access_public()


if __name__ == "__main__":
    print("Private Example:")
    main_private()

    print("\nProtected Example:")
    main_protected()

    print("\nPublic Example:")
    main_public()


# ## Abstract Class

# In[ ]:


'''1. Create an abstract class with abstract and non-abstract methods.
2. Create a sub class for an abstract class. Create an object in the child class for the 
abstract class and access the non-abstract methods
3. Create an instance for the child class in child class and call abstract methods
4. Create an instance for the child class in child class and call non-abstract methods'''


# # 

# In[ ]:


#1.


# In[ ]:


from abc import ABC, abstractmethod

class AbstractClass(ABC):
    @abstractmethod
    def abstract_method(self):
        pass

    def non_abstract_method(self):
        print("This is a non-abstract method")

class SubClass(AbstractClass):
    def abstract_method(self):
        print("Implementation of abstract method in SubClass")

def main():
    # Creating an object of SubClass
    obj = SubClass()

    # Accessing non-abstract method
    obj.non_abstract_method()

    # Attempting to call abstract method (will raise NotImplementedError)
    try:
        obj.abstract_method()
    except NotImplementedError as e:
        print("Abstract method is not implemented in SubClass:", e)

if __name__ == "__main__":
    main()


# In[ ]:


#2.


# In[ ]:


'''This is already demonstrated in the above code snippet. When an object of SubClass is created (obj = SubClass()), it can directly access the non-abstract method non_abstract_method().'''


# In[ ]:


#3.


# In[ ]:


class SubClass(AbstractClass):
    def abstract_method(self):
        print("Implementation of abstract method in SubClass")

    def call_abstract_method(self):
        self.abstract_method()

def main():
    # Creating an object of SubClass
    obj = SubClass()

    # Calling abstract method from within the class
    obj.call_abstract_method()

if __name__ == "__main__":
    main()


# In[ ]:


#4.


# In[ ]:


class SubClass(AbstractClass):
    def abstract_method(self):
        print("Implementation of abstract method in SubClass")

    def call_non_abstract_method(self):
        self.non_abstract_method()

def main():
    # Creating an object of SubClass
    obj = SubClass()

    # Calling non-abstract method from within the class
    obj.call_non_abstract_method()

if __name__ == "__main__":
    main()


# ## Packages

# In[ ]:


'''1. Create a program to create two class.
1.1. Create a constructor and a method for each class
1.2. Create a __init__.py for adding all packages
1.3. Import the respective packages
1.4. Call each class by creating an object to it 
1.5. Create a program by all the abov'''


# In[ ]:


#1 class1.py


# In[ ]:


class Class1:
    def __init__(self, name):
        self.name = name

    def method1(self):
        print("Method 1 in Class 1")
        print("Hello,", self.name)


# In[ ]:


# class2.py


# In[ ]:


class Class2:
    def __init__(self, name):
        self.name = name

    def method2(self):
        print("Method 2 in Class 2")
        print("Goodbye,", self.name)


# In[ ]:


#2.# Empty __init__.py file to make the directory a package


# In[ ]:


#3.


# In[ ]:


from package1.class1 import Class1
from package2.class2 import Class2


# In[ ]:


#4.


# In[ ]:


def main():
    obj1 = Class1("Alice")
    obj2 = Class2("Bob")

    obj1.method1()
    obj2.method2()

if __name__ == "__main__":
    main()


# In[ ]:


#5.


# In[ ]:


- main.py
- package1
- __init__.py
- class1.py
- package2
- __init__.py
- class2.py


# In[ ]:


class Class1:
    def __init__(self, name):
        self.name = name

    def method1(self):
        print("Method 1 in Class 1")
        print("Hello,", self.name)


# In[ ]:


class Class2:
    def __init__(self, name):
        self.name = name

    def method2(self):
        print("Method 2 in Class 2")
        print("Goodbye,", self.name)


# In[ ]:


from package1.class1 import Class1
from package2.class2 import Class2

def main():
    obj1 = Class1("Alice")
    obj2 = Class2("Bob")

    obj1.method1()
    obj2.method2()

if __name__ == "__main__":
    main()


# ## Files

# In[ ]:


'''1. Write a program to read text file
2. Write a program to write text to .txt file using InputStream
3. Write a program to read a file stream
4. Write a program to read a file stream supports random access
5. Write a program to read a file a just to a particular index using seek()
6. Write a program to check whether a file is having read access and write access permissions'''


# In[ ]:


#1.


# In[ ]:


def read_text_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print("File not found.")
    except IOError:
        print("Error reading the file.")

# Example usage:
read_text_file("example.txt")


# In[ ]:


#2.


# In[ ]:


def write_to_text_file(file_path, content):
    try:
        with open(file_path, 'w') as file:
            file.write(content)
            print("Content successfully written to", file_path)
    except IOError:
        print("Error writing to the file.")

# Example usage:
write_to_text_file("example.txt", "Hello, this is a test text.")


# In[ ]:


#3.


# In[ ]:


def read_file_stream(file_path):
    try:
        with open(file_path, 'rb') as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print("File not found.")
    except IOError:
        print("Error reading the file.")

# Example usage:
read_file_stream("example.txt")


# In[ ]:


#4.


# In[ ]:


def read_random_access(file_path, start, end):
    try:
        with open(file_path, 'rb') as file:
            file.seek(start)
            content = file.read(end - start)
            print(content)
    except FileNotFoundError:
        print("File not found.")
    except IOError:
        print("Error reading the file.")

# Example usage:
read_random_access("example.txt", 10, 20)


# In[ ]:


#5.


# In[ ]:


def read_from_index(file_path, index):
    try:
        with open(file_path, 'r') as file:
            file.seek(index)
            content = file.read()
            print(content)
    except FileNotFoundError:
        print("File not found.")
    except IOError:
        print("Error reading the file.")

# Example usage:
read_from_index("example.txt", 20)


# In[ ]:


#6.


# In[ ]:


import os

def check_file_permissions(file_path):
    try:
        # Check if file has read access
        if os.access(file_path, os.R_OK):
            print("File has read access.")
        else:
            print("File does not have read access.")

        # Check if file has write access
        if os.access(file_path, os.W_OK):
            print("File has write access.")
        else:
            print("File does not have write access.")
    except FileNotFoundError:
        print("File not found.")

# Example usage:
check_file_permissions("example.txt")


# ## Constructors

# In[ ]:


'''1. Write a class with a default constructor, one argument constructor and two argument 
constructors. Instantiate the class to call all the constructors of that class from a main 
class
2. Call the constructors(both default and argument constructors) of super class from a child 
class
3. Apply private, public, protected and default access modifiers to the constructor
4. Write a program which illustrates the concept of attributes of a constructor'''


# In[ ]:


#1.


# In[ ]:


class MyClass:
    def __init__(self, arg1=None, arg2=None):
        if arg1 is not None and arg2 is not None:
            self.arg1 = arg1
            self.arg2 = arg2
            print("Two argument constructor called with arg1 =", arg1, "and arg2 =", arg2)
        elif arg1 is not None:
            self.arg1 = arg1
            print("One argument constructor called with arg1 =", arg1)
        else:
            print("Default constructor called")

def main():
    obj1 = MyClass()
    obj2 = MyClass(10)
    obj3 = MyClass(20, 30)

if __name__ == "__main__":
    main()


# In[ ]:


#2.


# In[ ]:


class Parent:
    def __init__(self, arg=None):
        if arg is not None:
            print("Parent constructor called with arg =", arg)
        else:
            print("Parent default constructor called")

class Child(Parent):
    def __init__(self, arg=None):
        super().__init__(arg)

def main():
    obj1 = Child()
    obj2 = Child(10)

if __name__ == "__main__":
    main()


# In[ ]:


#3.


# In[ ]:


class MyClass:
    def __init__(self, arg=None):
        self.__private_attr = "Private attribute"
        self._protected_attr = "Protected attribute"
        self.public_attr = "Public attribute"
        self.default_attr = "Default attribute"

def main():
    obj = MyClass()
    # Accessing attributes
    print("Public attribute:", obj.public_attr)
    print("Protected attribute:", obj._protected_attr)
    # This will raise an AttributeError because private attributes are not accessible from outside the class
    try:
        print("Private attribute:", obj.__private_attr)
    except AttributeError as e:
        print(e)

if __name__ == "__main__":
    main()


# In[ ]:


#4.


# In[ ]:


class MyClass:
    def __init__(self, arg):
        self.arg = arg

def main():
    obj = MyClass(10)
    # Accessing attribute of constructor
    print("Argument passed to constructor:", obj.arg)

if __name__ == "__main__":
    main()


# ## Method Overloading

# In[ ]:


'''1. Write two methods with the same name but different number of parameters of same type 
and call the methods 
2. Write two methods with the same name but different number of parameters of different 
data type and call the methods 
3. Write two methods with the same name and same number of parameters of same type'''


# In[ ]:


#1.


# In[ ]:


class MyClass:
    def same_name_method(self, num1, num2=None):
        if num2 is None:
            print("Method with one parameter called. num1 =", num1)
        else:
            print("Method with two parameters called. num1 =", num1, "num2 =", num2)

def main():
    obj = MyClass()
    obj.same_name_method(10)
    obj.same_name_method(20, 30)

if __name__ == "__main__":
    main()

    


# In[ ]:


#2.


# In[ ]:


class MyClass:
    def same_name_method(self, num, text=None):
        if text is None:
            print("Method with one parameter (int) called. num =", num)
        else:
            print("Method with two parameters (int, str) called. num =", num, "text =", text)

def main():
    obj = MyClass()
    obj.same_name_method(10)
    obj.same_name_method(20, "Hello")

if __name__ == "__main__":
    main()


# In[ ]:


#3.


# In[ ]:


class MyClass:
    def same_name_method(self, *args):
        if len(args) == 1:
            print("Method with one parameter called. num =", args[0])
        elif len(args) == 2:
            print("Method with two parameters called. num1 =", args[0], "num2 =", args[1])

def main():
    obj = MyClass()
    obj.same_name_method(10)          # This will call the first method
    obj.same_name_method(20, 30)      # This will call the second method

if __name__ == "__main__":
    main()


# ## Exceptions

# In[ ]:


'''1. Write a program to generate Arithmetic Exception without exception handling
2. Handle the Arithmetic exception using try-catch block
3. Write a method which throws exception, Call that method in main class without try block
4. Write a program with multiple catch blocks
5. Write a program to throw exception with your own message
6. Write a program to create your own exception
7. Write a program with finally block
8. Write a program to generate Arithmetic Exception
9. Write a program to generate FileNotFoundException
10. Write a program to generate ClassNotFoundException
11. Write a program to generate IOException
12. Write a program to generate NoSuchFieldException'''


# In[ ]:


#1.


# In[ ]:


#This program will result in a ZeroDivisionError
result = 10 / 0


# In[ ]:


#2.


# In[ ]:


try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")


# In[ ]:


#3.


# In[ ]:


def method_with_exception():
    raise Exception("This is an exception")

method_with_exception()  # Calling without a try block


# In[ ]:


#4.


# In[ ]:


try:
    pass  # Placeholder for code that may raise different types of exceptions
except ValueError:
    print("ValueError occurred")
except TypeError:
    print("TypeError occurred")
except ZeroDivisionError:
    print("ZeroDivisionError occurred")


 


# In[ ]:


#5.


# In[ ]:


try:
    raise Exception("Custom exception message")
except Exception as e:
    print("Exception:", e)


# In[ ]:


#6.


# In[ ]:


class CustomException(Exception):
    pass

try:
    raise CustomException("This is a custom exception")
except CustomException as e:
    print("Custom exception:", e)


# In[ ]:


#7.


# In[ ]:


try:
    # Code that may raise an exception
except:
    # Exception handling
finally:
    # Code that will always execute, regardless of whether an exception occurred or not


# In[ ]:


#8.


# In[ ]:


try:
    result = 10 / 0
except ZeroDivisionError:
    print("Arithmetic Exception occurred: Cannot divide by zero")


# In[ ]:


#9.


# In[ ]:


try:
    with open("nonexistent_file.txt", "r") as file:
        pass
except FileNotFoundError:
    print("File not found")


# In[ ]:


#10.


# In[ ]:


try:
    # Try to import a module that doesn't exist
except ModuleNotFoundError:
    print("Class not found")


# In[ ]:


#11.


# In[ ]:


try:
    # Code that may raise an IO exception
except IOError:
    print("IO Exception occurred")


# In[ ]:


#12.


# In[ ]:


class MyClass:
    pass

try:
    my_object = MyClass()
    my_object.nonexistent_field  # This field does not exist
except AttributeError:
    print("NoSuchFieldException occurred: Field does not exist")


# ## Dictionary

# In[ ]:


'''1. Create a Dictionary with at least 5 key value pairs of the Student ID and Name
1.1. Adding the values in dictionary
1.2. Updating the values in dictionary
1.3. Accessing the value in dictionary
1.4. Create a nested loop dictionary
1.5. Access the values of nested loop dictionary
1.6. Print the keys present in a particular dictionary
1.7. Delete a value from a dictionary'''


# In[ ]:


#1.


# In[ ]:


# Create a dictionary of student IDs and names
student_dict = {
    101: "Alice",
    102: "Bob",
    103: "Charlie",
    104: "David",
    105: "Eve"
}


# In[ ]:


#1.1.


# In[ ]:


# Adding a new key-value pair
student_dict[106] = "Frank"
print(student_dict)


# In[ ]:


#1.2.


# In[ ]:


# Updating the value for a key
student_dict[101] = "Alice Smith"
print(student_dict)


# In[ ]:


#1.3


# In[ ]:


# Accessing the value for a specific key
print("Name of student with ID 103:", student_dict[103])


# In[ ]:


#1.4


# In[ ]:


# Creating a nested loop dictionary
nested_dict = {
    'outer_key1': {'inner_key1': 'value1', 'inner_key2': 'value2'},
    'outer_key2': {'inner_key3': 'value3', 'inner_key4': 'value4'}
}


# In[ ]:


#1.5


# In[ ]:


# Accessing values of the nested loop dictionary
print("Value of outer_key1:", nested_dict['outer_key1'])
print("Value of inner_key2 in outer_key1:", nested_dict['outer_key1']['inner_key2'])


# In[ ]:


#1.6


# In[ ]:


# Printing keys present in a particular dictionary
print("Keys in student_dict:", student_dict.keys())


# In[ ]:


#1.7


# In[ ]:


# Deleting a value from a dictionary
del student_dict[106]
print(student_dict)


# In[ ]:




