alist = [10,15,2,5,3,66,46,23,94]
print(alist)

def bubble(alist):
    for i in range(len(alist)-1, 0, -1):
        for j in range(i):
            if alist[j] > alist[j+1]:
                alist[j], alist[j+1] = alist[j+1], alist[j]
    return alist

alist = bubble(alist)
print(alist)
