#Problem: We have several people with a hashed password in "file.csv" and we need to find each person's password.
#We know a password is a number between 0000 and 9999.
#We know the hashed password is sha256.

import csv
from hashlib import sha256
sha256_to_password = dict()

for a in range(0,10):                
    for b in range(0,10):           
        for c in range(0,10):       
            for d in range(0,10):                              
                password = str(a)+str(b)+str(c)+str(d)         
                sha256_password =sha256(password.encode('utf-8')).hexdigest()
                sha256_to_password[sha256_password] = password        #Add to sha256_to_password dictionary.
                    
with open(r'c:\Users\Asus\Desktop\sha256\file.csv') as data:
    reader = csv.reader(data)
    for person,hashed_password in reader:
        print("%s's password is %s" %(person,sha256_to_password[hashed_password]))