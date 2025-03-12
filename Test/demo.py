# Example 1: Printing a Simple Message
print("Hello, Python!")
print("I love coding! 😊")

# Example 2: Printing Numbers
print(5)
print(10 + 3)
print(3.14)

# Example 3: Printing Multiple Things
print("My favorite fruit is", "Mango")
print("2 + 2 =", 2 + 2)


name = "Alice"  # String (Text)
age = 10        # Integer (Number)
height = 4.5    # Float (Decimal Number)
is_student = True  # Boolean (True/False)

print(name, age, height, is_student)



# Example 4: Using 'sep' to Change Separators
print("Apple", "Banana", "Cherry", sep="🍎")

# Example 5: Using 'end' to Stay on the Same Line
print("Hello", end=" ")
print("World!")

# Example 6: Printing Variables
name = "Luna"
age = 7
print("My name is", name, "and I am", age, "years old.")

# Example 7: Using f-strings (Cooler Way to Print!)
name = "Leo"
hobby = "drawing"
print(f"Hi! I'm {name} and I love {hobby}.")


# String
name = "Alice"  
print(type(name))  # Output: <class 'str'>

# Integer
age = 10  
print(type(age))  # Output: <class 'int'>

# Float
height = 4.5  
print(type(height))  # Output: <class 'float'>

# Boolean
is_student = True  
print(type(is_student))  # Output: <class 'bool'>

# List
fruits = ["Apple", "Banana", "Cherry"]  
print(type(fruits))  # Output: <class 'list'>

# Tuple
coordinates = (10.0, 20.5)  
print(type(coordinates))  # Output: <class 'tuple'>

# Dictionary
person = {"name": "Alice", "age": 10}  
print(type(person))  # Output: <class 'dict'>


count = 1  # Start at 1
while count <= 5:  # Keep looping while count is 5 or less
    print("Number:", count)
    count += 1  # Increase count by 1 each time

# Example:
x = 5
x += 2  # x = x + 2 (Now x is 7)
x *= 3  # x = x * 3 (Now x is 21)
print(x)  # Output: 21
