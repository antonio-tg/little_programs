# Common denominators
# You will have a list of rationals in the form
# [(1, 2), (1, 3), (1, 4)] ➜  [(6, 12), (4, 12), (3, 12)]

def ismul(a,b):
    if a/b == a//b:
        return True
    else:
        return False

def solution(list):
    cd = 1
    for cuple in list:
        cd *= cuple[1]
        print(cuple,cuple[0],cuple[1])
    for cuple in list:
        if cd/cuple[1] == cd//cuple[1]
    print(cd)
    #return cd


solution([(1, 2), (1, 3), (1, 4)])
