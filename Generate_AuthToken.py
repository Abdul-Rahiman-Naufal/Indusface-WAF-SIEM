import requests
from pathlib import Path
import time
from datetime import date, datetime


Log_Folder='C:\Indusface'

URL="https://tas.indusface.com/wafportal/rest/siem/v1/getAuthToken"
API_ID='APIKEY43xw11468'
API_Key='NAJpCcwoTLgHhZqhFUTVE9PGulkhw8OC'
Config=Log_Folder+'\Indusface.ini'

endTime=round(time.time() * 1000)
startTime=endTime-300000

headers = {'content-type': 'application/x-www-form-urlencoded'}

now = datetime.now()

try:
    response=requests.post(URL, headers=headers, auth=(API_ID, API_Key)).json()

    file = Path(Config)
    file.touch(exist_ok=True)
    with open(file, "w") as text_file:
        text_file.write(str(response['access_token']))
except Exception as e:    
    file = Path(Log_Folder+'\Error.log')
    file.touch(exist_ok=True)
    with open(file, "a") as text_file:
        current_time = now.strftime("%H:%M:%S")
        text_file.write(current_time+'   '+str(e)+'\n')
        text_file.write(current_time+'   '+str(response['errorMessages'])+'\n')
