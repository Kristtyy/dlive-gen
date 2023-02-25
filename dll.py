from requests import post
from random   import choices
from capmonster_python import RecaptchaV2Task
from os import system
class gen:
    def __init__(self):
        self.created = 0
        self.error   = 0
        self.ket     = input("Enter Your Capmonster Key: ")
        self.amt     = int(input("Enter amount to make: "))
        
    def solver(self):
        capmonster = RecaptchaV2Task(self.ket)
        task_id = capmonster.create_task("https://dlive.tv/", "6Lf5BmkUAAAAAKYk6gV1OzK05pOv99MOQoXSIrgj")
        result = capmonster.join_task_result(task_id)
        return result.get("gRecaptchaResponse")

    def apart(self):
        for _ in range(self.amt):
            system(f'title Free ass hell ^| Created : {self.created} ^| Error : {self.error}')
            self.email   = ''.join(choices('abcdefghijklmnopqrstuvwxyz', k=7))
            self.dpn     = ''.join(choices('abcdefghijklmnopqrstuvwxyz1234567890', k=7))
            self.passw   = ''.join(choices('abcdefghijklmnopqrstuvwxyz1234567890._-@!|:#%^&*', k=8))
            retour = self.solver()
            headers = {
                'authority': 'graphigo.prd.dlive.tv',
                'accept': '*/*',
                'accept-language': 'en-US,en;q=0.9',
                'content-type': 'application/json',
                'fingerprint': '08ef6ca782d84d796a7a72ed02a913bc',
                'gacid': '1952730419.1677154566',
                'origin': 'https://dlive.tv',
                'referer': 'https://dlive.tv/',
                'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-site',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
                'x-dlive-mid': '08ef6ca782d84d796a7a72ed02a913bc',
                'x-dlive-mtype': 'web',
                'x-dlive-mversion': 'local',
            }

            json_data = {
                'operationName': 'RegisterWithEmail',
                'variables': {
                    'email': self.email + "@gmaal.com",
                    'password': self.passw,
                    'recaptchaToken': retour,
                    'deviceType': 'WEB',
                    'displayname': f'{self.dpn}',
                    'language': 'en',
                },
                'extensions': {
                    'persistedQuery': {
                        'version': 1,
                        'sha256Hash': '01dd44cb2b5a8bd5eea8d3b7024295553447d2dc64490a2f15cd9332a1fc8c57',
                    },
                },
            }

            response = post('https://graphigo.prd.dlive.tv/', headers=headers, json=json_data)
            if response.json()['username'] == self.dpn:
                print("Succesfully registered")
                self.created += 1
                with open("Creations.txt", 'a') as f:
                    f.write(self.email + ":" + self.passw + ":" + self.dpn + "\n")

            else:
                print("Failed")
                self.error +=1

gen().apart()