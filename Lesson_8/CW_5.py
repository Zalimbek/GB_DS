class PersonNotFound(Exception):
    def __init__(self,txt):
        self.txt = txt

data = ['Ivan', 'Tom', 'Steve']
if not  data.count('Petr'):
    raise PersonNotFound('Персона не найдена')

#-----------------------------------------#
# import psutil
# print(psutil.disk_usage('./venv'))
#
# import requests
# resp = requests.get('https://github.com/requests')
# print(resp.status_code)

