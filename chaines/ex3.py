def verification(ip):
    if ip.find(".")==-1:
        return False
    ch = ip.split(".")
    if len(ch)!=4:
        return False

    i = 0
    while i<len(ch):
        if ch[i]=="":
            return False
        if not ch[i].isdigit():
            return False
        if not (0<=int(ch[i])<=255):
            return False
        i=i+1

    return True

def masqueB(ip):
    ch=ip.split("/")
    cidr=int(ch[1])
    masque=""
    for i in range(cidr):
        masque=masque+"1"
    for j in range(cidr,32):
        masque=masque+"0"
    i=0
    ch1=""
    while i<32:
        j=0
        while j<8:
            ch1=ch1+masque[i+j]
            j=j+1
        ch1=ch1+"."
        i=i+8
    return(ch1[:len(ch1)-1])

def convert(ch):
    sp=ch.split(".")
    i=0
    chh=""
    for el in sp:
        spp=0
        j=0
        for element in sp[i]:
            spp=spp+2**int(j)*int(element)
            j=j+1
        i=i+1
        chh=chh+str(spp)+"."
    return chh[:len(chh)-1]

hh=verification("192.168.0.1")
print(hh)
ch=masqueB("192.168.0.1/24")
print(ch)
chh=convert(ch)
print(chh)
