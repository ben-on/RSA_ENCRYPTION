import random
from math import *
        #dictionaries
alpha1={0:'0',1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9',10:'-',
    11:'a',12:'b',13:'c',14:'d',15:'e',16:'f',17:'g',18:'h',19:'i',20:'j',21:'k'
    ,22:'l',23:'m',24:'n',25:'o',26:'p',27:'q',28:'r',29:'s',30:'t',31:'u',
    32:'v',33:'w',34:'x',35:'y',36:'z',37:' ',38:'.',39:',',40:';',41:'@',42:'#',43:'A',
    44:'B',45:'C',46:'D',47:'E',48:'F',49:'G',50:'H',51:'I',52:'J',53:'K',54:'L',55:'M',56:'N',
    57:'O',58:'P',59:'Q',60:'R',61:'S',62:'T',63:'U',64:'V',65:'W',66:'X',67:'Y',68:'Z',69:'~',
    70:'!',71:'$',72:'%',73:'^',74:'*',75:'&',76:'(',77:')',78:'_',79:'+',80:'{',81:'}',82:':',83:'[',
    84:']',85:'|',86:'\\',87:"'",88:'"',89:'=',90:'>',91:'<',92:'/',93:'`',94:'’'}

alpha2={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'-':10,'a':11,'b':12,'c':13,
    'd':14,'e':15,'f':16,'g':17,'h':18,'i':19,'j':20,'k':21,
    'l':22,'m':23,'n':24,'o':25,'p':26,'q':27,'r':28,'s':29,'t':30,'u':31,'v':32,'w':33,
    'x':34,'y':35,'z':36,' ':37,'.':38,',':39,';':40,'@':41,'#':42,'A':43,'B':44,'C':45,'D':46,
    'E':47,'F':48,'G':49,'H':50,'I':51,'J':52,'K':53,'L':54,'M':55,'N':56,'O':57,'P':58,'Q':59,
    'R':60,'S':61,'T':62,'U':63,'V':64,'W':65,'X':66,'Y':67,'Z':68,'~':69,'!':70,'$':71,'%':72,
    '^':73,'*':74,'&':75,'(':76,')':77,'_':78,'+':79,'{':80,'}':81,':':82,'[':83,']':84,'|':85,'\\':86,
    "'":87,'"':88,'=':89,'>':90,'<':91,'/':92,'`':93,'’':94}
        #Eucledian GCD
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

      #number of prime factors
def factors(n):
    sum=2;
    for i in range(2,n//2+1):
        if n%i==0:
            sum+=1
    return  sum
                   #2 random number
p=random.randint(20,100)
q=random.randint(20,100)
                  #the first prime next to p and q
while factors(p) != 2:
    p += 1
while factors(q) != 2:
    q += 1
    #public key n.
n=p*q
phi_n=(p-1)*(q-1)
e=3
       # e must be relatively prime to (phi_n)
while phi_n % e == 0:
    e += 1
    #generate small random number (k).
k=1
d=((k*phi_n+1))/e
        # d must be an integer
while d%1!=0:
    k+=1
    d = ((k * phi_n + 1)) / e

d=int(d)
def encrypt(t):
    for i in range(len(t)):
        c = (alpha2[t[i]] ** e) % n
        encrypted.append(str(c))
def decrypt(h):
    for i in h:
        w = (int(i) ** d) % n
        decrypted.append(alpha1[w])
def formatedprint(t,l):
    for i in range(len(t)-1):
        if i%l==0:
            print()
        else:print(t[i],end='')
    #test
text="CreatingA simple graph G consists of a nonempty set V , called the vertices (nodes2 ) " \
  "of G, and a set E of two- element subsets of V . The members of E are called the edges of " \
  "G, and we write G D .V; E/. If a graph has more "
#encrypt the message and put on var (x)
encrypted=[]
encrypt(text)
x='%'.join(encrypted)
print("\n\ncipher text:")
print(formatedprint(x,90))
#decrypt back the original file
decrypted=[]
w=x.split('%')
decrypt(w)
y=''.join(decrypted)
print("\n\nOriginal message:")
print(formatedprint(y,90))
