#Given the triangle of consecutive odd numbers:

#             1
#          3     5
#       7     9    11
#   13    15    17    19   
#21    23    25    27    29
#...
#Calculate the sum of the numbers in the nth row of this triangle (starting at index 1) e.g.: (Input --> Output)

#1 -->  1
#2 --> 3 + 5 = 8

def sum_of_odd_numbers(n):
    return n**3

n = input('Ingress a number: ')
m = sum_of_odd_numbers(int(n))
print(f'The sum of the numbers in the {n} row of this triangle is {m}')