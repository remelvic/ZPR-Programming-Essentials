import sys  # rv
 
 
def main():
    k = sys.argv[1]
    try:
        k = int(k)
        if 0 < k < 99:
            tab = table(k)
            table_all(tab)
        else:
            print('ERROR')
    except:
        print('ERROR')
 
 
def Euklid(m, n):  # check numbers for common factors
    while n > 0:
        gen = n
        n = m % n
        m = gen
    if m > 1:
        return True  # number has common factors, write x
    else:
        return False  # has no common factors, write space ' '
 
 
def table(k):
    tab = []  # create lines in an empty table
    for m in range(1, k + 1):
        rad = []  # fill in empty lines
        for n in range(1, k + 1):
            if Euklid(m, n):
                rad.append('x')
            else:
                rad.append(' ')
        tab.append(rad)  # fill the table in rows
    return tab
 
 
def table_all(tab):
    rads = ['|'.join(map(str, rad)) for rad in tab]
    line = ('\n' + '-' * len(rads[0]) + '\n')  # transfer to a new line and write in it -
    table_final = line.join(map(str, rads))
    print(table_final)
 
 
if __name__ == '__main__':
    main()
