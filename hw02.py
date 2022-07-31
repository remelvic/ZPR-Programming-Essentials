import sys
from fractions import Fraction
 
 
f = open(sys.argv[1], "r")
line1 = f.readline()
p1 = list(map(Fraction, line1.split()))
line = f.readline()
p2 = list(map(Fraction, line.split()))
 
a = len(p1)
result = []
 
for i in range(len(p1) - len(p2), -1, -1):  # main function
    kof = p1[a - 1].numerator / p2[-1].numerator  # coefficient
    count = 0
 
    for j in range(i, a, +1):
        p1[j]._numerator = p1[j].numerator - p2[count].numerator * kof
        count += 1
 
    result.append(kof)
    a -= 1
f.close()
 
reverse = []
 
for i in range(len(result) - 1, - 1, -1):
    reverse.append(int(result[i]))
 
controler = False
space = ""
for i in range(len(p1) - 2, -1, -1):
 
    if controler == True:
        space = " " + space
        space = str(int(p1[i].numerator)) + space
    else:
        if p1[i]._numerator != 0:
            space = str(int(p1[i].numerator)) + space
            controler = True
 
for i in range(len(reverse)):
    if i == (len(reverse)-1):
        print(reverse[i], end='')
    else:
        print(reverse[i], end=' ')
print(end='\n')
 
if space == "":
    print('0')
else:
    print(space)
