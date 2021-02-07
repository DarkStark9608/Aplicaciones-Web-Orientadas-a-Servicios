import web
import requests
import json

render= web.template.render("diccionarios_Oxford/")

class Index():
  def GET(self):
    datos=None
    return render.index(datos)

  def POST(self)  :
    form=web.input()
    palabra=form.palabra
    
    app_id = "53add1c5"
    app_key = "927dec124becdf2ddc22330099edd7fe"
    language = "es"
    word_id = palabra
    fields = 'definitions'
    strictMatch = 'false'
    url = 'https://od-api.oxforddictionaries.com/api/v2/entries/'  + language + '/'  + word_id.lower()#+ '?fields=' + fields + '&strictMatch=' + strictMatch;
    r = requests.get(url, headers = {'app_id' : app_id, 'app_key' : app_key})

    palabras = r.json()
    items = palabras["results"][0]
    encoded = json.dumps(items)
    decoded = json.loads(encoded)
    
    significado=str(decoded['lexicalEntries'][0]['entries'][0]['senses'][0]['definitions'][0])
    definicion ="<label>'"+significado+"'</label>"
    
    datos={
      
      "Palabra":"Palabra buscada: "+palabra,
      "Significado":"Significado" + definicion,
      

    }
    return render.index(datos)
