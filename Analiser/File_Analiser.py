def counter(text,char):
    count = 0
    for c in text :
        if c == char:
            count += 1
    return count
filename = input("Enter your Filename: ")
with open(filename) as file :
    text = file.read()
for char in "abcdefghijklmnopqrstuvwxyz" :
    perc = 100 * counter(text,char) / len(text)
    print ("{0} = {1}".format(char,round(perc,2)))
