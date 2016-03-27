from critic.secrets import *
import requests
import json

mn_orig = str(input("Please enter a movie name\n>>> "))

omdb_name = mn_orig.replace(" ", "+").lower()

r = requests.get("https://www.tastekid.com/api/similar?q={}&k={}&type=movies&limit=5&info=1".format(omdb_name, tastekid_api))
data = json.loads(r.text)

dict_parse = data['Similar']['Results']
similar = [li['Name'] for li in dict_parse]
url = [li['yUrl'] for li in dict_parse]

# youtube = data['Similar']['Info']
# real_name = youtube[0]['Name']
# real_url = youtube[0]['yUrl']
#
# print(real_name, real_url)

print(similar, url)