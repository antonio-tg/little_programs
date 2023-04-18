# Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone number.
# Example create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"

def create_phone_number(n):
    a = str(n[0:3]).replace(', ','').replace('[','').replace(']','')
    b = str(n[3:6]).replace(', ','').replace('[','').replace(']','')
    c = str(n[6:10]).replace(', ','').replace('[','').replace(']','')
    n = f"({a}) {b}-{c}"
    return n

number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(number)
number = create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
print(number)
