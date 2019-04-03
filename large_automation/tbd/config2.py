from configparser import ConfigParser

parser = ConfigParser()
parser.read('database.config')

login_data = parser.get('database_config', 'login_data')
#username = parser.get('database_config', 'username')
headers=parser.get('database_config','headers')
session=parser.get('database_config','s')
#print(password)
#print(username)
print(login_data)
print(headers)
print(session)