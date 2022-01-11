#POWERED BY EP 10.01.22 (c)
import math
def decoderfin(stroka):
    def decoder(string):
        i=0
        string=string
        string=string.lower()
        stringtmp=""
        stringtmpe=""
        stringfin=""
        temp=""
        s=""
        lens=int(len(string)/3)
        while i<lens:
            stringtmp=stringtmp+string[i+lens]
            i=i+1
        stringtmp=stringtmp[::-1]
        i=0    
        while i<len(stringtmp)-1/2:
            stringtmpe=stringtmpe+stringtmp[i]
            i=i+1
        i=1
        if len(stringtmpe)%2!=0:
            while i<(len(stringtmpe)-1)/2+1:
                stringfin=stringfin+stringtmpe[i-1]+stringtmpe[round((len(stringtmpe)+1)/2)+(i-1)]
                i=i+1
            stringfin=stringtmpe[math.ceil((len(stringtmpe)+1)/2-1)]+stringfin
            stringfin=stringfin[::-1]
            return stringfin
        else:
            while i<(len(stringtmpe))/2+1:
                stringfin=stringfin+stringtmpe[i-1]+stringtmpe[round((len(stringtmpe))/2)+(i-1)]
                i=i+1
            i=0
            s=stringfin
            def replace(st):
                s = list(st)
                for c in range(0,len(s),2):
                    t=s[c]
                    s[c]=s[c+1]
                    s[c+1]=t
                return "".join(s)    
            stringfin=replace(s)
            stringfin=stringfin[::-1]
            return stringfin
    string=stroka[::-1]
    a=string.find("&")
    p=0
    stt=""
    while p<a:
        stt=stt+string[p]
        p=p+1
    k=""
    p=0
    while p<len(string)-a:
        k=k+string[a]
        a=a+1
    key=k
    string=stt
    con=int(string[0])
    string=string[1:]
    k=k[1:]
    ind=0
    key=k
    while ind<con:
        key=decoder(key)
        ind=ind+1
    key=int(key)
    ind=0
    while ind<key:
        string=decoder(string)
        ind=ind+1
    return string
inp=input("Input string: ")
print("Decoded string: "+str(decoderfin(inp)))
    
    
