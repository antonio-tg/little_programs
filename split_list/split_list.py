# This program solves the problem that a list in a query cannot have any length, to test the code an example is shown with a lot of 10, but in reality the lot would be 1000 or 10000 elements.

def crea_lis(var_list,lis):
    lot = 10
    if not lis:
        query= var_list+' IN (0)'
    elif len(lis) < lot:
        query= var_list+' IN ('+str(lis).replace('[','').replace(']','') + ')'
    else:
        query = var_list + ' IN '
        ini = 0
        for fin in range(lot, len(lis) + lot, lot):
            query = query + '(' + str(lis[ini:fin]).replace('[','').replace(']','') + ') OR '+ var_list+' IN '
            ini = fin
        query = query[:-14]
    return query

print(crea_lis('IDSALDO',list(range(60))))
