import requests

import json
app_id = "53add1c5"
app_key = "927dec124becdf2ddc22330099edd7fe"
language = "es"
word_id = "zapato"
fields = 'synonyms'
strictMatch = 'false'
url = 'https://od-api.oxforddictionaries.com/api/v2/entries/'  + language + '/'  + word_id.lower()#+ '?fields=' + fields + '&strictMatch=' + strictMatch;
r = requests.get(url, headers = {'app_id' : app_id, 'app_key' : app_key})

palabras = r.json()

items = palabras["results"][0]
encoded = json.dumps(items)
decoded = json.loads(encoded)
print(decoded['lexicalEntries'][0]['entries'][0]['senses'][0]['derivatives'][0]['text'])
#print(decoded['lexicalEntries'][0]['entries'][0]['senses'][0]['definitions'][0])
print("-------------------------")
print(items)


#print("code {}\n".format(r.status_code))
#print("text \n" + r.text)
#print("json \n" + json.dumps(r.json()))


#print("text \n" + r.text)
#print("json \n" + json.dumps(r.json()))