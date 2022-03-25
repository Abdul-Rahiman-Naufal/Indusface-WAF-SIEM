import requests
import json
from pathlib import Path
import time
from datetime import date, datetime

Log_Folder='C:\Indusface'

URL="https://tas.indusface.com/wafportal/rest/siem/v1/getAttackInfo"
API_Key=""

endTime=round(time.time() * 1000)
startTime=endTime-300000

with open (Log_Folder+"\Indusface.ini", "r") as file:
    API_Key = str(file.read().rstrip())

headers = {'content-type': 'application/json', "Authorization": "Bearer "+str(API_Key)}

data = {"startTime": startTime, "endTime": endTime}

response=requests.post(URL, data=json.dumps(data), headers=headers).json()

now = datetime.now()

try:
    logMessage=""

    if(response['successMessage']=="Success"):
        for row in response["data"]:
            if(bool(row["attacks"])==True):
                for attack in row["attacks"]:
                    logMessage=logMessage+str(attack)+"\n"
     
    today = str(date.today())
    hour=now.strftime("%H")

    # file = Path(Log_Folder+'\indusface-'+today+'-'+hour+'.log')
    file = Path(Log_Folder+'\indusface-'+today+'.log')
    
    file.touch(exist_ok=True)

    with open(file, "a") as text_file:
        text_file.write(logMessage)
except Exception as e:    
    file = Path(Log_Folder+'\Error.log')
    file.touch(exist_ok=True)
    with open(file, "a") as text_file:
        current_time = now.strftime("%H:%M:%S")
        text_file.write(current_time+'   '+str(e)+'\n')
        text_file.write(current_time+'   '+str(response['errorMessages'])+'\n')

        