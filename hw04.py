import re
import sys
# OK I use to mean True - False
OK = 0
 
count_tag = 0
f = open(sys.argv[1], 'r')
for line in f.readlines():
    # create a list and count tags in it
    count_tag_in_line = list(line).count('/')
    if count_tag_in_line > 0:
        count_tag += count_tag_in_line
    # looking for letters or numbers between tags
    text = re.findall(r'<.*>(\w+)', line)
    if text:
        OK += 1
 
f.close()
 
if OK > 0:
    print("pocet tagu:", count_tag)
    print("text validni")
else:
    print('text nevalidni')
