import crypt
import itertools

def probar (pass_,lista=[]):
    sal='$'+pass_.split('$')[1]+'$'+pass_.split('$')[2]
    for p in lista:
        clave=''
        for l in p:
            clave=clave+l
        key=crypt.crypt(clave,salt=sal)
        if pass_==key:
            print ('password obtained: ',clave)
            return
        else:
            pass

def main():
    data='root:$6$ms32yIGN$NyXj0YofkK14MpRwFHvXQW0yvUid.slJtgxHE2EuQqgD74S/GaGGs5VCnqeC.bS0MzTf/EFS3uspQMNeepIAc.:15503:0:99999:7:::'
    user=data.split(':')[0]
    passk=data.split(':')[1].strip()
    num='1234567890'
    sign='@!#$%&/¡*+[]{}-_. '
    alfa='abcdefghijklmnopqrstuvwxyz'
    alfanum=list(alfa+' ')
    passwords=[]
    print ('cracking password for: ',user)
    for n in range (0,41):
        passwords=list(itertools.product(alfanum,repeat=n))
        probar(passk,passwords)
if __name__=='__main__':
    main()
