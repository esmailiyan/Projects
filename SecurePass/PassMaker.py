""
*   Author: Mahdi Esmailiyan ( MS128 )
*   Created: 2020.12.17
*   In The Name of God
""
import random

text = ""
char = {1:"a" , 2:"b" , 3:"c" , 4:"d" , 5:"e" , 6:"f" , 7:"g" , 8:"h" , 9:"i" , 10:"j" , 11:"k" , 12:"l" , 13:"m" , 14:"n" , 15:"o" , 16:"p" , 17:"q" , 18:"r" , 19:"s" , 20:"t" , 21:"u" , 22:"v" , 23:"w" , 24:"x" , 25:"y" , 26:"z" , 27:"A" , 28:"B" , 29:"C" , 30:"D" , 31:"E" , 32:"F" , 33:"G" , 34:"H" , 35:"I" , 36:"J" , 37:"K" , 38:"L" , 39:"M" , 40:"N" , 41:"O" , 42:"P" , 43:"Q" , 44:"R" , 45:"S" , 46:"T" , 47:"U" , 48:"V" , 49:"W" , 50:"X" , 51:"Y" , 52:"Z" , 53:"0" , 54:"1" , 55:"2" , 56:"3" , 57:"4" , 58:"5" , 59:"6" , 60:"7" , 61:"8" , 62:"9" , 63:"-" ,
64:"+" , 65:"*" , 66:"/" , 67:"!" , 68:"@" , 69:"#" , 70:"$" , 71:"%" , 72:"^" , 73:"&" , 74:"`" , 75:"="}
print (" --------------------")
num = int(input(" Enter the number of password digits: "))
number = input(" Do you want any number? (yes/no): ")
if (number == "yes"):
    character = input(" Do you want any character? (yes/no): ")
    if (character == "yes"):
        dom = 75
    else :
        dom = 62
else :
    dom = 52
while (num):
    num -= 1
    p = random.randint(1,dom)
    text += char[p]
print(" --------------------")
print(" {0}: {1}".format("your Password" , text))
print(" --------------------")
file = open("password.txt","w")
file.write("your Password is : " + text)
file.close()
