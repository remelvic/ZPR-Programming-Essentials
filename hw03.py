import sys
f = open(sys.argv[1], "r")
word1 = f.readline()
word2 = f.readline()
 
word1 = word1[:-1]  # remove the last character "\ n"
 
a = ord('a')    # according
z = ord('z')    # to the
A = ord('A')    # ASCII
Z = ord('Z')    # table
 
for i in range(len(word1)):
    array1 = ord(word1[i])
    if A <= array1 <= Z or a <= array1 <= z:  # checking for correct characters
        pass
    else:
        print("Error: Chybny vstup!")
        sys.exit(1)
 
for i in range(len(word2)):  # checking for correct characters of the second line
    array2 = ord(word2[i])
    if A <= array2 <= Z or a <= array2 <= z:
        pass
    else:
        print("Error: Chybny vstup!")
        sys.exit(1)
 
if len(word1) != len(word2):     # check for array length
    print("Error: Chybna delka vstupu!")
    sys.exit(1)
 
 
def shift(arr_shift, size_arr_shift):  # shift fields letter by letter
    new = ''
    for j in range(size_arr_shift):
        mes = ord(arr_shift[j])
        if Z > mes >= A:
            new += chr(mes + 1)
        elif z > mes >= a:
            new += chr(mes + 1)
        elif mes == Z:
            new += chr(a)
        elif mes == z:
            new += chr(A)
    return new
 
 
def search(array_test, array_control):  # looking for the maximum match by characters
    count = 0
    for index in range(len(array_test)):
        if array_test[index] == array_control[index]:
            count += 1
            index += 1
    return count
 
 
maximum = search(word1, word2)
result = word1
for lu in range(len(word1)):
    word1 = shift(word1, len(word1))
    minimum = search(word1, word2)
    if search(word1, word2) > maximum:
        maximum = minimum
        result = word1
 
f = open("output.txt", "w")     # write the result
f.write(result)
