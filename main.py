import hashlib
from hashlib import md5
import base64
import string 
import numpy
from numpy import array
from numba import vectorize, cuda,jit
import pycuda







@cuda.jit
def solutions(hashed_pass,salt,pass_list):
    #Print("started")
    for xs in range(0,len(pass_list)):

        hash = hashlib.md5(salt+bytes(pass_list[xs], 'utf-8')).hexdigest()
        
        if hash == hashed_pass:
            print(hash)
            break

if __name__ == "__main__":

    File_read = open("Problem-1/shadowfile.txt","r", encoding='utf-8')
    File_readps = open("Problem-1/xato-net-10-million-passwords.txt","r", encoding='utf-8')
    File_result = open("shadowfileans.txt","r")
    a = File_read.readline()
    a =  File_read.readline()
    sa = File_read.read()
    sl = sa.split("\n")
    content = File_readps.read()
    #content = contentb.decode("utf-8")
    #pass_list= numpy.array(10000000,dtype=string)
    pass_list = content.split("\n")
    
    #s = s[s.find('$') +1 : len(s)-1]
    #s = s[s.find('$') +1 : len(s)-1]
    #s = s[0: s.find(':')]
    #salt.encode(encoding='UTF-8')
    #hashed_pass =s[s.find("$")+1:len(s)-1]
    #chars = "abcdefghijklmnopqustuvwxyz//\\.*"
    arrayp=[None]*2944
    a =0
    ab =3396
    place = ab
    arrayp[0]= sl[a:place]
    
    for i in range(1 ,2942): 
        a = place +1
        place = ab * i 
        temp =  content[a:place]
        arrayp[i]= temp
    place = ab * 2943
    arrayp[2943] = sl[place:]
    #solutions
    for ys in range(0,len(sl)):
        s = sl[ys]
        salt = s[0: s.find("$") -1]
        salt = base64.urlsafe_b64encode(bytes(salt, 'utf-8'))
        s = s[s.find('$') +1 : len(s)-1]
        s = s[s.find('$') +1 : len(s)-1]
        s = s[0: s.find(':')]
        hashed_pass =s[s.find("$")+1:len(s)-1]
        solutions(hashed_pass,salt,arrayp)
        #solutions(hashed_pass,salt,arrayp)
        #findsolindv(hashed_pass,salt,pass_list)

    



if False:
    chars = string.printable
    print(len(chars))
    lnth = 0
    ans = ""
    ys = 0
    for ys in range(0,len(sl)):
        s = sl[ys]
        salt = s[0: s.find("$") -1]
        salt = base64.urlsafe_b64encode(bytes(salt, 'utf-8'))
        s = s[s.find('$') +1 : len(s)-1]
        s = s[s.find('$') +1 : len(s)-1]
        s = s[0: s.find(':')]
        hashed_pass =s[s.find("$")+1:len(s)-1]
        for xs in range(0,len(pass_list)):

            hash = hashlib.md5(salt+bytes(pass_list[xs], 'utf-8')).hexdigest()
        
            if hash == hashed_pass:
                print(hash)
                break

    print(ys)


if False:
    for i in range(1,30):
        print(i)
        if len(ans)< i:
            ans = ans + 'a'
        for x in range(0,i):
            for y in range(0,len(chars)):
                ans = ans[0:x-1]+chars[y]+ans[x+1:len(ans)-1]
                ans2 = ans
                ans2.encode(encoding='UTF-8')
                hash = hashlib.md5(salt+bytes(ans, 'utf-8')).hexdigest()
                #hash.update(ans+salt)
                #hashed = base64.urlsafe_b64encode(hash.digest())
                if hash == hashed_pass:
                    print(hash)
                    break
    


