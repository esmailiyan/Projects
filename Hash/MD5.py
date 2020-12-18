import hashlib 
while (1):
    a = input("Enter Your Message: (or exit) ")
    if (a == "exit"):
        exit(0);
    result = hashlib.md5(a.encode()) 
    print("---------------------") 
    print(result.hexdigest())
    print("---------------------") 
