# Implement a function that accepts 3 integer values a, b, c. The function should return true if a triangle can be built with the sides of given length and false in any other case.

# (In this case, all triangles must have surface greater than 0 to be accepted).

# To solve this we will use the triangle inequality

def is_triangle(a, b, c):
    if a < b + c and b < a + c and c < a + b:
        return True
    else:
        return False

a = input('To find out if a triangle can be built with three numbers a,b and c\nplease enter the numbers a: ')
b = input('please enter the numbers b: ')
c = input('please enter the numbers c: ')
triangle = is_triangle(int(a),int(b),int(c))
if triangle:
    print(f'You can triangle can be constructed with the sides {a}, {b}, {c}')
else:
    print(f'You cannot build a triangle with the sides {a}, {b}, {c}')
