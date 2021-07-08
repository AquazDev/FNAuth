#Imports
import requests
from colorama import init, Fore, Back, Style
init()
import json
import os

class EndpointsURLs:
    codeurl = "https://www.epicgames.com/id/api/redirect?clientId=3446cd72694c4a4485d81b77adbb2141&responseType=code"
    tokenurl = "https://account-public-service-prod.ol.epicgames.com/account/api/oauth/token"
    nitestatsbearer = "https://api.nitestats.com/v1/epic/bearer"

#StartUp
class FNAuthStartUP:
    print (Fore.LIGHTMAGENTA_EX + '[FNAuth] ', end = "")
    print (Fore.WHITE + f'| Started FNAuth Made By AquazDev')
    print ('-------------------------------------------------')

#EXCode Question
class OpenDaLink:
    print("Open The Link Below And Copy Your ExCode | ex. code=", end = "")
    print(Fore.YELLOW + "f83b2a2ew8904deca04dda1804b65539\n")
    print(Fore.WHITE + "Link: " + EndpointsURLs.codeurl)
    print()
#EXCode Question
class ExCode:
    ExCode = input("Please Enter Your ExCode: ")
    print()
    print("ExCode Set To: " + f"'{ExCode}'")

#NitestatsBearer
class NiteStatsBearer:
    bearer = EndpointsURLs.nitestatsbearer
    request = requests.get(bearer)
    bearerToken = request.json()['accessToken']
    print()


#EG1
class EG1:
    Token = EndpointsURLs.tokenurl
    payload=f'grant_type=authorization_code&code={ExCode.ExCode}&token_type=eg1'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'basic MzQ0NmNkNzI2OTRjNGE0NDg1ZDgxYjc3YWRiYjIxNDE6OTIwOWQ0YTVlMjVhNDU3ZmI5YjA3NDg5ZDMxM2I0MWE='
        }
    response = requests.request("POST", Token, headers=headers, data=payload)
    response1 = response.json()['access_token']
    print(f'Access Token: ' + Fore.CYAN + response1)
