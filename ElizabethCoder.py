#POWERED BY EP 10.01.22 (c)
import random
import string
import re
def codefin(stroka):
    def coder(string):
        def randomupper(c):
            if random.random() > 0.5:
                return c.upper()
            return c.lower()
        def generate_random_string(length):
            letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZабвгдеёжзийклмнопрстуфхцчшщъыьэюя1234567890'
            rand_string = ''.join(random.choice(letters) for i in range(length))
            return rand_string
        i=1
        string=string
        string = string.split()
        string = ''.join(string)
        string=string.replace(',', '')
        string=string.replace('!', '')
        string=string.replace('?', '')
        string=string.replace(':', '')
        string=string.replace(';', '')
        string=string.replace('.', '')
        string=string.replace(')', '')
        string=string.replace('(', '')
        string=string.replace('*', '')
        string=string.replace('$', '')
        string=string.replace('#', '')
        string=string.replace('@', '')
        string=string.replace('%', '')
        string=string.replace('&', '')
        string=string.replace('^', '')
        string=string.replace('>', '')
        string=string.replace('<', '')
        string=string.replace('=', '')
        string=string.replace('+', '')
        string=string.replace('-', '')
        string=string.replace('/', '')
        string=string.replace('//', '')
        string=string.replace('"', '')
        string=string.replace('{', '')
        string=string.replace('}', '')
        string=string.replace('[', '')
        string=string.replace(']', '')
        string=string[::-1]
        string=''.join(map(randomupper, string))
        stringtmp=""
        stringtmp2=""
        while i<len(string):
            if i%2!=0:
                stringtmp=stringtmp+string[i]
            i=i+1
        i=0    
        while i<len(string):
            if i%2==0:
                stringtmp2=stringtmp2+string[i]
            i=i+1
        string=stringtmp+stringtmp2
        string=string[::-1]
        socket=''
        socket2=''
        socket=generate_random_string(len(string))
        socket2=generate_random_string(len(string))   
        string=socket2+string+socket
        return string
    string=stroka
    con=random.randint(1,5)
    ind=0
    while ind<con:
        string=coder(string)
        ind=ind+1
    ind=0
    tmp=random.randint(1,5)
    while ind<tmp:
        con=str(coder(str(con)))
        ind=ind+1
    final=str(tmp)+string+"&"+con
    return final
inp=input("Input string: ")
print("Encoded string: "+codefin(inp)[::-1])

