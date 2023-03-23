#ローカルのcsvを変更する

import gspread
from oauth2client.service_account import ServiceAccountCredentials
scope =['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)
sheet = client.open_by_key({シートurlのd/から/editまで}).worksheet({シート名})#シートurl、シート名に注意